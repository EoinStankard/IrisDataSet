#Name: Eoin Stankard
#Date: 24/04/2019
#Description: Project on the Iris Data Set
#******************************************************************************
#References:
#   https://gist.github.com/curran/a08a1080b88344b0c8a7
#   https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
#   https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module
#   http://www.learningaboutelectronics.com/Articles/How-to-plot-a-graph-with-matplotlib-from-data-from-a-CSV-file-using-the-CSV-module-in-Python.php
#   https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
#   https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html
#
#******************************************************************************
import csv
import os
import matplotlib.pyplot as plt 
import numpy as np

Flower = ["setosa","versicolor","virginica"]

#******************************************************************************
#Gets the maximum value for chosen species Sepal/Petals width/length
#
#   maxNum(c,f,opt)
#       c = Choice of 'sepal' or 'Petal' from "flowerFunct" function
#       f = Species of flower
#       opt = Data to be retrieved 'Sepal/Petal Width/Length'
#******************************************************************************				
def maxNum(c,f,opt):
    readfile(c,opt,"max",f)

#******************************************************************************
#Gets the minimum value for chosen species Sepal/Petals width/length
#
#   minNum(c,f,opt)
#       c = Choice of 'sepal' or 'Petal' from "flowerFunct" function
#       f = Species of flower
#       opt = Data to be retrieved 'Sepal/Petal Width/Length'
#******************************************************************************	
def minNum(c,f,opt):
    readfile(c,opt,"min",f)

#******************************************************************************
#Calculates the average species Sepal/Petal Width/Length
#
#   avgNum(c,f,opt)
#       c = Choice of 'sepal' or 'Petal' from "flowerFunct" function
#       f = Species of flower
#       opt = Data to be retrieved 'Sepal/Petal Width/Length'
#******************************************************************************	
def avgNum(c,f,opt):
    readfile(c,opt,"avg",f)
		
#******************************************************************************
#This function opens a ready only copy of the irisDataSet.csv file and then
#depending on what options were picked in the previous steps it will get the 
#data
#
#   readfile(c,opt,x,s)
#       c = Choice of 'sepal' or 'Petal'
#       opt = Data to be retrieved 'Sepal/Petal Width/Length'
#       x = Variable to check for data minimum ,maximum or average
#       s = String for species of flower
#******************************************************************************	
def readfile(c,opt,x,s):
    with open("iris.csv",'r') as df:
        reader = csv.reader(df, delimiter=',')
        minAns = 10
        maxAns = 0
        avgAns = 0
        count = 0

        if (c is 's') and (opt == 1) or  (c is 's') and (opt == 2)  or (c is 's') and (opt == 3):col = 0
        elif (c is 's') and (opt == 4) or (c is 's') and (opt == 5) or (c is 's') and (opt == 6):col = 1
        elif (c is 'p') and (opt == 1) or (c is 'p') and (opt == 2) or (c is 'p') and (opt == 3):col = 2
        elif (c is 'p') and (opt == 4) or (c is 'p') and (opt == 5) or (c is 'p') and (opt == 6):col = 3
        else:print("Error")
			
        if x == "min": #If the user requests the minimum
            for row in reader:
                if s in row:
                    if float(row[col]) <minAns:
                        minAns = float(row[col])
                else:continue
            if col ==0 and (c is 's'):print(f"{s.capitalize()} minimum sepal length is {minAns}")
            elif col ==1 and (c is 's'):print(f"{s.capitalize()} minimum sepal width is {minAns}")
            elif col ==2 and (c is 'p'):print(f"{s.capitalize()} minimum petal length is {minAns}")
            elif col ==3 and (c is 'p'):print(f"{s.capitalize()} minimum petal width is {minAns}")
            else: print("Error") 
        elif x == "max":#If the user requests the maximum
            for row in reader:
                if s in row:
                    if float(row[col]) >maxAns:
                        maxAns = float(row[col])
                    else:continue
                else:continue

            if col ==0 and (c is 's'):print(f"{s.capitalize()} maximum sepal length is {maxAns}")
            elif col ==1 and (c is 's'):print(f"{s.capitalize()} maximum sepal width is {maxAns}")
            elif col ==2 and (c is 'p'):print(f"{s.capitalize()} maximum petal length is {maxAns}")
            elif col ==3 and (c is 'p'):print(f"{s.capitalize()} maximum petal width is {maxAns}")
            else:print("Error") 
        elif x  == "avg":#If the user requests the Average
            for row in reader:
                if s in row:
                    count = count + 1
                    avgAns = avgAns + float(row[col])
                else:continue

            avgAns = avgAns/count
            if col ==0 and (c is 's'):print(f"{s.capitalize()} average sepal length is {avgAns}")
            elif col ==1 and (c is 's'):print(f"{s.capitalize()} average sepal width is {avgAns}")
            elif col ==2 and (c is 'p'):print(f"{s.capitalize()} average petal length is {avgAns}")
            elif col ==3 and (c is 'p'):print(f"{s.capitalize()} average petal width is {avgAns}")
            else:print("Error") 


			
