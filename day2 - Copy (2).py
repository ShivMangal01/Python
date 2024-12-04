import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

a = np.array(['a','b','c','d','e,','f'])
# print(a)

b= pd.Series([1,2,3,4,5,6])
# print(b)

data = pd.read_csv('student_admission_record_dirty.csv')
# print(data.info())

data = pd.read_csv('student_admission_record_dirty.csv')
# print(data.tail())

data = pd.read_csv('student_admission_record_dirty.csv')
# print(data.nunique())

data = pd.read_csv('student_admission_record_dirty.csv')
# print(data['City'].value_counts())

data = pd.read_csv('mentalhealth_dataset.csv')
print(data)

# a = [1,2,3]
# b = [2,4,0]
# plt.plot(a,b)
# plt.title('world')
# plt.xlabel('subject')
# plt.show()

a = [1,2,3,5,8,6,55,66,56,45]
b = [2,4,0,5,45,34,66,55,8,9]
plt.scatter(a,b)
plt.title('X')
plt.xlabel('Y')
plt.show()


