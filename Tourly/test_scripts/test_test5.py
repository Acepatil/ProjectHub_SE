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

class TestTest5():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test5(self):
    self.driver.get("http://127.0.0.1:5500/login.html")
    self.driver.set_window_size(794, 864)
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("raghu123@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("12345")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "open_menu").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > .navbar-link").click()
    self.driver.find_element(By.ID, "open_menu").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > .navbar-link").click()
    self.driver.find_element(By.ID, "open_menu").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .navbar-link").click()
    self.driver.find_element(By.ID, "open_menu").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) > .navbar-link").click()
    self.driver.find_element(By.ID, "open_menu").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(6) > .navbar-link").click()
  