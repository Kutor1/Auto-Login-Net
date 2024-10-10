from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# 配置 WebDriver 的路径
driver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'  # 替换为ChromeDriver 路径
service = Service(driver_path)
browser = webdriver.Chrome(service=service)

try:
    # 打开登录网站
    browser.get('http://10.50.2.2/')

    # 等待页面加载
    time.sleep(1)

    # 按顺序查找两个textbox
    username_fields = browser.find_elements(By.CLASS_NAME, 'edit_lobo_cell')
    # 输入账号
    username_fields[1].send_keys("2023072014")
    # 输入密码
    username_fields[2].send_keys("GZucm*270036")

    # 确认登录
    username_fields[0].click()

except Exception as e:
    print(f"发生错误: {e}")

finally:
    pass

