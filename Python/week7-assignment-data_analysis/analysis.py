import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris(as_frame=True)
df = iris.frame
df['species'] = df['target'].map(lambda t: iris.target_names[t])

# Explore
print("First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())

# Analysis
print("\nSummary stats:")
print(df.describe())
print("\nAverage sepal length per species:")
print(df.groupby('species')['sepal length (cm)'].mean())

# Visualizations
# 1. Line chart
plt.plot(df.index, df['sepal length (cm)'])
plt.title("Sepal Length Trend Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

# 2. Bar chart
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar')
plt.title("Average Petal Length per Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram
plt.hist(df['sepal length (cm)'], bins=10)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Count")
plt.show()

# 4. Scatter plot
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], c=df['target'])
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()
