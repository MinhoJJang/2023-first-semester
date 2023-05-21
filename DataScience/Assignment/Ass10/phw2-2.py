# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('decision_tree_data.csv')

# Encode categorical variables
df = pd.get_dummies(df)

# Define the features and target
X = df.drop('interview', axis=1)
y = df['interview']

# Define train/test splits
splits = [(0.1, 0.9), (0.2, 0.8), (0.3, 0.7)]

# Loop over splits
for test_size, train_size in splits:
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42, shuffle=True, stratify=y)

    # Create a decision tree model
    model = DecisionTreeClassifier(random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Calculate and print accuracy
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy ({train_size}/{test_size} split): {accuracy}")
