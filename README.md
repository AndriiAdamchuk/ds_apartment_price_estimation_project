# Property Rent Price Estimation Project
- Creted property rent estimation tool (MAE ˜53 EUR) to help people understand price thresholds in Berlin.
- Scraped 1000 property offers from spotahome.com using python and selenium.
- Engeneered features from text to define what property features and utility bills are included in the offering.
- Optimized Linear and Random Forest Regressors using GridSearchCV to find the best model.
- Client facing API using flask in progress...

## Code and Resources
- __Python Version__ 3.7
- __Packages__: pandas, numpy, plotly, selenium, sklearn
- __Scraper Article__: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
- __Markdown Cheatsheet__: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

## Web Scraping
Adjusted the web scraper code to collect the following information about 1000 property offers available in Berlin (Jan 2021).

- Main title
- Property type
- Monthly rent
- Bills
- Property features
- Deposit
- Property rules

## Data Cleaning
Cleaned the data to use for my model. The following changes have been made:

- Cleaned districts in Berlin (37).
- Cleaned property type (3).
- Parced min, max, avg monthly rent price.
- Parced flatmates number.
- Created columns including bills options:
  - Electricity
  - Water
  - Gas
  - WiFi
- Created columns including property features:
  - Furnished
  - Dishwasher
  - Washing mashine
  - Equipped kitchen
  - Balcony
  - Parking
  - TV
  - Oven
  - Elevator
- Parced deposit price.
- Created columns including languages spoken by landlords:
  - English
  - German
  - Russian
  - Spanish
- Created columns for property size, living space per person, if every inhabitant can have an access to 44.6 square metres of living space (german baseline)

## Exploratory Data Analysis
I checked the data distribution, correlation between features, counts categorical variables. Some graphs below. 

![](images/ds_apartment_price_estimation_newplot.png)
![](images/ds_apartment_price_estimation_hist3.png)
![](images/ds_apartment_price_estimation_map.png)
![](images/ds_apartment_price_estimation_corrplot.png)

## Model Building

- Transformed categorical variables into dummy variables. 
- Split data into train and test sets. Train set (30%).
- Used Mean Absolute Error to evaluate models. MAE was used because outliers are not bad for this type of model.
- Tried 6 models:
  - __Multiple Linear Regression__ - baseline for the model
  - __Random Forest__ - data has a lot of sparcity I decided to try RF __(best result)__
  - __RidgeRegression__ - works with small dataset and large number of features
  - __Lasso Regression__ - works with small dataset and large number of features
  - __ElasticNet__ 
  - __Support Vector Regression (kernel='linear')__ - works with small dataset and large number of features  __(worst result)__
  
  

## Model Performance
The Random Forest performed better then the rest models.

- __Random Forest__: MAE =  53.73

- __Lasso Regression__: MAE = 86.19
- __RidgeRegression__: MAE = 87.47
- __Multiple Linear Regression__: MAE = 88.70
- __ElasticNet__: MAE = 96.04
- __Support Vector Regression (kernel='linear')__: MAE = 371.62


## Production
...

