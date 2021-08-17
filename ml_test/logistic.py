from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = LogisticRegression()
clf = model.fit(X, y)
print(clf.predict(X))
print(clf.score(X, y))
