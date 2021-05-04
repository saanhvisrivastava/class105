# -*- coding: utf-8 -*-
"""class105.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bjEWB5aRx_6QvUcl1RPE66ZyYwgawv8q
"""

import csv
import math 

with open("data.csv",newline="")as f:
  reader=csv.reader(f)
  file_data=list(reader)

data=file_data[0]
#finding mean
def mean(data):
  n=len(data)
  total=0
  for i in data:
    total+=int(i)
  
  mean=total/n
  print(mean)
  return mean

  

  


#squaring and getting the values
sq_list=[]
for number in data:
  a=int(number)-mean(data)
  a=a**2
  sq_list.append(a)

#getting sum
sum=0
for i in sq_list:
  sum+=i

#dividing the sum by total value-1
result=sum/(len(data)-1)
#getting the deviation by taking sqaue root of the result
standard_deviation=math.sqrt(result)
print(standard_deviation)