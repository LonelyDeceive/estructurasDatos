import random
from sklearn.tree import DecisionTreeClassifier
def entrenar_modelo():
    X, y = [], []
    for _ in range(300):
        a, m, b = random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)
        X.append([a, m, b])
        if a >= m and a >= b:
            y.append(1)
        elif m >= a and m >= b:
            y.append(2)
        else:
            y.append(3)
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    return clf
