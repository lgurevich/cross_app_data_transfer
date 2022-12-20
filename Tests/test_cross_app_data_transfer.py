from Apps.ContactsApp import ContactsApp
from Apps.MessagesApp import MessagesApp
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import random
import string

def test_cross_app_data_transfer():
    
        ''' Connect to Contacts app and retrieve all contacts visible on the main screen'''
        contactsApp = ContactsApp()
        data_to_be_transfered = contactsApp.get_all_contacts()
        time.sleep(5)
        contactsApp.close_app()

        ''' Connect to Messages app and select a recipient '''
        messagesApp = MessagesApp()
        messagesApp.start_new_conversation()
        messagesApp.select_receipient()

        ''' Generate a random string to add to a transfered data message'''
        random_msg_string = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        message_to_be_sent = f"{random_msg_string} + {data_to_be_transfered}"
        
        ''' Send a message and verify it was received'''
        messagesApp.send_message(message_to_be_sent)
        assert messagesApp.is_message_recieved(message_to_be_sent)
        
        messagesApp.close_app()



