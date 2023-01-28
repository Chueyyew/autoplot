import csv

def readfile(source):
    
    ndict={}
    
    with open(source,newline='') as file:
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            if ' '==row[-1] or ''==row[-1]:
                x=row
                x.pop()
                ndict[x[-1]]=x[:-1]
            else:
                ndict[row[-1]]=row[:-1]
    
    return ndict

def readerror(source,mode,xlen=1,ylen=1):
    
    with open(source,newline='') as file:
        reader = csv.reader(file,delimiter=',')
        
        if mode=='multi':
            x=reader[0]
            y=reader[1]
            
            return x[1:-1],y[1:-1]
        else:
            x,y=[],[]
            for i in range(xlen):
                x.append(reader[0][1])
            for j in range(ylen):
                y.append(reader[1][1])
            return x,y
                
                

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
