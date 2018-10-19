#!/usr/bin/env

import ConfigParser
from time import sleep
from datetime import datetime, timedelta
from collections import OrderedDict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

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
        
    def tagged_photos(self):
        driver = self.driver
        tagged = driver.get("https://www.instagram.com/" + self.username  + "/tagged/")
        sleep(2)
        self.untag_photo()

        
    def untag_photo(self):
        # Recursive function will run until there are no more div's with the class name.
        driver = self.driver
        div = driver.find_elements_by_class_name("v1Nh3")
        if len(div) < 1:
            return False
        first_item = div[0]
        a = first_item.find_element_by_tag_name("a").click()
        sleep(2)
        driver.find_element_by_class_name("glyphsSpriteMore_horizontal__outline__24__grey_9").click()
        sleep(2)
        driver.find_element_by_xpath('//button[text()="Post Options"]').click()
        sleep(2)
        driver.find_element_by_xpath('//button[text()="Remove Tag"]').click()
        sleep(2)
        driver.find_element_by_xpath('//button[text()="Remove"]').click()
        sleep(2)
        driver.get("https://www.instagram.com/" + self.username  + "/tagged/")
        sleep(2)
        self.untag_photo()

    def saved_photos(self):
        driver = self.driver
        tagged = driver.get("https://www.instagram.com/" + self.username  + "/saved/")
        sleep(2)
        self.unsave_photo()

        
    def unsave_photo(self):
        # Recursive function will run until there are no more div's with the class name.
        driver = self.driver
        div = driver.find_elements_by_class_name("v1Nh3")
        if len(div) < 1:
            return False
        first_item = div[0]
        a = first_item.find_element_by_tag_name("a").click()
        sleep(2)
        driver.find_element_by_class_name("glyphsSpriteSave__filled__24__grey_9").click()
        sleep(2)
        driver.get("https://www.instagram.com/" + self.username  + "/saved/")
        sleep(2)
        self.unsave_photo()


def main():
    config = ConfigParser.ConfigParser()
    config.read('config.cfg')
    ig_username = config.get('instagram', 'username')
    ig_password = config.get('instagram', 'password')
    igni = instagramNukeIt(ig_username, ig_password)
    igni.login()
    igni.tagged_photos()
    igni.saved_photos()


if __name__ == '__main__':
    main()

