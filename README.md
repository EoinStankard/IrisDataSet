# Iris Data Set

This repository contains my solutions to the 2019 Project for the module Programming and Scripting in GMIT.
The Project decription is found in the Project-Instructions.pdf file

## How to download this repository
1. Go To Github
2. Click the download button or Clone
3. To Clone- Open the command prompt in the desired destionation of the Repo, Get the Repository HTTP address and type the following in the command line
    A. git clone "Address"
    
## How to run the code
1. Make sure Python is installed
2. Go to the location of the python scripts and open a command window
3. Make sure that both Dataset.py and iris.csv are cloned, Otherwise script will not work
3. Enter 'Python Dataset.py

## Code Functionality

This script will ask the user for multiple different inputs and will then output the result.

On running the script the user will be asked to choose a iris species or if they would like a plot of the data

If the user chose a iris specie they will be asked if they would Sepal or Petal data. They can also return to the home screen where they started.

The next user input is the last before they get there result. The user will be given seven choices. If the user had picked Setosa flower and Sepal data in the previous windows they will be given the following choices.                                                              1. Max Sepal Length                                                                                                                      2. Min Sepal Length                                                                                                                      3. Avg Sepal Length                                                                                                                      4. Max Sepal Width                                                                                                                      5. Min Sepal Width                                                                                                                      6. Avg Sepal Width                                                                                                                      7. Home                                                                                                                              For example if the user chose option one here they would get the following output                                                            "Setosa maximum sepal length is 5.8"

From the home menu if the user chose Plot they would be then asked if they would like Sepal or Petal Data plotted.
A plot diagram will then pop up showing for examle all petal data for the three species of flower. Each specie can be clearly distinguished dues to there colors and plot legend, The petal length will be on the Y-Axis and the petal width will be on the X-Axis 

Error checking is checking for an incorrect input and if the input is incorrect the program will end.This runs throughout the whole program

## References
  1. https://gist.github.com/curran/a08a1080b88344b0c8a7
  
  2. https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

  3. https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module
  
  4. http://www.learningaboutelectronics.com/Articles/How-to-plot-a-graph-with-matplotlib-from-data-from-a-CSV-file-using-the-CSV-module-in-Python.php

  5. https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
  
  6. https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html

