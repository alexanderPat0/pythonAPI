# AppOilSavings

AppOilSavings es una aplicación web desarrollada en Flask que permite a los usuarios obtener información sobre gasolineras cercanas. Utiliza Selenium para raspar los datos de un sitio web de gasolineras y los presenta a los usuarios a través de una API.

## Características

- Búsqueda de gasolineras basadas en la dirección, tipo de combustible y radio de búsqueda especificados por el usuario.
- Presentación de datos de gasolineras, incluyendo nombre, dirección, distancia, precio por litro y costo por depósito.

## Requisitos

- Flask
- Selenium
- WebDriver (ChromeDriver)

## Instalación

Para utilizar esta aplicación, necesitarás instalar las dependencias requeridas. Asegúrate de tener Python y pip instalados en tu sistema, y luego ejecuta:

pip install flask selenium

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:

python appoilsavings.py

La aplicación estará disponible en
http://34.175.24.171:8080/scrape?address=$address&selectedFuel=$fuel&radius=$radius

## API Endpoints

vEste endpoint acepta tres parámetros: address (dirección para la búsqueda), selectedFuel (tipo de combustible), y radius (radio de búsqueda en kilómetros). Retorna un JSON con los datos de las gasolineras encontradas.

@@Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar la aplicación, considera clonar el repositorio y realizar tus cambios.

Licencia
Distribuido bajo la licencia MIT. Ver LICENSE para más información.
