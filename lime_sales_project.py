#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:42:38 2018

@author: noisychannel
"""
#Day3 Project
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# creating a figure
fig = plt.figure(figsize = [12,8])

#Add subplot1
ax1 = fig.add_subplot(121)
x_values = range(len(months))

#plotting with line markers
ax1.plot(x_values, visits_per_month,
         marker='o',
         color = 'black')

#Title, axis labels, and legend
ax1.set(title = 'Total Visits per Month',
        xlabel='Months',
        ylabel= 'Visits per Month'
        ,xticks = x_values, 
        xticklabels = months)
ax1.legend(['Visits'],loc='best')


################
#Second Subplot
ax2 = fig.add_subplot(122)

#Plotting 3 lines, different colors
ax2.plot(x_values,key_limes_per_month,
         color='red',
         marker='x')
ax2.plot(x_values, persian_limes_per_month,
         color = 'blue',
         marker='o')
ax2.plot(x_values, blood_limes_per_month, 
         color = 'green',
         marker='')

ax2.set(title = 'Multiple Lime Types Sales per Month', 
        xlabel='Months', 
        ylabel = "Lime Sales",
        xticks=x_values,
        xticklabels=months)
ax2.legend(['Key Limes','Persian Limes', 'Blood Limes'], loc='best')

fig.savefig('goo.png')
plt.show()
