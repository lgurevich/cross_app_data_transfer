from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging
class BaseApp:

    ''' Constants'''
    ELEMENT_WAIT_TIME = 30

    ''' Class constructor '''
    def __init__(self, driver):
        self.driver = driver

    ''' Generic App Functions'''
    def get_element(self, by_locator):        

        logging.info(f"Locating element by: {by_locator}")
        ''' Generic method to retrieve an element based on provided locator'''
        if by_locator[0] == 'ID':
            element = WebDriverWait(self.driver, self.ELEMENT_WAIT_TIME).until(EC.visibility_of_element_located((AppiumBy.ID, by_locator[1])))
        if by_locator[0] == 'XPATH':
            element = WebDriverWait(self.driver, self.ELEMENT_WAIT_TIME).until(EC.visibility_of_element_located((AppiumBy.XPATH, by_locator[1])))

        return element

    def get_elements(self, by_locator):
        
        logging.info(f"Locating all elements by: {by_locator}")
        ''' Generic method  to retrieve a list of elements based on provided locator'''
        if by_locator[0] == 'ID':
            elements =  WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located((AppiumBy.ID, by_locator[1])))
        elif by_locator[0] == 'XPATH':
            elements =  WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located((AppiumBy.XPATH , by_locator[1])))

        return elements


    def click(self, by_locator):
        
        logging.info(f"Clicking on element by: {by_locator}")
        ''' Retrieve an element by provided locator and perform click '''
        self.get_element(by_locator).click()

    def send_data(self, by_locator, data):
        
        logging.info(f"Setting data for element by: {by_locator} ")
        ''' Retrieve an element by provided locator and enter data '''
        self.get_element(by_locator).send_keys(data)
        
    def close_app(self):
        logging.info(f"Closing active app")
        self.driver.quit()

