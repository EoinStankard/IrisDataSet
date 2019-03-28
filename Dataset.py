#Name: Eoin Stankard
#Date: 28/03/2019
#Description: Project on the Iris Data Set
import csv
import os

Flower = ["Setosa","Versicolor","Virginica"]
print("Please Select Iris Flower")
print("1. Setosa\n2. Versicolor\n3. Virginica\n4. Exit")
choice = input("Choice: ")

def flowerFunct(F):
    os.system('cls')
    print(f"Options for {F}")
    print("1. Max Sepal Length\n2. Min Sepal Length\n3. Avg Sepal Length")
    print("4. Max Petal Length\n5. Min Petal Length\n6. Avg Petal Length")



try:
    if int(choice)==1 or int(choice)==2 or int(choice)==3:
        flowerFunct(Flower[int(choice)-1])
    elif int(choice)==4:
        print("Exit")

except:
    print("Exception")