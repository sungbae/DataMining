#Assignment based on http://www.nasdaq.com/quotes/
#Feel free to use any libraries. 
#Make sure that the output format is perfect as mentioned in the problem.
#Also check the second row of the download dataset.
#If it follows a different format, avoid it or remove it.

"""
Student: Sung Bae
Class: Data Mining (csci 4502)
"""

import argparse
import numpy
import math

class DataSet:
    """
    Class to store a file's Data Set
    """
    def __init__(self, location):
        with open (location, "r") as myfile:
            self.readData=myfile.readlines();

def column_to_row(data, attribute):
    rows = [row.strip().split(',') for row in data]
    length = len(rows)
    header = rows[0]
    # Find which column holds the given attribute
    for i, att in enumerate(header):
        if att == attribute:
            index = i
            break
    # Convert that specific column into a list
    data_list = [i for i in zip(*rows)[index]]
    # Remove the first element (attribute) of the data list
    data_list.pop(0)
    # Get rid of empty strings in list
    data_list = filter(None, data_list)
    # Convert the string list into float list
    data_list_float = [float(i) for i in data_list]
    return data_list_float

def min_max(data_list):
    min_value = min(data_list)
    max_value = max(data_list)
    diff = max_value - min_value
    result = []
    for data in data_list:
        # normalized formula 0-1 is as follows: (x - min) / (max - min)
        normalized = (data - min_value) / diff
        # append original value and new value as a list
        result.append([data, normalized])
    return result

def z_score(data_list):
    mean = numpy.mean(data_list)
    std_deviation = numpy.std(data_list)
    result = []
    for data in data_list:
        # z_score formula is as follows: (x - mean) / standard_deviation
        normalized = (data - mean) / std_deviation
        # append original value and new value as a list
        result.append([data, normalized])
    return result

def normalization ( fileName , normalizationType , attribute):
    '''
    Input Parameters:
        fileName: The comma seperated file that must be considered for the normalization
        attribute: The attribute for which you are performing the normalization
        normalizationType: The type of normalization you are performing
    Output:
        For each line in the input file, print the original "attribute" value and "normalized" value seperated by <TAB> 
    '''
    data = DataSet(fileName).readData
    data_list = column_to_row(data, attribute)
    if normalizationType == 'min_max':
        result = min_max(data_list)
    elif normalizationType == 'z_score':
        result = z_score(data_list)

    result = zip(*result)

    for i in range(0, len(result[0])):
        print '{0} \t {1}'.format(result[0][i], result[1][i])


def correlation ( attribute1 , fileName1 , attribute2, fileName2 ):
    '''
    Input Parameters:
        attribute1: The attribute you want to consider from file1
        attribute2: The attribute you want to consider from file2
        fileName1: The comma seperated file1
        fileName2: The comma seperated file2
        
    Output:
        Print the correlation coefficient 
    '''
    # Grab the list of data
    data_1 = DataSet(fileName1).readData
    data_2 = DataSet(fileName2).readData
    data_list_1 = column_to_row(data_1, attribute1)
    data_list_2 = column_to_row(data_2, attribute2)
    # Now check if the size of the two data_list is the same, if not then return None
    data_list_1_length = len(data_list_1)
    data_list_2_length = len(data_list_2)
    if data_list_1_length != data_list_2_length:
        print 'Data size for {0} and {1} are different'.format(fileName1, filename2)
        return None
    # Grab the mean
    mean_1 = numpy.mean(data_list_1)
    mean_2 = numpy.mean(data_list_2)
    # I found the steps to calculate the correlation coefficient in the following site:
    # https://www.mathsisfun.com/data/correlation.html
    x = []
    y = []
    for i in range(0, data_list_1_length):
        x.append(data_list_1[i] - mean_1)
    for i in range(0, data_list_1_length):
        y.append(data_list_2[i] - mean_2)

    product_xy = []
    for i in range(0, data_list_1_length):
        product_xy.append(x[i] * y[i])

    x_squared = []
    y_squared = []
    for i in range(0, data_list_1_length):
        x_squared.append(math.pow(x[i], 2))
        y_squared.append(math.pow(y[i], 2))
    product_xy_sum = 0
    x_squared_sum = 0
    y_squared_sum = 0
    for i in range(0, data_list_1_length):
        product_xy_sum += product_xy[i]
        x_squared_sum += x_squared[i]
        y_squared_sum += y_squared[i]
    result = product_xy_sum / math.sqrt(x_squared_sum * y_squared_sum)
    print result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Mining HW2')
    parser.add_argument('-f1', type=str,
                            help="Location of filename1. Use only f1 when working with only one file.",
                            required=True)
    parser.add_argument("-f2", type=str, 
                            help="Location of filename2. To be used only when there are two files to be compared.",
                            required=False)
    parser.add_argument("-n", type=str, 
                            help="Type of Normalization. Select either min_max or z_score",
                            choices=['min_max','z_score'],
                            required=False)
    parser.add_argument("-a1", type=str, 
                            help="Type of Attribute for filename1. Select either open or high or low or close or volume",
                            choices=['open','high','low','close','volume'],
                            required=False)
    parser.add_argument("-a2", type=str, 
                            help="Type of Attribute for filename2. Select either open or high or low or close or volume",
                            choices=['open','high','low','close','volume'],
                            required=False)
    args = parser.parse_args()
    if ( args.n and args.a1 ):
        normalization( args.f1 , args.n , args.a1 )
    elif ( args.f2 and args.a1 and args.a2):
        correlation ( args.a1 , args.f1 , args.a2 , args.f2 )
    else:
        print "Kindly provide input of the following form:\nDMPythonHW2.py -f1 <filename1> -a1 <attribute> -n <normalizationType> \nDMPythonHW2.py -f1 <filename1> -a1 <attribute> -f2 <filename2> -a2 <attribute>"
