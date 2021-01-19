#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:43:44 2021

@author: andrii
"""

import selenium_data_scraper as sds
import pandas as pd
path='/Users/andrii/Documents/Git/ds_apartment_price_estimationa_project/chromedriver'

df = sds.get_apartments('berlin', 1000, path, False, 8)
df.to_csv("df_apartments.csv") 