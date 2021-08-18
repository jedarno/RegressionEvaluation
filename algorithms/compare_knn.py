from views.boxplot import boxplot
from test_framework.evaluate import evaluate
from svm import Svm

from sklearn.datasets import load_diabetes

#File used to test evaluation of knn

X, y = load_diabetes(return_X_y = True)
names, scores = evaluate(X, y, ridge_selected = True, lsqr_selected = True, svm_selected=True, knn_selected = True, kernel='linear')

boxplot(names, scores)
