from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time
import os
import random

PROGRAM_NAME = "FIIs"
CACHE_FILE = "gitPages.json"

FIIS = [
    "HGLG11", "KNRI11", "HGRU11", "PMLL11"
]

options = Options()
options.headless = True
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
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

for fii in FIIS:
    url = f"https://statusinvest.com.br/fundos-imobiliarios/{fii}"
    driver.get(url)

    time.sleep(random.uniform(3, 6))

    try:
        pvp = driver.find_element(
        By.XPATH,
        '//*[@id="main-2"]/div[2]/div[5]/div/div[2]/div/div[1]/strong'
        ).text
    except:
        pvp = "Não encontrado"

    cache[PROGRAM_NAME][fii] = {
        "P/VP": troca_ponto_por_virgula(pvp)
    }

    print(f'{fii} -> P/VP: {pvp}')

driver.quit()

with open(CACHE_FILE, "w", encoding="utf-8") as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)

print("Cache de FIIs atualizado!")