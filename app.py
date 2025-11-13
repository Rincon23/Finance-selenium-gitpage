from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time

TICKERS = [
    "SAPR3", "CMIG3", "CPFE3", "EGIE3", "ITUB3",
    "BBAS3", "BBSE3", "PSSA3", "B3SA3", "RADL3",
    "ODPV3", "WEGE3", "TGMA3", "ABEV3", "MDIA3",
    "SLCE3", "LEVE3", "VIVA3", "EZTC3", "VALE3",
    "CMIN3", "TIMS3", "PETR3"
]

CACHE_FILE = "vpa_cache.json"
cache = {}

options = Options()
options.headless = True
options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

for ticker in TICKERS:

    url = f"https://analitica.auvp.com.br/acoes/{ticker}"

    driver.delete_all_cookies()  # ok usar antes

    driver.get(url)
    time.sleep(2)  # aguardar carregamento

    # limpar localStorage APÓS entrar na página
    try:
        driver.execute_script("localStorage.clear();")
        driver.execute_script("sessionStorage.clear();")
    except Exception:
        pass  # ignora erros

    # pegar indicadores
    try:
        dy = driver.find_element(By.XPATH, "//div[h4[text()='Dividend yield']]/following-sibling::div").text
    except:
        dy = "Não encontrado"

    try:
        lpa = driver.find_element(By.XPATH, "//div[h4[text()='LPA']]/following-sibling::div").text
    except:
        lpa = "Não encontrado"

    try:
        vpa = driver.find_element(By.XPATH, "//div[h4[text()='VPA']]/following-sibling::div").text
    except:
        vpa = "Não encontrado"

    cache[ticker] = {"LPA": lpa, "VPA": vpa, "Div Yeld": dy}

driver.quit()

with open(CACHE_FILE, "w", encoding="utf-8") as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)

print("Cache atualizado:", cache)
