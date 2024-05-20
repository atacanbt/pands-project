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
        variable_summary.append(summary.to_string()) # converting the summary to string
        variable_summary.append("\n")

# TASK 2: Creating histograms for each variable
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column], kde=True) # creating a histogram with a kernel density estimate
        plt.title(f"Distribution of {column}") 
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.savefig(f"{column}_histogram.png") # saving the histogram as png files 
        plt.close() # closing the plot to avoid overlapping


# opening a file to write the summary of each variable
with open('summary.txt', 'w') as f:
    for line in variable_summary:
        f.write(line + '\n')

print("Summary of each variable is written to 'summary.txt' file. \nHistograms are saved as png files.")

# TASK 3: Scatter plot of each pair of variables
numeric_columns = data.select_dtypes(include=[np.number]).columns # selecting the numeric columns
sns.pairplot(data, vars=numeric_columns, hue='species') # creating a scatter plot for each pair of variables
plt.show()

print("Scatter plot of each pair of variables is displayed.")
