#!/usr/bin/env python
# coding: utf-8

# # Ibm peer graded assignment

# # It is the final assignment in the tools for datascience

# # list of datascience languages
# 1. Python
# 2. SQL (Structured Query Language)
# 3. R
# 4. Julia
# 5. Java Script
# 6. scala 
# 7. Java
# 8. Go

# # List data science libraries
# 1. TensorFlow
# 2. NumPy
# 3. SciPy 
# 4. Pandas
# 5. Matplotlib 
# 6. Keras
# 7. SciKit-Learn
# 8. PyTorch
# 9. Scrapy
# 10. BeautifulSoup
# 11. LightGBM
# 12. ELI5
# 13. Theano
# 14. NuPIC
# 15. Ramp
# 16. Pipenv
# 17. Bob
# 18. PyBrain
# 19. Caffe2
# 20. Chainer

# # Data science tools
# 1. Statistical Analysis System (SAS)
# 2. Apache Hadoop
# 3. Tableau
# 4. TensorFlow
# 5. BigML
# 6. Knime
# 7. RapidMiner
# 8. Excel
# 9. Apache Flink
# 10. PowerBI
# 11. Google Analytics
# 12. Python
# 13. R (RStudio)
# 14. DataRobot
# 15. D3.js
# 16. Microsoft HDInsight
# 17. Jupyter
# 18. Matplotlib
# 19. MATLAB
# 20. QlikView

# # Arithmetic expression examples

# In[1]:


5+5


# In[2]:


2*8


# In[3]:


4**2


# In[4]:


15/3


# In[5]:


999-199


# # Multiply and add numbers

# In[8]:


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,*,: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '*':
    result = num1 * num2
else:
    print("Input character is not recognized!")
print(num1, ch , num2, ":", result)


# # convert minutes to hours.

# In[11]:



def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

n = 12345
print(convert(n))


# # list Objectives

# In[13]:


class geeks:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

# creating list
list = []

# appending instances to list
list.append(geeks('Akash', 2))
list.append(geeks('Deependra', 40))
list.append(geeks('Reaper', 44))
list.append(geeks('veer', 67))

# Accessing object value using a for loop
for obj in list:
    print(obj.name, obj.roll, sep=' ')

print("")
# Accessing individual elements
print(list[0].name)
print(list[1].name)
print(list[2].name)
print(list[3].name)


# # Author’s name
# Romeo Kienzler

# In[ ]:




