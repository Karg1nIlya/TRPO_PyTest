from selenium.webdriver.chrome.options import Options
import unittest
import time
from selenium import webdriver
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_product_in_basket(browser):
    browser.get(link)
    browser.find_element_by_class_name('btn-add-to-basket').click()
    time.sleep(3)