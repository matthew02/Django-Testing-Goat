#!/usr/bin/env python3

import os
import unittest

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        firefox_path = os.environ.get('FIREFOX_PATH')
        binary = FirefoxBinary(firefox_path)
        self.browser = webdriver.Firefox(firefox_binary=binary)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Some users heard about a new to-do app and go check out the
        # homepage.
        self.browser.get('http://localhost:8000')

        # They notice the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)

        # They are immediately invited to enter a to-do item.

        # They type "Buy new fishing line" into a text box

        # When they press enter, the page updates, and now the page lists
        # "1: Buy fishing lures" as an item in a to-do list

        # There is still a text box inviting them to add more items. They enter
        # "Restring my fishing reel." into the text box.

        # The page updates again and now shows both items in the list

        # They wonder whether the site will remember their list. Then they see some
        # text explaining that the site has generated a unique URL for them.

        # They visit that unique url and the to-do list is there.

        # They are satisfied and leave.


if __name__ == '__main__':
    #unittest.main(warnings='ignore')
    unittest.main()

