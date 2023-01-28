#Autoplotter M3

import math
import scipy as sp
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

#custom functions
from functions.linearise import *
from functions.math import *
from functions.parser import *

def handler():
    x,y=[],[]
    dictionary=readfile('target/data.csv') #source
    x=list(dictionary.keys())
    for i in x:
        y.append(stats(list(map(float,dictionary[i])))[0])
    
    xerr,yerr=readerror('target/error.csv','single',xlen=len(x),ylen=len(y)) #source
    
    return list(map(float,x)),y,list(map(float,xerr)),list(map(float,yerr))

def main(x,y,xerr,yerr):
    xs,ys=linearise_function(x,y)
    xerr,yerr=propogate_error(xs,xerr,ys,yerr)

    m,c,sdm,sdc=graphing_stats(xs,ys)
    
    print('Equation of Graph is y='+str(m)+'x+'+str(c))
    print('Standard Deviation of m is '+str(sdm))
    print('Standard Deviation of c is '+str(sdc))
    
    plot(xs,ys,xerr,yerr)
    
    return

if __name__ == '__main__':
    x,y,xerr,yerr=handler()
    main(x,y,xerr,yerr)
