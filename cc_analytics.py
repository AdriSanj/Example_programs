# -*- coding: utf-8 -*-
"""
Created on Sun May  9 16:04:16 2021

@author: adria
"""
# Program for plot the value and rentability of cryptocurrencies.
# When the graphic is plotted, I recomend to use full screen mode for see
# the dates.

import numpy as np
import matplotlib.pyplot as plt
import investpy
from datetime import *

#----------------------------------------------------------#

def rentability(Data):
    # Function for calculate rentability.
    l = len(Data)
    R_n = np.zeros(l-1)
    for i in range(l-1):
        R_n[i] = Data[i+1]/Data[i]-1
    return R_n

#----------------------------------------------------------#

interval = 60               # Interval of days in the graphic

end_date = date.today()     # Today
ini_date = end_date - timedelta(days = interval)   # Initial day.

# Conversion to format dd/mm/yyyy for the investpy library.

end_date = end_date.strftime("%d/%m/%Y")
end_date = str(end_date)
ini_date = ini_date.strftime("%d/%m/%Y")
ini_date = str(ini_date)

print('Initial date: ', ini_date)
print('Ending date: ', end_date)

#----------------------------------------------------------#
# Election of the cryptocurrency.

currencie = input('Select cryptocurrency: ')

data = investpy.get_crypto_historical_data(crypto = currencie, from_date = ini_date, to_date = end_date)

#----------------------------------------------------------#

head_list = ['Open', 'High', 'Low', 'Close']  
h = 0       # Element of the head_list
    
rent = rentability(data[head_list[h]])

#----------------------------------------------------------#
# Plotting

plt.figure()
plt.subplot(2,1,1)
plt.plot(data[head_list[h]])
plt.grid(True, linestyle = '--', color = 'black', alpha = 0.5)
plt.title('Value')
plt.subplot(2,1,2)
plt.title('Rentability')
plt.plot(rent)
plt.xlabel('Day.')
plt.grid(True, linestyle = '--', color = 'black', alpha = 0.5)
plt.show()
