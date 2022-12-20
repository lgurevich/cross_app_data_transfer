from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Apps.BaseApp import BaseApp
from Config.config import TestData

import logging
import time

class ContactsApp(BaseApp):

    ''' Screen Locators '''
    CONTACTS = ('ID',"com.android.contacts:id/cliv_name_textview")
    
    ''' Class constructor '''
    def __init__(self):
        logging.info("Starting Contacts application")
        self.driver =  webdriver.Remote(TestData.driverURL, TestData.contactsAppDesiredCapabilities)

    ''' App functions '''
    def get_all_contacts(self):

        logging.info("Getting contacts information")
        ''' Retriving all contact objects from the main screen and getting text value of each retrieved contact '''
        contacts = self.get_elements(self.CONTACTS)
        time.sleep(5)
        list_of_contacts = []
        
        for contact in contacts:
            text = contact.get_attribute('text')
            list_of_contacts.append(text)
        
        return list_of_contacts

