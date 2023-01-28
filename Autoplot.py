#Autoplotter M3

import math
import scipy as sp
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt



def points():
    a = int(input('Number of Points: ')) #Establishing the number of data points overall
    b = int(input('Number of X readings: ')) #Entering the various X values, factoring multiple readings
    xs,ys,xerrs,yerrs=[],[],[],[]
    
    constant_x_error=input('Is X Error Constant (Y/N)')
    constant_y_error=input('Is Y Error Constant (Y/N)')
    
    if constant_y_error=='Y' or 'y':
        yerr=float(input('Error on Y:'))
        
        if constant_x_error=='Y' or 'y':
            xerr=float(input('Error on X:'))
        
            for i in range(a):
                y=float(input('Y: ')) #Entering the various Y values, whilst iterating across the number of data points

                if b>1:
                    xls=[]
                    for i in range(b):  
                        xls.append(xerr)
                    x,xerr=stats(xls) #Calculating error
                elif b==1:
                    x=float(input('X: '))

                print("Point is ("+str(x)+","+str(y)+")")
                xs.append(x)
                ys.append(y)
                xerrs.append(xerr)
                yerrs.append(yerr)
        else:
            for i in range(a):
                y=float(input('Y: ')) #Entering the various Y values, whilst iterating across the number of data points

                if b>1:
                    xls=[]
                    for i in range(b):  
                        xls.append(float(input('X: ')))
                    x,xerr=stats(xls) #Calculating error
                elif b==1:
                    x=float(input('X: '))

                print("Point is ("+str(x)+","+str(y)+")")
                xs.append(x)
                ys.append(y)
                xerrs.append(xerr)
                yerrs.append(yerr)
    else:
        if constant_x_error=='Y' or 'y':
            xerr=float(input('Error on Y:'))
        
            for i in range(a):
                y=float(input('Y: ')) #Entering the various Y values, whilst iterating across the number of data points
                yerr=float(input('Error on Y:'))
                
                if b>1:
                    xls=[]
                    for i in range(b):  
                        xls.append(xerr)
                    x,xerr=stats(xls) #Calculating error
                elif b==1:
                    x=float(input('X: '))
                    xerr=float(input('X Error: '))

                print("Point is ("+str(x)+","+str(y)+")")
                xs.append(x)
                ys.append(y)
                xerrs.append(xerr)
                yerrs.append(yerr)
        else:
            for i in range(a):
                y=float(input('Y: ')) #Entering the various Y values, whilst iterating across the number of data points
                yerr=float(input('Error on Y:'))
                
                if b>1:
                    xls=[]
                    for i in range(b):  
                        xls.append(float(input('X: ')))
                    x,xerr=stats(xls) #Calculating error
                elif b==1:
                    x=float(input('X: '))
                    xerr=float(input('X Error: '))

                print("Point is ("+str(x)+","+str(y)+")")
                xs.append(x)
                ys.append(y)
                xerrs.append(xerr)
                yerrs.append(yerr)

    return xs,ys,xerrs,yerrs

def plot(x,y,xerr,yerr):
    fig,ax=plt.subplots()
    a, b = np.polyfit(x, y, 1)
    
    ypoints=[]
    for i in x:
        ypoints.append(a*i+b)
    
    ax.plot(x, ypoints,color='black')

    ax.errorbar(x, y, yerr=yerr,xerr=xerr, fmt='none',ecolor='#000000',color='#000000',elinewidth=0.5,capsize=2)
    
    ax.text(-1, 0.35, 'y = ' + '{:.5f}'.format(a) + 'x' + ' + {:.5f}'.format(b), size=10)
    ax.set_xlabel("Distance R, r (m)")
    ax.set_ylabel('Amplitude of Wave, A (V)')
    ax.tick_params(axis='both',direction='inout')
    
    plt.savefig('Graph1',dpi=500)

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
    x,y,xerr,yerr=points()
    main(x,y,xerr,yerr)
