# 🚢 Titanic Survival Analysis — Exploratory Data Analysis (EDA)
<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib"/>
  <img src="https://img.shields.io/badge/Seaborn-41B4BD?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn"/>
</p>


🚢 EDA on Titanic Survival

This project performs Exploratory Data Analysis (EDA) on the Titanic dataset to uncover key patterns that influenced passenger survival.

The analysis includes:
Cleaning missing data (Age, Embarked, dropping Cabin).
Encoding categorical features (Sex, Embarked).
Creating clear, aesthetic visualizations with Seaborn & Matplotlib.
An interactive graph navigation system (Next / Previous buttons) so all plots can be explored in one window.

📊 Visualizations

The following insights are displayed:
Overall Survival Count – Survivors vs. Non-survivors.
Survival by Sex – Comparing male vs. female survival rates.
Survival by Passenger Class – Class differences in survival chances.
Age Distribution by Survival – Younger passengers had better odds.
Fare Distribution by Survival – Higher fare correlated with survival.
Correlation Heatmap – Relationships between numeric features.

⚙️ Tools Used

Python

Pandas, NumPy – data wrangling
Matplotlib, Seaborn – visualizations
Matplotlib Widgets – interactive Next/Previous navigation

🚀 Running the Project
# Install dependencies
pip install pandas numpy matplotlib seaborn

# Run the script
python Titanic-EDA.py


👉 The program opens a single interactive window. Use the Next ▶ / ◀ Previous buttons to cycle through the graphs.

📈 Key Findings

Females had much higher survival rates than males.
1st Class passengers were most likely to survive.
Younger passengers (children) had higher chances.
Higher ticket fare correlated positively with survival.