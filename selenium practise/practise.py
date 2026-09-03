from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html?utm_source=chatgpt.com")
print(driver.title)
text_element=driver.find_element(By.ID,"my-text-id")
text_element.send_keys("kushagra sharma")
password_element=driver.find_element(By.NAME,"my-password")
password_element.send_keys("Gu@12345")
text_element=driver.find_element(By.NAME,"my-textarea")
text_element.send_keys("Kushagr ais a good boy but currently not doing good may god blesss him")
drop_down=driver.find_element(By.NAME,"my-select")
select=Select(drop_down)
select.select_by_visible_text("Three")
dropdown_element=driver.find_element(By.NAME,"my-datalist")
dropdown_element.send_keys("Chicago")
file_input=driver.find_element(By.NAME,"my-file")
file_input.send_keys(r"C:/Users/kusha/Downloads/Kushagra_SharmaIT.pdf")
time.sleep(10)
driver.quit