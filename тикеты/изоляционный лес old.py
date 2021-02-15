import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv('/datasets/sales.csv')
data = df[['Sales', 'Profit']]

isolation_forest = IsolationForest(n_estimators=100)
estimator = isolation_forest.fit_predict(data)
outliers = [e for e in estimator if e == -1]

print("Количество аномалий: ", len(outliers))