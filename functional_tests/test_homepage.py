# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium import webdriver
import unittest, time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.support.wait import WebDriverWait

class HomePageTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(HomePageTest, cls).setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)
  
    @classmethod
    def tearDownClass(cls):
        cls.selenium.refresh()
        cls.selenium.quit()
        super(HomePageTest, cls).tearDownClass()

    def test_displays_home_page(self):
        self.selenium.get(self.live_server_url)
        html = self.selenium.page_source
        self.assertIn('Challenge Accepted!', html)
    
    def test_user_is_presented_with_registration_form(self):
        self.selenium.get(self.live_server_url)
        registration_link = self.selenium.find_element_by_id('button-registration')
        registration_link.click()
        time.sleep(2)
        registration_form = self.selenium.find_element_by_id('form-registration')
        self.assertEqual(registration_form.tag_name, 'form')
        