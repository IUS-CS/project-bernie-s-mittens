from django.test import TestCase
# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Create your tests here.

class TestFinaltests():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_user(self):
        # Test name: user
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        # 2 | setWindowSize | 854x704 |
        self.driver.set_window_size(854, 704)
        # 3 | click | linkText=Am I eligible? |
        self.driver.find_element(By.LINK_TEXT, "Am I eligible?").click()
        # 4 | click | id=id_home_state |
        self.driver.find_element(By.ID, "id_home_state").click()
        # 5 | select | id=id_home_state | label=INDIANA
        dropdown = self.driver.find_element(By.ID, "id_home_state")
        dropdown.find_element(By.XPATH, "//option[. = 'INDIANA']").click()
        # 6 | click | css=#id_home_state > option:nth-child(2) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_home_state > option:nth-child(2)").click()
        # 7 | click | id=id_work_state |
        self.driver.find_element(By.ID, "id_work_state").click()
        # 8 | select | id=id_work_state | label=KENTUCKY
        dropdown = self.driver.find_element(By.ID, "id_work_state")
        dropdown.find_element(By.XPATH, "//option[. = 'KENTUCKY']").click()
        # 9 | click | css=#id_work_state > option:nth-child(3) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_work_state > option:nth-child(3)").click()
        # 10 | click | id=id_age |
        self.driver.find_element(By.ID, "id_age").click()
        # 11 | type | id=id_age | 16
        self.driver.find_element(By.ID, "id_age").send_keys("16")
        # 12 | click | id=id_essential |
        self.driver.find_element(By.ID, "id_essential").click()
        # 13 | select | id=id_essential | label=Yes
        dropdown = self.driver.find_element(By.ID, "id_essential")
        dropdown.find_element(By.XPATH, "//option[. = 'Yes']").click()
        # 14 | click | css=#id_essential > option:nth-child(2) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_essential > option:nth-child(2)").click()
        # 15 | click | id=id_vaccine_group |
        self.driver.find_element(By.ID, "id_vaccine_group").click()
        # 16 | select | id=id_vaccine_group | label=Unknown
        dropdown = self.driver.find_element(By.ID, "id_vaccine_group")
        dropdown.find_element(By.XPATH, "//option[. = 'Unknown']").click()
        # 17 | click | css=option:nth-child(6) |
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(6)").click()
        # 18 | click | css=input:nth-child(7) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def test_user1(self):
        # Test name: user1
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        # 2 | setWindowSize | 854x704 |
        self.driver.set_window_size(854, 704)
        # 3 | click | linkText=Am I eligible? |
        self.driver.find_element(By.LINK_TEXT, "Am I eligible?").click()
        # 4 | click | id=id_home_state |
        self.driver.find_element(By.ID, "id_home_state").click()
        # 5 | select | id=id_home_state | label=KENTUCKY
        dropdown = self.driver.find_element(By.ID, "id_home_state")
        dropdown.find_element(By.XPATH, "//option[. = 'KENTUCKY']").click()
        # 6 | click | css=#id_home_state > option:nth-child(3) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_home_state > option:nth-child(3)").click()
        # 7 | click | id=id_work_state |
        self.driver.find_element(By.ID, "id_work_state").click()
        # 8 | select | id=id_work_state | label=KENTUCKY
        dropdown = self.driver.find_element(By.ID, "id_work_state")
        dropdown.find_element(By.XPATH, "//option[. = 'KENTUCKY']").click()
        # 9 | click | css=#id_work_state > option:nth-child(3) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_work_state > option:nth-child(3)").click()
        # 10 | click | id=id_age |
        self.driver.find_element(By.ID, "id_age").click()
        # 11 | type | id=id_age | 15
        self.driver.find_element(By.ID, "id_age").send_keys("15")
        # 12 | click | id=id_essential |
        self.driver.find_element(By.ID, "id_essential").click()
        # 13 | select | id=id_essential | label=Yes
        dropdown = self.driver.find_element(By.ID, "id_essential")
        dropdown.find_element(By.XPATH, "//option[. = 'Yes']").click()
        # 14 | click | css=#id_essential > option:nth-child(2) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_essential > option:nth-child(2)").click()
        # 15 | click | id=id_vaccine_group |
        self.driver.find_element(By.ID, "id_vaccine_group").click()
        # 16 | select | id=id_vaccine_group | label=A
        dropdown = self.driver.find_element(By.ID, "id_vaccine_group")
        dropdown.find_element(By.XPATH, "//option[. = 'A']").click()
        # 17 | click | css=#id_vaccine_group > option:nth-child(2) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_vaccine_group > option:nth-child(2)").click()
        # 18 | click | css=input:nth-child(7) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def test_user2(self):
        # Test name: user2
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        # 2 | setWindowSize | 854x704 |
        self.driver.set_window_size(854, 704)
        # 3 | click | linkText=Am I eligible? |
        self.driver.find_element(By.LINK_TEXT, "Am I eligible?").click()
        # 4 | click | id=id_home_state |
        self.driver.find_element(By.ID, "id_home_state").click()
        # 5 | select | id=id_home_state | label=KENTUCKY
        dropdown = self.driver.find_element(By.ID, "id_home_state")
        dropdown.find_element(By.XPATH, "//option[. = 'KENTUCKY']").click()
        # 6 | click | css=#id_home_state > option:nth-child(3) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_home_state > option:nth-child(3)").click()
        # 7 | click | id=id_work_state |
        self.driver.find_element(By.ID, "id_work_state").click()
        # 8 | select | id=id_work_state | label=INDIANA
        dropdown = self.driver.find_element(By.ID, "id_work_state")
        dropdown.find_element(By.XPATH, "//option[. = 'INDIANA']").click()
        # 9 | click | css=#id_work_state > option:nth-child(2) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_work_state > option:nth-child(2)").click()
        # 10 | click | id=id_age |
        self.driver.find_element(By.ID, "id_age").click()
        # 11 | type | id=id_age | 37
        self.driver.find_element(By.ID, "id_age").send_keys("37")
        # 12 | click | id=id_essential |
        self.driver.find_element(By.ID, "id_essential").click()
        # 13 | select | id=id_essential | label=No
        dropdown = self.driver.find_element(By.ID, "id_essential")
        dropdown.find_element(By.XPATH, "//option[. = 'No']").click()
        # 14 | click | css=#id_essential > option:nth-child(3) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_essential > option:nth-child(3)").click()
        # 15 | click | id=id_vaccine_group |
        self.driver.find_element(By.ID, "id_vaccine_group").click()
        # 16 | select | id=id_vaccine_group | label=Unknown
        dropdown = self.driver.find_element(By.ID, "id_vaccine_group")
        dropdown.find_element(By.XPATH, "//option[. = 'Unknown']").click()
        # 17 | click | css=option:nth-child(6) |
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(6)").click()
        # 18 | click | css=input:nth-child(7) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def test_user3(self):
        # Test name: user3
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        # 2 | setWindowSize | 854x704 |
        self.driver.set_window_size(854, 704)
        # 3 | click | linkText=Am I eligible? |
        self.driver.find_element(By.LINK_TEXT, "Am I eligible?").click()
        # 4 | click | id=id_age |
        self.driver.find_element(By.ID, "id_age").click()
        # 5 | type | id=id_age | 32
        self.driver.find_element(By.ID, "id_age").send_keys("32")
        # 6 | click | css=input:nth-child(7) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
        # 7 | click | id=id_home_state |
        self.driver.find_element(By.ID, "id_home_state").click()
        # 8 | select | id=id_home_state | label=KENTUCKY
        dropdown = self.driver.find_element(By.ID, "id_home_state")
        dropdown.find_element(By.XPATH, "//option[. = 'KENTUCKY']").click()
        # 9 | click | css=#id_home_state > option:nth-child(3) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_home_state > option:nth-child(3)").click()
        # 10 | click | css=input:nth-child(7) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
        # 11 | click | id=id_work_state |
        self.driver.find_element(By.ID, "id_work_state").click()
        # 12 | select | id=id_work_state | label=INDIANA
        dropdown = self.driver.find_element(By.ID, "id_work_state")
        dropdown.find_element(By.XPATH, "//option[. = 'INDIANA']").click()
        # 13 | click | css=#id_work_state > option:nth-child(2) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_work_state > option:nth-child(2)").click()
        # 14 | click | css=input:nth-child(7) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
        # 15 | click | id=id_essential |
        self.driver.find_element(By.ID, "id_essential").click()
        # 16 | select | id=id_essential | label=No
        dropdown = self.driver.find_element(By.ID, "id_essential")
        dropdown.find_element(By.XPATH, "//option[. = 'No']").click()
        # 17 | click | css=#id_essential > option:nth-child(3) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_essential > option:nth-child(3)").click()
        # 18 | click | css=input:nth-child(7) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
        # 19 | click | id=id_vaccine_group |
        self.driver.find_element(By.ID, "id_vaccine_group").click()
        # 20 | select | id=id_vaccine_group | label=A
        dropdown = self.driver.find_element(By.ID, "id_vaccine_group")
        dropdown.find_element(By.XPATH, "//option[. = 'A']").click()
        # 21 | click | css=#id_vaccine_group > option:nth-child(2) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_vaccine_group > option:nth-child(2)").click()
        # 22 | click | css=input:nth-child(7) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def test_user4(self):
        # Test name: user4
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        # 2 | setWindowSize | 854x704 |
        self.driver.set_window_size(854, 704)
        # 3 | click | linkText=Eligibility |
        self.driver.find_element(By.LINK_TEXT, "Eligibility").click()
        # 4 | click | id=id_home_state |
        self.driver.find_element(By.ID, "id_home_state").click()
        # 5 | select | id=id_home_state | label=INDIANA
        dropdown = self.driver.find_element(By.ID, "id_home_state")
        dropdown.find_element(By.XPATH, "//option[. = 'INDIANA']").click()
        # 6 | click | css=#id_home_state > option:nth-child(2) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_home_state > option:nth-child(2)").click()
        # 7 | click | id=id_work_state |
        self.driver.find_element(By.ID, "id_work_state").click()
        # 8 | select | id=id_work_state | label=INDIANA
        dropdown = self.driver.find_element(By.ID, "id_work_state")
        dropdown.find_element(By.XPATH, "//option[. = 'INDIANA']").click()
        # 9 | click | css=#id_work_state > option:nth-child(2) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_work_state > option:nth-child(2)").click()
        # 10 | click | id=id_essential |
        self.driver.find_element(By.ID, "id_essential").click()
        # 11 | select | id=id_essential | label=No
        dropdown = self.driver.find_element(By.ID, "id_essential")
        dropdown.find_element(By.XPATH, "//option[. = 'No']").click()
        # 12 | click | css=#id_essential > option:nth-child(3) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_essential > option:nth-child(3)").click()
        # 13 | click | id=id_vaccine_group |
        self.driver.find_element(By.ID, "id_vaccine_group").click()
        # 14 | select | id=id_vaccine_group | label=B
        dropdown = self.driver.find_element(By.ID, "id_vaccine_group")
        dropdown.find_element(By.XPATH, "//option[. = 'B']").click()
        # 15 | click | css=#id_vaccine_group > option:nth-child(3) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_vaccine_group > option:nth-child(3)").click()
        # 16 | click | css=input:nth-child(7) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
        # 17 | type | id=id_age | 126
        self.driver.find_element(By.ID, "id_age").send_keys("126")
        # 18 | click | css=input:nth-child(7) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
        # 19 | click | id=id_age |
        self.driver.find_element(By.ID, "id_age").click()
        # 20 | type | id=id_age | 119
        self.driver.find_element(By.ID, "id_age").send_keys("119")
        # 21 | click | css=input:nth-child(8) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(8)").click()

    def test_user5(self):
        # Test name: user5
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        # 2 | setWindowSize | 854x704 |
        self.driver.set_window_size(854, 704)
        # 3 | click | linkText=Home |
        self.driver.find_element(By.LINK_TEXT, "Home").click()
        # 4 | click | linkText=Eligibility |
        self.driver.find_element(By.LINK_TEXT, "Eligibility").click()
        # 5 | click | linkText=About |
        self.driver.find_element(By.LINK_TEXT, "About").click()
        # 6 | click | linkText=Eligibility |
        self.driver.find_element(By.LINK_TEXT, "Eligibility").click()
        # 7 | click | linkText=Home |
        self.driver.find_element(By.LINK_TEXT, "Home").click()
        # 8 | click | linkText=Am I eligible? |
        self.driver.find_element(By.LINK_TEXT, "Am I eligible?").click()
        # 9 | click | id=id_home_state |
        self.driver.find_element(By.ID, "id_home_state").click()
        # 10 | select | id=id_home_state | label=KENTUCKY
        dropdown = self.driver.find_element(By.ID, "id_home_state")
        dropdown.find_element(By.XPATH, "//option[. = 'KENTUCKY']").click()
        # 11 | click | css=#id_home_state > option:nth-child(3) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_home_state > option:nth-child(3)").click()
        # 12 | click | id=id_work_state |
        self.driver.find_element(By.ID, "id_work_state").click()
        # 13 | select | id=id_work_state | label=KENTUCKY
        dropdown = self.driver.find_element(By.ID, "id_work_state")
        dropdown.find_element(By.XPATH, "//option[. = 'KENTUCKY']").click()
        # 14 | click | css=#id_work_state > option:nth-child(3) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_work_state > option:nth-child(3)").click()
        # 15 | type | id=id_age | 18
        self.driver.find_element(By.ID, "id_age").send_keys("18")
        # 16 | click | id=id_age |
        self.driver.find_element(By.ID, "id_age").click()
        # 17 | click | id=id_essential |
        self.driver.find_element(By.ID, "id_essential").click()
        # 18 | select | id=id_essential | label=No
        dropdown = self.driver.find_element(By.ID, "id_essential")
        dropdown.find_element(By.XPATH, "//option[. = 'No']").click()
        # 19 | click | css=#id_essential > option:nth-child(3) |
        self.driver.find_element(By.CSS_SELECTOR, "#id_essential > option:nth-child(3)").click()
        # 20 | click | id=id_vaccine_group |
        self.driver.find_element(By.ID, "id_vaccine_group").click()
        # 21 | select | id=id_vaccine_group | label=D
        dropdown = self.driver.find_element(By.ID, "id_vaccine_group")
        dropdown.find_element(By.XPATH, "//option[. = 'D']").click()
        # 22 | click | css=option:nth-child(5) |
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(5)").click()
        # 23 | click | css=input:nth-child(7) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()