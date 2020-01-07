import matplotlib.pyplot as plt
import numpy as np
import math
import OptimalRUalloc;
import pandas as pd 


tmeanN=[]
tmeanU=[]
tmeanB=[]
tmeanL=[]

tPmeanN=[]
tPmeanU=[]
tPmeanB=[]
tPmeanL=[]

tHmeanN=[]
tHmeanU=[]
tHmeanB=[]
tHmeanL=[]


dataDistributionN=[]
dataDistributionU=[]
dataDistributionB=[]
dataDistributionL=[]

f_=[1,2,4,9]
F=9
cl=19

for j in range(2,F+1):

    itppN=[]
    itppU=[]
    itppB=[]
    itppL=[]
    itN=[]
    itU=[]
    itB=[]
    itL=[]
    itpN=[]
    itpU=[]
    itpB=[]
    itpL=[]
    

    for i in range(100):         
        #mu, sigma = 700.0,200.0 # mean and standard deviation

        muN, sigmaN = 750.0,200.0 
        sN = np.random.normal(muN, sigmaN, j)
        dataDistributionN.extend(sN);
        mN=[]
        for member in sN:
            member=abs(math.floor(member))
            #print(member)
            mN.append(member)
        
        r=[1024 for p in range(len(mN))]
        tempN=OptimalRUalloc.OptimalRuAllocAl(mN,f_,F,r)
        tN=tempN[0]
        tpN=tempN[1]
        itppN.append(tpN)
        itN.append(tN)
        itpN.append(8*(sum(mN)/tN))

        muU, sigmaU = 70.0,700.0
        sU = np.random.uniform(muU, sigmaU, j)
        dataDistributionU.extend(sU);
        mU=[]
        for member in sU:
            member=abs(math.floor(member))
            #print(member)
            mU.append(member)
        tempU=OptimalRUalloc.OptimalRuAllocAl(mU,f_,F,r)
        tU=tempU[0]
        tpU=tempU[1]
        itppU.append(tpU)
        itU.append(tU)
        itpU.append(8*(sum(mU)/tU))


        muB, sigmaB = 0.5,0.5
        sB = np.random.beta(muB, sigmaB, j)
        mB=[]
        for member in sB:
            member=abs(math.floor(member*1000))+50
            #print(member)
            mB.append(member)
        
        dataDistributionB.extend(mB)

        tempB=OptimalRUalloc.OptimalRuAllocAl(mB,f_,F,r)
        tB=tempB[0]
        tpB=tempB[1]
        itppB.append(tpB)
        itB.append(tB)
        itpB.append(8*(sum(mB)/tB))



        muL, sigmaL =  5.0,1.5
        sL = np.random.lognormal(muL, sigmaL, j)
        dataDistributionL.extend(sL)
        mL=[]
        for member in sL:
            member=abs(math.floor(member))
            print(member)
            mL.append(member)
        tempL=OptimalRUalloc.OptimalRuAllocAl(mL,f_,F,r)
        tL=tempL[0]
        tpL=tempL[1]
        itppL.append(tpL)        
        itL.append(tL)
        itpL.append(8*(sum(mL)/tL))
    
    tmeanN.append(((sum(itN)/100),j))
    tmeanU.append(((sum(itU)/100),j))
    tmeanB.append(((sum(itB)/100),j))
    tmeanL.append(((sum(itL)/100),j))

    tPmeanN.append(((sum(itppN)/100),j))
    tPmeanU.append(((sum(itppU)/100),j))
    tPmeanB.append(((sum(itppB)/100),j))
    tPmeanL.append(((sum(itppL)/100),j))

    tHmeanN.append(((sum(itpN)/100),j))
    tHmeanU.append(((sum(itpU)/100),j))
    tHmeanB.append(((sum(itpB)/100),j))
    tHmeanL.append(((sum(itpL)/100),j))

barWidth = 0.20
y=[]
yN=[]
xMeanTN=[]
for i in tmeanN:
    xMeanTN.append(i[0]*1000000)
    y.append(i[1])
    yN.append(i[1])
yU=[]
xMeanTU=[]
for i in tmeanU:
    xMeanTU.append(i[0]*1000000)
    yU.append(i[1]+barWidth)
yB=[]
xMeanTB=[]
for i in tmeanB:
    xMeanTB.append(i[0]*1000000)
    yB.append(i[1]+(2*barWidth))
yL=[]
xMeanTL=[]
for i in tmeanL:
    xMeanTL.append(i[0]*1000000)
    yL.append(i[1]+(3*barWidth))

plt.plot(y, xMeanTN,label='Normal Distribution',marker='o',markersize=9,linewidth=3)
plt.plot(y, xMeanTU,label='Uniform Distribution',marker='v',markersize=9,linewidth=3)
plt.plot(y, xMeanTB,label='Beta Distribution',marker='s',markersize=9,linewidth=3)
plt.plot(y, xMeanTL,label='Log-normal Distribution',marker='*',markersize=9,linewidth=3)
#plt.bar(yN, xMeanTN,label='Normal Distribution', color="red", width=barWidth)
#plt.bar(yU, xMeanTU,label='Uniform Distribution',color="blue", width=barWidth)
#plt.bar(yB, xMeanTB,label='Beta Distribution',color="green", width=barWidth)
#plt.bar(yL, xMeanTL, label='Log-normal Distribution',color="yellow", width=barWidth)


