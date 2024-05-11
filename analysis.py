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
data.head()
print(data.head())

FILENAME = "summary_of_each_variable.txt"
# Writing the summary of each variable to a text file
with open(FILENAME, 'w') as f:
    f.write("Summary of each variable\n")
    f.write("\n")
    f.write(str(data.describe()))
   