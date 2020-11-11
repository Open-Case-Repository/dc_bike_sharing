from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd

def run_model(data):
    X = data.drop(labels=['cnt'],axis=1)
    y = data['cnt']
    
    # Split into training data and test set
    split_idx = pd.to_datetime('July 1, 2012')
    X_train = X.loc[:split_idx]
    X_test = X.loc[split_idx:]
    y_train = y.loc[:split_idx]
    y_test = y.loc[split_idx:]
    
    lin_model = LinearRegression()
    lin_model.fit(X_train,y_train)
    y_pred = lin_model.predict(X_test)
    mse_score = metrics.mean_squared_error(y_test, y_pred)
    return mse_score

