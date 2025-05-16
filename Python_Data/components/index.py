# modules we'll use Data Cleaning
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Assigning of files into the DataFrame

df1 = pd.read_csv(r'C:\Users\talk2\Downloads\Python_Data\StudentData.csv')
df2 = pd.read_csv(r'C:\Users\talk2\Downloads\Python_Data\StudentTestingData.csv')


# set seed for reproducibility
np.random.seed(0) 

# Initial Data Exploration for Improved Visualization

# print(df1.head())
# print(df1.info())
# print(df1.describe())
# print(df1.isnull().sum())

# print(df2.head())
# print(df2.info())
# print(df2.describe())
# print(df2.isnull().sum())

# Convert 'Student Number' to numeric, coercing errors to NaN
df1['Student Number'] = pd.to_numeric(df1['Student Number'], errors='coerce')

# Convert relevant numeric columns in df2 to numeric, coercing errors
df2['Math Score'] = pd.to_numeric(df2['Math Score'], errors='coerce')
df2['Reading Score'] = pd.to_numeric(df2['Reading Score'], errors='coerce')
df2['Math Tutor Hours'] = pd.to_numeric(df2['Math Tutor Hours'], errors='coerce')
df2['Reading Tutor Hours'] = pd.to_numeric(df2['Reading Tutor Hours'], errors='coerce')

df1.columns = df1.columns.str.strip()  # Removes leading/trailing spaces
df2.columns = df2.columns.str.strip()  # Removes leading/trailing spaces

# Drop missing values: rows

df1_new = df1.dropna()
df2_new = df2.dropna()

# Fill in missing values automatically (There is backward_fill with 'bfill')

df1_fillna = df1.ffill().fillna(0)
df2_fillna = df2.ffill().fillna(0)

# print(df2_fillna)
# print(df1_fillna)

# Removal of duplicate values

df1_fillna_clean = df1_fillna.drop_duplicates(subset=['Student Number', 'Name', 'Extracurricular Activities'])

df2_fillna_clean = df2_fillna.drop_duplicates(subset=['District', 'City', 'Reading Tutor', 'Reading Tutor Hours'])

# print(df2_fillna_clean)

# Round all numeric columns in the dataframe
df1_fillna_clean_rounded = df1_fillna_clean.round(2)
df2_fillna_clean_rounded = df2_fillna_clean.round(2)


# Rename in df1 to match df2
df1_fillna_clean_rounded.rename(columns={'Student Number': 'StudentID'}, inplace=True)

# Merging the two Dataframe together with their Future Key
merged_df = pd.merge(df1_fillna_clean_rounded, df2_fillna_clean_rounded, on='StudentID', how='inner')

merged_df.to_csv("C:/Users/talk2/Downloads/Python_Data/merged_data.csv", index=False)



# print(df2_fillna_clean['StudentID'].nunique())

# DATA VISUALIZATION
print(merged_df.head())  # Check the first few rows
print(merged_df.describe())  # Get summary statistics
(merged_df.info())  # Get info about column types and non-null values
