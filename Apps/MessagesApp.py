from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Apps.BaseApp import BaseApp
from Config.config import TestData
import time
import logging


class MessagesApp(BaseApp):

    NEW_CONVERSATION_BTN = ('ID', "com.google.android.apps.messaging:id/start_new_conversation_button")
    SEND_MSG_BTN = ('ID', "com.google.android.apps.messaging:id/send_message_button_icon")
    RECEIPIENT_OPTION = ('ID', "com.google.android.apps.messaging:id/recipient_text_view")
    MSG_GROUP = ('XPATH', "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]")
    MSG_LINE = ('ID', "com.google.android.apps.messaging:id/compose_message_text")
    MESSAGES_CONTENT = ('ID',"com.google.android.apps.messaging:id/message_content")
    
    def __init__(self):
        logging.info("Starting Messages Application")
        self.driver = webdriver.Remote(TestData.driverURL, TestData.messageAppDesiredCapabilities)

    def start_new_conversation(self):
        
        ''' Starting a new message'''
        logging.info(f"Starting a new conversation")
        self.click(self.NEW_CONVERSATION_BTN)

    def select_receipient(self):

        ''' Selecting a receipient '''
        logging.info("Selecting receipient")
        self.click(self.RECEIPIENT_OPTION)
        self.click(self.MSG_GROUP)

    def send_message(self,data):

        ''' Entering message strin and clicking send '''
        logging.info("Sending a new message")
        self.send_data(self.MSG_LINE,str(data))
        self.click(self.SEND_MSG_BTN)

    def is_message_recieved(self, data):
        
        ''' Getting a list aff available messages'''
        logging.info(f"Validating if message was sent")
        messages =  self.get_elements(self.MESSAGES_CONTENT)
        message_found = False

        '''Iterating through all retrived massages and verifying the message was received '''
        for message in messages:
            if str(data) in message.get_attribute("content-desc"):
                logging.info(f"Message was found in a list of messages")
                message_found = True
        
        return message_found
