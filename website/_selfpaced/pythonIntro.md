---
layout: page
toc: true
title: Python Intro
slug: pythonIntro
type: development
order: 6
---

## Overview
Python is a high-level programming language that is interpreted rather than compiled. It is object-oriented, and as such it supports classes and also has many available data structures. It has many open-source libraries and resources that make it a very powerful and versatile tool for anyone looking to make an automated way to do a task.

While Python was first introduced in 1991, it was relatively unknown until the mid-2000s. Over the past few years, however, it has quickly become one of the most popular programming languages in the world.

## Installation
Python generally comes preinstalled on Ubuntu, but you can check which version you have by typing the following into your terminal:
```
python3 --version
```

If the above command says you don't have Python installed or if your Python version is not 3.8 (which is typically the default on Ubuntu 20), you can type the following into your terminal to get that version of Python:
```
sudo apt update
sudo apt install python3.8
```

There are also many other versions of Python you can download. Using other versions will become more important as you learn about Python Environments later on. For now, using the default version on your computer is a great starting point.

## Lecture Videos
On May 10th and 12th of 2021 we had an introduction to Python by Prof Lundrigan. The videos are embedded below


### Lecture 1
<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/KuD3mJxcwnk"> </iframe> 

<!--- #### Video Timestamps --->

### Lecture 2
<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/sq0_nicEFH8"> </iframe> 

<!--- #### Video Timestamps --->

{% include quizzes.html id=26 %}

{% include quizzes.html id=27 %}

<!--- ## Conclusion --->

## Follow-Up Activities

Create a command line utility that filters columns of a CSV file. The utility will take in a CSV file and column indexes that it should select. Use the following usage pattern:

```
usage: csv_parser.py [-h] [-c COLUMN] [-v] csv_file

Process CSV file.

positional arguments:
  csv_file              CSV file to be parsed

optional arguments:
  -h, --help            show this help message and exit
  -c COLUMN, --column COLUMN
                        columns to select from CSV file
  -v, --verbose         print logging messages
```


To build a command line tool, you will need to use [`argparse`](https://docs.python.org/3/library/argparse.html) or something similar. Your utility should work with any well formatted CSV file, but here is some example data to get you started: [small]({% link media/example_data.csv %}) and [large]({% link media/example_data_big.csv %}).

If you are already familiar with Python, increase the difficulty by allowing a URL to be passed in instead of a file. Your utility will download the CSV file and then parse it. The third-party library [`requests`](https://requests.readthedocs.io/en/latest/) will be useful  for this.

<!-- [`requests`](https://docs.python-requests.org/en/master/) link currently broken, add back later if it gets fixed -->

<!--- Certify your skills --->

## Additional Resources
For those who have not used Python before, there is a tutorial put out by python.org that is very helpful and gives a great introduction to the language. It is also a great tool for those who are familiar with Python already because it goes deeply into a lot of the available data structures and other aspects of the language. This tutorial is for Python3.10.4, which is the newest version out right now, but you can choose most of the previous versions on the drop-down menu that appears on the tutorial. The link to it is [here](https://docs.python.org/3.10/tutorial/index.html).