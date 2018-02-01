# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

loads_weigths = np.fromfile("C:\\Users\\x0272773\\Desktop\\darknet-master\\yolo.weights", dtype='f')
n = int(loads_weigths.size / 5)
f = open('C:\\Users\\x0272773\\Desktop\\darknet-master\\weight_convert.txt','w')

for i in range(5,n,5):
    msg = ' '.join(str(loads_weigths[j]) for j in range(i,i+5))
    msg+="\r\n"
    print(msg)
    f.writelines(msg)
    print("convert successfully ",i+1,"-",i+5)
    #print(loads_weigths.size,np.max(loads_weigths),np.min(loads_weigths))
f.close()