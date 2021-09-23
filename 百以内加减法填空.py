#!/usr/bin/python
import random
import time
from  PriSchMath.Cou10Fa import Subtraction as Cst
from  PriSchMath.Cou10Fa import Bit as Bit
from  PriSchMath.Po10Fa import Subtraction as Pst


def HengShi():
    ni=0
    while(ni==0):
        strHS=Cst()
        if strHS=="E":
            ni=0
        else:
            ni=1
    return   strHS
def bits():
    ni=0
    while(ni==0):
        strHS=Bit()
        if strHS==None:
            ni=0
        else:
            ni=1
    return   strHS
def ShuShiBit( ):
    strFuHao="| |"
    #个位
    b01=bits()
    #b02=Bit()
    #十位
    b10=bits()
    #b20=Bit()
    bb2= str(b01)+str(b10)
    #print(bb2)
    b1= bb2
    int_random = random.randint(0, 9)
    if(int_random!=0):
        if ( int_random % 2== 1):
            b1=strFuHao+str(b1)[1:].rjust(2,' ').ljust(3,' ')#截取后1位
        elif (int_random % 2 == 0):
            b1=str(b1)[:1].rjust(2,' ').ljust(3,' ')+strFuHao#截取第1位
    else:
        b1=strFuHao+strFuHao
        #print(b1)
    strList=[str(bb2),str(b1)]
    #dict_B={"BJ":List_B}
    #print(strList)
    return strList
def ShuShiList():
    dict_JS= {}
    dict_BJ={}
    strJS=""
    strBJS=""
    strJG="     "
    strHX="———"
    strSSHX=""
    strDS=""
    num=0
    for i in range(1000):

        dict_JS[i]=ShuShiBit()
        dict_BJ[i]=ShuShiBit()
        strLX=''.join(random.sample( '+-', 1))# 生成随机字符串  +-*/
        if strLX=="+":
            dss=int(dict_JS[i][0])+int(dict_BJ[i][0])#得数
            if(dss<100):
                strJS+=  "  "+dict_JS[i][1]+strJG#第一位
                strBJS+=  strLX+" "+dict_BJ[i][1]+strJG#第二位
                strDS+=repr(dss).rjust(3,' ')+strJG+strJG#得数
                strSSHX+=  strHX+strJG+"  "#横线
                num+=1
        elif strLX=="-":
            strJS+=  "  "+dict_JS[i][1]+strJG#第一位
            strBJS+=  strLX+" "+dict_BJ[i][1]+strJG#第二位
            strSSHX+=  strHX+strJG+"  "#横线
            ds=int(dict_JS[i][0]) - int(dict_BJ[i][0])
            if ds<0:
                strDS += repr(int(dict_BJ[i][0]) - int(dict_JS[i][0])).rjust(3, ' ') + strJG + strJG  # 得数
            else:
                strDS += repr(int(dict_JS[i][0]) - int(dict_BJ[i][0])).rjust(3, ' ') + strJG + strJG  # 得数
            num += 1
        if num==6:
            break;
    #strBJS= "{0}   {1}".format(dict_BJ[0][1],dict_BJ[1][1])
    print(strJS)
    print(strBJS+"\n"+strSSHX)
    print(strDS)
def ShuShi():
    strFH="+"
    JS=ShuShiBit()
    strJS=JS[0]
    strJSF=JS[1]
    BJ=ShuShiBit()
    strBJ=BJ[0]
    strBJF=BJ[1]
    HS=int(strJS)+int(strBJ)
    while(HS >100):
        return ShuShi()
    if int(strBJ)>int(strJS):
        str=strBJ
        strBJ=strJS
        strJS=str

        strF=strBJF
        strBJF=strJSF
        strJSF=strF
    strSS=" "+strJSF+"\n"+strFH+strBJF+"\n"+"————\n"+repr(HS)
    strHS= strJS+strFH+strBJ+"="
    #print (strHS)
    print (strSS)
    return  strSS

def SCHunHe():
    for i in range(10):
        print ("************************************{0}*************************************".format(i))
        ShuShiList()





#print("开始")
SCHunHe()
#print("结束")