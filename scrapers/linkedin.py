from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = "C:\Users\vinny\AppData\Local\Google\Chrome\User Data\Default"
chrome_driver_binary = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)


