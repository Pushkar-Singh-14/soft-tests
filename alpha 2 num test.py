import random
import time
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib import style
import time
 
style.use("ggplot")

fig = plt.figure(figsize=(13,8), dpi=100)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

ax1.set_title('Accuracy')
ax2.set_title('Total Time')
ax3.set_title('Average ')
Data=[]
path="/Users/pushkarsingh/Desktop/revise_alpha to num.txt"
path_report="/Users/pushkarsingh/Desktop/Tests/Reports/alpha 2 num test.txt"

test_count=1000
total_count=0
correct=0
wrong=0
timer=0
avg_consumed_time=[]
f=open(path,"a+")
list_alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
try:
    for i in range(test_count):
        
        x=random.randint(0,25)
        
        z=ord(list_alpha[x])-96
        
        tic=time.time()
        print("{}".format((list_alpha[x]).upper()))
        if (timer/60)>10.0 and (timer/60)<10.2:
            print("..")
        if (timer/60)>5.0 and (timer/60)<5.2:
            print(".")
        z_input = input()
        tac=time.time()
        consumed_time=round((tac-tic),2)
        avg_consumed_time.append(consumed_time)
        
        if(z_input=="e"):
            break
        total_count+=1

        try:
            if int(z_input)<1000:
                pass
        except:
            z_input=100
        
        if (int(z_input)==z):
            print("correct Time taken={}\n".format(consumed_time))
            correct+=1
            
        else:
            print("wrong {} Time taken={}\n".format(z,consumed_time))
            f.write(("{} = {}\n".format(list_alpha[x],z)))
            
            wrong+=1
        timer+=(consumed_time)
        
    score=(correct/total_count)*100
    avg=round(mean(avg_consumed_time),2)


    print("""
    total={}
    correct={} 
    wrong={}
    score={}%
    Avg Consume time={} sec
    Total time={} min""".format(total_count,correct,wrong,score,avg,round(timer/60,2)))
    f_report=open(path_report,"a+")
    date_stamp=time.strftime('%Y-%m-%d')
    f_report.write(("{} {} {} {}\n".format(date_stamp,score,timer/60,avg)))
    f_report.close()
    f_report=open(path_report,"r")
    for name in f_report.readlines():
        Data.append( [name.lower() for name in (name.split())])
    f_report.close()


    xar_acc=[]
    xar_time=[]
    xar_avg_time=[]
    yar=[]
    count=0

    for data in Data:
        xar_acc.append(float(data[1]))
        xar_time.append(float(data[2]))
        xar_avg_time.append(float(data[3]))
        count+=1
        yar.append(count)
        
    ax1.plot(yar,xar_acc)
    ax2.plot(yar,xar_time)
    ax3.plot(yar,xar_avg_time)

    fig.suptitle("Alphabet to Numbers")
except:
     print("""
    total={}
    correct={} 
    wrong={}
    """.format(total_count,correct,wrong))

f.close()

plt.show()    
