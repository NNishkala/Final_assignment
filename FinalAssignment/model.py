#importing libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import missingno as mnso
print("Successfully imported libraries")

#importing dataset
col_name=['Date', 'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 'Temp3pm', 'RainToday', 'RISK_MM', 'RainTomorrow']
we_pd=pd.read_csv("C:/Users/Admin/machine_learning/summer_io/csv_files/ka.csv",header=None,names=col_name)

x=we_pd.iloc[:, [2,3,4,5,6,8,11,12,13,14,15,16,17,18,19,20,21,22]].values
y=we_pd.iloc[:, 23].values
x1=np.delete(x,0,axis=0)
x2=np.delete(x1,0,axis=0)
x=x2
y1=np.delete(y,0)
y2=np.delete(y1,0)
y=y2

#logistic regression
print("Starting logistic regression:")
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)

accuracy=(cm[0][0]+cm[1][1])/(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1])
err=(cm[0][1]+cm[1][0])/(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1])

#results:
print("Results:")
print("accuracy is ",accuracy)
print("error is ",err)