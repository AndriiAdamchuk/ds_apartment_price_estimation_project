#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:59:50 2021

@author: andrii
"""

import pandas as pd

df = pd.read_csv('df_apartments.csv')

df = df.drop_duplicates()
df = df.drop('Unnamed: 0', axis = 1)

#defining districts in Berlin

def district(name):
    if 'wedding' in name.lower():
        return 'Wedding'
    elif 'prenzlauer berg' in name.lower() or 'prenzlauerberg' in name.lower():
        return 'Prenzlauer Berg'
    elif 'mitte' in name.lower() or 'central berlin' in name.lower():
        return 'Mitte'
    elif 'friedrichshain-kreuzberg' in name.lower():
        return 'Friedrichshain-Kreuzberg'
    elif ' friedrichshain' in name.lower() or ' freidrichshain' in name.lower() or ' ostkreuz' in name.lower():
        return 'Friedrichshain'
    elif 'neukölln' in name.lower() or 'reuterkiez' in name.lower():
        return 'Neukölln'
    elif 'kreuzberg' in name.lower():
        return 'Kreuzberg'
    elif 'charlottenburg' in name.lower():
        return 'Charlottenburg'
    elif 'pankow' in name.lower():
        return 'Pankow'
    elif 'friedenau' in name.lower():
        return 'Friedenau'
    elif 'tempelhof' in name.lower():
        return 'Tempelhof'
    elif 'moabi' in name.lower() or 'moabit' in name.lower():
        return 'Moabit'
    elif 'treptow-köpenick' in name.lower():
        return 'Treptow-Köpenick'
    elif 'tempelhof-schöneberg' in name.lower():
        return 'Tempelhof-Schöneberg'
    elif 'schöneberg' in name.lower():
        return 'Schöneberg'
    elif 'charlottenburg-wilmersdorf' in name.lower():
        return 'Charlottenburg-Wilmersdorf'
    elif 'wilmersdorf' in name.lower():
        return 'Wilmersdorf'
    elif 'lichtenberg' in name.lower():
        return 'Lichtenberg'
    elif 'treptow' in name.lower():
        return 'Treptow'
    elif 'weissensee' in name.lower():
        return 'Weissensee'
    elif 'spandau' in name.lower():
        return 'Spandau'
    elif 'reinickendorf' in name.lower():
        return 'Reinickendorf'
    elif 'westen' in name.lower() or 'westend' in name.lower():
        return 'Westend'
    elif 'adlershof' in name.lower():
        return 'Adlershof'
    elif 'schönefeld' in name.lower() or 'schulzendorf' in name.lower():
        return 'Schönefeld'
    elif 'gesundbrunnen' in name.lower():
        return 'Gesundbrunnen'
    elif 'marzahn' in name.lower():
        return 'Marzahn'
    elif 'teltow' in name.lower():
        return 'Teltow'
    elif 'tiergarten' in name.lower():
        return 'Tiergarten'
    elif 'steglitz' in name.lower():
        return 'Steglitz'
    elif 'hermsdorf' in name.lower():
        return 'Hermsdorf'    
    elif 'rudolfkiez' in name.lower():
        return 'Rudolfkiez'    
    elif 'marienfelde' in name.lower():
        return 'Marienfelde' 
    elif 'bavarian quarter' in name.lower():
        return 'Bavarian Quarter' 
    elif 'rudolfkiez' in name.lower():
        return 'Rudolfkiez' 
    elif 'rudolfkiez' in name.lower():
        return 'Rudolfkiez' 
    elif 'in berlin' in name.lower():
        return 'Berlin'  
    else:
        return('Other')

df['district'] = df['Main title'].apply(district)
#df['district'].value_counts()


#property type
df['property'] = df['property_type'].apply(lambda x: x.split()[0])
df['property'].value_counts()


#flatmates
def flatmates(prop_type):
    if 'flatmates' in prop_type:
        return int(prop_type.split()[1])
    else: 
        return 0

df['flatmates'] = df['property_type'].apply(flatmates)

#avg monthly price
df['monthly_price_min'] = df['monthly_rent'].apply(lambda x: x.split()[-2].split('-')[0])
df['monthly_price_max'] = df['monthly_rent'].apply(lambda x: x.split()[-2].split('-')[-1])

def integer(price):
    if price.isdigit() is True:
        return int(price)
    else:
        return 0

df['monthly_price_min'] = df['monthly_price_min'].apply(integer)
df['monthly_price_max'] = df['monthly_price_max'].apply(integer)
df['monthly_price_avg'] = (df.monthly_price_min + df.monthly_price_max)/2



def null_to_avg(price):
    if price == 0:
        return df[df['monthly_price_avg'] > 0].groupby('property').mean()['monthly_price_avg'][1]
    else:
        return price

    
df['monthly_price_avg'] = df['monthly_price_avg'].apply(null_to_avg)


# defining what's included in the bills
df['bills'] = df['bills'].apply(lambda x: ' '.join(x.splitlines()))                                                         #transforming multiple text lines into list and converting list to string  

df['bills_electricity_yn'] = df['bills'].apply(lambda x: 1 if 'electricity included' in x.lower() else 0)                   #electricity
df['bills_water_yn'] = df['bills'].apply(lambda x: 1 if 'water included' in x.lower() else 0)                               #water
df['bills_gas_yn'] = df['bills'].apply(lambda x: 1 if 'gas included' in x.lower() else 0)                                   #gas
df['bills_wifi_yn'] = df['bills'].apply(lambda x: 1 if 'wifi included' in x.lower() else 0)                                 #wifi


# defining property features
df['property_features'] = df['property_features'].apply(lambda x: ' '.join(str(x).splitlines()))                            #transforming multiple text lines into list and converting list to string  

df['feature_furnished_yn'] = df['property_features'].apply(lambda x: 1 if 'furnished' in x.lower() else 0)                  #furnished
df['feature_dishwasher_yn'] = df['property_features'].apply(lambda x: 1 if 'dishwasher' in x.lower() else 0)                #dishwasher
df['feature_washing_machine_yn'] = df['property_features'].apply(lambda x: 1 if 'washing machine' in x.lower() else 0)      #washing machine
df['feature_equipped_kitchen_yn'] = df['property_features'].apply(lambda x: 1 if 'equipped kitchen' in x.lower() else 0)    #equipped kitchen
df['feature_balcony_yn'] = df['property_features'].apply(lambda x: 1 if 'balcony or terrace' in x.lower() else 0)           #balcony or terrace
df['feature_parking_yn'] = df['property_features'].apply(lambda x: 1 if 'parking' in x.lower() else 0)                      #parking
df['feature_tv_yn'] = df['property_features'].apply(lambda x: 1 if 'tv' in x.lower() else 0)                                #tv
df['feature_oven_yn'] = df['property_features'].apply(lambda x: 1 if 'oven' in x.lower() else 0)                            #oven
df['feature_elevator_yn'] = df['property_features'].apply(lambda x: 1 if 'elevator' in x.lower() else 0)                    #elevator


#deposit
df['deposit'] = df['deposit'].apply(lambda x: x[0] if "month's rent" in x.lower() or "months' rent" in x.lower() else x).apply(lambda x: x.split('€')[0]).apply(lambda x: 0 if 'undefined' in x.lower() else x).apply(lambda x: str(x).replace(",", ""))
df['deposit'] = df.apply(lambda x: int(x['deposit']) * x['monthly_price_avg'] if int(x['deposit']) <= 4 else int(x['deposit']), axis = 1)   


#languages (english, german, russian, spanish)
df['property_rules'] = df['property_rules'].apply(lambda x: ' '.join(str(x).splitlines()))                                  #transforming multiple text lines into list and converting list to string

df['english_spoken_yn'] = df['property_rules'].apply(lambda x: 1 if 'english' in x.lower() else 0)                          #english
df['german_spoken_yn'] = df['property_rules'].apply(lambda x: 1 if 'german' in x.lower() else 0)                            #german
df['russian_spoken_yn'] = df['property_rules'].apply(lambda x: 1 if 'russian' in x.lower() else 0)                          #russian
df['spanish_spoken_yn'] = df['property_rules'].apply(lambda x: 1 if 'spanish' in x.lower() else 0)                          #spanish


#property size
def size(prop_type):
    if 'm2' in prop_type:
        return int(prop_type.split()[-2])
    else:
        return 0

df['total_living_space'] = df['property_type'].apply(size)


#calculating living space per person taking into consideration different types of property
#On average, every inhabitant has access to 44.6 square metres of living space.

df['living_space_per_person'] = df.apply(lambda x: x['total_living_space'] / x['flatmates'] if x['flatmates'] > 0 else x['total_living_space'], axis=1)


df_1 = df[df['living_space_per_person'] > 1].groupby('property').mean()['living_space_per_person']                          #calculating avg space per property for apartment, room, studio

df['space_per_person'] = df.apply(lambda x: df_1[0] if x['living_space_per_person'] <= 1 and 'Apartment' in x['property'] else x['living_space_per_person'], axis = 1)
df['space_per_person'] = df.apply(lambda x: df_1[1] if x['living_space_per_person'] <= 1 and 'Room' in x['property'] else x['space_per_person'], axis = 1)
df['space_per_person'] = df.apply(lambda x: df_1[2] if x['living_space_per_person'] <= 1 and 'Studio' in x['property'] else x['space_per_person'], axis = 1)

#updating missing property size values with (avg space per property * number of flatmates)
df['total_space'] = df.apply(lambda x: x['space_per_person'] * x['flatmates'] if x['total_living_space'] <= 5 and x['flatmates'] > 0 else x['total_living_space'], axis = 1)
df['total_space'] = df.apply(lambda x: x['space_per_person'] if x['total_space'] == 0 and x['flatmates'] == 0 else x['total_space'], axis = 1)

#checking if every inhabitant has access to 44.6 square metres of living space
df['has_access_yn'] = df['space_per_person'].apply(lambda x: 1 if x >= 44.6 else 0)

#print(df.columns.tolist())

df_eda = df[['district',
             'property', 
             'flatmates',
             'deposit',
             'monthly_price_avg',
             'space_per_person', 
             'total_space', 
             'has_access_yn',
             'bills_electricity_yn', 
             'bills_water_yn', 
             'bills_gas_yn', 
             'bills_wifi_yn', 
             'feature_furnished_yn', 
             'feature_dishwasher_yn', 
             'feature_washing_machine_yn', 
             'feature_equipped_kitchen_yn', 
             'feature_balcony_yn', 
             'feature_parking_yn', 
             'feature_tv_yn', 
             'feature_oven_yn', 
             'feature_elevator_yn', 
             'english_spoken_yn', 
             'german_spoken_yn', 
             'russian_spoken_yn', 
             'spanish_spoken_yn',
             'Main title', 
             'property_type', 
             'monthly_rent', 
             'bills', 
             'property_features', 
             'property_rules', 
             'monthly_price_min', 
             'monthly_price_max',  
             'total_living_space', 
             'living_space_per_person']]

df_eda.to_csv('df_eda.csv', index=False)
