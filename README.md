# python-project
This repository captures the contents of the term project submission of  Declan Reidy for the Programming and Scripting module for Higher Diploma in Data Analytics 2018

## Intial thoughts
The initial impression of the project is to break the requirements down into bitesize snippets. At first pass I'd like to attempt to write my own functions for the Average, Mean, Standard Deviation as well as Max and Min. First port of call has been: https://www.bigskyassociates.com/blog/bid/356764/5-Most-Important-Methods-For-Statistical-Data-Analysis

## Further investigation
Upon investigation over the past number of weeks it has become clear that several packages available for import into anaconda will best fulfil the brief of this project. Initially focusing on the scripting elements of the course led me to investigate writing my own functions. With time and reflection I came to the conclusion that the point of this project was to begin to think bigger and discover the power of python and it's associated libraries for data analysis.

## Investigative sources
Combining some research of how others have tackled this problem with a lot of learning around basic definitions of libraries and what they can offer for data analysis, led me to a common approach adopted by many. These analysts have used combinations of the Numpy, Pandas, Matplotlib and Seaborn imported libraries and some basic python commands to generate strong analyses and inflenced me to conduct my analysis in this way using basic statistical information and some relevant graphical plotting. My research and influences for this project are listed in Initial Research.

## Getting started
In order to get started in earnest I first began by reading my data file into Python. I found through research that a common and simple method to do this was by using the import csv library. To ensure I was indeed reading the correct file, I ran a simple test to check the first number of lines using the .head() command. This validated I was reading the correct file. You can find my attempts to get started in the First Steps Summary file

## Investigative method

### Method 1
As highlighted in Initial Research, the consensus methods of creating a data analysis tend to begin with basic concepts such as reading from a file of data, and performing some basic statistical analysis of the data within. Referenced in Further Research.py, my initial pass I focused on
1. Mean - using numpy.mean()
2. Min - using numpy.min()
3. Max - using numpy.max()
4. Variance - using numpy.var()
5. Standard Deviation - using numpy.std()
6. Count - using numpy.count_nonzero()

A very high level commentary can be formed based on these statistical findings, suggesting that:

#### Mean
Sepal Length: Setosa 5.006 Vericolor 5.936 Virgenica 6.588
Sepal Width: Setosa 3.42 Vericolor 2.77 Virgenica 2.974
Petal Length: Setosa 1.465 Vericolor 4.26 Virgenica 5.552
Petal width: Setosa 0.245 Vericolor 1.326 Virgenica 2.026

The Setosa species should be identifiable from the others primarily via the differences in the mean Petal lengths and widths. It holds that the Vericolor and 

#### Min
Sepal Length: Setosa 4.3 Vericolor 4.9 Virgenica 4.9
Sepal Width: Setosa 2.3 Vericolor 2.0 Virgenica 2.2
Petal Length: Setosa 1.0 Vericolor 3.0 Virgenica 4.5
Petal width: Setosa 0.1 Vericolor 1.0 Virgenica 1.4

#### Max
Sepal Length: Setosa 5.8 Vericolor 7.0 Virgenica 7.9
Sepal Width: Setosa 4.4 Vericolor 3.4 Virgenica 3.8
Petal Length: Setosa 1.9 Vericolor 5.1 Virgenica 6.9
Petal width: Setosa 0.6 Vericolor 1.8 Virgenica 2.5

#### Var
Sepal Length: Setosa 0.124 Vericolor 0.261 Virgenica 0.396
Sepal Width: Setosa 0.145 Vericolor 0.097 Virgenica 0.102
Petal Length: Setosa 0.03 Vericolor 0.216 Virgenica 0.298
Petal width: Setosa 0.011 Vericolor 0.038 Virgenica 0.074

#### Std
Sepal Length: Setosa 0.352 Vericolor 0.511 Virgenica 0.629
Sepal Width: Setosa 0.381 Vericolor 0.311 Virgenica 0.319
Petal Length: Setosa 0.173 Vericolor 0.465 Virgenica 0.546
Petal width: Setosa 0.107 Vericolor 0.196 Virgenica 0.272

At this very raw level it is difficult without a strong flair for statistics to truly draw and any real conclusions, so we need a more robust visualization technique to help us uncover what the data is really telling us about the entities it summarizes.

### Method 2
We need to find ways to graphically represent the data in order to better spot patterns with the naked eye.  
