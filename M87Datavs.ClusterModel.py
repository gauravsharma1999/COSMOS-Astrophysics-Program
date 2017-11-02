# -*- coding: utf-8 -*-
# CSV reading
#import plotly.plotly as py
#import plotly.graph_objs as go
import csv
import numpy as np
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import os
"""
Created on Fri Jul 29 11:19:30 2016

@author: Gaurav
"""

"""Cluster Model 2
Variables:
f2
csv_f2
data_list2F606W
data_list2F814W
data_list2F300W
data_list2F450W
count2
jim
x_axis2
y_axis2"""

f2 = open('ye.csv')
csv_f2 = csv.reader(f2)

#Array for F55W
data_list2F606W=[]
data_list2F814W=[]
data_list2F300W=[]
data_list2F450W=[]
count2 = 0

for row in csv_f2:
    if count2 != 0:
        count2 +=1
        data_list2F606W.append((row[8]))
        data_list2F814W.append((row[9]))
        data_list2F300W.append((row[3]))
        data_list2F450W.append((row[6]))
    else:
        count2 += 1
        continue
    

jim = []
jim2 = []
jim3=[]
jim4=[]  
  
for i in range(len(data_list2F606W)):
    try:
         jim.append(float(data_list2F606W[i]))
         jim2.append(float(data_list2F814W[i]))
         jim3.append(float(data_list2F300W[i]))
         jim4.append(float(data_list2F450W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis2 = np.zeros(len(jim))
y_axis2 = np.zeros(len(jim))
for j in range(len(jim)):
    print(j)
    x_axis2[j] = jim[j]-jim2[j]
    y_axis2[j] = jim3[j]-jim4[j]
    

f2.close()

"""Actual Data for M87 Galaxy"""

fActual = open('M87-606.csv')
fActual2= open('M87-814.csv')
fActual3= open('M87-300.csv')
fActual4= open('M87-450.csv')
csv_M87 = csv.reader(fActual)
csv_M872 = csv.reader(fActual2)
csv_M873 = csv.reader(fActual3)
csv_M874 = csv.reader(fActual4)
F606W=[]
F814W=[]
F300W=[]
F450W=[]


#Array for F55W


for row in csv_M87:
    F606W.append(row[12])
    

for row in csv_M872:
   F814W.append(row[12])
       
for row in csv_M873:
    F300W.append(row[12])
    
for row in csv_M874:
   F450W.append(row[12])
    
    
    
M87 = []
M872 = []
M873=[]
M874=[]  
  
for i in range(len(F606W)):
    try:
         M87.append(float(F606W[i]))
         M872.append(float(F814W[i]))
         M873.append(float(F300W[i]))
         M874.append(float(F450W[i]))
    
    except ValueError:
        continue
 #Graph Input

x = np.zeros(len(M87))
y = np.zeros(len(M87))

for j in range(len(M87)):
    print(j)
    x[j] = (M87[j]-0.090-23.01226+22.91335)-(M872[j]-0.058-22.10077+21.68402)
    y[j] = (M873[j]-0.182-20.76789+19.43571)-(M874[j]-0.127-21.93849+22.02992)



plt.plot(x_axis2,y_axis2,"-",label= "Cluster Model 2")
plt.scatter(x,y,color="red",label= "Hubble Legacy Archive Data")
plt.show()