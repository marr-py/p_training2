# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest


class TestAddGroup3(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        binary = FirefoxBinary("C:\Program Files\Mozilla Firefox\Firefox.exe")
        self.wd = webdriver.Firefox(firefox_binary=binary)
        self.wd.implicitly_wait(30)

    def test_add_group3(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("group no. 2")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("header")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("group header")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("footergroup")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("group 3")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("lasdkkjflks")
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("ldfkgjolj")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_link_text("Logout").click()


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
