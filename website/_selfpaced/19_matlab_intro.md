---
layout: page
toc: true
title: Matlab
slug: matlab
type: development
order: 14
---


## Matlab Overview

Matlab is a software used by engineers around the globe to perform mathematical computations, create graphs or models, manipulate matrices, and much more.

## Setup and Basics

FIXME: add content

## Basic plotting

Matlab offers a number of plotting capabilities.  The basic 2-D line plot requires the use of vectors, which can be created by using the form (starting point):(increment):(ending point). For example, the vector
```
  my_vector = 0:5:100
``` 
creates a vector starting at zero, ending at 100, which is incremented up by 5.

The command `plot(x,y)` creates a line-plot of the vectors x and y.  Make sure vectors x and y are of equal length.  For example, the vector
```
  x = 0:pi/30:4*pi;
```
creates a vector starting at 0 and incrementing up to 2pi.  
The vector
```
  y = sin(x);
```
creates a vector that has values that are the sine of the values in vector x.  
We can then use the command
```
plot(x,y);
```
to graph vector y versus x.

Learn more about plotting in Matlab:
  - [MathWorks plot Help Center](https://www.mathworks.com/help/matlab/ref/plot.html)

FIXME: add more content

## Manipulating matrices

FIXME: add content

