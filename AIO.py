import matplotlib.pyplot as plt
from matplotlib import style
import random
import time

path_report="/Users/pushkarsingh/Desktop/Tests/Reports/AIO test.txt"
style.use("ggplot")

fig = plt.figure(figsize=(13,8), dpi=100)
test_count=10
list_alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
pythagoras=[[3,4,5],[5,12,13],[7,24,25],[8,15,17],[9,40,41],[11,60,61],[12,35,37],[16,63,65],[20,21,29],[28,45,53]]
pct=[["9.09 inc", "8.33 dec"],["10 inc","9.09 dec"],["11.11 inc","10 dec"],["12.5 inc","11.11 dec"],["14.28 inc","12.5 dec"],["16.66 inc","14.28 dec"],["20 inc","16.66 dec"],["25 inc","20 dec"],["33.33 inc","25 dec"],["50 inc","33.33 dec"],["60 inc","37.5 dec"],["66.66 inc","40 dec"],["75 inc","42.85 dec"],["100 inc","50 dec"]]
rtp=[8,9,3,6,15,7,11,14,12]
count=8
num_list=[]
toe=time.time()

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
        t_add_start=time.time()
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
        t_add_stop=time.time()
    
    if switch==2:
        t2_start=time.time()
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
        t2_stop=time.time()
    if switch==3:
        t3_start=time.time()
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
        
        t3_stop=time.time()
    if switch==4:
        t4_start=time.time()
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

        t4_stop=time.time()
    
    if switch==5:
        t5_start=time.time()
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
        t5_stop=time.time()
    if switch==6:
        t6_start=time.time()
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
        t6_stop=time.time()
    if switch==7:
        t7_start=time.time()
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
        t7_stop=time.time()
    if switch==8:
        t8_start=time.time()
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
        t8_stop=time.time()
    if switch==9:
        t9_start=time.time()
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
        t9_stop=time.time() 
    
    if switch==10:
        t10_start=time.time()
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
        t10_stop=time.time()  
    if switch==11:
        t11_start=time.time()
        print("ratio to percentage")
        for i in range(15):
            k= random.randint(0,len(rtp)-1)
            res=round(((1/rtp[k])*100),2)
            z_input_15 = input()
            print("1/{}".format(rtp[k]))
            z_input_16 = input()
            print("{}%".format(res))
        t11_stop=time.time()  
    if switch==12:
        t12_start=time.time()
        print("percentage to ratio")
        for i in range(15):
            k= random.randint(0,len(rtp)-1)
            res=round(((1/rtp[k])*100),2)
            z_input_15 = input()
            print("{}%".format(res))
            z_input_16 = input()
            print("1/{}".format(rtp[k]))
        t12_stop=time.time()
####### Time #### Main ####
        
tac=time.time()
tic1=tac-toe
per_ques=tic1/test_count
per_ques=round((per_ques/60),2)
tic1=round((tic1/60),2)

minute=int(tic1)
sec=round(((tic1-minute)*60),2)


minute_pq=int(per_ques)
sec_pq=round(((per_ques-minute_pq)*60),2)
print("\n \n *******TOTAL TIME******** ")
print("total time: {} min {} sec".format(minute,sec))
print("time taken per ques: {} min {} sec".format(minute_pq,int(round(sec_pq,0))))

####### Time #### ADDITION ####
        
tic2=t_add_stop-t_add_start
per_ques=tic2/test_count
per_ques=round((per_ques/60),2)
tic2=round((tic2/60),2)

minute=int(tic2)
sec=round(((tic2-minute)*60),2)

minute_pq=int(per_ques)
sec_pq=round(((per_ques-minute_pq)*60),2)
print("\n \n *******ADDITION******** ")
print("total time: {} min {} sec".format(minute,sec))
print("time taken per ques: {} min {} sec".format(minute_pq,int(round(sec_pq,0))))

####### Time #### ALPHABET 2 NUMBERS ####
        
tic3=t2_stop-t2_start
per_ques=tic3/test_count
per_ques=round((per_ques/60),2)
tic3=round((tic3/60),2)

minute=int(tic3)
sec=round(((tic3-minute)*60),2)

minute_pq=int(per_ques)
sec_pq=round(((per_ques-minute_pq)*60),2)
print("\n \n *******ALPHABET TO NUMBER******** ")
print("total time: {} min {} sec".format(minute,sec))
print("time taken per ques: {} min {} sec".format(minute_pq,int(round(sec_pq,0))))

####### Time #### NUMBERS TO ALPHABET####
        
tic4=t3_stop-t3_start
per_ques=tic4/test_count
per_ques=round((per_ques/60),2)
tic4=round((tic4/60),2)

