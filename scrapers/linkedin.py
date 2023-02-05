import mechanize

browser = mechanize.Browser()
browser.set_handle_robots(False)
response = browser.open('http://www.google.com')
browser.submit(id='gbqfbb')
print(browser.code)
