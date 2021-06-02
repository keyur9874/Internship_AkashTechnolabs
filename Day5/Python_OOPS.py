#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''1. Create a class cal1 that will calculate sum of three numbers. Create
setdata() method which has three parameters that contain numbers.
Create display() method that will calculate sum and display sum.'''


class cal1:
    num1=''
    num2=''
    num3=''
    def setdata(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        
    def display(self):
        s = self.num1+self.num2+self.num3
        print('Sum of given 3 numbers is :',s)

obj_cal1 = cal1()
obj_cal1.setdata(12,3,5)
obj_cal1.display()


# In[2]:


'''2. Create a class cal2 that will calculate area of a circle. Create setdata()
method that should take radius from the user. Create area() method
that will calculate area . Create display() method that will display area .
'''
import math

class cal2:
    r=''
    a=''
    def setdata(self,radius):
        self.r=radius
        
    def area(self):
        self.a = math.pi * self.r*self.r
        
    def display(self):
        print('Area of circle is :',self.a)

obj_cal2 = cal2()
obj_cal2.setdata(5)
obj_cal2.area()
obj_cal2.display()


# In[3]:


'''3. Create a class cal3 that will calculate simple interest. Create
constructor method which has three parameters .Create calInterest()
method that will calculate Interest . Create display() method that will
display Interest.'''


class cal3:
    p,r,n = '','',''
    i=''
    def __init__(self,p,r,n):
        self.p=p
        self.r=r
        self.n=n
        
    def calInterest(self):
        self.i = self.p*self.r*self.n / 100
        
    def display(self):
        print('Interest is :',self.i)

obj_cal3 = cal3(20000,5,2)
obj_cal3.calInterest()
obj_cal3.display()


# In[4]:


'''4. Create a class cal4 that will calculate square of a number. Create
setdata() method which has one parameters that contain number.
Create display() method that will calculate sum.(Function should
return value).'''


class cal4:
    n=''
    sq=''
    def setdata(self,number):
        self.n=number
        
    def display(self):
        self.sq = self.n ** 2
        return self.sq


obj_cal4 = cal4()
obj_cal4.setdata(9)
square = obj_cal4.display()

print('Square is : ',end='')
print(square)


# In[5]:


'''5. Consider an employee class, which contains fields such as name and
designation. And a subclass, which contains a field salary. Write a
program for inheriting this relation.'''


class employee:
    name='Keyur'
    designation='Software Development Engineer'
    
    def parentmethod(self):
        print('This method is written in Parent Class')
        
class sub_employee(employee):
    salary = 123456
    
    def childmethod(self):
        print('This method is written in Child Class')
        print('Name :',self.name)
        print('Designation :',self.designation)
        print('Salary :',self.salary)
                
        
obj_emp = sub_employee()
obj_emp.parentmethod()
print('------')
obj_emp.childmethod()


# In[15]:


'''6. Create a class cal5 that will calculate area of a rectangle. Create
constructor method which has two parameters .Create calArea()
method that will calculate area of a rectangle. Create display() method
that will display area of a rectangle.
'''

class cal5:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calArea(self):
        self.area = self.length * self.width
    def display(self):
        print("Area Of This Rectangle : ",self.area)
        
obj_cal5 = cal5(10,15)
obj_cal5.calArea()
obj_cal5.display()


# In[18]:


'''7. Create a class cal6 that will calculate area of a square. Create setdata()
method that should take length from the user. Create area() method
that will calculate area . Create display() method that will display area .'''

class cal6:
    def setdata(self,length):
        self.length = length
    def area(self):
        self.ar = self.length ** 2
    def display(self):
        print("Area Of square :",self.ar)

obj_cal6 = cal6()
l = int(input("Enter Length Of Square : "))
obj_cal6.setdata(l)
obj_cal6.area()
obj_cal6.display()


# In[26]:


'''8. Write a program with use of inheritance: Define a class publisher that
stores the name of the title. Derive two classes book and tape, which
inherit publisher. Book class contains member data called page no and
tape class contain time for playing. Define functions in the appropriate
classes to get and print the details.'''

class publisher:
    def __init__(self,title):
        self.title = title

class book(publisher):
    def __init__(self,title,pages):
        super().__init__(title)
        self.pages = pages
    def display(self):
        print("Title Of Book :",self.title)
        print("Number of pages :",self.pages)
        
class tape(publisher):
    def __init__(self,title,time):
        super().__init__(title)
        self.time = time
    def display(self):
        print("Title Of Book :",self.title)
        print("Time taken for playing(hours) :",self.time)

bk = book("Big Data :",750)
bk.display()
print("---------------------")
tp = tape('Love Story',7)
tp.display()


# In[28]:


'''9. Create a class called scheme with scheme_id,
scheme_name,outgoing_rate, and message_charge. Derive customer
class form scheme and include cust_id, name and mobile_no
data.Define necessary functions to read and display data.
'''

class scheme:
    def __init__(self,scheme_id,scheme_name,outgoing_rate,message_charge):
        self.scheme_id = scheme_id
        self.scheme_name = scheme_name
        self.outgoing_rate = outgoing_rate
        self.message_charge = message_charge
    def display(self):
        print("----Scheme details----")
        print("Scheme_Id :",self.scheme_id)
        print("Scheme_Name ;",self.scheme_name)
        print("Outgoing_rate :",self.outgoing_rate)
        print("Message_charge :",self.message_charge)
class customer(scheme):
    def __init__(self,cust_id,name,mobile_no,scheme_id,scheme_name,outgoing_rate,message_charge):
        super().__init__(scheme_id,scheme_name,outgoing_rate,message_charge)
        self.cust_id = cust_id
        self.name = name
        self.mobile_no = mobile_no
    
    def display(self):
        print("----Customer Details----")
        print('Customer Id :',self.cust_id)
        print('Customer Name :',self.name)
        print("Mobile No :",self.mobile_no)
        super().display()
        
ct = customer(102,'Keyur','789XXXXX78',1203,'Free messages',0.6,0)
ct.display()
        


# In[30]:


'''Create a arith class. The class should have a parameterized constructor
and methods to add, subtract and multiply two numbers and to return
the answers'''

class arith:
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    def sum2(self):
        return(self.v1+self.v2)
    def sub(self):
        return(self.v1-self.v2)
    def mul(self):
        return(self.v1*self.v2)
    def div(self):
        return(self.v1/self.v2)

obj = arith(10,5)
print("Sum :",obj.sum2())
print("Sub :",obj.sub())
print("Mul :",obj.mul())
print("Div :",obj.div())


# In[ ]:




