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