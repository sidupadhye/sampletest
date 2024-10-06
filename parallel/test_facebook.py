import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_facebook():
    driver=webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    expected_title="YES facebook"
    actual_title=driver.title
    assert actual_title.__eq__(expected_title)
    assert driver.find_element(By.LINK_TEXT,"Meta Pay").click()
    driver.quit()