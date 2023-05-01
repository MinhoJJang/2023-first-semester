'''
Data Science
Project : Assignment 6 ( Team Assignment )
Author : Kim Minji (김민지) , 장민호 , 남장안
Due Date : 23.04.16
'''
'''
!pip install pandas
!pip install -U xlrd openpyxl
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
import seaborn as sns
import openpyxl

# ---------------------------------------------------------------------------
# ---------------------  Assignment (1/4)  ----------------------------------
#                       Student ID : 202135727
#                       Author : Kim Minji (김민지)
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

df = pd.read_excel("bmi_data_.xlsx")

# print dataset statistical data, feature names & data types.
print(df)
print(df.info())

# Plot height & weight histograms (bins=10) for each BMI value.
h = df.loc[:, ['Height (Inches)']].values
w = df.loc[:, ['Weight (Pounds)']].values

'''
    # Print height histogram.
plt.title("Histogram of result_Height")
plt.hist(h, bins=10)
Histo_height = plt
Histo_height.show()

    # Print weight histogram.
plt.title("Histogram of result_Weight")
plt.hist(w, bins=10)
Histo_weight = plt
Histo_weight.show()
'''

for i in range(0, 5):
    # Plot height & weight histograms (bins=10) for each BMI value.
    h = df.loc[df['BMI'] == i, ['Height (Inches)']].values
    w = df.loc[df['BMI'] == i, ['Weight (Pounds)']].values

    # Print height histogram.
    plt.title("height histogram of people with bmi %d" % i)
    plt.hist(h, bins=10)
    Histo_height = plt
    Histo_height.show()

    # Print weight histogram.
    plt.title("Weight histogram of people with bmi %d" % i)
    plt.hist(w, bins=10)
    Histo_weight = plt
    Histo_weight.show()


# Plot scaling results for height and weight.
#   Use StandardScaler, MinMaxScaler, and RobustScaler.

def My_Scaling(scaler, name):
    df2 = df.drop(['Sex', 'Age', 'BMI'], axis=1)

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

# ---------------------------------------------------------------------------
# ---------------------  Assignment (2/4)  ----------------------------------
#                       Student ID : 202033762
#                       Author : 장민호
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# Program: find outlier people
# Although the given dataset has BMI values, we are going to estimate the values as if we don’t know them
# We will compare the estimated BMI values (0 and 4) with the actual values to see how much our estimation is correct

# 1. Read the Excel dataset file, and compute the linear regression equation E for the input dataset D
from sklearn.linear_model import LinearRegression

# df=pd.read_csv("bmi_data_phw1.csv")

# Compute linear regression for height and weight.
h = df[["Height (Inches)"]].values
w = df["Weight (Pounds)"].values
reg = LinearRegression().fit(h, w)

# Print the linear regression equation.
print("Linear regression equation: y = {:.2f}x + {:.2f}".format(reg.coef_[0], reg.intercept_))

# plot linear regression line using plt.plot()
plt.scatter(h, w, color='blue')
plt.plot(h, reg.predict(h), color='red', linewidth=3)
plt.title("Linear regression for height and weight")
plt.xlabel("Height (Inches)")
plt.ylabel("Weight (Pounds)")
plt.show()

# 2. For (height h, weight w) of each record, compute e=w-w’, where w’ is obtained for h using E

# linear regression to predict weight based on height
w_pred = reg.predict(h)

# Calculate the difference between the actual weight and the predicted weight
weight_diff = w - w_pred

# Print plt of weight_diff
plt.scatter(h, weight_diff, color='green')
plt.axhline(y=0, color='r', linestyle='-')
plt.xlabel('Height (Inches)')
plt.ylabel('Weight difference (Pounds)')
plt.title('weight_diff Plot')
plt.show()

# ---------------------------------------------------------------------------
# ---------------------  Assignment (2/4)  ----------------------------------
#                       Student ID : 202135763
#                       Author : 남장안
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Normalize the e values and Decide a value α (≥0); for records with ze<-α, set BMI = 0; for those with ze>α, set BMI = 4

# normalize e values
e_mean = weight_diff.mean()
e_std = weight_diff.std()

ze = (weight_diff - e_mean) / e_std

# plot histogram of ze
plt.hist(ze, bins=10)
plt.xlabel('ze')
plt.ylabel('Frequency')
plt.title('histogram of ze')
histo_ze = plt
histo_ze.show()

# set BMI values based on ze
alpha = 1.0  # alpha is randomly specified as 2.0. it can be any value
df.loc[ze < -alpha, 'BMI'] = 0
df.loc[ze > alpha, 'BMI'] = 4

# print updated dataframe
print(df)

# ---------------------------------------------------------------------------
# ---------------------  Assignment (4/4)  ----------------------------------
#                       Student ID : 202135727
#                       Author : Kim Minji (김민지)
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# Divide the input dataset D into two groups Df and Dm according to gender.
Dm = df[df['Sex'] == 'Male']
Df = df[df['Sex'] == 'Female']
Dm_Ori = Dm.copy()
Df_Ori = Df.copy()

# Do the same as done previously for each of Df and Dm.

# Dm : print dataset statistical data, feature names & data types.
print(Dm)
print(Dm.info())
# Df : print dataset statistical data, feature names & data types.
print(Df)
print(Df.info())

# Dm : Plot height & weight histograms (bins=10) for each BMI value.
hm = Dm.loc[:, ['Height (Inches)']].values
wm = Dm.loc[:, ['Weight (Pounds)']].values
# Df : Plot height & weight histograms (bins=10) for each BMI value.
hf = Df.loc[:, ['Height (Inches)']].values
wf = Df.loc[:, ['Weight (Pounds)']].values

# Dm : Print height histogram.
plt.title("Dm : Histogram of result_Height")
plt.hist(hm, bins=10)
Dm_Histo_height = plt
Dm_Histo_height.show()

# Dm : Print weight histogram.
plt.title("Dm : Histogram of result_Weight")
plt.hist(wm, bins=10)
Dm_Histo_weight = plt
Dm_Histo_weight.show()

# Df : Print height histogram.
plt.title("Df : Histogram of result_Height")
plt.hist(hf, bins=10)
Dm_Histo_height = plt
Dm_Histo_height.show()

# Df : Print weight histogram.
plt.title("Df : Histogram of result_Weight")
plt.hist(wf, bins=10)
Df_Histo_weight = plt
Df_Histo_weight.show()

# Plot scaling results for height and weight.
# Use StandardScaler, MinMaxScaler, and RobustScaler.
# As Male and Female.

# These are Male data.
# Print plt of StandardScaler.
scaler = StandardScaler()
My_Scaling(scaler, "After StandardScaler : Male")

# Print plt of MinMaxScaler.
scaler = MinMaxScaler()
My_Scaling(scaler, "After MinMaxScaler : Male")

# Print plt of RobustScaler.
scaler = RobustScaler()
My_Scaling(scaler, "After RobustScaler : Male")

# These are Female data.
# Print plt of StandardScaler.
scaler = StandardScaler()
My_Scaling(scaler, "After StandardScaler : Female")

# Print plt of MinMaxScaler.
scaler = MinMaxScaler()
My_Scaling(scaler, "After MinMaxScaler : Female")

# Print plt of RobustScaler.
scaler = RobustScaler()
My_Scaling(scaler, "After RobustScaler : Female")

# Read the Excel dataset file, and compute the linear regression equation E for the input dataset D

# Dm : Compute linear regression for height and weight.
hm = Dm[["Height (Inches)"]].values
wm = Dm["Weight (Pounds)"].values
reg = LinearRegression().fit(hm, wm)

# Dm : Print the linear regression equation.
print("Dm : Linear regression equation: y = {:.2f}x + {:.2f}".format(reg.coef_[0], reg.intercept_))

# plot linear regression line using plt.plot()
plt.scatter(hm, wm, color='blue')
plt.plot(hm, reg.predict(hm), color='red', linewidth=3)
plt.title("Dm : Linear regression for height and weight")
plt.xlabel("Height (Inches)")
plt.ylabel("Weight (Pounds)")
plt.show()

# Df : Compute linear regression for height and weight.
hf = Df[["Height (Inches)"]].values
wf = Df["Weight (Pounds)"].values
reg = LinearRegression().fit(hf, wf)

# Df : Print the linear regression equation.
print("Df : Linear regression equation: y = {:.2f}x + {:.2f}".format(reg.coef_[0], reg.intercept_))

# plot linear regression line using plt.plot()
plt.scatter(hf, wf, color='blue')
plt.plot(hf, reg.predict(hf), color='red', linewidth=3)
plt.title("Df : Linear regression for height and weight")
plt.xlabel("Height (Inches)")
plt.ylabel("Weight (Pounds)")
plt.show()

# For (height h, weight w) of each record, compute e=w-w’, where w’ is obtained for h using E

# Dm : linear regression to predict weight based on height
w_pred1 = reg.predict(hm)

# Dm : Calculate the difference between the actual weight and the predicted weight
Dm_weight_diff = wm - w_pred1

# Dm : Print plt of weight_diff
plt.scatter(hm, Dm_weight_diff, color='green')
plt.axhline(y=0, color='r', linestyle='-')
plt.title('Dm : weight_diff Plot')
plt.xlabel('Height (Inches)')
plt.ylabel('Weight difference (Pounds)')
plt.show()

# Df : linear regression to predict weight based on height
w_pred2 = reg.predict(hf)

# Df : Calculate the difference between the actual weight and the predicted weight
Df_weight_diff = wf - w_pred2

# Df : Print plt of weight_diff
plt.scatter(hf, Df_weight_diff, color='green')
plt.axhline(y=0, color='r', linestyle='-')
plt.title('Df : weight_diff Plot')
plt.xlabel('Height (Inches)')
plt.ylabel('Weight difference (Pounds)')
plt.show()

# Normalize the e values and Decide a value α (≥0); for records with ze<-α, set BMI = 0; for those with ze>α, set BMI = 4

# Dm, Df : normalize e values--------------------
print("Check Dm_weight_diff")
print(Dm_weight_diff)
Dm_e_mean = Dm_weight_diff.mean()
Dm_e_std = Dm_weight_diff.std()

Dm_ze = (Dm_weight_diff - Dm_e_mean) / Dm_e_std
# ------------
Df_e_mean = Df_weight_diff.mean()
Df_e_std = Df_weight_diff.std()

Df_ze = (Df_weight_diff - Df_e_mean) / Df_e_std

# Dm, Df : plot histogram of ze------------------------
plt.hist(Dm_ze, bins=10)
plt.xlabel('ze')
plt.ylabel('Frequency')
plt.title('Dm : histogram of ze')
plt.show()
# histo_ze = plt
# histo_ze.show()

# ------------
plt.hist(Df_ze, bins=10)
plt.xlabel('ze')
plt.ylabel('Frequency')
plt.title('Df : histogram of ze')
plt.show()
# histo_ze = plt
# histo_ze.show()

# Dm, Df : set BMI values based on ze----------------------
alpha = 1.0  # alpha is randomly specified as 1.0. it can be any value
Dm.loc[Dm_ze < -alpha, 'BMI'] = 0
Dm.loc[Dm_ze > alpha, 'BMI'] = 4
# -------------------
Df.loc[Df_ze < -alpha, 'BMI'] = 0
Df.loc[Df_ze > alpha, 'BMI'] = 4

# Dm, Df : print updated dataframe--------------------
print(Dm)
print(Df)

# Compare My BMI estimates with the actual BMI values in the given dataset.
# If It is Not change, Then True.
# If It is change, Then False.
# Dm
print("Dm's change. If Same : True, If change : False.")
print(Dm.loc[:, ['BMI']].values == Dm_Ori.loc[:, ['BMI']].values)
print()

# Df
print("Df's change. If Same : True, If change : False.")
print(Df.loc[:, ['BMI']].values == Df_Ori.loc[:, ['BMI']].values)
