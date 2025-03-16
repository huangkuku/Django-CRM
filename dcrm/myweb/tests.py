from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8080/")

# 輸入帳號密碼
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.ID, "login").click()
# 確保登入成功
h1_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "main-header"))
)
assert "Records..." in h1_text.text

driver.quit()