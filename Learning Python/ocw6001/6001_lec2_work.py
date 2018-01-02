#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:47:34 2017

@author: moyouribhattacharjee
"""

## EXAMPLE: strings - put into notes
## EXAMPLE: output - put into notes
## EXAMPLE: input - put into notes 
## EXAMPLE: conditionals/branching 

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x / y is", x/y)
elif x < y:
    print("x is smaller")
elif x > y:
    print("y is smaller")
print("thanks!")

## EXAMPLE: remainder 

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")

## EXAMPLE: while loops 
## Try expanding this code to show a sad face if you go right
## twice and flip the table any more times than that. 
## Hint: use a counter

n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
while n == "right" or n == "Right":
    n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
print("\nYou got out of the Lost Forest!\n\o/")

#n = 0
#while n < 5:
#    print(n)
#    n = n+1

## EXAMPLE: for loops

#for n in range(5):
#    print(n)

#mysum = 0
#for i in range(10):
#    mysum += i
#print(mysum)

#mysum = 0
#for i in range(7, 10):
#    mysum += i
#print(mysum)

#mysum = 0
#for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#        mysum += 1
#print(mysum)

## EXAMPLE: perfect squares

#ans = 0
#neg_flag = False
#x = int(input("Enter an integer: "))
#if x < 0:
#    neg_flag = True
#while ans**2 < x:
#    ans = ans + 1
#if ans**2 == x:
#    print("Square root of", x, "is", ans)
#else:
#    print(x, "is not a perfect square")
#    if neg_flag:
#        print("Just checking... did you mean", -x, "?")


## TEST YOURSELF!
## Modify the perfect squares example to print 
## imaginary perfect sqrts if given a negative num.
