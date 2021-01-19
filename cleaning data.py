#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:59:50 2021

@author: andrii
"""

import pandas as pd
import numpy as np

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
    elif 'friedrichshain' in name.lower() or 'freidrichshain' in name.lower() or 'ostkreuz' in name.lower():
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
    elif 'moabi' in name.lower():
        return 'Moabi'
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
    elif 'westen' in name.lower():
        return 'Westen'
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



