from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
# Открываем веб-страницу
driver.get("https://www.selenium.dev/")

# Устанавливаем значение в LocalStorage
driver.execute_script("localStorage.setItem('testKey', 'Modsen');")

# Получаем значение из LocalStorage
value = driver.execute_script("return localStorage.getItem('testKey');")
print(f"Значение из LocalStorage: {value}")

# Удаляем значение из LocalStorage
driver.execute_script("localStorage.removeItem('testKey');")

# Проверяем, что значение удалено
value = driver.execute_script("return localStorage.getItem('testKey');")
print(f"Значение после удаления: {value}")

# Открываем веб-страницу
driver.get("https://www.selenium.dev/")

# Устанавливаем cookie
driver.add_cookie({"name": "Cookie", "value": "Cookie"})

# Получаем значение cookie
cookie = driver.get_cookie("Cookie")
print(f"Значение cookie: {cookie['value']}")

# Удаляем cookie
driver.delete_cookie("Cookie")

# Проверяем, что cookie удалено
cookie = driver.get_cookie("Cookie")
print(f"Cookie после удаления: {cookie}")
driver.quit()
