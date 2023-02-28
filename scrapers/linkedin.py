from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service)