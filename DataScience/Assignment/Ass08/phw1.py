import numpy as np
import pandas as pd


# Function to calculate entropy
def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy = -np.sum(
        [(counts[i] / np.sum(counts)) * np.log2(counts[i] / np.sum(counts)) for i in range(len(elements))])
    return entropy


# Function to calculate information gain
def info_gain(data, split_attribute, target_name="Outcome"):
    total_entropy = entropy(data[target_name])

    vals, counts = np.unique(data[split_attribute], return_counts=True)
    weighted_entropy = np.sum(
        [(counts[i] / np.sum(counts)) * entropy(data.where(data[split_attribute] == vals[i]).dropna()[target_name]) for
         i in range(len(vals))])

    information_gain = total_entropy - weighted_entropy
    return information_gain


# Function to build the decision tree
def build_tree(data, original_data, features, target_name="Outcome", parent_node_class=None):
    if len(np.unique(data[target_name])) <= 1:
        return np.unique(data[target_name])[0]
    elif len(data) == 0:
        return np.unique(original_data[target_name])[
            np.argmax(np.unique(original_data[target_name], return_counts=True)[1])]
    elif len(features) == 0:
        return parent_node_class
    else:
        parent_node_class = np.unique(data[target_name])[np.argmax(np.unique(data[target_name], return_counts=True)[1])]
        item_values = [info_gain(data, feature, target_name) for feature in features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        tree = {best_feature: {}}
        features = [i for i in features if i != best_feature]

        for value in np.unique(data[best_feature]):
            sub_data = data.where(data[best_feature] == value).dropna()
            subtree = build_tree(sub_data, data, features, target_name, parent_node_class)
            tree[best_feature][value] = subtree
        return tree


# Function to predict the outcome using the decision tree
def predict(query, tree, default=1):
    for key in list(query.keys()):
        if key in list(tree.keys()):
            try:
                result = tree[key][query[key]]
            except:
                return default
            result = tree[key][query[key]]
            if isinstance(result, dict):
                return predict(query, result)
            else:
                return result


# Prepare the dataset
data = pd.DataFrame([
    ['Suburban', 'Detached', 'High', 'No', 'Not responded'],
    ['Suburban', 'Detached', 'High', 'Yes', 'Not responded'],
    ['Rural', 'Detached', 'High', 'No', 'Responded'],
    ['Urban', 'Semi-detached', 'High', 'No', 'Responded'],
    ['Urban', 'Semi-detached', 'Low', 'No', 'Responded'],
    ['Urban', 'Semi-detached', 'Low', 'Yes', 'Not responded'],
    ['Rural', 'Semi-detached', 'Low', 'Yes', 'Responded'],
    ['Suburban', 'Terrace', 'High', 'No', 'Not responded'],
    ['Suburban', 'Semi-detached', 'Low', 'No', 'Responded'],
    ['Urban', 'Terrace', 'Low', 'No', 'Responded'],
    ['Suburban', 'Terrace', 'Low', 'Yes', 'Responded'],
    ['Rural', 'Terrace', 'High', 'Yes', 'Responded'],
    ['Rural', 'Detached', 'Low', 'No', 'Responded'],
    ['Urban', 'Terrace', 'High', 'Yes', 'Not responded']
], columns=['District', 'House Type', 'Income', 'PreviousCustomer', 'Outcome'])

# Building the decision tree
features = data.columns[:-1]
tree = build_tree(data, data, features)

# Print the decision tree structure
print(tree)

# Predict the marketing outcome for a new customer
query = {'District': 'Suburban', 'House Type': 'Detached', 'Income': 'Low', 'PreviousCustomer': 'Yes'}
prediction = predict(query, tree, default='Unknown')
print("Prediction:", prediction)

