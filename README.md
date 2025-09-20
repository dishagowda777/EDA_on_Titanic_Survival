# EDA on Titanic Survival Dataset

This project performs **Exploratory Data Analysis (EDA)** on the Titanic dataset to uncover patterns and insights about passenger survival. The dataset contains demographic and socio-economic details such as age, gender, passenger class, and fare.

---

## 📌 Objectives
- Clean and preprocess the Titanic dataset  
- Handle missing values and outliers  
- Perform descriptive statistics and feature analysis  
- Visualize key patterns using plots and graphs  
- Derive insights on which factors influenced passenger survival  

---

## 📊 Tools & Libraries
- Python  
- Pandas  
- NumPy  
- Matplotlib & Seaborn  
- Jupyter Notebook  

---

## 📈 Key Insights
- Female passengers had higher survival rates compared to males  
- First-class passengers had better survival chances than third-class  
- Younger passengers survived more often than older ones  
- High ticket fares correlated with higher survival probability  

---

## 📷 Sample Visualizations

### Age Distribution
![Age Distribution](EDA_on_Titanic_Survival_main/Output_graphs/Age-Distribution.png)

### Age vs Survival
![Age vs Survival](EDA_on_Titanic_Survival_main/Output_graphs/Age-vs-Survival.png)

### Correlation Heatmap
![Correlation Heatmap](EDA_on_Titanic_Survival_main/Output_graphs/Correlation-heatmap.png)

### Survival Count
![Survival Count](EDA_on_Titanic_Survival_main/Output_graphs/Survial-count.png)

### Survival by Passenger Class
![Survival by Passenger Class](EDA_on_Titanic_Survival_main/Output_graphs/Survival-by-passenger-class.png)

### Survival by Sex
![Survival by Sex](EDA_on_Titanic_Survival_main/Output_graphs/Survival-by-sex.png)

### Pairplot
![Pairplot](EDA_on_Titanic_Survival_main/Output_graphs/pairplot.png)

---

## 🚀 How to Run
1. Clone the repository:
```bash
git clone https://github.com/Chethana-git/EDA_on_Titanic_Survival.git
cd EDA_on_Titanic_Survival
pip install -r requirements.txt



EDA_on_Titanic_Survival/
│
├─ EDA_on_Titanic_Survival_main/
│   ├─ Output_graphs/           # All screenshots
│   ├─ Titanic-EDA.py           # Main EDA script
│   ├─ README.md                # Internal folder README (optional)
│   └─ train.csv                # Dataset
├─ README.md                    # Main README
├─ requirements.txt             # Python dependencies
└─ .gitignore                   # Ignore files like __pycache__, etc.
