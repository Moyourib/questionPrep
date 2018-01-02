#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 00:00:42 2017

@author: moyouribhattacharjee
"""
#Problem Set 1

#Part A
#
annual_salary = float(input("What is your current annual salary?: "))
portion_saved = float(input("What % would you like to put aside in savings? (please enter a decimal between 0 and 1): "))
total_cost = float(input("How much does your dream home cost? (enter the cost with no commas: "))

portion_down_payment = 0.25 #default down payment is 25% of home cost
current_savings = 0 #default will start at zero
r = 0.04 #default annual return on savings
month_counter = 0

if annual_salary == 0: #check to make sure salary is zero, else infinite loops
    print("Your salary is not conducive to getting your dream house. Get a job.")
else:
    limit = total_cost*portion_down_payment
    while current_savings < limit:
        current_savings = current_savings + (((current_savings*r)/12) + ((annual_salary/12)*portion_saved)) #how much you add/month
        month_counter = month_counter + 1
    print("It will take you", month_counter, "months to get your dream house's down payment!")

#Part B

annual_salary = float(input("What is your current annual salary?: "))
semi_annual_raise = float(input("What is your semi annual raise(as a decimal): "))
portion_saved = float(input("What % would you like to put aside in savings? (please enter a decimal between 0 and 1): "))
total_cost = float(input("How much does your dream home cost? (enter the cost with no commas: "))

portion_down_payment = 0.25 #default down payment is 25% of home cost
current_savings = 0 #default will start at zero
r = 0.04 #default annual return on savings
month_counter = 0

if annual_salary == 0: #check to make sure salary is zero, else infinite loops
    print("Your salary is not conducive to getting your dream house. Get a job.")
else:
    limit = total_cost*portion_down_payment
    while current_savings < limit:
        current_savings = current_savings + (((current_savings*r)/12) + ((annual_salary/12)*portion_saved)) #how much you add/month
        month_counter = month_counter + 1
        if month_counter%6 == 0:
            annual_salary = annual_salary*(1.0+semi_annual_raise)
    print("It will take you", month_counter, "months to get your dream house's down payment!")

#Part C

annual_salary = float(input("What is your current annual salary?: "))
#pseudocode!



print("It will take you", month_counter, "months to get your dream house's down payment!")
