# %% [markdown]
# # EDA — Sample Superstore (gráficas individuales)
# - Cada gráfico en su propia figura
# - Títulos y ejes claros
# - Archivos .png guardados en figs/

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# tema visual
sns.set_theme(context="notebook", style="whitegrid")
pd.options.display.float_format = "{:,.2f}".format

# helper para guardar y mostrar sin repetir código
FIGS_DIR = Path("figs")
FIGS_DIR.mkdir(exist_ok=True)

def save_and_show(filename: str):
    plt.tight_layout()
    plt.savefig(FIGS_DIR / f"{filename}.png", dpi=150, bbox_inches="tight")
    plt.show()

# cargar datos
df = pd.read_csv("data/SampleSuperStore.csv")
print(df.shape)
print(df.info())
print(df.isnull().sum())

# %% [markdown]
# ## 1) Distribución de *Sales*

# %%
plt.figure(figsize=(9,5))
sns.histplot(df["Sales"], bins=40, kde=True)
plt.title("Distribución de Sales")
plt.xlabel("Sales")
plt.ylabel("Frecuencia")
save_and_show("sales_distribution")

# %% [markdown]
# ## 2) Top 20 ciudades por **cantidad de pedidos**
# (usamos barras horizontales para que las etiquetas no se amontonen)

# %%
top_city_counts = (
    df["City"].value_counts()
      .head(20)
      .rename_axis("City")
      .reset_index(name="Count")
)

plt.figure(figsize=(9,7))
sns.barplot(data=top_city_counts, x="Count", y="City")
plt.title("Top 20 ciudades por cantidad de pedidos")
plt.xlabel("Número de pedidos")
plt.ylabel("Ciudad")
save_and_show("top20_cities_count")

# %% [markdown]
# ## 3) Top 15 ciudades por **ventas totales (Sales)**

# %%
top_city_sales = (
    df.groupby("City")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(15)
      .reset_index()
)

plt.figure(figsize=(9,6))
sns.barplot(data=top_city_sales, x="Sales", y="City")
plt.title("Top 15 ciudades por ventas totales")
plt.xlabel("Ventas (Sales)")
plt.ylabel("Ciudad")
save_and_show("top15_cities_sales")

# %% [markdown]
# ## 4) Ventas totales por *Category*

# %%
cat_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

plt.figure(figsize=(7,5))
sns.barplot(data=cat_sales, x="Category", y="Sales")
plt.title("Ventas totales por Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=15)
save_and_show("category_sales")

# %% [markdown]
# ## 5) Top 15 Sub-Category por **Profit acumulado**

# %%
sub_profit = (
    df.groupby("Sub-Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(15)
      .reset_index()
)

plt.figure(figsize=(9,6))
sns.barplot(data=sub_profit, x="Profit", y="Sub-Category")
plt.title("Top 15 Sub-Category por Profit")
plt.xlabel("Profit")
plt.ylabel("Sub-Category")
save_and_show("top15_subcategory_profit")

# %% [markdown]
# ## 6) Relación **Discount vs Profit**

# %%
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="Discount", y="Profit", alpha=0.5, s=18)
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
save_and_show("discount_vs_profit")

# %% [markdown]
# ## 7) Matriz de correlación (numéricas)
# *Nota:* excluimos Postal Code porque no es una métrica.

# %%
num = df.select_dtypes("number").drop(columns=["Postal Code"], errors="ignore")
plt.figure(figsize=(6,5))
sns.heatmap(num.corr(numeric_only=True), annot=True, fmt=".2f", square=True, cbar=True)
plt.title("Matriz de correlación")
save_and_show("correlation_matrix") 