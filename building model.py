#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:04:33 2021

@author: andrii
"""
#https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('df_final.csv')

#create train test split
from sklearn.model_selection import train_test_split
X = df.drop('monthly_price_avg', axis=1)
y = df['monthly_price_avg'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


#Multiple Linear Regression
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train,y_train) 

np.mean(cross_val_score(lm,X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))








#Lasso Regression
#ElasticNet
#Random Forest
#RidgeRegression
#Support Vector Regression (kernel='linear')
#tune models GridsearchCV
