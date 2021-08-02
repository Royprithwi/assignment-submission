#!/usr/bin/env python
# coding: utf-8

# 1) After running the following code, what does the variable bacon contain?
# 
# bacon = 22
# 
# bacon + 1=23

# 2) What should the values of the following two terms be?
# 
# 'spam' + 'spamspam'='spamspamspam'
# 
# 'spam' * 3='spamspamspam'
# 

# 3) How can you tell the difference between break and continue?
# ans-With the break statement we can stop the loop before it has looped through all the items.
# With the continue statement we can stop the current iteration of the loop, and continue with the next.

# 4) In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# There is no difference between them.

# 5) Using a for loop, write a short programme that prints the numbers 1 to 10 Then, using a while loop, create an identical programme that prints the numbers 1 to 10.
# a = [1,2,3,4,5,6,7,8,9,10]
# for x in a:
#         print(x)
#         a = 1
# while a <=10 :
#     print(a)
#     a += 1

# 6) Given a number x, determine whether the given number is Armstrong number or not.
# 
# Input : 153
# 
# Output : Yes
# 
# 153 is an Armstrong number.
# 
# 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3 = 153

# 7) Program to find Sum of squares of first n natural numbers.
# squaresum(n) :
#      sm = 0
#     for i in range(1, n+1) :
#         sm = sm + (i * i)
#          return sm
# 
#  

# 8) Program to Reverse words in a given String in Python.
# reverse="word"[::-1]
# print(reverse)

# 9) Given a list of numbers, write a Python program to find the sum of all the elements in the list.
# 
# Input: [10,12,13]
# 
# Output: 35
# lst = []
# num = int(input('How many numbers: '))
# for n in range(num):
#     numbers = int(input('Enter number '))
#     lst.append(numbers)
# print("Sum of elements in given list is :", sum(lst))

# 10) Write a Python program to print all even numbers between 10-1000.
# for number in range(10, 100):
#     if(number % 2 == 0):
#         print("{0}".format(number))

# In[1]:


bacon = 22

bacon + 1


# In[2]:


'spam' + 'spamspam'


# In[3]:


'spam' * 3


# In[4]:


range(10)


# In[5]:


range(0, 10)


# In[6]:


range(0,10,1)


# In[8]:


a = [1,2,3,4,5,6,7,8,9,10]
for x in a:
    print(x)


# In[9]:


a = 1
while a <=10 :
    print(a)
    a += 1


# In[10]:


if x=x*x*x:
    print("armstrong number")


# In[20]:


squaresum(n) :
    sm = 0
   for i in range(1, n+1) :
       sm = sm + (i * i)
        n=4
print(squaresum(n))


# In[21]:


reverse="word"[::-1]
print(reverse)


# In[22]:


lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))


# In[29]:




for number in range(10, 100):
    if(number % 2 == 0):
        print("{0}".format(number))


# In[ ]:




