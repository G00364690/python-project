# Declan Reidy 25/04/2018
# Initial Analysis including implementation of research ideas including 

# Updated 27/04/2018
# Updates including printing basic statistical measurements to the terminal for all species
# defining the dataset as a data frame in python including d and df below.
# Addition of boxplo

# Attempted Update 29/04/2018
# Errors showing for dataframe df based on input d. Difficult to diagnose.
# Calculate various metrics

# Discover with the tutorial
# # Including more advanced libraries
# Reference: https://stackoverflow.com/questions/26678467/export-a-pandas-dataframe-as-a-table-image

import numpy as np
import pandas as pd
import matplotlib as pl
import matplotlib.pyplot as plt
import seaborn as sbn
import subprocess

# Display a snippet of the data - The first 10 lines.
# Reference: https://www.kaggle.com/danalexandru/simple-analysis-of-iris-dataset

import csv
data = pd.read_csv("data/iris.csv", header = 0)
data = data.reset_index()
data.head(10)
print(data.head(10))

# Expanding tutorial into max and min, variance and standard deviation using the numpy library. 
# tuturial examples are limited to column 1 and want to perform calculations across multiple columns.
# We won't print these definitions later.

data = np.genfromtxt("data/iris.csv",delimiter=",")

firstcol = data[1:,0]
meanfirstcol = np.mean(data[1:,0])
minfirstcol = np.min(data[1:,0])
maxfirstcol = np.max(data[1:,0])
varfirstcol = np.var(data[1:,0])
stdfirstcol = np.std(data[1:,0])
countfirstcol = np.count_nonzero(data[1:,0])

# Calculating the basic statistics across our data range and rounding to a maximum of 3 digits.
# As we have 3 species and 4 measurements we'll need to compare the 3 species using like for like measurements.
# This results in needing to compare Sepal Length in CM across the 3 different species and so on.
# This results in 12 variables per statistical measurement.
# Separating the known data set by species. We'll call these later to print in cases of like for like.
# mean
mean_set_sep_len = np.mean(data[1:50,0]).round(3)
mean_set_sep_wid = np.mean(data[1:50,1]).round(3)
mean_set_pet_len = np.mean(data[1:50,2]).round(3)
mean_set_pet_wid = np.mean(data[1:50,3]).round(3)

mean_ver_sep_len = np.mean(data[51:101,0]).round(3)
mean_ver_sep_wid = np.mean(data[51:101,1]).round(3)
mean_ver_pet_len = np.mean(data[51:101,2]).round(3)
mean_ver_pet_wid = np.mean(data[51:101,3]).round(3)

mean_vir_sep_len = np.mean(data[101:151,0]).round(3)
mean_vir_sep_wid = np.mean(data[101:151,1]).round(3)
mean_vir_pet_len = np.mean(data[101:151,2]).round(3)
mean_vir_pet_wid = np.mean(data[101:151,3]).round(3)

# min
min_set_sep_len = np.min(data[1:50,0])
min_set_sep_wid = np.min(data[1:50,1])
min_set_pet_len = np.min(data[1:50,2])
min_set_pet_wid = np.min(data[1:50,3])

min_ver_sep_len = np.min(data[51:101,0])
min_ver_sep_wid = np.min(data[51:101,1])
min_ver_pet_len = np.min(data[51:101,2])
min_ver_pet_wid = np.min(data[51:101,3])

min_vir_sep_len = np.min(data[101:151,0])
min_vir_sep_wid = np.min(data[101:151,1])
min_vir_pet_len = np.min(data[101:151,2])
min_vir_pet_wid = np.min(data[101:151,3])

# max
max_set_sep_len = np.max(data[1:50,0])
max_set_sep_wid = np.max(data[1:50,1])
max_set_pet_len = np.max(data[1:50,2])
max_set_pet_wid = np.max(data[1:50,3])

max_ver_sep_len = np.max(data[51:101,0])
max_ver_sep_wid = np.max(data[51:101,1])
max_ver_pet_len = np.max(data[51:101,2])
max_ver_pet_wid = np.max(data[51:101,3])

max_vir_sep_len = np.max(data[101:151,0])
max_vir_sep_wid = np.max(data[101:151,1])
max_vir_pet_len = np.max(data[101:151,2])
max_vir_pet_wid = np.max(data[101:151,3])

