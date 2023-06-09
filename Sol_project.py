import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

"""**Data Importing and Processing**

In this section, I imported the data and isolated my target variable which is Solubility. The data is then split into 80% training data and 20% test data. 
"""

df = pd.read_csv('/content/solubility-dataset.csv')
df.head()

x = df.drop('Solubility', axis=1)
x

y = df.Solubility
y

x_train, x_test, y_train, y_test= train_test_split(x,y, test_size=0.2, random_state=90)

x_train

y_train

x_test

y_test

"""**Linear Regression Model**

In this section, LinearRegression from sklearn is being used to build the model based on the training data. Performance metrics, MSE and R2, are being used to determine the performance of the model. 
"""

reg = LinearRegression()
reg.fit(x_train, y_train)

y_pred_train = reg.predict(x_train)
y_pred_test = reg.predict(x_test)

reg_train_mse = mean_squared_error(y_train, y_pred_train)
reg_train_r2 = r2_score(y_train, y_pred_train)

reg_test_mse= mean_squared_error(y_test, y_pred_test)
reg_test_r2= r2_score(y_test, y_pred_test)

print(reg_train_mse)
print(reg_train_r2)
print(reg_test_mse)
print(reg_test_r2)

"""**Visualisation**"""

plt.figure(figsize=(6,6))
plt.scatter(x=y_train, y=y_pred_train, c='hotpink', alpha=0.1)
o = np.polyfit(y_train, y_pred_train, 1)
p = np.poly1d(o)
plt.plot(y_train,p(y_train),'red')
plt.ylabel('Predicted Solubility')
plt.xlabel('Experimental Solubility')
