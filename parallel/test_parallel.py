import time

import pytest
from selenium import webdriver

def test_google():
    driver=webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.close()

def test_filpkart():
    driver=webdriver.Chrome()
    driver.get("https://www.filpkart.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.close()

def test_facebook():
    driver=webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.close()

def test_nike():
    driver=webdriver.Chrome()
    driver.get("https://www.nike.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.close()

def test_w3school():
    driver=webdriver.Chrome()
    driver.get("https://www.w3school.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.close()
