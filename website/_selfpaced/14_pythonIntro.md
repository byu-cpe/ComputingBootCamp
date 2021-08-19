---
layout: page
toc: true
title: Python Intro
slug: pythonIntro
type: development
order: 6
---

## Lecture Videos
On May 10th and 12th of 2021 we had an introduction to Python by Prof Lundrigan. The videos are embedded below


### Lecture 1
<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/KuD3mJxcwnk"> </iframe> 



### Lecture 2
<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/sq0_nicEFH8"> </iframe> 


{% include quizzes.html id=11 %}

{% include quizzes.html id=12 %}

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

If you are already familiar with Python, increase the difficulty by allowing a URL to be passed in instead of a file. Your utility will download the CSV file and then parse it. The third-party library [`requests`](https://docs.python-requests.org/en/master/) will be useful for this.
