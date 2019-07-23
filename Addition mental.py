import random
import time
import matplotlib.pyplot as plt
from matplotlib import style

fig = plt.figure(figsize=(13,8), dpi=100)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

path_report="/Users/pushkarsingh/Desktop/Tests/Reports/mental addition test.txt"
j=0
count=0
##
test_count=50
##
toe=time.time()
for i in range(test_count):
        
    x=random.randint(1,50)
    a=random.randint(1,20)
    y=random.randint(1,50)
    b=random.randint(1,9)
    
    z=(x+y+a+b)
    x_input = input()
    if ((x_input)==""):
        j+=1
        print("{}/{}".format(j,test_count))
        print("{} + {} + {} + {}".format(x,a,y,b))
        
    
    z_input = input()
    if ((z_input)==""):
        print("{}\n".format(z))
tac=time.time()

tic=tac-toe

tic=round((tic/60),2)

print("total time: {}".format(tic))

f_report=open(path_report,"a+")
f_report.write(("{} {}\n".format(j,tic)))
f_report.close()
Data1=[]    
f_report=open(path_report,"r")    
for name in f_report.readlines():
    Data1.append( [name.lower() for name in (name.split())])
f_report.close()
xar_count=[]
xar_total_time=[]
yar=[]
for data in Data1:
    xar_count.append(float(data[0]))
    xar_total_time.append(float(data[1]))
    count+=1
    yar.append(count)
ax1.plot(yar,xar_count)
ax2.plot(yar,xar_total_time)

plt.show()    
