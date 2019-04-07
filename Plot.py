import csv
import os
import matplotlib.pyplot as plt 
import numpy as np

def readfile():
    x,x1,x2=[],[],[]
    y,y1,y2=[],[],[]

    with open("iris.csv",'r') as df:
        reader = csv.reader(df, delimiter=',')
        for row in reader:
            if "setosa" in row:
                x.append(float(row[0]))
                y.append(float(row[1]))
                #print(row[0],row[1])
                plt.plot(x,y, "or")
            elif "virginica" in row:
                x1.append(float(row[0]))
                y1.append(float(row[1]))
                #print(row[0],row[1])
                plt.plot(x1,y1, "ob")
            elif "versicolor" in row:
                x2.append(float(row[0]))
                y2.append(float(row[1]))
                #print(row[0],row[1])
                plt.plot(x2,y2, "og")
            else:
                continue
    #plt.legend(['Setosa','ff'])
    #plt.legend(['Virginica'])
    plt.legend(('Setosa','Virginica','Versicolor'))
    plt.show()
    

readfile()