# -*- coding: utf-8 -*-
"""decease_keras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ukp5FVPA00hhiBILNW0csmxWV2MlFM7N
"""

from google.colab import files

uploaded = files.upload()

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
# %matplotlib inline
warnings.filterwarnings('ignore')

df = pd.read_csv('data.csv')
df.head()

df = df.drop(columns=['id', 'Unnamed: 32'], axis=1)

df.describe()

df.info()

df.shape

df.isna().sum()

df2=df.drop(['diagnosis'],axis=1,inplace=False)

df.info()

from sklearn.model_selection import train_test_split
X = df.drop(columns=['diagnosis'])
df['diagnosis'] = np.where(df['diagnosis']=='M', 1, 0)
Y = df['diagnosis']
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30)

from sklearn.preprocessing import Normalizer
norm = Normalizer()
norm.fit(x_train)
X_train_norm = norm.transform(x_train)
X_test_norm = norm.transform(x_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X_train_norm, y_train)

print("Accuracy: ",model.score(X_test_norm, y_test) * 100)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,f1_score
model = DecisionTreeClassifier()

model.fit(X_train_norm, y_train)

print("Accuracy: ",model.score(X_test_norm, y_test) * 100)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,f1_score
model = RandomForestClassifier()
model.fit(X_train_norm, y_train)
y_pred = model.predict(X_test_norm)
print(classification_report(y_test, y_pred))

from keras.models import Sequential
from keras.layers import Dense
from keras.utils.vis_utils import plot_model

Model = Sequential()

Model.add(Dense(units= 16, activation = 'relu', input_dim=30))
Model.add(Dense(units=8, activation='relu'))
Model.add(Dense(units=6, activation='relu'))
Model.add(Dense(units=1, activation='sigmoid'))

Model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

Model.summary()

plot_model(Model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

history=Model.fit(X_train_norm, y_train,validation_split=0.2, batch_size=1, epochs=50)

prediction = Model.predict(X_test_norm[1:])

prediction