# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:40:35 2020

@author: Vinod
"""
from selenium import webdriver
import time
driver_path = r'D:\postdoc\Collab\Mohali\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(driver_path)
url = 'https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing/data'
driver.get(url)
time.sleep(8)  # sleep some time for waiting

elem = driver.find_elements_by_class_name('toggle')[0]
# get the first dropdown button
elem.click()  # click it.

dropdown = driver.find_element_by_css_selector('.options')
for state in dropdown.find_elements_by_css_selector('li'):
    print(state.text)  # get the text in dropdown menu
    if state.text == "West Bengal":
        state.click()
        time.sleep(4)
        elem = driver.find_elements_by_class_name('toggle')[1]
        # get the second dropdown button
        elem.click()  # click it.
        dropdown = driver.find_element_by_css_selector('.options')
        for city in dropdown.find_elements_by_css_selector('li'):
            print(city.text)  # get the text in dropdown menu
            if city.text == "Siliguri":
                city.click()
                time.sleep(4)
                elem = driver.find_elements_by_class_name('toggle')[2]
                # get the third dropdown button
                elem.click()
                time.sleep(4)
                dropdown = driver.find_element_by_css_selector('.options')
                for station in dropdown.find_elements_by_css_selector('li'):
                    print(station.text)
                    station.click()
                    # dropdown = driver.find_element_by_css_selector('fa fa-angle-down')
                    driver.find_element_by_xpath("//*[text()='Select Parameter']").click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//*[text()='Select All']").click()
                    driver.find_elements_by_class_name('toggle')[3].click()
                    # Tabular
                    dropdown = driver.find_element_by_css_selector('.options')
                    dropdown.find_elements_by_css_selector('li')[0].click()
                    time.sleep(1)
                    driver.find_elements_by_class_name('toggle')[4].click()
                    # Tabular
                    dropdown = driver.find_element_by_css_selector('.options')
                    dropdown.find_elements_by_css_selector('li')[2].click()
                    
