#!/usr/bin/python
import random
import time
from  PriSchMath.Cou10Fa import Subtraction as Cst
from  PriSchMath.Po10Fa import Subtraction as Pst

def SCHunHe():
    for i in range(50):
        #time.sleep(0.05)

        if (i % 10 == 0):
            print("")
            print("-------------{0}--------------用时：".format(i*6))
            time.sleep(0.1)
        if i>0:
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
            print(" (   )          (   )         (   )         (   )         (   )         (   )\n"
              " "+"(   )"+"          "+"(   )"+"         "+"(   )"+"         "+"(   )"+"         "+"(   )"+"         "+"(   )\n"
                  "———"+"         ———"+"        ———"+"        ———"+"        ———"+"        ———\n")

            #s=Cst()
            #print(str(i)+"   "+s)
print("开始")
SCHunHe()
print("结束")