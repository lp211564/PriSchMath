#!/usr/bin/python
import random




def randoms():
    int_random=0
    int_random=random.randint(10, 99)
    return int_random
def Bit():
    int_random=random.randint(1, 9)
    if(int_random==0):
        return Bit()
    return int_random


#减法
def Subtraction():
    #个位
    b01=Bit()
    b02=Bit()
    #十位
    b10=Bit()
    b20=Bit()
    JS=0
    BJS=0
    ds=0
    ss=""
    if b01>b02:
        JS=b02
        BJS=b01
    elif b01<b02:
        JS=b01
        BJS=b02
    elif b01==b02:
        return 'E'

    if b10 > b20:
        ss = str(b10*10+JS) + " - " + str(b20*10+BJS) + " = "
        ds =(b10*10+JS)-(b20*10+BJS)
    elif b01 < b02:
        ss = str(b20*10+JS) + " - " + str(b10*10+BJS) + " = "
        ds = (b20*10+JS) - (b10*10+BJS)
    else :
        ss=Subtraction()
    while (ds < 0):
        ss = Subtraction()
        return ss
    return ss
'''
    na=randoms()
    nb=randoms()
    if na>nb:
        ss=str(na)+" - "+str(nb)+" = "
        return ss
    elif na<nb:
        ss=str(nb) + " - " + str(na) + " = "
        return ss
    else:
        Subtraction()
'''
def SC():
    for i in range(180):

        if (i % 10 == 0):
            print("-------------{0}--------------用时：".format(i*6))
        if i>0:
            getStr=Subtraction()
            RunStr=""
            for ii in range(6):
                getStr = Subtraction()
                while(getStr=='E'):
                    getStr = Subtraction()
                RunStr+=getStr+"    "

            print(RunStr)

            s=Subtraction()
            #print(str(i)+"   "+s)
#print("开始")
#SC()
#print("结束")