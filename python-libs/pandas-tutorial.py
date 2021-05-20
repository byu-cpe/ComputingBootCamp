import pandas as pd
import numpy as np

#######################
# Series

# A series is a 1-D labeled array of any data type

# Can be created from many different things
# From dictionary
dict = {'name': 'josh', 'date': 23, 'school':'BYU'}
s_from_dict = pd.Series(dict)

print(s_from_dict)

# From ndarray
s_from_array = pd.Series(np.random.randn(6), index=['a', 'b', 'c', 'd', 'e', 'f'])
print(s_from_array)

# From list
# If leave index off, will automatically create one for your
s_from_list = pd.Series(['hello', 3, 5, 's', 'r'])
print(s_from_list)


# Can index into series like a list or ndarray
print(s_from_list[0])
print(s_from_list[0:3])

print(s_from_list[[0,2]])

# Can also get and set values by index label:
print(s_from_dict['name'])
s_from_dict['date'] = 27
print(s_from_dict)

# Lots of nice operations on series (happen by label)

s1 = pd.Series({'a':5, 'b':3, 'c':2, 'd':9})
s2 = pd.Series({'b':3, 'c':2, 'd':9, 'e':8})

print(s1+s2)

######################
# Data Frames

# 2D Array ofr labeled data with columns of potentially
# different types

# Many ways to create a data frame

# Create from dictionary of nd arrays
d = {'Names':['Joshua', 'Philip', 'Jeffrey', 'Mike', 'Brent', 'Brad', 'DJ'],
     'Offices':['460F EB', '450J EB', '460G EB', '450P EB', '450M EB', '450H EB', '450B EB'],
     'Rank':['Assistant', 'Assistant', 'Assistant', 'Full', 'Full', 'Full', 'Full'],
     'Research':['Robotics', 'Networking', 'HLS, FPGAs', 'Reliability', 'CAD Tools', 'FPGAs', 'Computer Vision']}
df = pd.DataFrame(d)


# Create from dictionary of Series or dicts
d = {"Mangelson": pd.Series(['Joshua', '460F EB', 'Assistant', 'Robotics'], index=['Name', 'Office', 'Rank', 'Research']),
     "Lundrigan": pd.Series(['Philip', '450J EB', 'Assistant', 'Networking'], index=['Name', 'Office', 'Rank', 'Research']),
     "Goeders": pd.Series(['Jeffrey', '460G EB', 'Assistant', 'HLS'], index=['Name', 'Office', 'Rank', 'Research']),     
     "Wirthlin": pd.Series(['Mike', '450P EB', 'Full', 'Reliability'], index=['Name', 'Office', 'Rank', 'Research']),
     "Nelson": pd.Series(['Brent', '450M EB', 'Full', 'FPGA CAD Tools'], index=['Name', 'Office', 'Rank', 'Research'])}

df = pd.DataFrame(d)
print(df)

# Wait the columns and rows seem to be offset.
df = df.T
print(df)

# Why use Series?
# Lets you organize by the information you have
# Dr. Goeders office is under construction right now, so lets say he doesn't have an office (or we don't know what it is)
d = {"Mangelson": pd.Series(['Joshua', '460F EB', 'Assistant', 'Robotics'], index=['Name', 'Office', 'Rank', 'Research']),
     "Lundrigan": pd.Series(['Philip', '450J EB', 'Assistant', 'Networking'], index=['Name', 'Office', 'Rank', 'Research']),
     "Goeders": pd.Series(['Jeffrey', 'Assistant', 'HLS'], index=['Name', 'Rank', 'Research']),     
     "Wirthlin": pd.Series(['Mike', '450P EB', 'Full', 'Reliability'], index=['Name', 'Office', 'Rank', 'Research']),
     "Nelson": pd.Series(['Brent', '450M EB', 'Full', 'FPGA CAD Tools'], index=['Name', 'Office', 'Rank', 'Research'])}
df = pd.DataFrame(d).T

# Create Dataframe by importing from csv
air_quality = pd.read_csv('example_data.csv')

print(air_quality)

print(air_quality.columns)

import matplotlib
#matplotlib.use('QT4Agg')
import matplotlib.pyplot as plt

air_quality.plot(x='created_at', y ='PM1.0_CF1_ug/m3')
air_quality.plot(x='created_at', y=['PM1.0_CF1_ug/m3', 'PM2.5_CF1_ug/m3', 'PM10.0_CF1_ug/m3'])
plt.show()
