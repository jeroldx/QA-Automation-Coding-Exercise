from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class AutomationExercise(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_search_in_google(self):
        driver = self.driver
        driver.get("http://www.google.com")
        search_bar = driver.find_element(by=By.NAME, value="q")
        search_bar.send_keys("RTS Labs")
        search_bar.send_keys(Keys.ENTER)
        search_results = driver.find_elements(by=By.XPATH, value='//div[@id="search"]//a/h3')
        search_results[0].click()
        self.assertEqual("https://rtslabs.com/", driver.current_url)

    def tearDown(self):
        self.driver.close()

