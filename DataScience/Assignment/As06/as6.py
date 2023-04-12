'''
Data Science
Project : Assignment 6 ( Team Assignment )
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


#---------------------------------------------------------------------------
#---------------------  Assignment (2/7)  ----------------------------------
#                       Author : Kim Minji
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

df=pd.read_csv("bmi_data_phw1.csv")

# print dataset statistical data, feature names & data types.
print(df)
print(df.info())

# Plot height & weight histograms (bins=10) for each BMI value.
h = df.loc[:,['Height (Inches)']].values
w = df.loc[:,['Weight (Pounds)']].values

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


# Plot scaling results for height and weight.
#   Use StandardScaler, MinMaxScaler, and RobustScaler.

def My_Scaling(scaler,name):

    df2=df.drop(['Sex','Age','BMI'],axis=1)

    scaled_df=scaler.fit_transform(df2)
    scaled_df=pd.DataFrame(scaled_df,columns=['Height (Inches)','Weight (Pounds)'])

    fig, (ax1,ax2)=plt.subplots(ncols=2)

    ax1.set_title('Before Scaling')
    sns.kdeplot(df2['Height (Inches)'],ax=ax1)
    sns.kdeplot(df2['Weight (Pounds)'],ax=ax1)

    ax2.set_title(name)
    sns.kdeplot(scaled_df['Height (Inches)'],ax=ax2)
    sns.kdeplot(scaled_df['Weight (Pounds)'],ax=ax2)

    plt.show()

# Print plt of StandardScaler.
scaler=StandardScaler()
My_Scaling(scaler,"After StandardScaler")

# Print plt of MinMaxScaler.
scaler=MinMaxScaler()
My_Scaling(scaler,"After MinMaxScaler")

# Print plt of RobustScaler.
scaler=RobustScaler()
My_Scaling(scaler,"After RobustScaler")
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# Author: 202033762 장민호
# Programming Homework 1 (2/4)
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

# Author: 202033762 장민호
# Programming Homework 1 (2/4)
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
#---------------------------------------------------------------------------