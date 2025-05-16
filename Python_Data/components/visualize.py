# modules we'll use Data Cleaning
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the saved merged data

df = pd.read_csv(r"C:/Users/talk2/Downloads/Python_Data/merged_data.csv", index_col=None)




# Calculate average and median for Math and Reading scores
avg_math_score = df['Math Score'].mean()
avg_reading_score = df['Reading Score'].mean()

median_math_score = df['Math Score'].median()
median_reading_score = df['Reading Score'].median()

print(f"Average Math Score: {avg_math_score}")
print(f"Average Reading Score: {avg_reading_score}")
print(f"Median Math Score: {median_math_score}")
print(f"Median Reading Score: {median_reading_score}")


# Correlation between tutor hours and scores
corr_math = df['Math Tutor Hours'].corr(df['Math Score'])
corr_reading = df['Reading Tutor Hours'].corr(df['Reading Score'])

print(f"Correlation between Math Tutor Hours and Math Score: {corr_math}")
print(f"Correlation between Reading Tutor Hours and Reading Score: {corr_reading}")

# DISTRIBUTION ANALYSIS


# Math Score Distribution
sns.histplot(df['Math Score'], kde=True, color='blue', bins=10)
plt.title('Math Score Distribution')
plt.xlabel('Math Score')
plt.ylabel('Frequency')
plt.show()

# Reading Score Distribution
sns.histplot(df['Reading Score'], kde=True, color='green', bins=10)
plt.title('Reading Score Distribution')
plt.xlabel('Reading Score')
plt.ylabel('Frequency')
plt.show()
