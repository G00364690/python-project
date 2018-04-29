## What’s been written about the Iris Data set?
The data set was created by Fisher for his 1936 paper entitled: “the use of multiple measurements in taxonomic problems”.   The data is 50 samples from each of 3 related species of iris flower. The three species are setosa, sersicolor and virginica. Four features were measured: Sepal length, Sepal width, Petal length and Petal width. The fifth attribute to analyse each data line is the species or class.

## Some examples of good analyses at a quick search (I have found these are clearest in Kaggle):

1.	https://www.kaggle.com/danalexandru/simple-analysis-of-iris-dataset
Simple analysis of the data set. 

Imported NumPy, pandas, matplotlib, pyplot, pylab, seaborn.

Analysed 150 data samples with respect to:
	Sepal length range, variance and standard deviation
	Sepal width range, variance and standard deviation
	Petal length range, variance and standard deviation
	Petal width range, variance and standard deviation
  
2.	https://www.kaggle.com/farheen28/iris-dataset-analysis-using-knn

Simple analysis of the data set.
Imported Seaborn.

Using Facetgrid, analysed the 3 species of iris plotting sepal length against sepal width. Setosa is easily distinguished while versicolor and verginica can’t be distinguished using this approach. Using pairplot we can see petal length versus petal width gives a clear indication of the data set.

3.	https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis

Imported Matplotlib.pyplot
Not a comprehensive plot and plots petal width on the Y axis and petal length on the X axis. This is a much cleaner visual correlation when the axes are inverted.
Using K - Nearest Neighbours (KNN) Algorithm 

4.	https://www.kaggle.com/sridharcr/data-analysis-iris-dataset

Using correlation matrices and normalisation techniques to predict outcomes. 
Predict the species based on its 4 primary characteristics.

5.	https://www.kaggle.com/camontanezp/learning-python-data-analysis-with-iris

Using seaborn and pairplotting to discover the linear correlation between Petal length and Petal width and the clear separation of the different species based on this analysis.

6.	http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

Using eigenvalues to plot eigenvectors and show 3D modelling of the data. (advanced)

## First learnings
Introduction to all: http://josephcslater.github.io/scipy-numpy-matplotlib-pylab.html
Pandas v NumPy: https://stackshare.io/stackups/pandas-vs-numpy

Numpy:  NumPy (pronounced /ˈnʌmpaɪ/ (NUM-py) or sometimes /ˈnʌmpi/ (NUM-pee)) is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. 
https://en.wikipedia.org/wiki/NumPy

Pandas:  pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way toward this goal	
https://pandas.pydata.org/pandas-docs/stable/

Matplotlib: Matplotlib is a plotting library for the Pythonprogramming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK+ 
https://en.wikipedia.org/wiki/Matplotlib

Pyplot:  Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. ... For simple plotting the pyplot module provides a MATLAB-like interface, particularly when combined with IPython
https://matplotlib.org/

Scatterplot: A scatter plot of y vs x with varying marker size and/or colour.
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html

%pylab is a "magic function" that you can call within IPython, or Interactive Python. By invoking it, the IPython interpreter will import matplotlib and NumPy modules such that you'll have convenient access to their functions.
http://jakevdp.github.io/mpl_tutorial/tutorial_pages/tut1.html

SciPy (pronounced /ˈsaɪpaɪ'/ "Sigh Pie") is an open-source Python library used for scientific computing and technical computing. ... The NumPy stack is also sometimes referred to as the SciPy stack.
https://en.wikipedia.org/wiki/SciPy

Seaborn: seaborn: statistical data visualization. Seaborn is a Pythonvisualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.
https://seaborn.pydata.org/

Pairplot: By default, this function will create a grid of Axes such that each variable in data will by shared in the y-axis across a single row and in the x-axis across a single column. The diagonal Axes are treated differently, drawing a plot to show the univariate distribution of the data for the variable in that column.
https://seaborn.pydata.org/generated/seaborn.pairplot.html

k-nearest neighbors algorithm. In pattern recognition, the k-nearest neighbors algorithm (k-NN) is a non-parametricmethod used for classification and regression. In both cases, the input consists of the k closest training examples in the feature space.
https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
© 2018 GitHub, Inc.

## Further Development of ideas

Data Frames: http://www.datasciencemadesimple.com/get-list-column-headers-column-name-python-pandas/

Visual Analysis libraries: 
The consenus visual analysis package appears to be Seaborn. Boxplotting, FacetGrid and Pairplotting can show the relationship between 3 different species when comparing multiple variables.
Boxplot documentation: https://seaborn.pydata.org/generated/seaborn.boxplot.html
FacetGrid documentation: https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
PairPlot documentation: https://seaborn.pydata.org/generated/seaborn.pairplot.html
