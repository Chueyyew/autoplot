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


