import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('data/SampleSuperstore.csv')

# Basic checks
df.info()

print(df["Category"].value_counts())
print(df["Sub-Category"].value_counts())

print(df.groupby("Segment")["Sales"].sum())
print(df.groupby("State")["Profit"].mean().sort_values(ascending=False).head(5))
print(df.groupby("State")["Profit"].mean().sort_values().head(5))


sns.scatterplot(x="Discount", y="Profit", data=df, alpha=0.5)
plt.show()




