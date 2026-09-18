import time
from selenium import webdriver
import sys

print("ПУТЬ К ПИТОНУ:", sys.executable)


print("Запуск браузера...")
driver = webdriver.Chrome()  # или другой браузер, который используете
driver.get("https://github.com")
time.sleep(3)
driver.quit()
print("Тест завершен успешно!")
