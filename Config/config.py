class TestData:
    driverURL = 'http://127.0.0.1:4723/wd/hub'
    
    contactsAppDesiredCapabilities = {
        "platformName": "android",
        "appium:platformVersion": "12",
        "appium:deviceName": "FakeAndroid",
        "appium:appPackage": "com.android.contacts",
        "appium:appActivity": "com.android.contacts.activities.PeopleActivity"  
    }

    messageAppDesiredCapabilities = {
        "platformName": "android",
        "appium:platformVersion": "12",
        "appium:deviceName": "FakeAndroid",
        "appium:appPackage": "com.google.android.apps.messaging",
        "appium:appActivity": "com.google.android.apps.messaging.ui.ConversationListActivity"  
    }