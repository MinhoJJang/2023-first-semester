from sklearn import tree, metrics, ensemble
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np

# Load the iris dataset
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target

# Split the iris dataset into 10 different subsets and 1 test set
sss = StratifiedShuffleSplit(n_splits=10, test_size=30, random_state=0)

# Creating DecisionTreeClassifier
dtc = tree.DecisionTreeClassifier()

# Creating BaggingClassifier
bagging = ensemble.BaggingClassifier(dtc, n_estimators=10)

# Loop through all iris bagging datasets to train the bagging classifier
for train_index, _ in sss.split(X, y):
    X_train, y_train = X[train_index], y[train_index]
    bagging.fit(X_train, y_train)

# Split data for final testing
sss_test = StratifiedShuffleSplit(n_splits=1, test_size=30, random_state=42)
train_index, test_index = next(sss_test.split(X, y))
X_test, y_test = X[test_index], y[test_index]

# Now we use the test dataset for prediction
y_pred = bagging.predict(X_test)

# Creating a confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)

# Creating a classification report
class_report = classification_report(y_test, y_pred)
print("Classification Report:\n", class_report)

# Calculating accuracy
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)
