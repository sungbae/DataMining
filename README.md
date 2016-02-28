# DataMining

Introduces basic data mining concepts and techniques for discovering interesting patterns hidden in large-scale data sets, focusing on issues relating to effectiveness and efficiency. Topics covered include data preprocessing, data warehouse, association, classification, clustering, and mining specific data types such as time-series, social networks, multimedia, and Web data.

### Homework 1
Given the MAGIC Gamma Telescope Data Set (http://archive.ics.uci.edu/ml/datasets/MAGIC+Gamma+Telescope)


1. Write a python program that takes one command line argument i (i ∈ [1, 10]) and computes the following values for the i-th attribute of the dataset: N (number of objects), min, max, mean, standard deviation, Q1, median, Q3, IQR. Output all the values in a single line, separated by comma.

2. Generate a scatter plot using the 4th and 5th attributes. You can use any plotting tool, such as excel, matlab, gnuplot, R, python, etc.

### Homework 2
Stock quotes analysis. Go to http://www.nasdaq.com/quotes/, enter a symbol in step 1 (e.g., “HD”) and click “Historical Quotes” in step 2. On the next page, you can select different time frame (e.g., “3 Years”), view the data, and download the data as a .csv file using the link at the bottom of the page. Please note that if you download the .csv file when the stocks are still trading, the first line has a different format. You can either remove that first line or download the .csv files when the stock market is closed. 

1. Given a single filename, attribute type, and normalization method, compute the corresponding normalized attributed values. Using range [0, 1.0] for min-max normalization.  Output two values per line: the original attributed value and the normalized attribute value, separated by the < tab > key. 

   E.g., python DMPythonHW2.py -f1 FB.csv -a1 volume -n min_max

2. Given two filenames, their corresponding attribute types, compute the correlation coefficient between the two attributes types in the two files. Output a single value, which is the correlation coefficient. 

   E.g., python DMPythonHW2.py -f1 FB.csv -a1 high -f2 FB.csv -a2 low 
   
   E.g., python DMPythonHW2.py -f1 FB.csv -a1 open -f2 AAPL.csv -a2 open 
