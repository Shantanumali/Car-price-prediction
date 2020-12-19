import pandas as pd
import numpy as np

df=pd.read_csv('car data.csv')
print(df.head())
final_dataset=df[['Year','Selling_Price','Present_Price','Kms_Driven','Fuel_Type','Seller_Type','Transmission','Owner']]
print(final_dataset.head())
final_dataset['Current Year']=2020
final_dataset['no_year']=final_dataset['Current Year']- final_dataset['Year']
final_dataset.drop(['Year'],axis=1,inplace=True)
final_dataset=pd.get_dummies(final_dataset,drop_first=True)
final_dataset=final_dataset.drop(['Current Year'],axis=1)
X=final_dataset.iloc[:,1:]
y=final_dataset.iloc[:,0]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)
print(X_train.columns)
from sklearn import metrics

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(X_train,y_train)
pred = reg.predict(X_test)
print('MAE:', metrics.mean_absolute_error(y_test, pred))
print('MSE:', metrics.mean_squared_error(y_test, pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, pred)))

print(reg.predict([[0,1,45280,0,3.46,0,1,6]]))
import pickle
file = open('regression_model.pkl', 'wb')
pickle.dump(reg, file)
