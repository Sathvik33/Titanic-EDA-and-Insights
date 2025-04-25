import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

BASE_DIR=os.path.dirname(__file__)
DATA_PATH=os.path.join(BASE_DIR,"data","Titanic Dataset.csv")
data=pd.read_csv(DATA_PATH)
print(data)


"""Create a summary DataFrame"""
summary=pd.DataFrame({
    "Mean: ": data.mean(numeric_only=True),
    "Median: ": data.median(numeric_only=True),
    "Standard Deviation: ": data.std(numeric_only=True),
    "Minimun: ": data.min(numeric_only=True),
    "Maximum: ": data.max(numeric_only=True),
    "Variance: ": data.var(numeric_only=True)
})
print(summary)


numerical_values=data.select_dtypes(include="number").columns
sns.set(style="whitegrid")
for i in numerical_values:
    plt.figure(figsize=(10,5))
    sns.histplot(data[i], kde=True, bins=30,color="blue")
    plt.title(f"Distribution of {i}")
    plt.xlabel(i)
    plt.ylabel("Frequency")
    plt.show()

for i in numerical_values:
    plt.figure(figsize=(10,5))
    sns.boxplot(x=data[i],color="green")
    plt.title(f"Boxplot of {i}")
    plt.xlabel(i)
    plt.show()

data[numerical_values]=data[numerical_values].fillna(data[numerical_values].mean())
print(data.isnull().sum())
print(data.info())

categorical_values=data.select_dtypes(include="object").columns
print(categorical_values)
for i in categorical_values:
    data[i] = data[i].fillna(data[i].mode()[0])

print(data.isnull().sum())

"""Corelation Matrix"""
plt.figure(figsize=(10, 8))
corr_matrix = data[numerical_values].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()


"""Pairplot"""
plt.figure(figsize=(10, 8))
sns.pairplot(data[numerical_values])
plt.title("Pairplot of Numeric Features", y=1.02)
plt.show()