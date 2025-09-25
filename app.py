from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

TICKERS = ["CMIG4",
            "ISAE4",
            "BBSE3",
            "TAEE11",
            "BBAS3",
            "DIRR3",
            "ITSA4",
            "BBDC4",
            "CPLE6",
            "CSNA3",
            "PETR4",
            "POMO4",
            "CURY3",
            "CPFE3",
            "GOAU4",
            "BRAP4",
            "VALE3",
            "TIMS3",
            "CMIN3",
            "MRFG3",
            "CXSE3",
            "PSSA3",
            "EQTL3",
            "ABEV3",
            "BBAS3",
            "CPFE3",
            "ITSA3",
            "RADL3",
            "B3SA3",
            "BBSE3",
            "WEGE3",
            "EGIE3"]
CACHE_FILE = "vpa_cache.json"
cache = {}

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)

for ticker in TICKERS:
    driver.get(f"https://finance.yahoo.com/quote/{ticker}.SA/key-statistics")
    try:
        element = driver.find_element(By.XPATH, '//td[text()="Book Value Per Share"]/following-sibling::td')
        cache[ticker] = element.text
    except:
        cache[ticker] = "Não encontrado"

driver.quit()

# Salva cache em JSON
with open(CACHE_FILE, "w") as f:
    json.dump(cache, f)

print("Cache atualizado:", cache)