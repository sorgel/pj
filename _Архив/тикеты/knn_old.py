import pandas as pd
from pyod.models.knn import KNN
from sklearn.ensemble import IsolationForest

df = pd.read_csv('/datasets/sales.csv')
data = df[['Sales', 'Profit']]

model = KNN()
estimation_knn = model.fit_predict(data) == 1
outliers_knn = estimation_knn.sum()
print("Количество аномалий (KNN): ", outliers_knn)

model = IsolationForest(n_estimators=100)
estimation_iforest = model.fit_predict(data) == -1
outliers_iforest = estimation_iforest.sum()
print("Количество аномалий (изоляционный лес): ", outliers_iforest)

print("Совпало: ", (estimation_knn & estimation_iforest).sum())