# variance
var_set_sep_len = np.var(data[1:50,0]).round(3)
var_set_sep_wid = np.var(data[1:50,1]).round(3)
var_set_pet_len = np.var(data[1:50,2]).round(3)
var_set_pet_wid = np.var(data[1:50,3]).round(3)

var_ver_sep_len = np.var(data[51:101,0]).round(3)
var_ver_sep_wid = np.var(data[51:101,1]).round(3)
var_ver_pet_len = np.var(data[51:101,2]).round(3)
var_ver_pet_wid = np.var(data[51:101,3]).round(3)

var_vir_sep_len = np.var(data[101:151,0]).round(3)
var_vir_sep_wid = np.var(data[101:151,1]).round(3)
var_vir_pet_len = np.var(data[101:151,2]).round(3)
var_vir_pet_wid = np.var(data[101:151,3]).round(3)

#standard deviation
std_set_sep_len = np.std(data[1:50,0]).round(3)
std_set_sep_wid = np.std(data[1:50,1]).round(3)
std_set_pet_len = np.std(data[1:50,2]).round(3)
std_set_pet_wid = np.std(data[1:50,3]).round(3)

std_ver_sep_len = np.std(data[51:101,0]).round(3)
std_ver_sep_wid = np.std(data[51:101,1]).round(3)
std_ver_pet_len = np.std(data[51:101,2]).round(3)
std_ver_pet_wid = np.std(data[51:101,3]).round(3)

std_vir_sep_len = np.std(data[101:151,0]).round(3)
std_vir_sep_wid = np.std(data[101:151,1]).round(3)
std_vir_pet_len = np.std(data[101:151,2]).round(3)
std_vir_pet_wid = np.std(data[101:151,3]).round(3)

#print the results
print("Mean")
print("Sepal Length: Setosa", mean_set_sep_len, "Versicolor", mean_ver_sep_len, "Virginica", mean_vir_sep_len)
print("Sepal Width: Setosa", mean_set_sep_wid, "Versicolor", mean_ver_sep_wid, "Virginica", mean_vir_sep_wid)
print("Petal Length: Setosa", mean_set_pet_len, "Versicolor", mean_ver_pet_len, "Virginica", mean_vir_pet_len)
print("Petal width: Setosa", mean_set_pet_wid, "Versicolor", mean_ver_pet_wid, "Virginica", mean_vir_pet_wid)
print("")
print("Min")
print("Sepal Length: Setosa", min_set_sep_len, "Versicolor", min_ver_sep_len, "Virginica", min_vir_sep_len)
print("Sepal Width: Setosa", min_set_sep_wid, "Versicolor", min_ver_sep_wid, "Virginica", min_vir_sep_wid)
print("Petal Length: Setosa", min_set_pet_len, "Versicolor", min_ver_pet_len, "Virginica", min_vir_pet_len)
print("Petal width: Setosa", min_set_pet_wid, "Versicolor", min_ver_pet_wid, "Virginica", min_vir_pet_wid)
print("")
print("Max")
print("Sepal Length: Setosa", max_set_sep_len, "Versicolor", max_ver_sep_len, "Virginica", max_vir_sep_len)
print("Sepal Width: Setosa", max_set_sep_wid, "Versicolor", max_ver_sep_wid, "Virginica", max_vir_sep_wid)
print("Petal Length: Setosa", max_set_pet_len, "Versicolor", max_ver_pet_len, "Virginica", max_vir_pet_len)
print("Petal width: Setosa", max_set_pet_wid, "Versicolor", max_ver_pet_wid, "Virginica", max_vir_pet_wid)
print("")
print("Variance")
print("Sepal Length: Setosa", var_set_sep_len, "Versicolor", var_ver_sep_len, "Virginica", var_vir_sep_len)
print("Sepal Width: Setosa", var_set_sep_wid, "Versicolor", var_ver_sep_wid, "Virginica", var_vir_sep_wid)
print("Petal Length: Setosa", var_set_pet_len, "Versicolor", var_ver_pet_len, "Virginica", var_vir_pet_len)
print("Petal width: Setosa", var_set_pet_wid, "Versicolor", var_ver_pet_wid, "Virginica", var_vir_pet_wid)
print("")
print("Standard Deviation")
print("Sepal Length: Setosa", std_set_sep_len, "Versicolor", std_ver_sep_len, "Virginica", std_vir_sep_len)
print("Sepal Width: Setosa", std_set_sep_wid, "Versicolor", std_ver_sep_wid, "Virginica", std_vir_sep_wid)
print("Petal Length: Setosa", std_set_pet_len, "Versicolor", std_ver_pet_len, "Virginica", std_vir_pet_len)
print("Petal width: Setosa", std_set_pet_wid, "Versicolor", std_ver_pet_wid, "Virginica", std_vir_pet_wid)


