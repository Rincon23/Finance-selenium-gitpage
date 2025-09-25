from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

TICKERS = ["BBAS3", "ITSA3", "PETR4"]
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