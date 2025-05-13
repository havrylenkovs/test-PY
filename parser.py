import requests
from bs4 import BeautifulSoup

# URL сайту
url = "https://quotes.toscrape.com"

# Надсилаємо GET-запит до сайту
response = requests.get(url)

# Парсимо HTML
soup = BeautifulSoup(response.text, "lxml")

# Знаходимо всі цитати
quotes = soup.find_all("span", class_="text")

print("ЦИТАТИ ЗІ САЙТУ:\n")
for quote in quotes:
    print(quote.text)
