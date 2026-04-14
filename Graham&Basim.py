from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time
import os
import random

PROGRAM_NAME = "Graham&Basim"
CACHE_FILE = "gitPages.json"

TICKERS = [
    "SAPR3", "SBSP3", "CMIG3", "CPFE3", "EGIE3", "ITUB3", "BBDC3",
    "BBAS3", "BBSE3", "PSSA3", "B3SA3", "ITSA3", "RADL3",
    "ODPV3", "WEGE3", "TGMA3", "ABEV3", "MDIA3",
    "SLCE3", "LEVE3", "VIVA3", "EZTC3", "VALE3",
    "CMIN3", "TIMS3", "PETR3", "KLBN3"
]

options = Options()
options.headless = True
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

def troca_ponto_por_virgula(valor):
    if not isinstance(valor, str):
        return valor
    return valor.replace(".", ",")

# Carrega cache existente
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        cache = json.load(f)
else:
    cache = {}

cache.setdefault(PROGRAM_NAME, {})

driver = webdriver.Chrome(options=options)

for ticker in TICKERS:
    url = f"https://statusinvest.com.br/acoes/{ticker}"
    driver.get(url)

    time.sleep(random.uniform(3, 6))

    try:
        dy = driver.find_element(
            By.XPATH,
            '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[1]/div/div/strong'
        ).text
    except:
        dy = "Não encontrado"

    try:
        lpa = driver.find_element(
            By.XPATH,
            '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[11]/div/div/strong'
        ).text
    except:
        lpa = "Não encontrado"

    try:
        vpa = driver.find_element(
            By.XPATH,
            '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[9]/div/div/strong'
        ).text
    except:
        vpa = "Não encontrado"

    cache[PROGRAM_NAME][ticker] = {
        "LPA": troca_ponto_por_virgula(lpa),
        "VPA": troca_ponto_por_virgula(vpa),
        "Div Yield": troca_ponto_por_virgula(dy)
    }

    print(f"""
        "LPA": "{troca_ponto_por_virgula(lpa)}",
        "VPA": "{troca_ponto_por_virgula(vpa)}",
        "Div Yield": "{troca_ponto_por_virgula(dy)}"
        """)


driver.quit()

with open(CACHE_FILE, "w", encoding="utf-8") as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)

print(f"Cache atualizado ({PROGRAM_NAME})")
