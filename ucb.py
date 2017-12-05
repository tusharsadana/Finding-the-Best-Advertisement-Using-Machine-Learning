# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

N=10000 #number of users
d=10 #number of ads

numbers_of_selection = [0] * d
sums_of_rewards = [0] * d

ads_selected = []


for n in range(N):
    ad=0
    max_upper_bound = 0 
    for i in range(d):
        average_reward = sums_of_rewards[i]/ numbers_of_selection[i]
        delta_i = math.sqrt(3/2 * math.log(n+1) / numbers_of_selection[i] )
        upper_bound = average_reward + delta_i
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
            
        
        
        
    
    