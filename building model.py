#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:04:33 2021

@author: andrii
"""
#https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html
#https://dss.princeton.edu/online_help/analysis/interpreting_regression.htm


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('df_final.csv')

#create train test split
from sklearn.model_selection import train_test_split
X = df.drop('monthly_price_avg', axis=1)
y = df['monthly_price_avg'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


#Multiple Linear Regression
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error

lm = LinearRegression()
lm.fit(X_train,y_train) 

np.mean(cross_val_score(lm,X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))


#Lasso Regression
lm_l = Lasso()
np.mean(cross_val_score(lm_l,X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))


#Random Forest
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor()
np.mean(cross_val_score(rf,X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))


#RidgeRegression
from sklearn.linear_model import Ridge
r = Ridge()
np.mean(cross_val_score(r,X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))


#ElasticNet
from sklearn.linear_model import ElasticNet

en = ElasticNet()
np.mean(cross_val_score(en,X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))


#Support Vector Regression (kernel='linear')
from sklearn import svm

svm = svm.SVR()
np.mean(cross_val_score(svm,X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))

#tune models GridsearchCV
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse', 'mae'), 'max_features':('auto', 'sqrt', 'log2')}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error', cv=3)
gs.fit(X_train,y_train)

gs.best_score_
gs.best_estimator_


tpred_lm = lm.predict(X_test)
tpred_lm_l = lm.predict(X_test)
tpred_rf = lm.predict(X_test)


from sklearn.metrics import mean_absolute_error

mean_absolute_error(y_test, tpred_lm)
mean_absolute_error(y_test, tpred_lm_l)
mean_absolute_error(y_test, tpred_rf)



import pickle
pickl = {'model': gs.best_estimator_}
pickle.dump( pickl, open( 'model_file' + ".p", "wb" ))




 