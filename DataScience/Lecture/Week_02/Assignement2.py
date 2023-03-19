# Numpy Exercise - 1
import numpy as np

np.random.seed(20230319)
wt = ((90.0-40.0)*np.random.random_sample(size=100)+40).round(1)
ht = ((200.0-140.0)*np.random.random_sample(size=100)+140).round(1)
bmi_array = ((wt / ht**2)*(10**4)).round(1)

print(bmi_array)

# MatPlotlib Exercise - 2
import matplotlib.pyplot as plt

bmi_range = [0,min(bmi_array), 18.5, 25, 30, max(bmi_array), 50]
weight_status = ['Underweight', 'Healthy', 'Overweight', 'Obese']

# 이때, BMI 기준에 맞는 범위의 숫자 개수를 알아야 한다.
underweight = len([bmi for bmi in bmi_array if bmi < 18.5])
healthy = len([bmi for bmi in bmi_array if 18.5 <= bmi < 25])
overweight = len([bmi for bmi in bmi_array if 25 <= bmi < 30])
obese = len([bmi for bmi in bmi_array if 30 <= bmi ])
bmi_status = [underweight, healthy, overweight, obese]

# Scatter plot
wt = ((90.0-40.0)*np.random.random_sample(size=100)+40).round(1)
ht = ((200.0-140.0)*np.random.random_sample(size=100)+140).round(1)
plt.scatter(ht, wt, color='b')
plt.xlabel('height')
plt.ylabel('weight')
plt.title('the correlation between height and weight')
plt.show()

# Pie Chart
# plt.pie(bmi_status, labels=weight_status, autopct='%d%%')
# plt.title('students BMI status')
# plt.show()

# Histogram
# plt.hist(bmi_array, bins=[min(bmi_array),18.5,25,30,max(bmi_array)])
# plt.xticks(bmi_range)
# plt.xlabel('Weight status')
# plt.ylabel("Number of students in that BMI state")
# plt.title('students BMI status')
# plt.show()

# Bar Chart
# Plot the student distribution for each bmi level
# plt.bar(weight_status, bmi_status)
# plt.xlabel('Weight status')
# plt.ylabel("Number of students in that BMI state")
# plt.title('students BMI status')
# plt.show()



