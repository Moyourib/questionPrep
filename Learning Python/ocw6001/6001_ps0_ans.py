#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 00:14:55 2017

@author: moyouribhattacharjee
"""
import math
import numpy

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))

type(x)
print ( "x**y = ", x**y )
print ( "log(x) with the math module = ", int(math.log(x, 2)))
print ( "log(x) with the numpy module = ", int(numpy.log2(x)))