# Reducing original work to peripheral notes: 
# Printing results
# print("the average of sepal length of Iris Setosa: ",meanfirstcol)
# print("the min value of first column is: ",minfirstcol)
# print("the max value of first column is: ",maxfirstcol)
# print("the variance of first column is: ",varfirstcol)
# print("the standard deviation of first column is: ",stdfirstcol)
# print("the count of first column is: ",countfirstcol)

#Expanding the results to multiple columns with a loop
# with open("data/iris.csv") as f: #Read data file iris.csv
# for line in f: #for each line in the file
    
#    print(line.split(",")[0],"",line.split(",")[1],"",line.split(",")[2],"",line.split(",")[3])



# Using strings and lists to summarise total number of species in the data set
# https://stackoverflow.com/questions/997797/what-does-s-mean-in-python

species_list = list(data["Species"].unique())
print("Types of species: %s\n" % species_list)
print("")

# Create a DataFrame to structure the data correctly
# Reference: http://www.datasciencemadesimple.com/get-list-column-headers-column-name-python-pandas/

# Created a dataframe to print the full data out. This code working on 25/04/2018 but I have made some change that I cannot seem to rectify and it now returns an error.
# Error has arisen and after many hours searching I cannot diagnose the nature of the error.
# The DF returned the data cleanly in table format.

import numpy as np
import pandas as pd

d = {
    "SepalLengthCm" : data[:,0],
    "SepalWidthCm" : data[:,1],
    "PetalLengthCm" : data[:,2],
    "PetalWidtCm" : data[:,3],
    "Species" : data[:,4]}

df = pd.DataFrame(d,columns=[ "SepalLengthCm" , "SepalWidthCm" ,"PetalLengthCm" , "PetalWidthCm" , "Species" ])
print(df)

# Build on Tutorial and plot the data on a histogram. 
# The consenus visual analysis package appears to be Seaborn. Many other analysts have used FacetGrid function to show the relationship between 3 different species when comparing multiple variables.
# Boxplot documentation: https://seaborn.pydata.org/generated/seaborn.boxplot.html
# FacetGrid documentation: https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
# PairPlot documentation: https://seaborn.pydata.org/generated/seaborn.pairplot.html

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sbn

# Study each measurement variable independently of others and compare and contrast species using box plotting
# Boxplot documentation: https://seaborn.pydata.org/generated/seaborn.boxplot.html

sbn.boxplot(x="Species",y="SepalLengthCm",data=data)
sbn.boxplot(x="Species",y="SepalWidthCm",data=data)
sbn.boxplot(x="Species",y="PetalLengthCm",data=data)
sbn.boxplot(x="Species",y="PetalWidthCm",data=data)

# Show the plots
plt.show()

# Plot 2 variables against each other. From the statistical analysis the 
# FacetGrid documentation: https://seaborn.pydata.org/generated/seaborn.FacetGrid.html

sbn.FacetGrid(data,hue="Species",size=6).map(plt.scatter, "SepalLengthCm", "SepalWidthCm").add_legend()
sbn.FacetGrid(data,hue="Species",size=6).map(plt.scatter, "PetalLengthCm", "PetalWidthCm").add_legend()
sbn.FacetGrid(data,hue="Species",size=6).map(plt.scatter, "SepalLengthCm", "PetalLengthCm").add_legend()
sbn.FacetGrid(data,hue="Species",size=6).map(plt.scatter, "SepalWidthCm", "PetalWidthCm").add_legend()

# Show the plots
plt.show()

# Advanced, plot all 12 combinations of Sepal variable versus Petal variable together. This can be achieved through Pairplotting.
# PairPlot documentation: https://seaborn.pydata.org/generated/seaborn.pairplot.html

sbn.pairplot(data, hue="Species",size=3, diag_kind="hist")

# Show the plot
plt.show()
