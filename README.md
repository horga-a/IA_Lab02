# IA Lab 02 — NumPy, Pandas, Matplotlib & Seaborn

## Overview

This repository contains the implementation for **Artificial Intelligence Laboratory #02 (2025–2026)**.
The lab focuses on **Exploratory Data Analysis (EDA)** in Python using the core data science libraries:

* **NumPy** — numerical computation with multidimensional arrays
* **Pandas** — data manipulation and analysis with DataFrames
* **Matplotlib** — basic data visualization
* **Seaborn** — statistical data visualization

The goal of the lab is to understand how to load, explore, analyze, and visualize datasets using a complete EDA workflow.

---

# Objectives

The main objectives of this laboratory are:

* Learn how to use **NumPy arrays** and vectorized numerical operations.
* Work with **Pandas DataFrames** for data exploration and transformation.
* Create **basic visualizations** using Matplotlib.
* Create **statistical visualizations** using Seaborn.
* Perform **Exploratory Data Analysis (EDA)** on real datasets such as **Iris**, **Tips**, and **Titanic**.

---

# Technologies Used

* Python 3.10+
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook / Google Colab (for the notebook task)

---

# Project Structure

```
ia-lab02-numpy-pandas/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── cerinta_3_1_numpy.py
├── cerinta_3_2_pandas.py
├── cerinta_3_3_matplotlib.py
├── cerinta_3_4_seaborn.py
├── cerinta_3_5_heatmap.py
├── cerinta_3_6_titanic.py
│
└── tema/
    ├── tema_a_numpy.py
    ├── tema_b_tips.py
    ├── tema_c_dashboard.py
    ├── tema_d_bonus_iris.py
    └── tema_e_colab.ipynb
```

---

# Installation

## 1. Clone the repository

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```
numpy>=1.26.0
pandas>=2.1.0
matplotlib>=3.8.0
seaborn>=0.13.0
```

---

# Laboratory Tasks

## 3.1 NumPy Arrays

File: `cerinta_3_1_numpy.py`

Topics covered:

* Creating arrays
* Statistical operations
* Vectorized calculations
* Performance comparison between Python lists and NumPy arrays

---

## 3.2 Iris Dataset Exploration

File: `cerinta_3_2_pandas.py`

Operations performed:

* Load dataset using Seaborn
* Explore structure and statistics
* Filter and select data
* Group by species
* Add derived columns

---

## 3.3 Matplotlib Visualizations

File: `cerinta_3_3_matplotlib.py`

Creates a **2×2 subplot figure** including:

* Line plot (average sepal length)
* Scatter plot (petal length vs width)
* Bar chart (number of flowers per species)
* Histogram (sepal length distribution)

The resulting image is saved as:

```
grafice_iris_matplotlib.png
```

---

## 3.4 Seaborn Distributions

File: `cerinta_3_4_seaborn.py`

Visualizations include:

* Histogram with KDE
* Boxplot
* Violinplot
* Tip distribution by day (Tips dataset)

Output image:

```
distributii_seaborn.png
```

---

## 3.5 Correlation Heatmap

File: `cerinta_3_5_heatmap.py`

Steps performed:

* Compute **Pearson correlation matrix**
* Visualize correlations using **Seaborn heatmap**
* Automatically detect strong correlations

Output image:

```
heatmap_corelatie_iris.png
```

---

## 3.6 Titanic Dataset Analysis

File: `cerinta_3_6_titanic.py`

Analysis performed:

* Survival rate by **sex**
* Survival rate by **passenger class**
* Pivot table with survival statistics
* Visualization using **bar plots**

Output image:

```
titanic_analiza.png
```

---

# Homework Tasks

Inside the `tema/` directory.

### A — NumPy Matrix Operations

* Generate matrices
* Perform matrix multiplication
* Compute statistics
* Bonus: matrix inverse and determinant

---

### B — Tips Dataset Analysis

Using Pandas:

* Dataset statistics
* Tip average per day and sex
* Tip percentage calculation
* Top 5 most generous tables
* Grouped statistics by day and smoker

---

### C — Visualization Dashboard

Creates a **2×2 dashboard** with:

* Scatter plot
* Boxplot
* Histogram with KDE
* Barplot with confidence intervals

All based on the **Tips dataset**.

---

### D — Bonus: Iris Visualization

* Full **pairplot**
* Multiple **violin plots**
* Saved figures as PNG

---

### E — Google Colab Notebook

Notebook version of the **Titanic analysis** including:

* Markdown explanations
* Data exploration
* Visualizations
* Final conclusions

File:

```
tema_e_colab.ipynb
```

---

# Datasets Used

Datasets are loaded using **Seaborn**:

* Iris dataset
* Tips dataset
* Titanic dataset

They are automatically downloaded and cached locally by Seaborn.

---

# Key Concepts Learned

* Vectorized computation with NumPy
* DataFrame manipulation with Pandas
* Exploratory Data Analysis (EDA)
* Data visualization principles
* Statistical graphics with Seaborn

---

# References

* NumPy Documentation — https://numpy.org/doc/
* Pandas Documentation — https://pandas.pydata.org/docs/
* Matplotlib Documentation — https://matplotlib.org/
* Seaborn Documentation — https://seaborn.pydata.org/
* Python Data Science Handbook — Jake VanderPlas

---

# Notes

* The `.venv/` directory is **excluded from GitHub** using `.gitignore`.
* Generated images are saved locally when running the scripts.
* Scripts can be executed individually depending on the task.

---

