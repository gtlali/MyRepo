# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:19:19 2020

@author: HY3798
"""
m, t = 1, 2  # multiple values can be assigned

def my_function(y,r):
  print("Hello from a my_function") 
  print(y, r," this method will compute a*c + 10 " )
  x = lambda a,c : a *c+ 10  
  print("value of expersion (a*c)+10: ",x(y,r))  
    
def my_while(j):
  print("Hello from a my_while",j) 
  i = j
  while i < 6:
    print(i)
    i += 1
