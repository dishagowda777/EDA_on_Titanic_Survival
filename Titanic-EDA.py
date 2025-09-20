import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# ------------------------------
# Load & Preprocess Data
# ------------------------------
df = pd.read_csv("train.csv")

# Handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)

# Encode categorical variables (for correlation heatmap)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# ------------------------------
# Define Plots (as functions)
# ------------------------------
plots = [
    lambda ax: sns.countplot(data=df, x='Survived', palette="Set2", ax=ax),
    lambda ax: sns.countplot(data=df, x='Sex', hue='Survived', palette="Set1", ax=ax),
    lambda ax: sns.countplot(data=df, x='Pclass', hue='Survived', palette="muted", ax=ax),
    lambda ax: sns.boxplot(data=df, x='Survived', y='Age', palette="Set3", ax=ax),
    lambda ax: sns.histplot(data=df, x='Fare', hue='Survived', bins=40, kde=True, ax=ax),
    lambda ax: sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
]

titles = [
    "Overall Survival Count",
    "Survival by Sex",
    "Survival by Passenger Class",
    "Age vs Survival (Boxplot)",
    "Fare Distribution by Survival",
    "Correlation Heatmap"
]

# ------------------------------
# Interactive Navigation
# ------------------------------
current = {'index': 0}
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.2)

def update_plot():
    ax.clear()
    plots[current['index']](ax)
    ax.set_title(titles[current['index']], fontsize=14)
    fig.canvas.draw_idle()

def next_plot(event):
    current['index'] = (current['index'] + 1) % len(plots)
    update_plot()

def prev_plot(event):
    current['index'] = (current['index'] - 1) % len(plots)
    update_plot()

# Buttons
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bprev = Button(axprev, 'Previous')
bnext.on_clicked(next_plot)
bprev.on_clicked(prev_plot)

# Show first plot
update_plot()
plt.show()
