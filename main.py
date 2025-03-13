import json
import requests
import os

# Загружаем API-ключ из config.json
CONFIG_FILE = "config.json"

if not os.path.exists(CONFIG_FILE):
    raise FileNotFoundError(f"Ошибка: файл {CONFIG_FILE} не найден.")

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    content = f.read().strip()
    if not content:
        raise ValueError("Ошибка: config.json пуст.")

    config = json.loads(content)
    API_KEY = config.get("api_key", "").strip()

    if not API_KEY:
        raise ValueError("Ошибка: API-ключ отсутствует или пуст.")

# Базовый URL API
BASE_URL = "https://api.ataix.kz"

def get_request(endpoint):
    """Функция для выполнения GET-запросов к API"""
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "API-KEY": API_KEY,
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Вызывает ошибку, если код ответа != 200
    return response.json()

# Запрашиваем данные сразу при запуске
print("\nСписок всех валют:")
print(get_request("/api/currencies"))

print("\nСписок всех торговых пар:")
print(get_request("/api/symbols"))

print("\nЦены всех монет и токенов:")
print(get_request("/api/prices"))
