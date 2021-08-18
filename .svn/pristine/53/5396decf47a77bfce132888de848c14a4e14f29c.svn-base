from sklearn.datasets import load_boston

from evaluate import evaluate

X, y = load_boston(return_X_y = True)
names, scores  = evaluate(X, y, ridge_selected = True, lsqr_selected = True, kernel='linear')

for name, score in names, scores:
  print(name, " : ", score) 
