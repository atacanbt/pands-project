# analysis.py
# 
# author: Atacan Buyuktalas

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the dataset
data = pd.read_csv("pands-project/iris.data")

# TASK 1: Summary of each variable in the dataset

# created a list to store the summary of each variable
variable_summary = []

# Calculating the summary of each variable
for column in data.columns[:-1]: # the last column is not numeric so it is excluded
    if pd.api.types.is_numeric_dtype(data[column]): # checking if the column is numeric
        summary = data[column].describe()
        # Appending the summary of each variable to the list
        variable_summary.append(f"Summary for {column}:")
        variable_summary.append(summary.to_string())
        variable_summary.append("\n")

# Writing the summary of each variable to a text file
with open('summary.txt', 'w') as f:
    for line in variable_summary:
        f.write(line + '\n')

# TASK 2: Histograms