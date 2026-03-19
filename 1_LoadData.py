import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Load dataset   # header(0 = 1st row, None = No col-header), index_col(0 = 1st col, False = No row-label)
dataset = pd.read_csv("https://raw.githubusercontent.com/bhevencious/CSC_215/refs/heads/main/housing.csv",
                      header=0, index_col=False)

# Textual: Preview dataset 1
# P1: "median_income" is not payroll-realistic, seems to need x $10,000
print(dataset.head(), "\n") #1st 5 rows
print(dataset.tail(), "\n") #last 5 rows

# Fix P1: Recalibrate "median_income" for realism (x $10,000)
dataset["median_income"] = dataset["median_income"] * 10000
print(dataset.head(), "\n") #1st 5 rows
print(dataset.tail()) #last 5 rows

# return dataset