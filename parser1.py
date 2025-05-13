from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import csv

# Налаштування браузера
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # "новий" headless-режим
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://gagadget.com/uk/search/?q=samsung"
driver.get(url)
time.sleep(3)

all_articles = []

while True:
    print("📄 Парсимо сторінку:", driver.current_url)

    titles = driver.find_elements(By.CSS_SELECTOR, "a.article__title")

    for title in titles:
        text = title.text.strip()
        link = title.get_attribute("href")
        if text and link:
            all_articles.append((text, link))

    try:
        next_btn = driver.find_element(By.LINK_TEXT, "Наступна сторінка")
        next_btn.click()
        time.sleep(3)
    except NoSuchElementException:
        print("⛔ Кінець сторінок.")
        break

driver.quit()

# Зберігаємо в CSV
filename = "samsung_news.csv"
with open(filename, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])  # заголовки колонок
    writer.writerows(all_articles)

print(f"\n✅ CSV збережено як: {filename}")
