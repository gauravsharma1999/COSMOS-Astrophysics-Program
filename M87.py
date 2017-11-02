# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 09:28:37 2016

@author: Gaurav
"""

# CSV reading
#import plotly.plotly as py
#import plotly.graph_objs as go
import csv
import numpy as np
#import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import pyplot as plt
import os
#os.getcwd()

"""Cluster Model 1
Variables:
f
csv_f
data_listF606W
data_listF814W
data_listF300W
data_listF450W
count
bob
x_axis
y_axis"""

f = open('ClusterModel1.csv')
csv_f = csv.reader(f)

#Array for F555W
data_listF606W=[]
data_listF814W=[]
data_listF300W=[]
data_listF450W=[]
count = 0

for row in csv_f:
    if count != 0:
        count +=1
        data_listF606W.append((row[13]))
        data_listF814W.append((row[18]))
        data_listF300W.append((row[6]))
        data_listF450W.append((row[10]))
    else:
        count += 1
        continue
    

bob = []
bob2 = []
bob3=[]
bob4=[]  
  
for i in range(len(data_listF606W)):
    try:
         bob.append(float(data_listF606W[i]))
         bob2.append(float(data_listF814W[i]))
         bob3.append(float(data_listF300W[i]))
         bob4.append(float(data_listF450W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis = np.zeros(len(bob))
y_axis = np.zeros(len(bob))
for j in range(len(bob)):
    print(j)
    x_axis[j] = bob[j]-bob2[j]
    y_axis[j] = bob3[j]-bob4[j]
    

f.close()

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

f2 = open('ClusterModel2.csv')
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


"""Cluster Model 3
Variables:
f3
csv_f3
data_list3F606W
data_list3F814W
data_list3F300W
data_list3F450W
count3
joe
x_axis3
y_axis3"""

f3 = open('ClusterModel3.csv')
csv_f3 = csv.reader(f3)

#Array for F55W
data_list3F606W=[]
data_list3F814W=[]
data_list3F300W=[]
data_list3F450W=[]
count3 = 0

for row in csv_f3:
    if count3 != 0:
        count3 +=1
        data_list3F606W.append((row[8]))
        data_list3F814W.append((row[9]))
        data_list3F300W.append((row[3]))
        data_list3F450W.append((row[6]))
    else:
        count3 += 1
        continue
    

joe = []
joe2 = []
joe3=[]
joe4=[]  
  
for i in range(len(data_list3F606W)):
    try:
         joe.append(float(data_list3F606W[i]))
         joe2.append(float(data_list3F814W[i]))
         joe3.append(float(data_list3F300W[i]))
         joe4.append(float(data_list3F450W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis3 = np.zeros(len(jim))
y_axis3 = np.zeros(len(jim))
for j in range(len(jim)):
    print(j)
    x_axis3[j] = joe[j]-joe2[j]
    y_axis3[j] = joe3[j]-joe4[j]
    

f3.close()

"""Cluster Model 4
Variables:
f4
csv_f4
data_list4F606W
data_list4F814W
data_list4F300W
data_list4F450W
count4
bill
x_axis4
y_axis4"""

f4 = open('ClusterModel4.csv')
csv_f4 = csv.reader(f4)

#Array for F55W
data_list4F606W=[]
data_list4F814W=[]
data_list4F300W=[]
data_list4F450W=[]
count4 = 0

for row in csv_f4:
    if count4 != 0:
        count4 +=1
        data_list4F606W.append((row[8]))
        data_list4F814W.append((row[9]))
        data_list4F300W.append((row[3]))
        data_list4F450W.append((row[6]))
    else:
        count4 += 1
        continue
    

bill = []
bill2 = []
bill3=[]
bill4=[]  
  
for i in range(len(data_list4F606W)):
    try:
         bill.append(float(data_list4F606W[i]))
         bill2.append(float(data_list4F814W[i]))
         bill3.append(float(data_list4F300W[i]))
         bill4.append(float(data_list4F450W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis4 = np.zeros(len(bill))
y_axis4 = np.zeros(len(bill))
for j in range(len(bill)):
    print(j)
    x_axis4[j] = bill[j]-bill2[j]
    y_axis4[j] = bill3[j]-bill4[j]
    

f4.close()

"""Cluster Model 5
Variables:
f5
csv_f5
data_list5F606W
data_list5F814W
data_list5F300W
data_list5F450W
count5
tom
x_axis5
y_axis5"""

f5 = open('ClusterModel5.csv')
csv_f5 = csv.reader(f5)

#Array for F55W
data_list5F606W=[]
data_list5F814W=[]
data_list5F300W=[]
data_list5F450W=[]
count5 = 0

for row in csv_f5:
    if count5 != 0:
        count5 +=1
        data_list5F606W.append((row[8]))
        data_list5F814W.append((row[9]))
        data_list5F300W.append((row[3]))
        data_list5F450W.append((row[6]))
    else:
        count5 += 1
        continue
    

tom = []
tom2 = []
tom3=[]
tom4=[]  
  
for i in range(len(data_list5F606W)):
    try:
         tom.append(float(data_list5F606W[i]))
         tom2.append(float(data_list5F814W[i]))
         tom3.append(float(data_list5F300W[i]))
         tom4.append(float(data_list5F450W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis5 = np.zeros(len(tom))
y_axis5 = np.zeros(len(tom))
for j in range(len(tom)):
    print(j)
    x_axis5[j] = tom[j]-tom2[j]
    y_axis5[j] = tom3[j]-tom4[j]
    

f5.close()

"""Cluster Model 6
Variables:
f6
csv_f6
data_list6F606W
data_list6F814W
data_list6F300W
data_list6F450W
count6
dan
x_axis6
y_axis6"""

f6 = open('ClusterModel6.csv')
csv_f6 = csv.reader(f6)

#Array for F55W
data_list6F606W=[]
data_list6F814W=[]
data_list6F300W=[]
data_list6F450W=[]
count6 = 0

for row in csv_f6:
    if count6 != 0:
        count6 +=1
        data_list6F606W.append((row[8]))
        data_list6F814W.append((row[9]))
        data_list6F300W.append((row[3]))
        data_list6F450W.append((row[6]))
    else:
        count6 += 1
        continue
    

dan = []
dan2 = []
dan3=[]
dan4=[]  
  
for i in range(len(data_list6F606W)):
    try:
         dan.append(float(data_list6F606W[i]))
         dan2.append(float(data_list6F814W[i]))
         dan3.append(float(data_list6F300W[i]))
         dan4.append(float(data_list6F450W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis6 = np.zeros(len(dan))
y_axis6 = np.zeros(len(dan))
for j in range(len(dan)):
    print(j)
    x_axis6[j] = dan[j]-dan2[j]
    y_axis6[j] = dan3[j]-dan4[j]
    

f6.close()

"""Cluster Model 7
Variables:
f7
csv_f7
data_list7F606W
data_list7F814W
data_list7F300W
data_list7F450W
count7
ted
x_axis7
y_axis7"""

f7 = open('ClusterModel7.csv')
csv_f7 = csv.reader(f7)

#Array for F55W
data_list7F606W=[]
data_list7F814W=[]
data_list7F300W=[]
data_list7F450W=[]
count7 = 0

for row in csv_f7:
    if count7 != 0:
        count7 +=1
        data_list7F606W.append((row[8]))
        data_list7F814W.append((row[9]))
        data_list7F300W.append((row[3]))
        data_list7F450W.append((row[6]))
    else:
        count7 += 1
        continue
    

ted = []
ted2 = []
ted3=[]
ted4=[]  
  
for i in range(len(data_list7F606W)):
    try:
         ted.append(float(data_list7F606W[i]))
         ted2.append(float(data_list7F814W[i]))
         ted3.append(float(data_list7F300W[i]))
         ted4.append(float(data_list7F450W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis7 = np.zeros(len(ted))
y_axis7 = np.zeros(len(ted))
for j in range(len(ted)):
    print(j)
    x_axis7[j] = ted[j]-ted2[j]
    y_axis7[j] = ted3[j]-ted4[j]
    

f7.close()

"""Cluster Model 8
Variables:
f8
csv_f8
data_list8F555W
data_list8F814W
data_list8F336W
data_list8F439W
count8
hal
x_axis8
y_axis8"""

f8 = open('ClusterModel8.csv')
csv_f8 = csv.reader(f8)

#Array for F55W
data_list8F606W=[]
data_list8F814W=[]
data_list8F300W=[]
data_list8F450W=[]
count8 = 0

for row in csv_f8:
    if count8 != 0:
        count8 +=1
        data_list8F606W.append((row[8]))
        data_list8F814W.append((row[9]))
        data_list8F300W.append((row[3]))
        data_list8F450W.append((row[6]))
    else:
        count8 += 1
        continue
    

hal = []
hal2 = []
hal3=[]
hal4=[]  
  
for i in range(len(data_list8F606W)):
    try:
         hal.append(float(data_list8F606W[i]))
         hal2.append(float(data_list8F814W[i]))
         hal3.append(float(data_list8F300W[i]))
         hal4.append(float(data_list8F450W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis8 = np.zeros(len(hal))
y_axis8 = np.zeros(len(hal))
for j in range(len(hal)):
    print(j)
    x_axis8[j] = hal[j]-hal2[j]
    y_axis8[j] = hal3[j]-hal4[j]
    

f8.close()





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

 
fActual.close()

"""Best fit isochrone
Variables:
f2
csv_f2
data_list9F606W
data_list9F814W
data_list9F300W
data_list9F450W
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
x_axis9 = np.zeros(len(jim))
y_axis9 = np.zeros(len(jim))
for j in range(len(jim)):
    print(j)
    x_axis9[j] = jim[j]-jim2[j]
    y_axis9[j] = jim3[j]-jim4[j]
    

f2.close()

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 14}
mpl.rc('font', **font)

plt.xticks([-0.25,0,0.5,1.0,1.5])
plt.plot(x_axis,y_axis,label= "Cluster Model 1")
plt.plot(x_axis2,y_axis2,"-",label= "Cluster Model 2")
plt.plot(x_axis3,y_axis3,"-",label= "Cluster Model 3")
plt.plot(x_axis4,y_axis4,"-",label= "Cluster Model 4")
plt.plot(x_axis5,y_axis5,"-",label= "Cluster Model 5")
plt.plot(x_axis6,y_axis6,"-",label= "Cluster Model 6")
plt.plot(x_axis7,y_axis7,"-",label= "Cluster Model 7")
plt.plot(x_axis8,y_axis8,"-",label= "Cluster Model 8")
plt.scatter(x,y,color="red",label= "Hubble Legacy Archive Data")
plt.xlabel('F606W-F814W', fontsize=16,weight='bold')
plt.ylabel('F300W-F450W', fontsize=16,weight='bold')
plt.plot(x_axis9,y_axis9,"-",linewidth=5)
plt.arrow( 0.0,0.3,0.3556,0.5111, fc="k", ec="k",head_width=0.03, head_length=0.05 )
plt.title('M87 Color-Color Diagram', loc = 'center',weight='bold')
plt.legend(loc= "lower right")
plt.grid(True)
plt.show()
