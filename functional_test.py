import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goesto check out its homepage
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(
            by=By.TAG_NAME, value='h1').text
        self.assertIn('To-Do', header_text)
        inputbox = self.browser.find_element(by=By.ID, value='id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)

        table = self.browser.find_element(by=By.ID, value='id_list_table')
        # returns a list of elements
        rows = table.find_elements(by=By.TAG_NAME, value='tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            'New to-do item did not appear in table!'
        )

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
