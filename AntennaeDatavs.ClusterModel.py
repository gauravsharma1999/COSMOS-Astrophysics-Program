# -*- coding: utf-8 -*-
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
Created on Fri Jul 29 11:35:48 2016

@author: Gaurav
"""

"""Cluster Model 7
Variables:
f7
csv_f7
data_list7F555W
data_list7F814W
data_list7F336W
data_list7F439W
count7
ted
x_axis7
y_axis7"""

f7 = open('yeye.csv')
csv_f7 = csv.reader(f7)

#Array for F55W
data_list7F555W=[]
data_list7F814W=[]
data_list7F336W=[]
data_list7F439W=[]
count7 = 0

for row in csv_f7:
    if count7 != 0:
        count7 +=1
        data_list7F555W.append((row[7]))
        data_list7F814W.append((row[9]))
        data_list7F336W.append((row[4]))
        data_list7F439W.append((row[5]))
    else:
        count7 += 1
        continue
    

ted = []
ted2 = []
ted3=[]
ted4=[]  
  
for i in range(len(data_list7F555W)):
    try:
         ted.append(float(data_list7F555W[i]))
         ted2.append(float(data_list7F814W[i]))
         ted3.append(float(data_list7F336W[i]))
         ted4.append(float(data_list7F439W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis7 = np.zeros(len(ted))
y_axis7 = np.zeros(len(ted))
for j in range(len(ted)):
    x_axis7[j] = ted[j]-ted2[j]
    y_axis7[j] = ted3[j]-ted4[j]
    

f7.close()

"""Actual Data for Antennae Galaxies"""

fActual = open('F555Wsort.csv')
fActual2= open('F814Wsort.csv')
fActual3= open('F336Wsort.csv')
fActual4= open('F439Wsort.csv')
csv_Antennae = csv.reader(fActual)
csv_Antennae2 = csv.reader(fActual2)
csv_Antennae3 = csv.reader(fActual3)
csv_Antennae4 = csv.reader(fActual4)

tempList=[]
tempList2=[]
tempList3=[]
tempList4=[]

filter1=[]
filter2=[]
filter3=[]
filter4=[]

F555W=[]
F814W=[]
F336W=[]
F439W=[]

filter1_strings = [thing for thing in csv_Antennae]

for i in range(len(filter1_strings)):
    try:
        tempList.append(float(filter1_strings[i][0]))
        tempList.append(float(filter1_strings[i][1]))
    except ValueError:
        continue

    filter1.append(tempList)
    tempList=[]

filter2_strings=[x for x in csv_Antennae2]

for i in range(len(filter2_strings)):
    try:    
        tempList2.append(float(filter2_strings[i][0]))
        tempList2.append(float(filter2_strings[i][1]))
    except ValueError:
        continue
    
    filter2.append(tempList2)
    tempList2=[]

filter3_strings=[x for x in csv_Antennae3]

for i in range(len(filter3_strings)):
    try:
        tempList3.append(float(filter3_strings[i][0]))
        tempList3.append(float(filter3_strings[i][1]))
    
    except ValueError:
        continue
    filter3.append(tempList3)
    tempList3=[]
    
filter4_strings=[x for x in csv_Antennae4]
        
for i in range(len(filter4_strings)):
    try:    
        tempList4.append(float(filter4_strings[i][0]))
        tempList4.append(float(filter4_strings[i][1]))
    except ValueError:
        continue
    filter4.append(tempList4)
    tempList4=[]
    
"""antennae = []
antennae2 = []
antennae3=[]
antennae4=[]  

for i in range(len(filter4)):
    try:
         antennae.append(float(filter1[i]))
         antennae2.append(float(filter2[i]))
         antennae3.append(float(filter3[i]))
         antennae4.append(float(filter4[i]))
    
    except ValueError:
        continue
   """ 
f1_ID = []
f2_ID= []
f3_ID=[]
f4_ID=[]

for i in range(len(filter2)):
    f1_ID.append(filter1[i][0])

for i in range(len(filter2)):
    f2_ID.append(filter2[i][0])

for i in range(len(filter2)):
    f3_ID.append(filter3[i][0])
    
for i in range(len(filter2)):
    f4_ID.append(filter4[i][0])
    
    try:
        a=f2_ID.index(filter1[i][0])
        b=f3_ID.index(filter1[i][0])
        c=f4_ID.index(filter1[i][0])
        #if abs(filter1[i][0]-filter2[j][0])<0.0001 and abs(filter1[i][0]-filter3[j][0])<0.0001 and abs(filter1[i][0]-filter4[i][0])<0.0001: 
           # print("Appended: ", filter1[row][1])
        F555W.append(filter1[i][1])
        F814W.append(filter2[a][1])
        F336W.append(filter3[b][1])
        F439W.append(filter4[c][1])
        print("shduqwh")
    except ValueError:
         continue

#Array for F55W

"""countAntennae = 0

for row in csv_Antennae:
    if countAntennae != 0:
        countAntennae +=1
        F555W.append((row[2]))
        F814W.append((row[3]))
        F336W.append((row[0]))
        F439W.append((row[1]))               
    else:
        countAntennae += 1
        continue
   """ 


  

 #Graph Input

x = np.zeros(len(F814W))
y = np.zeros(len(F814W))

for j in range(len(F814W)):
    x[j] = (F555W[j]-0.123-22.57336+22.57747)-(F814W[j]-0.069-22.10077+21.68402)
    y[j] = (F336W[j]-0.199-20.61961+19.44119)-(F439W[j]-0.162-20.77772+20.93019)

 
fActual.close()

plt.plot(x_axis7,y_axis7,"-",label= "Cluster Model 7")
plt.scatter(x,y,color="red",label= "Hubble Legacy Archive Data")
plt.show()