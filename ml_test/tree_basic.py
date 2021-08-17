from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier  # 经典的决策树分类算法

X, y = load_iris(return_X_y=True)
clf = DecisionTreeClassifier().fit(X, y)
print(clf.predict(X))
print(clf.score(X, y))
