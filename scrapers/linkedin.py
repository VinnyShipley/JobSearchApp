from webbot import Browser
driver = Browser()



import mechanize

browser = mechanize.Browser()
browser.set_handle_robots(False)
response = browser.open('http://www.linkedin.com')
print(response.code)
for f in browser.forms():
  print(f)
