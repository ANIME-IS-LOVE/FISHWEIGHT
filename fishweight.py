# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11yl2DnyhWR3_0TMCKdThqqIaAO81v8rf
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns


url = 'https://github.com/ybifoundation/Dataset/raw/main/Fish.csv'
df = pd.read_csv(url)


print(df.head())


print(df.describe())


print(df.isnull().sum())

df = pd.get_dummies(df, columns=['Species'], drop_first=True)

X = df.drop('Weight', axis=1)
y = df['Weight']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')


plt.scatter(y_test, y_pred)
plt.xlabel('Actual Weights')
plt.ylabel('Predicted Weights')
plt.title('Actual vs Predicted Weights')
plt.show()