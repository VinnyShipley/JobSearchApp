import mechanize

browser = mechanize.Browser()
browser.set_handle_robots(False)
response = browser.open('http://www.google.com')
print(response.code)
