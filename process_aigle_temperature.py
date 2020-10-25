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

def Average_Temperature(year_data, year):
    avrg_janv = np.nanmean(year_data[0:31])
    avrg_fev = np.nanmean(year_data[31:59])
    avrg_mars = np.nanmean(year_data[59:90])
    avrg_avril = np.nanmean(year_data[90:120])
    avrg_mai = np.nanmean(year_data[120:151])
    avrg_juin = np.nanmean(year_data[151:181])
    avrg_juil = np.nanmean(year_data[181:212])
    avrg_aout = np.nanmean(year_data[212:243])
    avrg_sept = np.nanmean(year_data[243:273])
    avrg_oct = np.nanmean(year_data[273:304])
    avrg_nov = np.nanmean(year_data[304:334])
    avrg_dec = np.nanmean(year_data[334:365])
    
    """month = np.array(["janv", "fev", "mars", "avril", "mai", "juin", "juil", "aout", "sept", "oct", "nov", "dec"])"""
    avrg = np.array([avrg_janv, avrg_fev, avrg_mars, avrg_avril, avrg_mai, avrg_juin, avrg_juil, avrg_aout, avrg_sept, avrg_oct, avrg_nov, avrg_dec]) #tableau contenant les moyennes (des arrays de dimension (1,1))
    
    year_average = 0
    for i in range(len(avrg)):
        year_average += avrg[i]/12
    
    return ("Average temperature", avrg), ("Year average", (format(year_average, ".2f")))

"""print("1981\n", Average_Temperature(temperatures_1981, 1981))
print("\n1991\n", Average_Temperature(temperatures_1991, 1991))
print("2001\n", Average_Temperature(temperatures_2001, 2001))
print("2011\n", Average_Temperature(temperatures_2011, 2011))"""

mean_1981, year_avrg_1981 = Average_Temperature(temperatures_1981, 1981) 
mean_1991, year_avrg_1991 = Average_Temperature(temperatures_1991, 1991)
mean_2001, year_avrg_2001 = Average_Temperature(temperatures_2001, 2001)
mean_2011, year_avrg_2011 = Average_Temperature(temperatures_2011, 2011)


plt.figure(figsize=(8,6), dpi=120)
x = np.arange(1,13)
plt.plot(x, mean_1981[1], color='b', label='1981 mean = ' +str(year_avrg_1981[1])) 
plt.plot(x, mean_1991[1], color='g', label='1991 mean = ' +str(year_avrg_1991[1]))           
plt.plot(x, mean_2001[1], color='tab:orange', label='2001 mean = ' +str(year_avrg_2001[1]))
plt.plot(x, mean_2011[1], color='r', label='2011 mean = ' +str(year_avrg_2011[1]))
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],["janv", "fev", "mars", "avril", "mai", "juin", "juil", "aout", "sept", "oct", "nov", "dec"])
plt.grid(axis="y")
plt.xlabel("months")
plt.ylabel("mean temperature")
plt.title("Aigle - Average temperature per month")
plt.legend()
plt.show()