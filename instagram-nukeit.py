#!/usr/bin/env

import ConfigParser
from time import sleep
from datetime import datetime, timedelta
from collections import OrderedDict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException 
# from selenium.webdriver.support import expected_conditions
# import pickle

class instagramNukeIt():

    def __init__(self, username, password):

        if username == None:
            print "no username provided in config, please add now"
            return False
        if password == None:
            print "no password provided in config"
            return False

        self.username = username
        self.password = password
        chrome_options = webdriver.ChromeOptions()
        # prefs = {"profile.default_content_setting_values.notifications" : 2}
        # chrome_options.add_experimental_option("prefs",prefs)

        self.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", chrome_options=chrome_options)


    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        a = driver.find_element_by_name('username')
        a.send_keys(self.username)
        b = driver.find_element_by_name('password')
        b.send_keys(self.password)
        c = driver.find_element_by_xpath('//button[text()="Log in"]')
        c.click()
        sleep(2)
        
    def untag_photo(self):
        driver = self.driver
        driver.get("https://www.instagram.com/" + self.username  + "/tagged/")
        # Click the Tagged photos button
        # loop the photos, and remove the 
        #driver.find_element_by_xpath()
       

def main():
    config = ConfigParser.ConfigParser()
    config.read('config.cfg')
    ig_username = config.get('instagram', 'username')
    ig_password = config.get('instagram', 'password')
    start_date = config.get('instagram', 'start_date')
    end_date = config.get('instagram', 'end_date')

    igni = instagramNukeIt(ig_username, ig_password)
    igni.login()


if __name__ == '__main__':
    main()
    
# TestUser = instagramNukeIt("aaa", "hello")
# TestUser.login()
# TestUser.untag_photo()
# TestUser.closeBrowser()