minute=int(tic4)
sec=round(((tic4-minute)*60),2)

minute_pq=int(per_ques)
sec_pq=round(((per_ques-minute_pq)*60),2)
print("\n \n *******NUMBER TO ALPHABET******** ")
print("total time: {} min {} sec".format(minute,sec))
print("time taken per ques: {} min {} sec".format(minute_pq,int(round(sec_pq,0))))


####### Time #### SQUARE####
        
tic5=t4_stop-t4_start
per_ques=tic5/test_count
per_ques=round((per_ques/60),2)
tic5=round((tic5/60),2)

minute=int(tic5)
sec=round(((tic5-minute)*60),2)

minute_pq=int(per_ques)
sec_pq=round(((per_ques-minute_pq)*60),2)
print("\n \n *******NUMBER TO ALPHABET******** ")
print("total time: {} min {} sec".format(minute,sec))
print("time taken per ques: {} min {} sec".format(minute_pq,int(round(sec_pq,0))))


####### Time #### SQUARE ROOT ####
        
tic6=t5_stop-t5_start
per_ques=tic6/test_count
per_ques=round((per_ques/60),2)
tic6=round((tic6/60),2)

minute=int(tic6)
sec=round(((tic6-minute)*60),2)

minute_pq=int(per_ques)
sec_pq=round(((per_ques-minute_pq)*60),2)
print("\n \n *******SQUARE ROOT******** ")
print("total time: {} min {} sec".format(minute,sec))
print("time taken per ques: {} min {} sec".format(minute_pq,int(round(sec_pq,0))))

####### Time #### CUBE ####
        
tic7=t6_stop-t6_start
per_ques=tic7/test_count
per_ques=round((per_ques/60),2)
tic7=round((tic7/60),2)

minute=int(tic7)
sec=round(((tic7-minute)*60),2)

minute_pq=int(per_ques)
sec_pq=round(((per_ques-minute_pq)*60),2)
print("\n \n *******CUBE******** ")
print("total time: {} min {} sec".format(minute,sec))
print("time taken per ques: {} min {} sec".format(minute_pq,int(round(sec_pq,0))))

####### Time #### CUBE ROOT ####
        
tic8=t7_stop-t7_start
per_ques=tic8/test_count
per_ques=round((per_ques/60),2)
tic8=round((tic8/60),2)

minute=int(tic8)
sec=round(((tic8-minute)*60),2)

minute_pq=int(per_ques)
sec_pq=round(((per_ques-minute_pq)*60),2)
print("\n \n *******CUBE ROOT ******** ")
print("total time: {} min {} sec".format(minute,sec))
print("time taken per ques: {} min {} sec".format(minute_pq,int(round(sec_pq,0))))


####### Time #### MULTIPLICATION ####
        
tic9=t8_stop-t8_start
per_ques=tic9/test_count
per_ques=round((per_ques/60),2)
tic9=round((tic9/60),2)

minute=int(tic9)
sec=round(((tic9-minute)*60),2)

minute_pq=int(per_ques)
sec_pq=round(((per_ques-minute_pq)*60),2)
print("\n \n *******MULTIPLICATION******** ")
print("total time: {} min {} sec".format(minute,sec))
print("time taken per ques: {} min {} sec".format(minute_pq,int(round(sec_pq,0))))

####### Time #### PYTHAGOREAN TRIPLET ####
        
tic10=t9_stop-t9_start
per_ques=tic10/test_count
per_ques=round((per_ques/60),2)
tic10=round((tic10/60),2)

minute=int(tic10)
sec=round(((tic10-minute)*60),2)

minute_pq=int(per_ques)
sec_pq=round(((per_ques-minute_pq)*60),2)
print("\n \n *******PYTHAGOREAN TRIPLET******** ")
print("total time: {} min {} sec".format(minute,sec))
print("time taken per ques: {} min {} sec".format(minute_pq,int(round(sec_pq,0))))

####### Time #### PCT ####
        
tic11=t10_stop-t10_start
per_ques=tic11/test_count
per_ques=round((per_ques/60),2)
tic11=round((tic11/60),2)

minute=int(tic11)
sec=round(((tic11-minute)*60),2)

minute_pq=int(per_ques)
sec_pq=round(((per_ques-minute_pq)*60),2)
print("\n \n *******PCT ******** ")
print("total time: {} min {} sec".format(minute,sec))
print("time taken per ques: {} min {} sec".format(minute_pq,int(round(sec_pq,0))))

####### Time #### RATIO TO PERCENTAGE ####
        
