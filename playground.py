#!/usr/bin/env python3
## WEEK 2 ----

# Regular expressions

import re
#from tkinter import E # don't know why this was imported

#s = ("If I’m not in a hurry, then I should stay. " +
 #   "On the other hand, if I leave, then I can sleep.")

#print(s)
#print(re.findall(r'[Ii]f (.*), then', s))
#print(bool(0))

# Basic file processing


#print("a".encode("utf-8"))


#print(list("a".encode("utf-8"))  )            # Show as a list of integers


# reading a file
#f = open("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/exercises_instructions.txt", "r") # Let's open this notebook file, 
                              # which is essentially a text file.
                              # So you can open it in a texteditor as well.
        
#for i in range(10):            # And read the first five lines
    #line = f.readline()
    #print(f"Line {i}: {line}", end="")
#f.close()

#s = ''
#print(s)
#print(type(s))
#s = int('0'+s)
#print(type(s))


#w = '1.F.1.  Project Gutenberg volunteers and employees expend considerable'
#print(w)
#a = re.split(r'\s', w)
#print(a)
#print(type(a), len(a))
#for i in a:
    #print(len(i))
    #print(i.endswith(r'[\w]$'))
 #   if not re.findall(r'[a-zA-Z0-9]$', i) or not re.findall(r'^[a-zA-Z0-9]', i): # si le mot ne finit/commence pas par une lettre ou chiffre 
        #z = []
        #z.append(i)
        #z.append(i.strip("""!"#$%&'()*,-./:;?@[]_"""))
  #      print(i.strip("""!"#$%&'()*,-./:;?@[]_"""))


#import sys
#
#from statistics import mean, variance
#help(open)
#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))
#print(sys.argv[1:])

#a = (float(15.904), float(904.15), float(567.3457))
#d = {"oui": 1}
#print(d)
#j = "test"
#print(re.findall(r'\.(.*)', j)[0])
#print(type(a))


## Classes and objects
#class MyClass:
 #     x = 5

#print(MyClass)
#p1 = MyClass()
#print(p1.x)
#print(type(p1))

## Corey Schafer YT ----
#class Employee:
    
 #   raise_amt  = 1.04

  #  def __init__(self, first, last, pay):
   #     self.first = first
    #    self.last = last
     #   self.email = first + "." + last + "@company.com"
      #  self.pay = pay
        
    #def fullname(self):
     #   return f"{self.first}, {self.last}"
    
    #def apply_raise(self):
     #   self.pay = int(self.pay * self.raise_amt)

    #def __repr__(self):
     #   return f"Employee {self.first}, {self.last}, {self.pay}"
    
    #pass

#emp_1 = Employee("Corey", "Schafer", 50000)
#emp_2 = Employee()
#print(emp_1)
#print(Employee("Lionel", "Ngoubou", "150K").first)
#print(emp_2)
#emp_1.first = "Corey"
#print(emp_1.email)

## StackOverflow ----
#class MyClass(object):
 #   def __str__(self):
  #      return "MyClass([])"
   # def __repr__(self):
    #        return "I am an instance of MyClass at address "+hex(id(self))
 
#m = MyClass()
#print(MyClass())
#MyClass([])
#m
#I am an instance of MyClass at address 0x108ed5a10

#a = int(15/3)
#a.from_bytes
#print(a)

#class B(object):
 #   def f(self):
  #      print("Executing B.f")
   # def g(self):
    #    print("Executing B.g")
    
#class C(B):
 #   def g(self):
  #      print("Executing C.g")
        
#x=C()
#x.f() # inherited from B
#x.g() # overridden by C
#print(issubclass(C,B))
#y = B()
#print(isinstance(x,B)== isinstance(x,C)==isinstance(y,B))
#print(isinstance(y,C))
#print(5/4)
#x = 5
#y = 4
#print(x.__truediv__(y))
#print(x.__div__(y))

## EXCEPTIONS ----

#L=[1,2,3]
#try:
 #   print(L[43])
#except IndexError:
 #   print("Fuck it, i'm prison mike")

#n=len(L)
#s=sum(L)
#print(float(s)/n) 
#print(len(L))

#def compute_average(L):
 #   n=len(L)
  #  s=sum(L)
   # return float(s)/n # error is noticed here !!!
#mylist=[]
#while True:
 #   try:
  #      x=float(input("Give a number (non-number quits): "))
   #     mylist.append(x)
    #except ValueError:
     #   break
#try:
 #   average=compute_average(mylist)
  #  print("Average is", average)
#except ZeroDivisionError:
    # and the error is handled here
 #   if len(mylist) == 0:
  #      print("Tried to compute the average of empty list of numbers")
   # else:
    #    print("Something strange happened")

s = "abd 123 1.2 test 13.2 -1".split(" ")
ls = []

for i in s:

    if len(re.findall(r'[-]?\b[\d]+\b', i)) == 1: # if it is an integer
        #print(re.findall(r'\b[\d]+\b', i)[0]) # print integers
        ls.append(re.findall(r'[-]?\b[\d]+\b', i)[0])
        #print(type(re.findall(r'\b[\d]+\b', i)[0]))
    elif len(re.findall(r'[-]?\b[\d]+\b', i)) > 1:
        #print(".".join(re.findall(r'\b[\d]+\b', i)))
        ls.append(".".join(re.findall(r'\b[\d]+\b', i)))
        #print(re.findall(r'\b[\d]+\b', i))
        # join the numbers by a point # but where should i put the point
    else:
       continue
print(ls)
    