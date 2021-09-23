#!/usr/bin/python
import random
import time
from  PriSchMath.Cou10Fa import Subtraction as Cst
from  PriSchMath.Po10Fa import Subtraction as Pst

def SCHunHe():
    for i in range(45):
        #time.sleep(0.05)


        if i>-1:
            if (i % 5 == 0):
                print("")
                inY=i * 6+30
                bt=str(i/5+1)[:-2]
                print("{1}、-------------{0}--------------         日期：".format(repr(inY),bt))
                time.sleep(0.1)
            RunStr=""
            '''if (random.randint(1, 9) % 2 == 0):#随机生成加减法算式
                getStr=Cst()
            else:
                getStr = Pst()'''
            for ii in range(6):
                rr=random.randint(1, 9)
                if (rr % 2 == 0):#随机生成加减法算式
                    getStr=Cst()
                else:
                    getStr = Pst()
                while(getStr=='E'):
                    if (rr % 2 == 0):
                        getStr = Cst()
                    else:
                        getStr = Pst()
                RunStr+=getStr+"    "
            print(RunStr)
            print("")
            print("")
            print("")
            #print(" (   )          (   )         (   )         (   )         (   )         (   )\n"
             # " "+"(   )"+"          "+"(   )"+"         "+"(   )"+"         "+"(   )"+"         "+"(   )"+"         "+"(   )\n"
              #    "———"+"         ———"+"        ———"+"        ———"+"        ———"+"        ———\n")

            #s=Cst()
            #print(str(i)+"   "+s)
print("开始")
SCHunHe()
print("结束")