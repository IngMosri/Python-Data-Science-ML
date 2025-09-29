
# 🛒 Exploratory Data Analysis: Supermarket Sales

This repository is part of my **Data Science / Machine Learning learning journey with Python**.  
It demonstrates how to set up a clean, reproducible project in GitHub, configure virtual environments, and perform an initial **Exploratory Data Analysis (EDA)** on the **Sample Superstore dataset** using `pandas`, `matplotlib`, and `seaborn`.

---

## 📂 Repository Structure

Python-Data-Science-ML/
│
├── data/              # local datasets (NOT pushed to GitHub, only .gitkeep placeholder)
├── notebook_py/       # analysis scripts in .py format
│   └── test_env.py    # environment test script
│   └── eda_supermarket.py   # main EDA script
├── figs/              # exported charts from EDA
├── requirements.txt   # project dependencies
└── README.md

---

## 📊 Dataset

- Source: [Kaggle — Sample Superstore](https://www.kaggle.com/datasets/roopacalistus/superstore)  
- Size: ~10,000 rows  
- Columns include:  
  - Categorical: `Ship Mode`, `Segment`, `Country`, `City`, `State`, `Region`, `Category`, `Sub-Category`  
  - Numerical: `Sales`, `Quantity`, `Discount`, `Profit`  

---

## ⚙️ Environment Setup

1. **Clone repository**
   ```bash
   git clone https://github.com/IngMosri/Python-Data-Science-ML.git
   cd Python-Data-Science-ML

	2.	Create and activate virtual environment

python -m venv .venv
source .venv/bin/activate    # macOS/Linux
.venv\Scripts\activate       # Windows


	3.	Install dependencies

pip install -r requirements.txt


	4.	Run environment test

python notebook_py/test_env.py

Output confirms Python path and versions of Pandas/Numpy.

⸻

🚀 How to Run the Analysis

From the project root:

python notebook_py/eda_supermarket.py

	•	Generates multiple plots (each in a separate figure).
	•	All plots are automatically exported to the figs/ folder.

⸻

📈 Example Outputs

Sales Distribution

Top 15 Cities by Sales

Discount vs Profit

Correlation Matrix


⸻

✅ Key Findings (Week 1)
	•	No missing values in the dataset; data types are clean.
	•	Technology is the leading category in sales.
	•	New York City and Los Angeles dominate sales volume.
	•	High discounts strongly reduce profit (negative correlation).

⸻

📌 Progress Log
	•	✔️ Repo cleaned and reset (removed heavy files, added .gitignore).
	•	✔️ Configured .venv for Python 3.12.
	•	✔️ Added base dependencies: numpy, pandas, matplotlib, seaborn.
	•	✔️ Created requirements.txt for reproducibility.
	•	✔️ Tested environment with test_env.py.
	•	✔️ Implemented eda_supermarket.py with Markdown-style sections and clear plots.
	•	✔️ Added figs/ folder for chart exports.
	•	✔️ Updated README with structure, setup instructions, outputs, and findings.

⸻

🎯 Next Steps
	•	Week 2: Advanced data manipulation with groupby, pivot_table, and merges.
	•	Improve visualizations (boxplots, pairplots, category breakdowns).
	•	Document insights in README + prepare for first ML task.
