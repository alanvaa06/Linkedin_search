"""
Este script usa Selenium 4 en modo no-obsoleto, mejoras de manejo de DataFrames
con pd.concat, scrolling con JavaScript, y gestión flexible de tiempos de espera.
"""

import time
import random
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Si deseas usar webdriver_manager:
# pip install webdriver-manager
# from webdriver_manager.chrome import ChromeDriverManager

# Configuración
PROXY = ""  # Cambia o elimina si no deseas usar proxy
URL_LOGIN = "https://www.linkedin.com/login"
USERNAME = ""  # Tu usuario
PASSWORD = ""  # Tu contraseña

# Driver local (reemplaza la ruta a tu chromedriver)
# Para usar proxy en Selenium 4, se requiere configuración adicional.
# Revisa la documentación oficial de Selenium.

service = Service("driver/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument(f"--proxy-server={PROXY}")


# Inicia el driver
driver = webdriver.Chrome(service=service, options=options)

# Cambio
