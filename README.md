# python-project
This repository captures the contents of the term project submission of  Declan Reidy for the Programming and Scripting module for Higher Diploma in Data Analytics 2018

## Intial thoughts
The initial impression of the project is to break the requirements down into bitesize snippets. At first pass I'd like to attempt to write my own functions for the Average, Mean, Standard Deviation as well as Max and Min. First port of call has been: https://www.bigskyassociates.com/blog/bid/356764/5-Most-Important-Methods-For-Statistical-Data-Analysis

## Further investigation
Upon investigation over the past number of weeks it has become clear that several packages available for import into anaconda will best fulfil the brief of this project. Initially focusing on the scripting elements of the course led me to investigate writing my own functions. With time and reflection I came to the conclusion that the point of this project was to begin to think bigger and discover the power of python and it's associated libraries for data analysis.

## Investigative sources
Combining some research of how others have tackled this problem with a lot of learning around basic definitions of libraries and what they can offer for data analysis, led me to a common approach adopted by many. These analysts have used combinations of the Numpy, Pandas, Matplotlib and Seaborn imported libraries and some basic python commands to generate strong analyses and inflenced me to conduct my analysis in this way using basic statistical information and some relevant graphical plotting. My research and influences for this project are listed in Initial Research.

## Getting started
In order to get started in earnest I first began by reading my data file into Python. I found through research that a common and simple method to do this was by using the import csv library. To ensure I was indeed reading the correct file, I ran a simple test to check the first number of lines using the .head() command. This validated I was reading the correct file. You can find my attempts to get started 

## Investigative method

### Method 1 - Statistical Analysis
As highlighted in Initial Research, the consensus methods of creating a data analysis tend to begin with basic concepts such as reading from a file of data, and performing some basic statistical analysis of the data within. Referenced in Further Research.py, my initial pass I focused on
1. Mean - using numpy.mean()
2. Min - using numpy.min()
3. Max - using numpy.max()
4. Variance - using numpy.var()
5. Standard Deviation - using numpy.std()
6. Count - using numpy.count_nonzero()

A very high level commentary can be formed based on these statistical findings, suggesting that:

#### Mean
Sepal Length: Setosa 5.006 Versicolor 5.936 Virginica 6.588
Sepal Width: Setosa 3.42 Versicolor 2.77 Virginica 2.974
Petal Length: Setosa 1.465 Versicolor 4.26 Virginica 5.552
Petal width: Setosa 0.245 Versicolor 1.326 Virginica 2.026

The mean analysis tells us the Setosa species should be identifiable from the others with the naked eye primarily via the differences in the mean Petal lengths and widths. It holds that the Versicolor and Virginica species would not be so easily identifiable, but nonetheless more identifiable through the Petal measurements as compared to the Sepal measurements.

#### Min
Sepal Length: Setosa 4.3 Versicolor 4.9 Virginica 4.9
Sepal Width: Setosa 2.3 Versicolor 2.0 Virginica 2.2
Petal Length: Setosa 1.0 Versicolor 3.0 Virginica 4.5
Petal width: Setosa 0.1 Versicolor 1.0 Virginica 1.4

#### Max
Sepal Length: Setosa 5.8 Versicolor 7.0 Virginica 7.9
Sepal Width: Setosa 4.4 Versicolor 3.4 Virginica 3.8
Petal Length: Setosa 1.9 Versicolor 5.1 Virginica 6.9
Petal width: Setosa 0.6 Versicolor 1.8 Virginica 2.5

The min-max of the data set again show that the Versicolour and the Virginica are virtually indistinguishable to the naked eye. While the Virginica is larger by all measurements in the mean, it also holds true for the min and max. Given the min and the max overlap signigicantly we need more information to adequately analyse our data set.

#### Variance
Sepal Length: Setosa 0.124 Versicolor 0.261 Virginica 0.396
Sepal Width: Setosa 0.145 Versicolor 0.097 Virginica 0.102
Petal Length: Setosa 0.03 Versicolor 0.216 Virginica 0.298
Petal width: Setosa 0.011 Versicolor 0.038 Virginica 0.074

The very low variance in general across the 3 species with respect to Petal measurements would lead us to assume the best correlations lie there. 

#### Standard Deviation
Sepal Length: Setosa 0.352 Versicolor 0.511 Virginica 0.629
Sepal Width: Setosa 0.381 Versicolor 0.311 Virginica 0.319
Petal Length: Setosa 0.173 Versicolor 0.465 Virginica 0.546
Petal width: Setosa 0.107 Versicolor 0.196 Virginica 0.272

At this very raw level it is difficult without a strong flair for statistics to truly draw and any real conclusions, so we need a more robust visualization technique to help us uncover what the data is really telling us about the entities it summarizes.

### Method 2
We need to find ways to graphically represent the data in order to better spot patterns with the naked eye. 

#### Box plotting
Looking at each variable individually can help us see interesting trends among the various species to help identify them from each other. Simple box plots for each measurement variable can show very clearly the separation and grouping of the various species when analysed by measurement variables in turn. (See Figures 1-4)

sbn.boxplot(x="Species",y="SepalLengthCm",data=data) # Figure 1:  Visual confirmation of Sepal length distinguishable across 3 species
sbn.boxplot(x="Species",y="SepalWidthCm",data=data) # Figure 2: Visual confirmation of Sepal width indistinguishable between VER/VIR
sbn.boxplot(x="Species",y="PetalLengthCm",data=data) # Figure 3: Visual confirmation of large variance in Virginica relative to Setosa
sbn.boxplot(x="Species",y="PetalWidthCm",data=data) # Figure 4 Visual confirmation of large variance in Virginica

#### Facet Grids
Having looked at the measurement variables individually plotted, now we can progress into plotting 2 at a time. Using Facet Grids we can plot each of the species simply by looking at 2 of the 4 measurements. Some obvious examples to plot are Sepal v Sepal, Petal v Petal, Length v Length, Width v Width. (See Figures 5-8)

Here a very interesting correlation comes to the fore, showing that the 3 species can be easily categorised into distinctive species when considering only Petal length and Petal width. (see Figure 6).

sbn.FacetGrid(data,hue="Species",size=6).map(plt.scatter, "SepalLengthCm", "SepalWidthCm").add_legend() # Figure 5
sbn.FacetGrid(data,hue="Species",size=6).map(plt.scatter, "PetalLengthCm", "PetalWidthCm").add_legend() # Figure 6
sbn.FacetGrid(data,hue="Species",size=6).map(plt.scatter, "SepalLengthCm", "PetalLengthCm").add_legend() # Figure 7
sbn.FacetGrid(data,hue="Species",size=6).map(plt.scatter, "SepalWidthCm", "PetalWidthCm").add_legend() # Figure 8

#### Pair Plots
A more advanced technique for plotting all 3 species of iris flower against all combinations of multiple measurement variables together, the use of a pair plot will confirm the work done by our Facet Grids for the combinations specified above, but also test other less obvious combinations for correlation. 

sbn.pairplot(data, hue="Species",size=3, diag_kind="hist") # Figure 9

Running the PairPlot above using the seaborn library allows us to generate Figure 9 and confirm our hypothesis surrounding the correlation between Petal Length and Petal Width being the clearest indicator across the 3 species when attempting to classify an unknown iris sample.
