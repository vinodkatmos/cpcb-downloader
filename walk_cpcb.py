# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:40:35 2020

@author: Vinod
"""
# %% imports and definitions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date
import time
import yaml


def click_dropdown(idx):
    elem = driver.find_elements_by_class_name('toggle')[idx]
    # get the first dropdown button
    elem.click()  # click it.


def date_picker(date_time, typ):
    year = date_time.year
    month = date_time.strftime('%b').upper()
    day = date_time.day
    from_date = driver.find_element_by_xpath('//*[@id="{}"]/angular2-date-picker/div/div[1]/i'.format(typ))
    from_date.click()
    from_year = driver.find_element_by_xpath('//*[@id="{}"]/angular2-date-picker/div/div[2]/div[3]/div'.format(typ))
    from_year.click()
    driver.find_element_by_xpath('//*[@id="{}"]'.format(year)).click()
    from_month = driver.find_element_by_xpath('//*[@id="{}"]/angular2-date-picker/div/div[2]/div[2]/div'.format(typ))
    from_month.click()
    # driver.find_element_by_xpath('//*[@id="{}"]'.format(month)).click()
    driver.find_element_by_id('{}'.format(typ)).find_element_by_class_name('months-view').find_element_by_id(month).click()
    row = 1 + int(day/7)
    col = (day % 7) + 1
    driver.find_element_by_xpath('//*[@id="{}"]/angular2-date-picker/div/div[2]/table[2]/tbody/tr[{}]/td[{}]/span'.format(typ, row, col)).click()
    driver.find_element_by_xpath('//*[@id="{}"]/angular2-date-picker/div/div[2]/div[6]/div'.format(typ)).click()


# YYYY, m, d format
start_date = date(2018, 1, 1)
end_date = date(2019, 12, 1)
driver_path = r'D:\postdoc\Collab\Mohali\chromedriver\chromedriver.exe'
sfl = r'D:\postdoc\Collab\Mohali\cpcb_downloader\cpcb-downloader\station.yml'
url = 'https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing/data'
with open(sfl) as conf:
    stations = yaml.safe_load(conf)

# %% loop through differnet stations
state_2_download = ['Punjab']
for state_text in stations.keys():
    if state_text not in state_2_download:
        continue
    for city_text in stations[state_text].keys():
        for station_text in stations[state_text][city_text]:
            driver = webdriver.Chrome(driver_path)
            driver.get(url)
            delay = 8  # sleep some time (in seconds) for waiting
            try:
                myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'toggle')))
                print("Page is ready!")
            except TimeoutException:
                print("Loading took too much time!")
                continue
            click_dropdown(0)
            dropdown = driver.find_element_by_css_selector('.options')
            for state in dropdown.find_elements_by_css_selector('li'):
                downloaded = False
                if state.text == state_text:
                    state.click()
                    time.sleep(2)
                    click_dropdown(1)
                    dropdown = driver.find_element_by_css_selector('.options')
                    for city in dropdown.find_elements_by_css_selector('li'):
                        if city.text != city_text:
                            continue
                        city.click()
                        time.sleep(2)
                        click_dropdown(2)
                        dropdown = driver.find_element_by_css_selector('.options')
                        for station in dropdown.find_elements_by_css_selector('li'):
                            if station.text != station_text:
                                continue
                            station.click()
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
                            # start date
                            date_picker(start_date, "date")    
                            # end date
                            date_picker(end_date, "date2")  # not working
                            # to_date = driver.find_element_by_xpath('//*[@id="date2"]/angular2-date-picker/div/div[1]/span')
                            driver.execute_script("arguments[0].innerHTML= '{}';".format(end_date),
                                                  to_date);
                            time.sleep(1)
                            # click submit
                            driver.find_element_by_xpath('/html/body/app-root/app-caaqm-dashboard/div/div/main/section/app-caaqm-view-data/div/div/div[5]/button').click()
                            time.sleep(5)
                            # download excel file
                            driver.find_element_by_xpath('/html/body/app-root/app-caaqm-dashboard/div/div/main/section/app-caaqm-view-data-report/div[2]/div[1]/div[2]/div/div/a[2]/i').click()           
                            time.sleep(10)
                            driver.close()
                            downloaded = True
                        break
                if downloaded:
                    break