plt.xlabel('number of clients',fontsize=16)
plt.ylabel(r'Frame Transmission time $\mu$sec'     ,fontsize=16)
plt.grid(True)
#plt.xticks([r + barWidth for r in range(len(xMeanTN))], y)
#yy=[ri + barWidth+barWidth for ri in range(2,len(y)+2)]
#plt.xticks(yy, y)
#plt.title("Number of clients vs OFDMA Frame Transmission time",fontsize=16)

plt.legend(fontsize=16,loc='upper left')

plt.show()


y=[]
xMeanTrN=[]
for i in tHmeanN:
    xMeanTrN.append(i[0]/1000000)
    y.append(i[1])
xMeanTrU=[]
for i in tHmeanU:
    xMeanTrU.append(i[0]/1000000)
    
xMeanTrB=[]
for i in tHmeanB:
    xMeanTrB.append(i[0]/1000000)

xMeanTrL=[]
for i in tHmeanL:
    xMeanTrL.append(i[0]/1000000)

plt.plot(y, xMeanTrN,label='Normal Distribution',marker='o',linewidth=3,markersize=9)
plt.plot(y, xMeanTrU,label='Uniform Distribution',marker='v',linewidth=3,markersize=9)
plt.plot(y, xMeanTrB,label='Beta Distribution',marker='s',linewidth=3,markersize=9)
plt.plot(y, xMeanTrL,label='Log-normal Distribution',marker='*',linewidth=3,markersize=9)


plt.xlabel('number of clients',fontsize=16)
plt.ylabel("Aggregate Downlink throughput  (Mbps)",fontsize=16)
plt.grid(True)
#plt.title("Number of clients vs Ap Rate",fontsize=16)

plt.legend(fontsize=16,loc='lower left')

plt.show()



y=[]
xMeanTpN=[]
for i in tPmeanN:
    xMeanTpN.append(i[0]/1000000)
    y.append(i[1])
xMeanTpU=[]
for i in tPmeanU:
    xMeanTpU.append(i[0]/1000000)
    
xMeanTpB=[]
for i in tPmeanB:
    xMeanTpB.append(i[0]/1000000)

xMeanTpL=[]
for i in tPmeanL:
    xMeanTpL.append(i[0]/1000000)

plt.plot(y, xMeanTpN,label='Normal Distribution',marker='o',markersize=9,linewidth=3)
plt.plot(y, xMeanTpU,label='Uniform Distribution',marker='v',markersize=9,linewidth=3)
plt.plot(y, xMeanTpB,label='Beta Distribution',marker='s',markersize=9,linewidth=3)
plt.plot(y, xMeanTpL,label='Log-normal Distribution',marker='*',markersize=9,linewidth=3)

plt.xlabel('number of clients',fontsize=16)
#plt.rcParams["font.family"] = "Arial"
plt.ylabel(r'Average padding $\mu$sec',fontsize=16)
plt.grid(True)
#plt.title("Number of clients vs Avg padding",fontsize=16)

plt.legend(fontsize=16,loc='upper left')

plt.show()

dist=[]
for i in y:
    dist.append("Normal")
data1 = {'transmission_time':xMeanTN,'padding duration':xMeanTpN,"throughput":xMeanTrN ,'Clients':y,'distribution':dist} 

dist=[]
for i in y:
    dist.append("Log-normal")
data2 = {'transmission_time':xMeanTL,'padding duration':xMeanTpL,"throughput":xMeanTrL ,'Clients':y,'distribution':dist} 
dist=[]
for i in y:
    dist.append("Beta")
data3 = {'transmission_time':xMeanTB,'padding duration':xMeanTpB,"throughput":xMeanTrB ,'Clients':y,'distribution':dist} 
  
dist=[]
for i in y:
    dist.append("Uniform")
data4 = {'transmission_time':xMeanTU,'padding duration':xMeanTpU,"throughput":xMeanTrU ,'Clients':y,'distribution':dist} 
  
# Create DataFrame 
df1 = pd.DataFrame(data1) 
df2 = pd.DataFrame(data2) 
df3 = pd.DataFrame(data3) 
df4 = pd.DataFrame(data4) 
df1.append(df2)
df1.append(df3)
df1.append(df4)
df1 .to_csv("brute1.csv")
barWidth=0.25
# Make the plot
plt.bar(y, xMeanTN, color='blue', width=barWidth, edgecolor='white', label='MMRU_alloc')
plt.bar(yU, xMeanTN, color='green', width=barWidth, edgecolor='white', label='Brute force')
 
# Add xticks on the middle of the group bars
plt.xlabel('Number of clients',fontsize=16)
plt.ylabel(r'Frame Transmission time $\mu$sec'     ,fontsize=16)

yy=[ri + barWidth for ri in range(2,len(y)+2)]
plt.xticks(yy, y)
plt.grid(True)

#plt.title("Number of clients vs OFDMA Frame Transmission time ",fontsize=16)
# Create legend & Show graphic
plt.legend(fontsize=16,loc='upper left')
plt.show()




plt.hist(dataDistributionN,normed=True, bins=30)
plt.xlabel('Packet size',fontsize=16)
plt.title("packet size histogram for normal Distribution",fontsize=16)
plt.show()


plt.hist(dataDistributionU,normed=True, bins=30)
plt.xlabel('Packet size')
plt.title("packet size histogram for Uniform Distribution")
plt.show()

plt.hist(dataDistributionB,normed=True, bins=30)
plt.xlabel('Packet size')
plt.title("packet size histogram for beta Distribution")
plt.show()

plt.hist(dataDistributionL,normed=True, bins=30)
plt.xlabel('Packet size')
plt.title("packet size histogram for Lognormal Distribution")
plt.show()

