#Autoplotter M3

import math
import scipy as sp
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

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
