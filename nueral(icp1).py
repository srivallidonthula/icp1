#!/usr/bin/env python
# coding: utf-8

# In[14]:


#question1-1
import random
data = input("enter data : ")

split =  random.randrange(3, len(data)-2)

data = data.replace(data[split:],"")
data = data[::-1]
print(data)


# In[ ]:


#question1-2
num1 = int(input("enter number 1 :"))
num2 = int(input("enter number 2 :"))

print("\n addition : ",(num1+num2))
print("subtraction : ",(num1-num2))
print("divison : ",(num1/num2))
print("multiplication : ",(num1*num2))


# In[18]:


#question 2
inputValue = input("enter string :")

inputValue = inputValue.replace("python","pythons")

print(inputValue)


# In[16]:


#question3
marks = int(input("Enter Students score : "))

if(marks<=100 and marks>=90):
    print("Grade = A")
elif(marks<=89 and marks>=80):
     print("Grade = B")
elif(marks<=79 and marks>=70):
     print("Grade = C") 
elif(marks<=69 and marks>=60):
     print("Grade = D")
elif(marks<=59 and marks>=0):
     print("Grade = F")


# In[ ]:




