'''
Created on Jul 21, 2017

@author: Mark Zeagler
'''
total = 0
curr = 0
count = 0
while curr >= 0:
    curr = int(input("Input a value (or -1 when you are finished): "))
    if curr >= 0:
        total += curr
        count += 1
average = total / count
print("The average is: ", average)