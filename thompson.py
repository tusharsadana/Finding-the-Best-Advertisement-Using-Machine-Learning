# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 04:11:06 2017

@author: Tushar
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

N=10000 #number of users
d=10 #number of ads

zero = [0]*d
one = [0]*d

ads_selected = []
total_reward = 0

for n in range(N):
    ad=0
    max_random = 0 
    for i in range(d):
        random_beta = random.betavariate(one[i]+1, zero[i]+1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    if reward == 1:
        one[ad]+=1
    else:
        zero[ad]+=1
        
    total_reward+=reward

plt.hist(ads_selected)
plt.title("Ads selected")
plt.xlabel("Ads")
plt.ylabel("Number of times each add was selected")
plt.show()

            
        
        
        
    
    