---
layout: page
toc: true
title: Python Packages
slug: pythonAdv
type: development
order: 9
---

## Lecture Video 
On May 14, 2021 Prof Mangelson gave a tutorial on how to use the Numpy, Pandas, and Matplotlib python packages. The video is embedded bellow. Most of the instructions from the lecture as well as additional information can be found in the following sections. 

<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/hdDKcOLD-5M"> </iframe> 

### Video Timestamps

* Installation
* numpy - 2:29
  * Creating a numpy array - 3:46
  * Array indexing - 9:28
  * Array operations - 12:16
* matplotlib - 26:42
  * General graphing - 27:55
  * Other types of plots - 38:32
* pandas - 48:39

## Overview

In this module, we are going to provide an introduction to several essential python libraries. There are many many more libraries than we can cover and the details of each library is much larger than we can fully cover as well, so this is just supposed to give you a brief introduction to some essential libraries and their basic use.

In particular, in this module, we will cover the basic usage of the following libraries:
* pandas
* matplotlib
* numpy

### Installing the Libs

Installing these packages is relatively easy. All you need to do is:

```
# Source your local environment 
source ~/myenv/bib/activate
# Install via pip
pip install numpy pandas matplotlib
```


## Numpy

Numpy is a library that supports various numerical and mathematical operations on arrays and matrices.

### Numpy Arrays

The primary data structures in numpy are numpy arrays that can be either singular or multi-dimensional. There are many different methods that can be used to create a numpy array:
* Create from a python list, or a list of lists, or lists of lists of lists...
* Create and fill with zeros (np.zeros)
* Create and fill with ones (np.ones)
* Create without initializing (np.empty)
* Create with an incremental range of values (np.arange)
* Create with a linear spacing of values (np.linspace)
* And many others...

More information about the many different ways of creating these arrays can be found at:
<https://numpy.org/doc/stable/user/absolute_beginners.html>

### Array Operations

Numpy also provides a variety of methods for manipulating and operating on arrays. These range from things like sorting, reshaping, masking, and concatenating arrays to numerical operations such as summing, applying an operation to every element, to linear algera operations such as matrix multiplication, matrix transpose, matrix inversion, and matrix decomposition.

Numpy is designed in such a way that for most operations you can avoid iterating through all elements of the array by hand and apply operations to every element with only a single command. It is considered un-pythonic to use for loops on numpy arrays.

There are way too many methods and operations for us to cover all of them here, but you can find more information at the numpy official documentation site: <https://numpy.org/doc/stable/reference/routines.html>

### Followup Activities

Your followup assignment for numpy is to look through the documentation at the link above(and google for what you can't find there) and try out the operations related to the following topics:

* Array creation - Try creating arrays using np.ones, np.zeros, np.arange, np.linspace, and from lists of lists.
* Array indexing - Try out the various methods for accessing array elements,  See: <https://numpy.org/doc/stable/reference/arrays.indexing.html>
* Array Operations
  * Sort an array
  * Find the unique elements in an array
  * Search an array for a specific value
* Generating random arrays or values - Try out the various methods for generating random values, see: <https://numpy.org/doc/1.16/reference/routines.random.html>. In particular, try out:
  * Generating random values from a normal distribution
  * Generating random values from a multi-variate normal distribution
  * Generating random values from a uniform distribution
* Running statistical and mathematical operations an array of elements:
  * Calculate the sum of an array
  * Calcualte the sum of a 2D array along the columns/rows
  * Calculate the mean of an array
  * Calculate the standard deviation of an array
  * Calculate the covariance of the columns of a 2D array
* Performing matix operations on a 2D-array or pair of 2D-arrays:
  * Perform matrix multiplication between two arrays of matching sizes
  * Calculate the dot product between two arrays
  * Calculate the eigenvalue, Cholesky, and SVD decompositions of a matrix
*Broadcasting

## Matplotlib

Matplotlib is a library for plotting and visualizing data. It provides functionality for generating many different kinds of plots and graphs and even for plotting in 3-dimensions and displaying images.

### Figures, Axes, Axis, and Artists

There are four main data structures used in matplotlib:
* Figures - A figure is the highest-level object that can consist of multiple plots
* The Axes - An individual axes is a specific plot or graph
* An Axis - An axis a number-line-like object that keeps track of the limits and borders of a plot
* An Artist - An artist is the actual data or object that is plotted on the figure

### A Simple Example

Creating a figure is relatively easy:
```
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # a figure with a single Axes
```

We can then generate a plot by simply calling the "plot" function on the axis. Additional functions can be called to add labels, titles, and legends.

```
x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.

# Citation: Example from matplotlib.org tutorial
```

For more information see: <https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py>

### Followup Activities

The standard line plot described is just one of many many plots that can be generated by matplotlib.

For a followup activity, read more about the following topics and experiment with some of the methods provided (if you don't know what these plots mean or why they are used, take this opportunity to learn that as well):
* Histograms - <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html>
* Box plots - <https://matplotlib.org/3.2.2/api/_as_gen/matplotlib.pyplot.boxplot.html>
* Bar plots - <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html>
* Scatter plots - <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter>
* Plotting a 3D Surface - <https://matplotlib.org/stable/gallery/mplot3d/surface3d.html>
* Log plots - (Try to find this documentation your self)
* heatmaps/images (plt.imshow()) - (Try to find this documentation your self)
* Plotting a 3D bar graph - (Try to find this documentation your self)
* Plotting latex-notation in the plot - (Try to find this documentation your self)
* Specifying markder shape, color, etc... - <https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html>

## Pandas

Pandas is a library that enables interaction with and analysis of tabulated datasets. For example, the csv parser similar to the one you implemented in the previous module is built into pandas.

The two main data stuctures in pandas are:
* Series - A 1-D list of labeled data that can be of varying types
* DataFrame - A 2-D table where each column is of specific type

Each of these data structures can be created in a variety of ways ranging from dictionaries, to lists, to numpy arrays (for Series) and from dictionaries of lists, numpy arrays, dictionaries, or Series (for DataFrames).

Find more information at: <https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html>

In addition to providing many helpful functions for manipulating and organizing data, pandas also provides methods for plotting/visualizing data, working with time series, reading/writing to/from files, and many more.

### Followup Activities

For a followup activity, read more about the following topics and experiment with some of the methods provided:
* File I/O <https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html>
* Working with timestamps and time series <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html>
* Plotting/visualization <https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html>
* Statistical tools <https://pandas.pydata.org/pandas-docs/stable/user_guide/computation.html>

## Helpful Links

* BYU ACME Tutorials - <https://foundations-of-applied-mathematics.github.io/>
* Numpy Docs - <https://numpy.org/doc/stable/>
* Matplotlib Docs - <https://matplotlib.org/stable/tutorials/index.html>
* Panda Docs - <https://pandas.pydata.org/>
