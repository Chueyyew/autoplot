#Not to be edited

import math
import scipy as sp
import numpy as np
import pandas as pd

def stats(x):
    if len(x)>10:
        #Large Data Sets
        average=sum(x)/len(x)
        xix2=[]
        for i in x:
            xix2.append((i-average)**2)
        sd=np.sqrt(sum(xix2)/len(x))
        uncertaintyAverage=sd/np.sqrt(len(x))
    else:
        #Small Data Sets
        average=sum(x)/len(x)
        Range=max(x)-min(x)
        uncertainty=Range/2
        uncertaintyAverage=uncertainty/np.sqrt(len(x))
        
    return average,uncertaintyAverage

def graphing_stats(x,y):
    sx=sum(x)
    sy=sum(y)
    n=len(x)
    
    lsx2=[]
    for i in x:
        lsx2.append(i**2)
    sx2=sum(lsx2)
    
    lsxy=[]
    for i in range(n):
        lsxy.append(x[i]*y[i])
    sxy=sum(lsxy)
    
    m=(((n*sxy)-(sx*sy))/((n*sx2)-((sx)**2)))
    c1=(sy*sx2)-(sx*sxy)
    c2=(n*sx2)-((sx)**2)
    c=c1/c2
    
    lssd2=[]
    for i in range(n):
        lssd2.append((y[i]-m*x[i]-c)**2)
    sd2=sum(lssd2)
    
    sdm=np.sqrt((n*sd2)/((n-2)*((n*sx2)-((sx)**2))))
    
    sdc=sdm*np.sqrt((sx2/n))
    
    return m,c,sdm,sdc