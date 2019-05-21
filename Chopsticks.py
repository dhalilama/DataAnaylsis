#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 23:00:16 2019

@author: ajay
"""
import matplotlib as plt
import numpy as np
cs = pd.read_table('chopstick2_rcb.dat','\s+')
type1 = cs['type']==1 
type2 = cs['type']==2
type3 = cs['type']==3
type4 = cs['type']==4
type5 = cs['type']==5
type6 = cs['type']==6
good = cs['eff'] >= 27
fair = (cs['eff']>= 22) & (cs['eff'] < 27)
poor = cs['eff']<22 
barwidth=.2
plt.axis([-1, 6, 0, 20])
plt.ylabel('Frequency')
plt.xlabel('Chopsticks Type')
plt.title('Comparison of 6 Lengths of Chopsticks of Feeding Efficiency') 
plt.xticks(np.arange(6)+1/2,['Type1','Type2','Type3','Type4','Type5','Type6']) 

plt.bar(np.arange(6),[len(cs[type1 & good].index),
                      len(cs[type2 & good].index),
                      len(cs[type3 & good].index), 
                      len(cs[type4 & good].index), 
                      len(cs[type5 & good].index), 
                      len(cs[type6 & good].index)], 
        barwidth, color='r', label='Good')
plt.bar(np.arange(6)+barwidth,[len(cs[type1 & fair].index),
                               len(cs[type2 & fair].index),
                               len(cs[type3 & fair].index), 
                               len(cs[type4 & fair].index), 
                               len(cs[type5 & fair].index), 
                               len(cs[type6 & fair].index)], 
        barwidth, color='b', label='fair')
plt.bar(np.arange(6)+2*barwidth,[len(cs[type1 & poor].index),
                                 len(cs[type2 & poor].index),
                                 len(cs[type3 & poor].index), 
                                 len(cs[type4 & poor].index), 
                                 len(cs[type5 & poor].index), 
                                 len(cs[type6 & poor].index)], 
        barwidth, color='g', label='poor')

plt.legend()
plt.show()
