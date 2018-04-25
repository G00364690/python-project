# Declan Reidy 25/04/2018
# Initial Analysis

# Calculate various metrics

# Discover with the tutoriali
import numpy as np
data = np.genfromtxt("data/iris.csv",delimiter=",")

# Expanding tutorial into max and min, variance and standard deviation
firstcol = data[1:,0]
meanfirstcol = np.mean(data[1:,0])
minfirstcol = np.min(data[1:,0])
maxfirstcol = np.max(data[1:,0])
varfirstcol = np.var(data[1:,0])
stdfirstcol = np.std(data[1:,0])
countfirstcol = np.count_nonzero(data[1:,0])

# Printing results
print("the average of first column is: ",meanfirstcol)
print("the min value of first column is: ",minfirstcol)
print("the max value of first column is: ",maxfirstcol)
print("the variance of first column is: ",varfirstcol)
print("the standard deviation of first column is: ",stdfirstcol)
print("the count of first column is: ",countfirstcol)

# More advanced libraries
# Reference: https://stackoverflow.com/questions/26678467/export-a-pandas-dataframe-as-a-table-image
import pandas as pd
import matplotlib as pl
import subprocess

# Display a snippet of the data - The first 10 lines.
# Reference: https://www.kaggle.com/danalexandru/simple-analysis-of-iris-dataset

import csv
data = pd.read_csv("data/iris.csv", header = 0)
data = data.reset_index()
data.head(10)

# Using strings and lists to summarise total number of species in the data set
# https://stackoverflow.com/questions/997797/what-does-s-mean-in-python

species_list = list(data["Species"].unique())
print("Types of species: %s\n" % species_list)

# Create a DataFrame to structure the data correctly
# Reference: http://www.datasciencemadesimple.com/get-list-column-headers-column-name-python-pandas/

d = {
    "SepalLengthCm" : data[:,0],
    "SepalWidthCm" : data[:,1],
    "PetalLengthCm" : data[:,2],
    "PetalWidtCm" : data[:,3],
    "Species" : data[:,4]}

df = pd.DataFrame(d,columns=[ "SepalLengthCm" , "SepalWidthCm" ,"PetalLengthCm" , "PetalWidthCm" , "Species" ])
df

# Build on Tutorial and plot the data on a histogram
import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show
