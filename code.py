#Importing the necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#Reading the dataset
df = pd.read_csv('/content/Salary Data (1).csv')
print(df.shape)
df.head()


#An overview of the dataset
df.info()


#Statistical information of numeric features of the dataset
print(df.describe())


#Count of unique values for each categorical columns
for col in ('Gender', 'Education Level', 'Job Title'):
    print(f'for column {col}, there is {df[col].nunique()} unique values.')


#Scatter plot for Salary and Age features
plt.scatter(df['Age'], df['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Scatter plot for Salary and Age')
plt.show()


#Scatter plot for Salary and Years of Experience
plt.scatter(df['Years of Experience'], df['Salary'])
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Scatter plot for Salary and Years of Experience')
plt.show()


# 📊 Histogram
plt.figure(figsize=(10, 5))
hist_plot = sns.histplot(df['Salary'], bins=20, color='red')
# Add value labels on top of bars
for bar in hist_plot.patches:
    height = bar.get_height()
    if height > 0:
        hist_plot.text(bar.get_x() + bar.get_width()/2, height + 1, int(height), ha='center', fontsize=9)

plt.title("Distribution of Salaries")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()


# Pie chart
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'pink'])
plt.title("Gender Distribution")
plt.axis('equal')  # Equal aspect ratio ensures pie is a circle
plt.show()


#📦 Boxplot
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Salary'], color='skyblue')
plt.title("Boxplot of Salaries")
plt.xlabel("Salary")
plt.show()


#Explore correlation between age,Years of Experience, Salary.
cor = df[['Age', 'Years of Experience', 'Salary']].corr()
plt.figure(figsize=(5, 6))
sns.heatmap(cor, annot=True, fmt=".2f", linewidths=0.5, cmap="coolwarm")
plt.title("Correlation between Age, Experience, and Salary")
plt.show()


# Barplot
top_jobs = df.groupby("Job Title")["Salary"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(13, 6))
sns.barplot(x=top_jobs.index, y=top_jobs.values, color="green")
plt.title("Top 10 Job Titles by Average Salary")
plt.xlabel("Job Title")
plt.ylabel("Average Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Line Plot
top_10_jobs = df.groupby('Job Title')['Salary'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.lineplot(x=top_10_jobs.index, y=top_10_jobs.values, marker='o', linewidth=2)
plt.xticks(rotation=45)
plt.title("Top 10 Job Titles by Average Salary")
plt.xlabel("Job Title")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.show()


# Plotting the line chart
top_10_jobs = df.groupby('Job Title')['Salary'].mean().sort_values(ascending=False).head(10).reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=top_10_jobs, x='Job Title', y='Salary', marker='o', linewidth=2)
plt.title("Top 10 Job Titles by Average Salary")
plt.xlabel("Job Title")
plt.ylabel("Average Salary")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# Z-score based outlier detection on Salary
arr = np.array(df['Salary'])
mean_salary = arr.mean()
std_salary = arr.std(ddof=1)
z_score_salary = (arr - mean_salary) / std_salary
# Find extreme outliers where |Z| > 3
outliers = arr[np.abs(z_score_salary) > 3]
print("Outlier Salaries (Z-score > 3):")
print(outliers)
