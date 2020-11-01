# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:40:35 2020

@author: Vinod
"""
from selenium import webdriver
from datetime import datetime
import time
import yaml

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


# YYYY, m, d format
start_date = datetime(2018, 1, 1).strftime('%d-%b-%Y %H:%M')
end_date = datetime(2020, 9, 1).strftime('%d-%b-%Y %H:%M')
with open(sfl) as conf:
    stations = yaml.safe_load(conf)
states_2_download = ["West Bengal"]
# states_2_download = states
click_dropdown(0)
dropdown = driver.find_element_by_css_selector('.options')
for state in dropdown.find_elements_by_css_selector('li'):
    if state.text not in states_2_download:
        continue
    state.click()
    time.sleep(4)
    click_dropdown(1)
    dropdown = driver.find_element_by_css_selector('.options')
    for city in dropdown.find_elements_by_css_selector('li'):
        print(city.text)  # get the text in dropdown menu
        # if city.text == "Siliguri":
        city.click()
        time.sleep(2)
        click_dropdown(2)
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
            # Criteria
            dropdown = driver.find_element_by_css_selector('.options')
            dropdown.find_elements_by_css_selector('li')[2].click()
            # select dates
            from_date = driver.find_element_by_xpath('/html/body/app-root/app-caaqm-dashboard/div/div/main/section/app-caaqm-view-data/div/div/div[4]/div[1]/div/div/div/angular2-date-picker/div/div[1]/span')
            driver.execute_script("arguments[0].innerHTML= '{}';".format(start_date),
                                  from_date);
            time.sleep(1)

            to_date = driver.find_element_by_xpath('//*[@id="date2"]/angular2-date-picker/div/div[1]/span')
            driver.execute_script("arguments[0].innerHTML= '{}';".format(end_date),
                                  to_date);
            time.sleep(1)
            # click submit
            driver.find_element_by_xpath('/html/body/app-root/app-caaqm-dashboard/div/div/main/section/app-caaqm-view-data/div/div/div[5]/button').click()
            time.sleep(5)
            # download excel file
            driver.find_element_by_xpath('/html/body/app-root/app-caaqm-dashboard/div/div/main/section/app-caaqm-view-data-report/div[2]/div[1]/div[2]/div/div/a[2]/i').click()
                
