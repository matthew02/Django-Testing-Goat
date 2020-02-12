import os

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


FIREFOX_PATH = os.environ.get('FIREFOX_PATH')
print(FIREFOX_PATH)
BINARY = FirefoxBinary(FIREFOX_PATH)
BROWSER = webdriver.Firefox(firefox_binary=BINARY)
#BROWSER = webdriver.Firefox()
BROWSER.get('http://localhost:8000')

assert 'Django' in BROWSER.title