tic12=t11_stop-t11_start
per_ques=tic12/test_count
per_ques=round((per_ques/60),2)
tic12=round((tic12/60),2)

minute=int(tic12)
sec=round(((tic12-minute)*60),2)

minute_pq=int(per_ques)
sec_pq=round(((per_ques-minute_pq)*60),2)
print("\n \n *******RATIO TO PERCENTAGE******** ")
print("total time: {} min {} sec".format(minute,sec))
print("time taken per ques: {} min {} sec".format(minute_pq,int(round(sec_pq,0))))

####### Time #### PERCENTAGE TO RATIO ####
        
tic13=t12_stop-t12_start
per_ques=tic13/test_count
per_ques=round((per_ques/60),2)
tic13=round((tic13/60),2)

minute=int(tic13)
sec=round(((tic13-minute)*60),2)

minute_pq=int(per_ques)
sec_pq=round(((per_ques-minute_pq)*60),2)
print("\n \n *******PERCENTAGE TO RATIO******** ")
print("total time: {} min {} sec".format(minute,sec))
print("time taken per ques: {} min {} sec".format(minute_pq,int(round(sec_pq,0))))

date_stamp=time.strftime('%Y-%m-%d')
f_report=open(path_report,"a+")
f_report.write(("{} {} {} {} {} {} {} {} {} {} {} {} {} {}\n".format(date_stamp, tic1,tic2,tic3,tic4,tic5,tic6 ,tic7, tic8, tic9,tic10,tic11,tic12,tic13)))
f_report.close()

f_report=open(path_report,"r")
Data=[]    
for name in f_report.readlines():
        Data.append( [name.lower() for name in (name.split())])
f_report.close()


t1=[]
t2=[]
t3=[]
t4=[]
t5=[]
t6=[]
t7=[]
t8=[]
t9=[]
t10=[]
t11=[]
t12=[]
t13=[]
yar=[]
count=0

for data in Data:
    
    t1.append(float(data[1]))
    t2.append(float(data[2]))
    t3.append(float(data[3]))
    t4.append(float(data[4]))
    t5.append(float(data[5]))
    t6.append(float(data[6]))
    t7.append(float(data[7]))
    t8.append(float(data[8]))
    t9.append(float(data[9]))
    t10.append(float(data[10]))
    t11.append(float(data[11]))
    t12.append(float(data[12]))
    t13.append(float(data[13]))
    count+=1
    yar.append(count)
 
ax = plt.subplot2grid((10,6), (0,0), colspan=6, rowspan=2)
ax.plot(yar,t1,label='Total')
ax.legend(loc='best')

ax = plt.subplot2grid((10,6), (2,0), rowspan=2,colspan=2)
ax.plot(yar,t2,label='Add')
ax.legend(loc='best')

ax = plt.subplot2grid((10,6), (2,2), rowspan=2,colspan=2)
ax.plot(yar,t3,label="A2N")
ax.legend(loc='best')

ax = plt.subplot2grid((10,6), (2,4), rowspan=2,colspan=2)
ax.plot(yar,t4,label="N2A")
ax.legend(loc='best')

ax = plt.subplot2grid((10,6), (4,0), rowspan=2,colspan=2)
ax.plot(yar,t5,label="sq")
ax.legend(loc='best')

ax = plt.subplot2grid((10,6), (4,2), rowspan=2,colspan=2)
ax.plot(yar,t6,label="sq root")
ax.legend(loc='best')

ax = plt.subplot2grid((10,6), (4,4), rowspan=2,colspan=2)
ax.plot(yar,t7,label="cube")
ax.legend(loc='best')

ax = plt.subplot2grid((10,6), (6,0), rowspan=2,colspan=2)
ax.plot(yar,t8,label="cube root")
ax.legend(loc='best')

ax = plt.subplot2grid((10,6), (6,2), rowspan=2,colspan=2)
ax.plot(yar,t9,label="mul")
ax.legend(loc='best')

ax = plt.subplot2grid((10,6), (6,4), rowspan=2,colspan=2)
ax.plot(yar,t10,label="py triplet")
ax.legend(loc='best')

ax = plt.subplot2grid((10,6), (8,0), rowspan=2,colspan=2)
ax.plot(yar,t11,label="PCT")
ax.legend(loc='best')

ax = plt.subplot2grid((10,6), (8,2), rowspan=2,colspan=2)
ax.plot(yar,t12,label="R2P")
ax.legend(loc='best')

ax = plt.subplot2grid((10,6), (8,4), rowspan=2,colspan=2)
ax.plot(yar,t13,label="P2R")
ax.legend(loc='best')
         
plt.show()
