import numpy as np;
import math;
import matlab.engine;

def timeReq(dataSize,rusize, mcs_QAM):

        if (dataSize==0):
                symbols=0;
        mcs_QAM_=1024
        if rusize<242:
            if mcs_QAM>=256:
                mcs_QAM_=256;
            else:
                mcs_QAM_=mcs_QAM
        else:
            if mcs_QAM<1024:
                mcs_QAM_=mcs_QAM;
            else:
                mcs_QAM_=1024
        bits=dataSize*8;
        encodeingRate=5.0/6.0;
        bitsPerSec=math.log(mcs_QAM_,2)*encodeingRate*(26*rusize);
        symbols=bits/bitsPerSec;
        symbolDuration=symbols*0.0000144;
     
        return symbolDuration; 

def getTimeArr(clients,m,R):
        timeArr=[0 for i in range(len(clients)*len(m))];
        k=0;
        for i in range(0,len(clients)):
                for j in range(0,len(m)):
                    timeArr[k]=timeReq(clients[i],m[j],R[i]);
                    k=k+1;
        timeArr.sort() 
        return timeArr;

def alloc(clients,f,R,F,T):
    clients.sort()
    ruVector=[0 for i in range(len(clients))]
    r=0
    B=[]
    if F==9:
        B=[9,4,2,1]
    elif F==19:
        B=[18,8,4,2,1]
    else:
        B=[37,16,8,4,2,1]
    for i in clients:

        for j in f:
            t_=timeReq(i,j,R[r])
            if B[f.index(j)]>=0:
                if t_<=T:
                    ruVector[r]=j;
                    B[f.index(j)]=B[f.index(j)]-1;
                    break;   
        r=r+1;
    ruSum=0;
    count=0
    for i in ruVector:
        if i !=0:
            ruSum=ruSum+i;
            count=count+1;
    if ruSum<=F and count==len(clients):
        print(ruVector)

        return (True,ruVector);
    else:
        return (False,ruVector);



import matlab.engine

def GetAllocationIndex(ruAllocArray):
    allocationIndexStr="";
    if len(ruAllocArray)==9:
        allocationIndexStr="00000000"
    elif len(ruAllocArray)==8:
        if ruAllocArray[7]==2:
            allocationIndexStr="00000001"
        elif ruAllocArray[0]==2:
            allocationIndexStr="00001000"
        elif ruAllocArray[5]==2:
            allocationIndexStr="00000010"
        elif ruAllocArray[2]==2:
            allocationIndexStr="00000100"
    elif len(ruAllocArray)==7:
        if ruAllocArray[6]==2 and ruAllocArray[5]==2:
            allocationIndexStr="00000011"
        elif ruAllocArray[6]==2 and ruAllocArray[2]==2:
            allocationIndexStr="00000101"
        elif ruAllocArray[2]==2 and ruAllocArray[4]==2:
            allocationIndexStr="00000110"
        elif ruAllocArray[6]==2 and ruAllocArray[0]==2:
            allocationIndexStr="00001001"
        elif ruAllocArray[0]==2 and ruAllocArray[4]==2:
            allocationIndexStr="00001010"
        elif ruAllocArray[0]==2 and ruAllocArray[1]==2:
            allocationIndexStr="00001100"
    elif len(ruAllocArray)==6:
        if ruAllocArray[5]==2 and ruAllocArray[4]==2 and ruAllocArray[2]==2:
            allocationIndexStr="00000111"
        elif ruAllocArray[5]==2 and ruAllocArray[4]==2 and ruAllocArray[0]==2:
            allocationIndexStr="00001011"
        elif ruAllocArray[5]==2 and ruAllocArray[1]==2 and ruAllocArray[0]==2:
            allocationIndexStr="00001101"
        elif ruAllocArray[3]==2 and ruAllocArray[1]==2 and ruAllocArray[0]==2:
            allocationIndexStr="00001110"
    elif len(ruAllocArray)==5:
        if ruAllocArray[2]==1 and ruAllocArray[0]==2 and ruAllocArray[4]==2:
            allocationIndexStr="00001111"
    import webbrowser
    webbrowser.open('https://i.imgur.com/FVldYF4.png')
    return allocationIndexStr;

def createMatlabFrame(ruVec_,Tx_t_,BW_,mcs_,data_):
    eng = matlab.engine.start_matlab()
    tf = eng.createFrame(GetAllocationIndex(ruVec_),Tx_t_,BW_,mcs_,data_)
    print(tf)
    return tf;

#tx_signal=createMatlabFrame([2,1,1,1,2,2],127,'CBW20',3,[500,500,500,600,600,800])


def OptimalRuAllocAl(clients,f,F,R):
    n=len(clients);
    #sortedClients=clients.sort()
    timeArray=getTimeArr(clients,f,R);
    #time=timeArray.sort();
    for t in timeArray:
       res=alloc(clients,f,R,F,t)
       if res[0]==True:
           print(t);
           tpadding=[];
           i=0;
           ruVector=res[1]
           f= open("rualloc.txt","a+")

           for j in ruVector:
               ti=timeReq(clients[i],j,R[i]);
               tpadding.append(t-ti);
               i=i+1;


           f.write(t.__str__()+","+(sum(tpadding)/n).__str__()+"\n")
           f.close()
           tx_signal=createMatlabFrame(ruVector,int(t*1000000),'CBW20',3,clients)
           
           
           return (t,(sum(tpadding)/n))
           break;


    return 0;



f=OptimalRuAllocAl([50,50,50,60,60,60,60,80],[1,2,4,9],9,[8,8,8,8,8,8,8,8])

