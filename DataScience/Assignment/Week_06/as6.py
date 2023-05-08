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
#---------------------------------------------------------------------------





