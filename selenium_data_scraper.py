#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 18:00:47 2020

@author: andrii
"""


from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

def get_apartments(city, num_apartments, verbose, slp_time):
    
##Running webdriver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path='/Users/andrii/Documents/Git/ds_apartment_price_estimationa_project/chromedriver', options=options)
    driver.set_window_size(1200, 1200)
    url = 'https://www.spotahome.com/'+ city +''
    driver.get(url)
    apartments = []
    
    while len(apartments) < num_apartments:
        time.sleep(slp_time) #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        
        try:
            driver.find_element_by_id("onetrust-accept-btn-handler").click()
        except ElementClickInterceptedException:
            pass
        
        time.sleep(slp_time)
        
        #Going through each job in this page
        apartment_list = driver.find_elements_by_class_name('l-list__item')
        for apartment_list in apartment_list:
            
            print("Progress: {}".format("" + str(len(apartments)) + "/" + str(num_apartments)))
            if len(apartments) >= num_apartments:
                break
            
            apartment_list.click()  #You might 
            #print('apartment list clicked')
            time.sleep(slp_time)
            collected_successfully = False
            
            while not collected_successfully:
                try:       
                    #main_title = driver.find_element_by_xpath('.//div[@class="property-title"]').text
                    main_title = driver.find_element_by_xpath('.//h1[@class="root__Heading___OmV4c dark__Heading___OmV4c large__Heading___OmV4c left__Heading___OmV4c inline__Heading___OmV4c property-title__heading"]').text
                    property_type = driver.find_element_by_xpath('.//div[@class="property-title__details"]').text
                    monthly_rent = driver.find_element_by_xpath('.//div[@class="list-row list-row--withBorder"]').text                
                    bills = driver.find_element_by_xpath('.//div[@class="bill-description__title__wrapper"]').text
                    property_features = driver.find_element_by_xpath('.//div[@class="listing-tag-container"]').text
                    deposit = driver.find_element_by_xpath('.//b[@class="listing-pricing-structured__security-deposit"]').text
                    property_rules = driver.find_element_by_xpath('.//div[@class="property-rules__collapsible__description"]').text
                    #print('collected main_info')
                    collected_successfully = True
                except:
                    time.sleep(slp_time)

            if verbose:
                print("Main title: {}".format(main_title[:500]))
                print("property_type: {}".format(property_type[:500]))
                print("monthly_rent: {}".format(monthly_rent[:500]))
                print("bills: {}".format(bills[:500]))
                print("property_features: {}".format(property_features[:500]))
                print("deposit: {}".format(deposit[:500]))
                print("property_rules: {}".format(property_rules[:500]))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                #print("Title_2: {}".format(title_2[:500]))
                #print("Price: {}".format(price[:500]))
   

            try:
                driver.find_element_by_xpath('.//button[@class="button__Button___OmV4c alt__Button___OmV4c secondary__Button___OmV4c normal__Button___OmV4c listing-preview-header__button"]').click()  #clicking to the X.
                #print('X button clicked')
            except NoSuchElementException:
                pass

           
            apartments.append({"Main title" : main_title, 
            "property_type" : property_type,
            "monthly_rent" : monthly_rent,
            "bills" : bills,
            "property_features" : property_features,
            "deposit" : deposit,
            "property_rules" : property_rules})
           
            
            #Clicking on the "next page" button
        try:
            driver.find_element_by_xpath('.//l-list__item[@class="next"]//a').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_apartments, len(apartments)))
            break
            
    return pd.DataFrame(apartments)

df = get_apartments('berlin', 2, False, 3)
df
