# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:35:03 2020

@author: Vinod
"""

from selenium import webdriver
import yaml
import time

driver_path = r'D:\postdoc\Collab\Mohali\chromedriver\chromedriver.exe'
sfl = r'D:\postdoc\Collab\Mohali\cpcb_downloader\cpcb-downloader\station.yml'
driver = webdriver.Chrome(driver_path)
url = 'https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing/data'
driver.get(url)
time.sleep(8)  # sleep some time for waiting


def click_dropdown(idx):
    elem = driver.find_elements_by_class_name('toggle')[idx]
    # get the first dropdown button
    elem.click()  # click it.


stations = {}
click_dropdown(0)
dropdown_state = driver.find_element_by_css_selector('.options')
num_states = len(dropdown_state.find_elements_by_css_selector('li'))
for s in range(num_states):
    state = dropdown_state.find_elements_by_css_selector('li')[s]
    state_name = state.text
    stations[state_name] = {}
    state.click()
    time.sleep(2)
    click_dropdown(1)
    dropdown_city = driver.find_element_by_css_selector('.options')
    num_city = len(dropdown_city.find_elements_by_css_selector('li'))
    for i in range(num_city):
        city = dropdown_city.find_elements_by_css_selector('li')[i]
        city_name = dropdown_city.find_elements_by_css_selector('li')[i].text
        stations[state_name][city_name] = []
        city.click()
        time.sleep(2)
        click_dropdown(2)
        dropdown_station = driver.find_element_by_css_selector('.options')
        for station in dropdown_station.find_elements_by_css_selector('li'):
            stations[state_name][city_name].append(station.text)
        # Activate city refernce again
        if i < num_city:
            click_dropdown(1)
            dropdown_city = driver.find_element_by_css_selector('.options')
    # Activate state refernce again
    if s < num_states:
        click_dropdown(0)
        dropdown_state = driver.find_element_by_css_selector('.options')
driver.close()
# save the state dictionary as yaml
with open(sfl, 'w') as outfile:
    yaml.dump(stations, outfile, default_flow_style=False)
