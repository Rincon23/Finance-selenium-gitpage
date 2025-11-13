from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

TICKERS = [
    "SAPR3",
    "CMIG3",
    "CPFE3",
    "EGIE3",
    "ITUB3",
    "BBAS3",
    "BBSE3",
    "PSSA3",
    "B3SA3",
    "RADL3",
    "ODPV3",
    "WEGE3",
    "TGMA3",
    "ABEV3",
    "MDIA3",
    "SLCE3",
    "LEVE3",
    "VIVA3",
    "EZTC3",
    "VALE3",
    "CMIN3",
    "TIMS3",
    "PETR3"
]

CACHE_FILE = "vpa_cache.json"
cache = {}

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)

for ticker in TICKERS:
    driver.get(f"https://statusinvest.com.br/acoes/{ticker}")
    
    try:
        vpa = driver.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[9]/div/div/strong').text
    except:
        vpa = "Nao encontrado"

    try:
        dy = driver.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[1]/div/div/strong').text
    except:
        dy = "Não encontrado"

    try:
        lpa = driver.find_element(By.XPATH, '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[11]/div/div/strong').text
    except:
        lpa = "Não encontrado"


    
    cache[ticker] = {"LPA": lpa,"VPA": vpa, "Div Yeld": dy}

driver.quit()

# Salva cache em JSON
with open(CACHE_FILE, "w") as f:
    json.dump(cache, f)

print("Cache atualizado:", cache)
