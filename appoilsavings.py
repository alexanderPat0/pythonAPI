import time
import json
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument("start-maximized")
    options.add_argument("window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
    
    driver = webdriver.Chrome(options=options)

    address = request.args.get('address')
    selected_fuel = request.args.get('selectedFuel')
    search_radius = request.args.get('radius', '2')  
    url = "https://www.ocu.org/coches/gasolina-y-carburantes/calculadora/gasolineras/"

    driver.get(url)

    try:
        cookie_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
        cookie_button.click()

        input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "UserAddress")))
        input_field.send_keys(address)
        time.sleep(3)
        input_field.send_keys(Keys.ARROW_DOWN) 
        time.sleep(1)       
        input_field.send_keys(Keys.ENTER)

        slider = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "KmRadius")))
        driver.execute_script("arguments[0].setAttribute('value', arguments[1])", slider, search_radius)

        dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "FuelType")))
        Select(dropdown).select_by_value(selected_fuel)

        submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "submitButton")))
        submit_button.click()
        
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "table--responsive")))
        rows = driver.find_elements(By.CSS_SELECTOR, "div.table--responsive.desktop-only table tbody tr")

        gas_stations = []
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            if columns:
                station_data = {
                    "id": columns[0].text.strip(),
                    "name": columns[1].text.strip(),
                    "address": columns[2].text.strip(),
                    "address_url": columns[2].find_element(By.TAG_NAME, "a").get_attribute("href"),
                    "distance": columns[3].text.strip(),
                    "price_per_liter": columns[4].text.strip(),
                    "cost_deposit": columns[5].text.strip()
                }
                gas_stations.append(station_data)

        return jsonify(gas_stations)

    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
