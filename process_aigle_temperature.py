#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:06:14 2020

@author: maelebelmont
"""

#Import Numpy

import numpy as np
from matplotlib import pyplot as plt

# Import de Pandas
import pandas as pd
temperatures_aigle = pd.read_csv('aigle_1980-12-31_2019-07-09.csv', sep=';', usecols=[1, 2], index_col=0, parse_dates=True, dtype={'t06200ds': np.float64}, na_values='-')
start_date_1981 = '1981-01-01'
end_date_1981 = '1981-12-31'
temperatures_1981 = temperatures_aigle[start_date_1981 : end_date_1981].values

start_date_1991 = '1991-01-01'
end_date_1991 = '1991-12-31'
temperatures_1991 = temperatures_aigle[start_date_1991 : end_date_1991].values

start_date_2001 = '2001-01-01'
end_date_2001 = '2001-12-31'
temperatures_2001 = temperatures_aigle[start_date_2001 : end_date_2001].values

start_date_2011 = '2011-01-01'
end_date_2011 = '2011-12-31'
temperatures_2011 = temperatures_aigle[start_date_2011 : end_date_2011].values

def average_temperature(year_data):
    avrg_janv = sum(year_data[0:31])/31
    avrg_fev = sum(year_data[31:59])/28
    avrg_mars = sum(year_data[59:90])/31
    avrg_avril = sum(year_data[90:120])/30
    avrg_mai = sum(year_data[120:151])/31
    avrg_juin = sum(year_data[151:181])/30
    avrg_juil = sum(year_data[181:212])/31
    avrg_aout = sum(year_data[212:243])/31
    avrg_sept = sum(year_data[243:273])/30
    avrg_oct = sum(year_data[273:304])/31
    avrg_nov = sum(year_data[304:334])/30
    avrg_dec = sum(year_data[334:365])/31
    
    month = np.array(["janv", "fev", "mars", "avril", "mai", "juin", "juil", "aout", "sept", "oct", "nov", "dec"]).reshape((12,1))
    avrg = np.array([avrg_janv, avrg_fev, avrg_mars, avrg_avril, avrg_mai, avrg_juin, avrg_juil, avrg_aout, avrg_sept, avrg_oct, avrg_nov, avrg_dec]) #tableau contenant les moyennes (des arrays de dimension (1,1))
    month_avrg = np.hstack((month, avrg)) #tableau contenant les mois avec leur température moyenne
    
    year_average = 0
    for i in range(len(avrg)):
        year_average += avrg[i][0]/12
    
    return ("AVERAGE TEMPERATURE EVERY MONTH", month_avrg), ("AVERAGE TEMPERATURE THAT YEAR", year_average)

print("1981\n", average_temperature(temperatures_1981))
print("\n1991\n", average_temperature(temperatures_1991))
print("2001\n", average_temperature(temperatures_2001))
print("2011\n", average_temperature(temperatures_2011))




    
    