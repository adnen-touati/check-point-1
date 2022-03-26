#!/usr/bin/env python
# coding: utf-8

# In[1]:


#QUESTION 1 


first_name = input()
last_name = input()
print (last_name,first_name)


# In[2]:


#question 2

x = input()
str(x)
a=x+x
b=x+x+x

y=int(a)+int(b)+int(x)
print(y)


# In[3]:


#question 3
x=input()
x=int(x)
if x %2==0 :
    print (x, "is an even number")
else:
    print (x, "is an odd number")


# In[4]:


#Question 4
for i in range (2000,3201,1):
    if i % 7 == 0 & i%5 == 0 :
        print (i)
        


# In[5]:


#question 5
nbr = int(input('Entrez un nombre : '))
fact = 1
for i in range(1, nbr+1):
    fact = fact * i
print (nbr,'! = ',fact)


# In[14]:


#question 7
x=int(input())
if x>=500:
    print (('reduced price is ='),float((x * 50) / 100))
elif x>=200 and x<500:
    print (('reduced price is ='),float((x*70)/100))
else :
    print (('reduced price is ='),float((x*90)/100))


# In[ ]:




