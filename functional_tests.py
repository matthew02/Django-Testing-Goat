from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


BINARY = FirefoxBinary('/usr/bin/firefox-developer-edition')
BROWSER = webdriver.Firefox(firefox_binary=BINARY)
#BROWSER = webdriver.Firefox()
BROWSER.get('http://localhost:8000')

assert 'Django' in BROWSER.title
