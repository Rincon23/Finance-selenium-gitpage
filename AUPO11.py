from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time
import os
import random

PROGRAM_NAME = "AUPO11"
CACHE_FILE = "gitPages.json"

options = Options()
options.headless = False
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

driver = webdriver.Chrome(options=options)

url = "https://statusinvest.com.br/etfs/aupo11"
driver.get(url)

# Delay variável (anti-bot)
time.sleep(random.uniform(3, 6))

try:
    ct = driver.find_element(
        By.XPATH,
        '//*[@id="main-2"]/div[1]/div[1]/div[1]/div/div[1]/strong'
    ).text
except:
    ct = "Não encontrado"

driver.quit()

ct = troca_ponto_por_virgula(ct)

# ✅ SALVA SOMENTE NO BLOCO DO PROGRAMA
cache.setdefault(PROGRAM_NAME, {})
cache[PROGRAM_NAME]["Cota"] = ct

with open(CACHE_FILE, "w", encoding="utf-8") as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)

print(f"Cache atualizado ({PROGRAM_NAME}):", cache[PROGRAM_NAME])
