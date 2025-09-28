# %% [markdown]
# # Exploratory Data Analysis: Supermarket Sales

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv("data/SampleSuperStore.csv")
print(df.shape)
print(df.info())

# %%
# Nulos
print(df.isnull().sum())

# %%
# Ejemplo de análisis: ventas por ciudad
sns.countplot(x="City", data=df)
plt.show()

# %%
# Ejemplo: distribución de ingresos totales
sns.histplot(df["Total"], bins=30, kde=True)
plt.show()