#******************************************************************************
#This function is called after the user picks a species of flower,
#This will give the user two new menus
#One to choose if the would live Sepal or Petal Data
#The Second to give data options for what was selected in the first menu 
#
#   flowerFunct(F)
#       F = Chosen species of Flower
#******************************************************************************	
def flowerFunct(F):
    os.system('cls')
    print(f"Options for {F.capitalize()}")
    print("1. Sepal Data\n2. Petal Data")
    print("3. Home\n")
    sp = input("Choice: ")
    if int(sp)==1:
        os.system('cls')
        print(f"Options for {F.capitalize()}")
        print("1. Max Sepal Length\n2. Min Sepal Length\n3. Avg Sepal Length")
        print("4. Max Sepal Width\n5. Min Sepal Width\n6. Avg Sepal Width")
        print("7. Home\n")
        option = input("Choice: ")
        if int(option)==1:maxNum("s",F,int(option))
        elif int(option)==2:minNum("s",F,int(option))
        elif int(option)==3:avgNum("s",F,int(option))
        elif int(option)==4:maxNum("s",F,int(option))
        elif int(option)==5:minNum("s",F,int(option))
        elif int(option)==6:avgNum("s",F,int(option))
        elif int(option)==7:Init()
        else:print("Error")
    elif int(sp)==2:
        os.system('cls')
        print(f"Options for {F.capitalize()}")
        print("1. Max Petal Length\n2. Min Petal Length\n3. Avg Petal Length")
        print("4. Max Petal Width\n5. Min Petal Width\n6. Avg Petal Width")
        print("7. Home\n")
        option = input("Choice: ")
        if int(option)==1:maxNum("p",F,int(option))
        elif int(option)==2:minNum("p",F,int(option))
        elif int(option)==3:avgNum("p",F,int(option))
        elif int(option)==4:maxNum("p",F,int(option))
        elif int(option)==5:minNum("p",F,int(option))
        elif int(option)==6:avgNum("p",F,int(option))
        elif int(option)==7:Init()
        else:print("Error")
    elif int (sp)==3:Init()
    else:print("Incorrect input")

#******************************************************************************
#This function is called and will plot a graph with all species data for 
#either the species sepal or data
#******************************************************************************	

def plotData():
    os.system('cls')
    x,x1,x2=[],[],[]
    y,y1,y2=[],[],[]
    print("1. Plot Sepal data for all species\n2. Plot Petal Data for all species\n3. Home")
    choice = input("Choice: ")

    if int(choice)==1:
        plotName = "Sepal"
        rowX = 1
        rowY = 0
    elif int(choice)==2:
        plotName = "Petal"
        rowX = 3
        rowY = 2
    elif int(choice)==3:
        Init()
    else:
        print("Incorrect input given")

    with open("iris.csv",'r') as df:
        reader = csv.reader(df, delimiter=',')
        for row in reader:
            if "setosa" in row:
                x.append(float(row[rowX]))
                y.append(float(row[rowY]))
            elif "virginica" in row:
                x1.append(float(row[rowX]))
                y1.append(float(row[rowY]))
            elif "versicolor" in row:
                x2.append(float(row[rowX]))
                y2.append(float(row[rowY]))
            else:
                continue
    plt.plot(x,y, "or") 
    plt.plot(x1,y1, "ob")  
    plt.plot(x2,y2, "og")  
    plt.legend(('Setosa','Virginica','Versicolor')) 
    plt.title(f'Plotting all species {plotName} data')
    plt.xlabel(f'{plotName} Length')
    plt.ylabel(f'{plotName} Width')
    plt.show()
	

    
#******************************************************************************
#On Running the script this is where the program will start.
#It asks the user for choice species that they would like data on
#After the user picks the species of flower that they would like data on 
#the flowerFunction will be called giving the user multiple options
#
#******************************************************************************	
def Init():
    os.system('cls')
    print("Please Select Iris Species")
    print("1. Setosa\n2. Versicolor\n3. Virginica\n4. Plot All\n5. Exit")
    choice = input("Choice: ")
    if int(choice)==1 or int(choice)==2 or int(choice)==3:flowerFunct(Flower[int(choice)-1])
    elif int(choice)==4:plotData()
    elif int(choice)==5:print("Exit")
    else:print("Incorrect input value")


#******************************************************************************
#
#
#******************************************************************************	
try:
    Init()

except:
    print("Exception, Incorrect input given")