'''
Data Science
Project : Lab 2
Author : Kim Minji ,
Due Date : 23.04.16



'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
import seaborn as sns
from sklearn.linear_model import LinearRegression
# ----------------------------------------- (2/7) ------------------------------------------

df = pd.read_csv("bmi_data_lab2.csv")

# print dataset statistical data, feature names & data types.
print(df)
print(df.info())

# ----------------------------------------- (3/7) ------------------------------------------

# Identify dirty records with likely-wrong or missing height or weight values
dirty_records = df[(df['Height (Inches)'] < 10) | (df['Height (Inches)'] > 250) | (df['Weight (Pounds)'] < 20) | (
        df['Weight (Pounds)'] > 180)]

# Make likely-wrong values NAN
df.loc[(df['Height (Inches)'] < 10) | (df['Height (Inches)'] > 250) | (df['Weight (Pounds)'] < 20) | (
        df['Weight (Pounds)'] > 180), ['Height (Inches)', 'Weight (Pounds)']] = pd.NA

# Print number of rows with NAN and number of NAN for each column
print('Number of rows with NAN:', df.isna().any(axis=1).sum())
print('Number of NAN for each column:\n', df.isna().sum())

# Extract rows without NAN
clean_df = df.dropna()
# print(clean_df)

# ----------------------------------------- (2/7) ------------------------------------------

for i in range(0,5):
    # Plot height & weight histograms (bins=10) for each BMI value.
    h= clean_df.loc[clean_df['BMI']==i, ['Height (Inches)']].values
    w= clean_df.loc[clean_df['BMI']==i, ['Weight (Pounds)']].values

    # Print height histogram.
    plt.title("height histogram of people with bmi %d" %i)
    plt.hist(h, bins=10)
    Histo_height = plt
    Histo_height.show()

    # Print weight histogram.
    plt.title("Weight histogram of people with bmi %d" %i)
    plt.hist(w, bins=10)
    Histo_weight = plt
    Histo_weight.show()


# Plot scaling results for height and weight.
#   Use StandardScaler, MinMaxScaler, and RobustScaler.

def My_Scaling(scaler, name):
    df2 = clean_df.drop(['Sex', 'Age', 'BMI'], axis=1)

    scaled_df = scaler.fit_transform(df2)
    scaled_df = pd.DataFrame(scaled_df, columns=['Height (Inches)', 'Weight (Pounds)'])

    fig, (ax1, ax2) = plt.subplots(ncols=2)

    ax1.set_title('Before Scaling')
    sns.kdeplot(df2['Height (Inches)'], ax=ax1)
    sns.kdeplot(df2['Weight (Pounds)'], ax=ax1)

    ax2.set_title(name)
    sns.kdeplot(scaled_df['Height (Inches)'], ax=ax2)
    sns.kdeplot(scaled_df['Weight (Pounds)'], ax=ax2)

    plt.show()


# Print plt of StandardScaler.
scaler = StandardScaler()
My_Scaling(scaler, "After StandardScaler")

# Print plt of MinMaxScaler.
scaler = MinMaxScaler()
My_Scaling(scaler, "After MinMaxScaler")

# Print plt of RobustScaler.
scaler = RobustScaler()
My_Scaling(scaler, "After RobustScaler")

# ----------------------------------------- (5/7) ------------------------------------------
# Author: 202033762 Jang Min Ho
# Missing value manipulation (more elaborate)
# Clean the dirty values using linear regression

# Cleaning the Input Dataset:
# Compute the linear regression equation E for (height, weight) values in the input dataset

# For dirty height and weight values, compute replacement values using E
# Computed with known weight and height values, respectively


# Function to identify and replace dirty data
def clean_data(row, model, coef, intercept):
    height = row["Height (Inches)"]
    weight = row["Weight (Pounds)"]

    # linear regression, to clean the data using y = coef * x + intercept
    if pd.isna(height) and not pd.isna(weight):
        row["Height (Inches)"] = (weight - intercept) / coef
    elif pd.isna(weight) and not pd.isna(height):
        row["Weight (Pounds)"] = coef * height + intercept

    return row


# Function to check the valid data
def is_valid_height(height):
    min_height = 30  # Minimum height in inches
    max_height = 90  # Maximum height in inches
    return min_height <= height <= max_height


# Function to check the valid data
def is_valid_weight(weight):
    min_weight = 80  # Minimum weight in pounds
    max_weight = 300  # Maximum weight in pounds
    return min_weight <= weight <= max_weight


# Read the dataset
data = pd.read_csv("bmi_data_lab2.csv")

# Clean the data
# If the data is invaild, set them np.nan
data["Height (Inches)"] = data["Height (Inches)"].apply(
    lambda x: float(x) if not pd.isna(x) and is_valid_height(x) else np.nan)
data["Weight (Pounds)"] = data["Weight (Pounds)"].apply(
    lambda x: float(x) if not pd.isna(x) and is_valid_weight(x) else np.nan)

# Prepare the data for linear regression
known_data = data.dropna(subset=["Height (Inches)", "Weight (Pounds)"])
print(known_data)
X = known_data["Height (Inches)"].values.reshape(-1, 1)
y = known_data["Weight (Pounds)"].values

# Train the linear regression model
E = LinearRegression()
E.fit(X, y)

# Calculate the coefficients
coefficient = E.coef_[0]
intercept = E.intercept_

# Print the linear regression equation
print(f"Linear Regression Equation: E(y) = {coefficient:.2f} * x + {intercept:.2f}")

# Replace dirty values using the linear regression equation
data_cleaned = data.apply(clean_data, axis=1, args=(E, coefficient, intercept))


# Do the same for the groups divided by gender.
# the dirty value of a female record is cleaned using the equation E_f computed for the female group
def clean_data_gender_bmi(row, model_f, coef_f, intercept_f, model_m, coef_m, intercept_m):
    height = row["Height (Inches)"]
    weight = row["Weight (Pounds)"]
    sex = row["Sex"]

    if sex == "Female":
        if pd.isna(height) and not pd.isna(weight):
            row["Height (Inches)"] = (weight - intercept_f) / coef_f
        elif pd.isna(weight) and not pd.isna(height):
            row["Weight (Pounds)"] = coef_f * height + intercept_f
    else:  # Male
        if pd.isna(height) and not pd.isna(weight):
            row["Height (Inches)"] = (weight - intercept_m) / coef_m
        elif pd.isna(weight) and not pd.isna(height):
            row["Weight (Pounds)"] = coef_m * height + intercept_m

    return row


# Prepare the data for linear regression for each gender
known_data_female = known_data[known_data["Sex"] == "Female"]
known_data_male = known_data[known_data["Sex"] == "Male"]

X_female = known_data_female["Height (Inches)"].values.reshape(-1, 1)
y_female = known_data_female["Weight (Pounds)"].values

X_male = known_data_male["Height (Inches)"].values.reshape(-1, 1)
y_male = known_data_male["Weight (Pounds)"].values

# Train the linear regression model for each gender
E_female = LinearRegression()
E_female.fit(X_female, y_female)

E_male = LinearRegression()
E_male.fit(X_male, y_male)

# Calculate the coefficients for each gender
coefficient_female = E_female.coef_[0]
intercept_female = E_female.intercept_

coefficient_male = E_male.coef_[0]
intercept_male = E_male.intercept_

# Print the linear regression equations for each gender
print(f"Female Linear Regression Equation: E_f(y) = {coefficient_female:.2f} * x + {intercept_female:.2f}")
print(f"Male Linear Regression Equation: E_m(y) = {coefficient_male:.2f} * x + {intercept_male:.2f}")

# Replace dirty values using the gender-specific linear regression equations
data_cleaned_gender = data.apply(clean_data_gender_bmi, axis=1, args=(
    E_female, coefficient_female, intercept_female, E_male, coefficient_male, intercept_male))

# 2. Do the same for the groups divided by BMI, 1 to 3
def clean_data_bmi(row, model, coefs, intercepts):
    height = row["Height (Inches)"]
    weight = row["Weight (Pounds)"]
    bmi = row["BMI"]

    if pd.isna(bmi):
        return row

    bmi = int(bmi)

    if pd.isna(height) and not pd.isna(weight):
        row["Height (Inches)"] = (weight - intercepts[bmi]) / coefs[bmi]
    elif pd.isna(weight) and not pd.isna(height):
        row["Weight (Pounds)"] = coefs[bmi] * height + intercepts[bmi]

    return row


# Prepare the data for linear regression for each BMI group
models_bmi = [None] * 4
coefs_bmi = [None] * 4
intercepts_bmi = [None] * 4

# Prepare the data for linear regression. Add BMI feature
known_data = data.dropna(subset=["Height (Inches)", "Weight (Pounds)", "BMI"])

# print(known_data)

for i in range(1, 4):
    known_data_bmi = known_data[known_data["BMI"] == i]

    X_bmi = known_data_bmi["Height (Inches)"].values.reshape(-1, 1)
    y_bmi = known_data_bmi["Weight (Pounds)"].values

    # Train the linear regression model for each BMI group
    E_bmi = LinearRegression()
    E_bmi.fit(X_bmi, y_bmi)

    # Calculate the coefficients for each BMI group
    coefficient_bmi = E_bmi.coef_[0]
    intercept_bmi = E_bmi.intercept_

    # Print the linear regression equation for each BMI group
    print(f"BMI {i} Linear Regression Equation: E_{i}(y) = {coefficient_bmi:.2f} * x + {intercept_bmi:.2f}")

    models_bmi[i] = E_bmi
    coefs_bmi[i] = coefficient_bmi
    intercepts_bmi[i] = intercept_bmi


# Replace dirty values using the BMI-specific linear regression equations
data_cleaned_bmi = data.apply(clean_data_bmi, axis=1, args=(models_bmi, coefs_bmi, intercepts_bmi))



# 3. Draw a scatter plot of (height, weight) in the clean dataset emphasizing previously dirty records with a different color
# For a dirty record, compare the replacement values computed using different regression equations
# e.g., the height replacement values for a dirty record (NAN, w) computed using E and Ef might be different

# GENERAL

# Create a boolean mask to identify dirty records
dirty_mask = (
    data['Height (Inches)'].isna() | data['Weight (Pounds)'].isna()
)

# Clean the data using different regression equations
data_cleaned = data_cleaned

# Separate clean and dirty records
clean_records = data_cleaned[~dirty_mask]
dirty_records = data_cleaned[dirty_mask]

# Plot the scatter plot with different colors for clean and dirty records
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(clean_records["Height (Inches)"], clean_records["Weight (Pounds)"], color='blue', label='Clean Records', alpha=0.5)
ax.scatter(dirty_records["Height (Inches)"], dirty_records["Weight (Pounds)"], color='red', label='Dirty Records', alpha=0.5)

# Calculate and plot the linear regression lines
height_range = np.linspace(data_cleaned["Height (Inches)"].min(), data_cleaned["Height (Inches)"].max(), 100)

# Plot the overall linear regression line
weight_overall = coefficient * height_range + intercept
ax.plot(height_range, weight_overall, color='red', label='Overall Linear Regression', linestyle="-")

ax.set_xlabel('Height (Inches)')
ax.set_ylabel('Weight (Pounds)')
ax.legend()
plt.show()

# =========================
# GENDER
# Clean the data using different regression equations
data_cleaned = data_cleaned_gender

# Separate clean and dirty records
clean_records = data_cleaned[~dirty_mask]
dirty_records = data_cleaned[dirty_mask]

# Plot the scatter plot with different colors for clean and dirty records
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(clean_records["Height (Inches)"], clean_records["Weight (Pounds)"], color='blue', label='Clean Records', alpha=0.5)
ax.scatter(dirty_records["Height (Inches)"], dirty_records["Weight (Pounds)"], color='red', label='Dirty Records', alpha=0.5)

# Plot the gender-specific linear regression lines
weight_female = coefficient_female * height_range + intercept_female
weight_male = coefficient_male * height_range + intercept_male
ax.plot(height_range, weight_female, color='pink', label='Female Linear Regression', linestyle="--")
ax.plot(height_range, weight_male, color='blue', label='Male Linear Regression', linestyle="--")

ax.set_xlabel('Height (Inches)')
ax.set_ylabel('Weight (Pounds)')
ax.legend()
plt.show()

# ============================
# BMI
# Clean the data using different regression equations
data_cleaned = data_cleaned_bmi

# Separate clean and dirty records
clean_records = data_cleaned[~dirty_mask]
dirty_records = data_cleaned[dirty_mask]

# Plot the scatter plot with different colors for clean and dirty records
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(clean_records["Height (Inches)"], clean_records["Weight (Pounds)"], color='blue', label='Clean Records', alpha=0.5)
ax.scatter(dirty_records["Height (Inches)"], dirty_records["Weight (Pounds)"], color='red', label='Dirty Records', alpha=0.5)

# Plot the BMI-specific linear regression lines
for i in range(1, 4):
    weight_bmi = coefs_bmi[i] * height_range + intercepts_bmi[i]
    ax.plot(height_range, weight_bmi, label=f'BMI {i} Linear Regression', linestyle="-.")

ax.set_xlabel('Height (Inches)')
ax.set_ylabel('Weight (Pounds)')
ax.legend()
plt.show()
