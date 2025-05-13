from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Запускаємо браузер у звичайному режимі (видно вікно)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Відкриваємо Google
driver.get("https://www.google.com")

# Чекаємо 5 секунд, щоб побачити, що все працює
time.sleep(5)

# Закриваємо браузер
driver.quit()
