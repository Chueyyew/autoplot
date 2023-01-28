import math
import scipy as sp
import numpy as np
import pandas as pd

def linearise_function(x,y):
    xs,ys=[],[]
    for i in x:
        xi=i
        xs.append(xi)
    for j in y:
        yi=j/2
        ys.append(yi)
    return xs,ys

def propogate_error(x,xerr,y,yerr):
    xs,ys=[],[]
    xcount=0
    for i in xerr:
        xi=i
        xs.append(xi)
        xcount=xcount+1
    ycount=0
    for j in yerr:
        yi=j/2
        ys.append(yi)
        ycount=ycount+1
    return xs,ys

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