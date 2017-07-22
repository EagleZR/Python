'''
Created on Jul 21, 2017

@author: Mark Zeagler
'''
print("A line is defined as y=mx+b")
m = int(input("Enter a value for m: "))
b = int(input("Enter a value for b: "))
x = int(input("Enter an x value to find the corresponding y-value: "))
y = m * x + b
print(y, "=", m, "(", x, ") +", b)