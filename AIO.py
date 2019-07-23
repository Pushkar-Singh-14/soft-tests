import matplotlib.pyplot as plt
from matplotlib import style
import random
import time

path_report="/Users/pushkarsingh/Desktop/Tests/Reports/AIO test.txt"

test_count=10
list_alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
pythagoras=[[3,4,5],[5,12,13],[7,24,25],[8,15,17],[9,40,41],[11,60,61],[12,35,37],[16,63,65],[20,21,29],[28,45,53]]
pct=[["9.09 inc", "8.33 dec"],["10 inc","9.09 dec"],["11.11 inc","10 dec"],["12.5 inc","11.11 dec"],["14.28 inc","12.5 dec"],["16.66 inc","14.28 dec"],["20 inc","16.66 dec"],["25 inc","20 dec"],["33.33 inc","25 dec"],["50 inc","33.33 dec"],["60 inc","37.5 dec"],["66.66 inc","40 dec"],["75 inc","42.85 dec"],["100 inc","50 dec"]]
rtp=[8,9,3,6,15,7,11,14,12]
count=8
num_list=[]
tac=time.time()

fig = plt.figure(figsize=(13,8), dpi=100)
ax1 = fig.add_subplot(1,1,1)

for i in range(1,13):
    num_list.append(i)
    c=len(num_list)
for i in range(c):
    y=random.randint(0,len(num_list)-1)
    #print(y)
    switch=num_list[y]
    #print("switch={}".format(switch))
    num_list.remove(switch)

    if switch==1:
        print("Addition")
        for i in range(test_count):

            x=random.randint(1,50)
            a=random.randint(1,20)
            y=random.randint(1,50)
            b=random.randint(1,9)

            z=(x+y+a+b)
            x_input = input()
            if ((x_input)==""):
                print("{} + {} + {} + {}".format(x,a,y,b))


            z_input = input()
            if ((z_input)==""):
                print("{}\n".format(z))
    
    if switch==2:
        print("alphabet to numbers")
        try:
            for i in range(test_count):

                x=random.randint(0,25)

                z=ord(list_alpha[x])-96
                z_input_2 = input()
                print("{}".format((list_alpha[x]).upper()))
                z_input_1 = input()
                print("{}\n".format(z))
        except:
            pass
    
    if switch==3:
        print("number to alphabet")
        try:
            for i in range(test_count):

                x=random.randint(0,25)

                z=ord(list_alpha[x])-96
                z_input_3 = input()
                print("{}\n".format(z))
                z_input_4 = input()
                print("{}".format((list_alpha[x]).upper()))

        except:
            pass
        
    
    if switch==4:
        print("square")
        try:
            for i in range(test_count):
                x=random.randint(11,30)
                z=(x*x)
                z_input_5 = input()
                print("{}".format(x))
                z_input_6 = input()
                print("{}".format(z))
        except:
            pass        
        
    
    if switch==5:
        print("square root")
        try:
            for i in range(test_count):
                x=random.randint(11,30)
                z=(x*x)
                z_input_7 = input()
                print("{}".format(z))
                z_input_8 = input()
                print("{}".format(x))
        except:
            pass        
        
    if switch==6:
        print("cube")
        try:
            for i in range(test_count):
                x=random.randint(1,13)
                z=(x*x*x)
                z_input_5 = input()
                print("{}".format(x))
                z_input_6 = input()
                print("{}".format(z))
        except:
            pass   
        
    if switch==7:
        print("cube root")
        try:
            for i in range(test_count):
                x=random.randint(1,13)
                z=(x*x*x)
                z_input_5 = input()
                print("{}".format(z))
                z_input_6 = input()
                print("{}".format(x))
        except:
            pass 
    
    if switch==8:
        print("multiplication")
        try:
            for i in range(15):

                x=random.randint(12,18)
                a=random.randint(1,9)
                z=(x*a)
                z_input_9 = input()
                print("{} x {} ".format(x,a))
                z_input_10 = input()
                print("{} ".format(z))
        except:
            pass 
    
    if switch==9:
        print("pythagoras triplets")
        for i in range(10):
            
            p=random.randint(0,9)
            num_list_py=[]
            for i in range(0,3):
                num_list_py.append(i)
                c=len(num_list_py)
            for i in range(0,c):
                y=random.randint(0,len(num_list_py)-1)

                switch1=num_list_py[y]
                #print("switch={}".format(switch))
                num_list_py.remove(switch1)
                if i==0:
                    j=switch1
                if i==1:
                    k=switch1
                else:
                    l=switch1
            #print(j,k,p)
            z_input_11 = input()
            print(pythagoras[p][j],pythagoras[p][k])
            z_input_12 = input()
            print(pythagoras[p][l])
            
    
    if switch==10:
        print("product contantcy table")
        for i in range(len(pct)):
            p=random.randint(0,len(pct)-1)
            num_list_py=[]
            for i in range(0,2):
                num_list_py.append(i)
                c=len(num_list_py)
            for i in range(0,c):
                y=random.randint(0,len(num_list_py)-1)

                switch2=num_list_py[y]
                #print("switch={}".format(switch))
                num_list_py.remove(switch2)
                if i==0:
                    j=switch2
                else:
                    l=switch2
            #print(j,k,p)
            z_input_13 = input()
            print(pct[p][j])
            z_input_14 = input()
            print(pct[p][l])
            
    if switch==11:
        print("ratio to percentage")
        for i in range(15):
            k= random.randint(0,len(rtp)-1)
            res=round(((1/rtp[k])*100),2)
            z_input_15 = input()
            print("1/{}".format(rtp[k]))
            z_input_16 = input()
            print("{}%".format(res))
            
    if switch==12:
        print("percentage to ratio")
        for i in range(15):
            k= random.randint(0,len(rtp)-1)
            res=round(((1/rtp[k])*100),2)
            z_input_15 = input()
            print("{}%".format(res))
            z_input_16 = input()
            print("1/{}".format(rtp[k]))
            
toe=time.time()
tic=toe-tac      
tic=round((tic/60),2)

print(tic)
f_report=open(path_report,"a+")
f_report.write(("{}\n".format(tic)))
f_report.close()
Data1=[]    
f_report=open(path_report,"r")    
for name in f_report.readlines():
    Data1.append(name)
f_report.close()
xar=[]
yar=[]
for data in Data1:
    xar.append(float(data))
    count+=1
    yar.append(count)
plt.plot(yar,xar)
plt.show()
