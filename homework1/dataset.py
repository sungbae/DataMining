#Assignment based on MAGIC Gamma Telescope Data Set ( http://archive.ics.uci.edu/ml/datasets/MAGIC+Gamma+Telescope )

"""
Student: Sung Bae
Class: Data Mining (csci 4502)
Date: 01/26/2016
"""

import argparse
import math
import random
import matplotlib.pyplot as plt

class DataSet:
    """
    Class to store the MAGIC Gamma Telescope Data Set
    """
    def __init__(self, location):
        with open (location, "r") as myfile:
            self.readData=myfile.readlines();

def quicksort(lst):
    n = len(lst)
    if (n < 2):
        return lst
    pivot = random.choice(lst)
    lst_left = []
    lst_mid = []
    lst_right = []
    i = 0
    while (i < n):
        if (lst[i] < pivot):
            lst_left.append(lst[i])
            i = i + 1
        elif (lst[i] == pivot):
            lst_mid.append(lst[i])
            i = i + 1
        else:
            lst_right.append(lst[i])
            i = i + 1
    return quicksort(lst_left) + lst_mid + quicksort(lst_right)

def column_to_row(data, ithAttribute):
    rows = (row.strip().split(',') for row in data)
    data_list = [float(i) for i in zip(*rows)[ithAttribute-1]]
    return data_list

def standard_deviation(data_list_sorted, noOfObjects, mean):
    differences = []
    for i in range(0, noOfObjects):
        differences.append(data_list_sorted[i]-mean)
    differences_squared = [i**2 for i in differences]
    variance = sum(differences_squared)/noOfObjects

    standardDeviation = math.sqrt(variance)

    return standardDeviation

def get_quartiles(data_list_sorted, noOfObjects):
    middle = noOfObjects / 2
    even = True
    if noOfObjects % 2 == 0:
        median = (data_list_sorted[middle-1] + data_list_sorted[middle]) / 2.0
    else:
        median = data_list_sorted[middle]
        even = False
    data_list_sorted_q1 = []
    data_list_sorted_q3 = []
    quart_midpoint = len(data_list_sorted) / 4
    for i in range(0, middle-1):
        data_list_sorted_q1.append(data_list_sorted[i])
    if not even:
        middle += 1
    for i in range(middle, noOfObjects):
        data_list_sorted_q3.append(data_list_sorted[i])
    if len(data_list_sorted_q1) % 2 == 0:
        q1 = (data_list_sorted_q1[quart_midpoint-1] + data_list_sorted_q1[quart_midpoint]) / 2.0
    else:
        q1 = data_list_sorted_q1[quart_midpoint]
    if len(data_list_sorted_q3) % 2 == 0:
        q3 = (data_list_sorted_q3[quart_midpoint-1] + data_list_sorted_q3[quart_midpoint]) / 2.0
    else:
        q3 = data_list_sorted_q3[quart_midpoint]
    iqr = q3 - q1
    return q1, median, q3, iqr

def calculate(data, ithAttribute):
    """
    Input Parameters:
        data: The data that is read from the file.
        ithAttribute: The ith Attribute for which the various properties must be calculated.

    Default value of 0,infinity,-infinity are assigned to all the variables as required. 
    Objective of the function is to calculate:  N (number of objects), min, max, mean, standard deviation, Q1, median, Q3, IQR
    """
    noOfObjects , minValue , maxValue , mean , standardDeviation , q1 , median , q3 ,iqr = [0,"-inf","inf",0,0,0,0,0,0]
    data_list = column_to_row(data, ithAttribute)
    data_list_sorted = quicksort(data_list)
    noOfObjects = len(data_list_sorted)
    total_value = 0
    for i in range(0, noOfObjects):
        total_value += data_list_sorted[i]
    minValue = data_list_sorted[0]
    maxValue = data_list_sorted[noOfObjects-1]
    mean = total_value/noOfObjects
    standardDeviation = standard_deviation(data_list_sorted, noOfObjects, mean)
    quartiles = get_quartiles(data_list_sorted, noOfObjects)
    q1 = quartiles[0]
    median = quartiles[1]
    q3 = quartiles[2]
    iqr = quartiles[3]
    return noOfObjects , minValue , maxValue, mean, standardDeviation , q1 , median , q3 , iqr

def graph(data):
    attribute4 = column_to_row(data, 4)
    attribute5 = column_to_row(data, 5)
    plt.plot(attribute4,attribute5, 'ro')
    plt.xlabel('4th attribute (fConc)')
    plt.ylabel('5th attribute (fConc1)')
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Mining HW1')
    parser.add_argument('--i', type=int,
                            help="ith attribute of the dataset ( limit 1 to 10 )",
                            default=5,
                            choices=set((1,2,3,4,5,6,7,8,9,10)) ,
                            required=True)
    parser.add_argument("--data", type=str, 
                            help="Location of the downloaded file",
                            default="magic04.data.txt", 
                            required=False)
    args = parser.parse_args()
    data = DataSet(args.data)
    print ','.join(map(str,calculate(data.readData,args.i)))
    graph(data.readData)
