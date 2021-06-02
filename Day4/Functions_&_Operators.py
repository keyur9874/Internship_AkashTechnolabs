#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Simple function

def function1():
    print('Hello Keyur')

function1()


# In[2]:


# Function with argument

def function2(name):
    print('Hello',name)

function2('Keyur')  


# In[3]:


# Function with return value

def function3(name):
    return 'Hello '+name

name = function3('Keyur')  
print(name)


# In[4]:


# More than 1 return values

def function4(name):
    return 'Hello '+name, 'Welcome'

name, greetings = function4('Keyur')  
print(name)
print(greetings)


# In[5]:


# Default arguments

def function5(name='Default'):
    print('User :',name)

function5()
function5('Keyur')


# In[6]:


# Keyword Arguments(fixed)

def function6(name='Default', age=18):
    print('User :',name)
    print('Age :',age)

function6('Keyur',19)
function6(age=22, name='Keyur')


# In[7]:


# Non Keyword Arguments(variable)

def add(*numbers):
    sum=0
    for n in numbers:
        sum+=n
    print('Sum is :',sum)
    
add(12,13,14,15)
add(13,13)


# In[8]:


# Keyword Arguments(variable)

def info(**data):
    for i,j in data.items():
        print(i,':',j)
    
info(name='Nick')
info(name='Nick',age='20',phone='11111')


# In[9]:


# Variable Scope

z=10
def scope():
    z=99
    print('Inside function :',z)
    
print('Outside function :',z)
scope()


# In[10]:


# Model Import

import base

base.base_function('Keyur')


# In[11]:


# Arithmetic Function

x=20
y=5

print('x+y :',x+y)
print('x-y :',x-y)
print('x*y :',x*y)
print('x/y :',x/y)
print('x%y :',x%y)
print('x//y :',x//y)
print('x**y :',x**y)


# In[12]:


# Comparison Function

x=20
y=5

print('x>y :',x>y)
print('x<y :',x<y)
print('x==y :',x==y)
print('x!=y :',x!=y)
print('x>=y :',x>=y)
print('x<=y :',x<=y)


# In[13]:


# Logical Function

x=True
y=False

print('x and y :',x and y)
print('x or y :',x or y)
print('not y :',not y)


# In[14]:


# Assignment Function

x=3
print('x=3 :',x)
x+=3
print('x+=3 :',x)
x-=1
print('x-=1 :',x)
x*=9
print('x*=9 :',x)
x/=2
print('x/=2 :',x)
x%=8
print('x%=8 :',x)
x//=2
print('x//=2 :',x)
x**=3
print('x**=3 :',x)


# In[15]:


# Membership and Identity operators

lst=[1,2,3,4]

print(1 in lst)
print(3 not in lst)

x=12
y=12
print(x is y)

x=12
y=12.0
print(x is y)


# In[ ]:




