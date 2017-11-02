# CSV reading
#import plotly.plotly as py
#import plotly.graph_objs as go
import csv
import numpy as np
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import os
import matplotlib as mpl
from matplotlib import rc, rcParams
#os.getcwd()

"""Cluster Model 1
Variables:
f
csv_f
data_listF555W
data_listF814W
data_listF336W
data_listF439W
count
bob
x_axis
y_axis"""

f = open('ClusterModel1.csv')
csv_f = csv.reader(f)

#Array for F55W
data_listF555W=[]
data_listF814W=[]
data_listF336W=[]
data_listF439W=[]
count = 0

for row in csv_f:
    if count != 0:
        count +=1
        data_listF555W.append((row[11]))
        data_listF814W.append((row[18]))
        data_listF336W.append((row[7]))
        data_listF439W.append((row[9]))
    else:
        count += 1
        continue
    

bob = []
bob2 = []
bob3=[]
bob4=[]  
  
for i in range(len(data_listF555W)):
    try:
         bob.append(float(data_listF555W[i]))
         bob2.append(float(data_listF814W[i]))
         bob3.append(float(data_listF336W[i]))
         bob4.append(float(data_listF439W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis = np.zeros(len(bob))
y_axis = np.zeros(len(bob))
for j in range(len(bob)):
    x_axis[j] = bob[j]-bob2[j]
    y_axis[j] = bob3[j]-bob4[j]
    

f.close()

"""Cluster Model 2
Variables:
f2
csv_f2
data_list2F555W
data_list2F814W
data_list2F336W
data_list2F439W
count2
jim
x_axis2
y_axis2"""

f2 = open('ClusterModel2.csv')
csv_f2 = csv.reader(f2)

#Array for F55W
data_list2F555W=[]
data_list2F814W=[]
data_list2F336W=[]
data_list2F439W=[]
count2 = 0

for row in csv_f2:
    if count2 != 0:
        count2 +=1
        data_list2F555W.append((row[7]))
        data_list2F814W.append((row[9]))
        data_list2F336W.append((row[4]))
        data_list2F439W.append((row[5]))
    else:
        count2 += 1
        continue
    

jim = []
jim2 = []
jim3=[]
jim4=[]  
  
for i in range(len(data_list2F555W)):
    try:
         jim.append(float(data_list2F555W[i]))
         jim2.append(float(data_list2F814W[i]))
         jim3.append(float(data_list2F336W[i]))
         jim4.append(float(data_list2F439W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis2 = np.zeros(len(jim))
y_axis2 = np.zeros(len(jim))
for j in range(len(jim)):
    x_axis2[j] = jim[j]-jim2[j]
    y_axis2[j] = jim3[j]-jim4[j]
    

f2.close()


"""Cluster Model 3
Variables:
f3
csv_f3
data_list3F555W
data_list3F814W
data_list3F336W
data_list3F439W
count3
joe
x_axis3
y_axis3"""

f3 = open('ClusterModel3.csv')
csv_f3 = csv.reader(f3)

#Array for F55W
data_list3F555W=[]
data_list3F814W=[]
data_list3F336W=[]
data_list3F439W=[]
count3 = 0

for row in csv_f3:
    if count3 != 0:
        count3 +=1
        data_list3F555W.append((row[7]))
        data_list3F814W.append((row[9]))
        data_list3F336W.append((row[4]))
        data_list3F439W.append((row[5]))
    else:
        count3 += 1
        continue
    

joe = []
joe2 = []
joe3=[]
joe4=[]  
  
for i in range(len(data_list3F555W)):
    try:
         joe.append(float(data_list3F555W[i]))
         joe2.append(float(data_list3F814W[i]))
         joe3.append(float(data_list3F336W[i]))
         joe4.append(float(data_list3F439W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis3 = np.zeros(len(jim))
y_axis3 = np.zeros(len(jim))
for j in range(len(jim)):
    x_axis3[j] = joe[j]-joe2[j]
    y_axis3[j] = joe3[j]-joe4[j]
    

f3.close()

"""Cluster Model 4
Variables:
f4
csv_f4
data_list4F555W
data_list4F814W
data_list4F336W
data_list4F439W
count4
bill
x_axis4
y_axis4"""

f4 = open('ClusterModel4.csv')
csv_f4 = csv.reader(f4)

#Array for F55W
data_list4F555W=[]
data_list4F814W=[]
data_list4F336W=[]
data_list4F439W=[]
count4 = 0

for row in csv_f4:
    if count4 != 0:
        count4 +=1
        data_list4F555W.append((row[7]))
        data_list4F814W.append((row[9]))
        data_list4F336W.append((row[4]))
        data_list4F439W.append((row[5]))
    else:
        count4 += 1
        continue
    

bill = []
bill2 = []
bill3=[]
bill4=[]  
  
for i in range(len(data_list4F555W)):
    try:
         bill.append(float(data_list4F555W[i]))
         bill2.append(float(data_list4F814W[i]))
         bill3.append(float(data_list4F336W[i]))
         bill4.append(float(data_list4F439W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis4 = np.zeros(len(bill))
y_axis4 = np.zeros(len(bill))
for j in range(len(bill)):
    x_axis4[j] = bill[j]-bill2[j]
    y_axis4[j] = bill3[j]-bill4[j]
    

f4.close()

"""Cluster Model 5
Variables:
f5
csv_f5
data_list5F555W
data_list5F814W
data_list5F336W
data_list5F439W
count5
tom
x_axis5
y_axis5"""

f5 = open('ClusterModel5.csv')
csv_f5 = csv.reader(f5)

#Array for F55W
data_list5F555W=[]
data_list5F814W=[]
data_list5F336W=[]
data_list5F439W=[]
count5 = 0

for row in csv_f5:
    if count5 != 0:
        count5 +=1
        data_list5F555W.append((row[7]))
        data_list5F814W.append((row[9]))
        data_list5F336W.append((row[4]))
        data_list5F439W.append((row[5]))
    else:
        count5 += 1
        continue
    

tom = []
tom2 = []
tom3=[]
tom4=[]  
  
for i in range(len(data_list5F555W)):
    try:
         tom.append(float(data_list5F555W[i]))
         tom2.append(float(data_list5F814W[i]))
         tom3.append(float(data_list5F336W[i]))
         tom4.append(float(data_list5F439W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis5 = np.zeros(len(tom))
y_axis5 = np.zeros(len(tom))
for j in range(len(tom)):
    x_axis5[j] = tom[j]-tom2[j]
    y_axis5[j] = tom3[j]-tom4[j]
    

f5.close()

"""Cluster Model 6
Variables:
f6
csv_f6
data_list6F555W
data_list6F814W
data_list6F336W
data_list6F439W
count6
dan
x_axis6
y_axis6"""

f6 = open('ClusterModel6.csv')
csv_f6 = csv.reader(f6)

#Array for F55W
data_list6F555W=[]
data_list6F814W=[]
data_list6F336W=[]
data_list6F439W=[]
count6 = 0

for row in csv_f6:
    if count6 != 0:
        count6 +=1
        data_list6F555W.append((row[7]))
        data_list6F814W.append((row[9]))
        data_list6F336W.append((row[4]))
        data_list6F439W.append((row[5]))
    else:
        count6 += 1
        continue
    

dan = []
dan2 = []
dan3=[]
dan4=[]  
  
for i in range(len(data_list6F555W)):
    try:
         dan.append(float(data_list6F555W[i]))
         dan2.append(float(data_list6F814W[i]))
         dan3.append(float(data_list6F336W[i]))
         dan4.append(float(data_list6F439W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis6 = np.zeros(len(dan))
y_axis6 = np.zeros(len(dan))
for j in range(len(dan)):
    x_axis6[j] = dan[j]-dan2[j]
    y_axis6[j] = dan3[j]-dan4[j]
    

f6.close()

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

f7 = open('ClusterModel7.csv')
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
data_list8F555W=[]
data_list8F814W=[]
data_list8F336W=[]
data_list8F439W=[]
count8 = 0

for row in csv_f8:
    if count8 != 0:
        count8 +=1
        data_list8F555W.append((row[7]))
        data_list8F814W.append((row[9]))
        data_list8F336W.append((row[4]))
        data_list8F439W.append((row[5]))
    else:
        count8 += 1
        continue
    

hal = []
hal2 = []
hal3=[]
hal4=[]  
  
for i in range(len(data_list8F555W)):
    try:
         hal.append(float(data_list8F555W[i]))
         hal2.append(float(data_list8F814W[i]))
         hal3.append(float(data_list8F336W[i]))
         hal4.append(float(data_list8F439W[i]))
    
    except ValueError:
        continue
 #Graph Input
x_axis8 = np.zeros(len(hal))
y_axis8 = np.zeros(len(hal))
for j in range(len(hal)):
    x_axis8[j] = hal[j]-hal2[j]
    y_axis8[j] = hal3[j]-hal4[j]
    

f8.close()



# list comprehension
# a = [x for x in f_actual]


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

"""Best fit isochrone:
f7
csv_f7
data_list9F555W
data_list9F814W
data_list9F336W
data_list9F439W
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
x_axis9 = np.zeros(len(ted))
y_axis9 = np.zeros(len(ted))
for j in range(len(ted)):
    x_axis9[j] = ted[j]-ted2[j]
    y_axis9[j] = ted3[j]-ted4[j]
    

f7.close()

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 18}
mpl.rc('font', **font)

plt.xticks([-0.25,0,0.5,1.0,1.5])
plt.plot(x_axis,y_axis,"-",label= "Cluster Model 1")
plt.plot(x_axis2,y_axis2,"-",label= "Cluster Model 2")
plt.plot(x_axis3,y_axis3,"-", label= "Cluster Model 3")
plt.plot(x_axis4,y_axis4,"-", label= "Cluster Model 4")
plt.plot(x_axis5,y_axis5,"-", label= "Cluster Model 5")
plt.plot(x_axis6,y_axis6,"-", label= "Cluster Model 6")
plt.plot(x_axis7,y_axis7,"-",label= "Cluster Model 7")
plt.plot(x_axis8,y_axis8,"-", label= "Cluster Model 8")
plt.scatter(x,y,color="red",label="Hubble Legacy Archive Data")
plt.plot(x_axis9,y_axis9,"-",linewidth=5)

(0.3001/0.439)*a
plt.arrow( 0.0,0.1,0.339,0.3008, fc="k", ec="k",head_width=0.03, head_length=0.05, label= "Reddening Vector: AV=1" )
plt.xlabel('F555W-F814W',weight='bold')
plt.ylabel('F336W-F439W',weight='bold')
plt.title('Antennae Color-Color Diagram', loc = 'center',weight='bold')
plt.grid(True)
plt.legend(loc= "lower right")
plt.show()
