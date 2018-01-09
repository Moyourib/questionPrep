#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 00:00:42 2017

@author: moyouribhattacharjee
"""
#Problem Set 1

#Part A
#
#annual_salary = float(input("What is your current annual salary?: "))
#portion_saved = float(input("What % would you like to put aside in savings? (please enter a decimal between 0 and 1): "))
#total_cost = float(input("How much does your dream home cost? (enter the cost with no commas: "))
#
#portion_down_payment = 0.25 #default down payment is 25% of home cost
#current_savings = 0 #default will start at zero
#r = 0.04 #default annual return on savings
#month_counter = 0
#
#if annual_salary == 0: #check to make sure salary is zero, else infinite loops
#    print("Your salary is not conducive to getting your dream house. Get a job.")
#else:
#    limit = total_cost*portion_down_payment
#    while current_savings < limit:
#        current_savings = current_savings + (((current_savings*r)/12) + ((annual_salary/12)*portion_saved)) #how much you add/month
#        month_counter = month_counter + 1
#    print("It will take you", month_counter, "months to get your dream house's down payment!")

#Part B

#annual_salary = float(input("What is your current annual salary?: "))
#semi_annual_raise = float(input("What is your semi annual raise(as a decimal): "))
#portion_saved = float(input("What % would you like to put aside in savings? (please enter a decimal between 0 and 1): "))
#total_cost = float(input("How much does your dream home cost? (enter the cost with no commas: "))
#
#portion_down_payment = 0.25 #default down payment is 25% of home cost
#current_savings = 0 #default will start at zero
#r = 0.04 #default annual return on savings
#month_counter = 0
#
#if annual_salary == 0: #check to make sure salary is zero, else infinite loops
#    print("Your salary is not conducive to getting your dream house. Get a job.")
#else:
#    limit = total_cost*portion_down_payment
#    while current_savings < limit:
#        current_savings = current_savings + (((current_savings*r)/12) + ((annual_salary/12)*portion_saved)) #how much you add/month
#        month_counter = month_counter + 1
#        if month_counter%6 == 0:
#            annual_salary = annual_salary*(1.0+semi_annual_raise)
#    print("It will take you", month_counter, "months to get your dream house's down payment!")

#Part C

#pseudocode!
#ask for starting salary, and then check to see if 
#if 36 * salary < 250000, then break and print "It is not possible to pay the down payment in threee years"
#else
#get a number between 0 and 10000
#divide by 10000, to get a decimal between 0 and 1 to four decimal places
#for each rate, you go through the calculation from part b, and check to see your current savings:
#    after 36 months. if its less than down payment and greater than epsilon difference, then 
#    set decimal higher, else set decimal lower

annual_salary = float(input("What is your current annual salary?: "))

current_savings = 0
r = 0.04
semi_annual_raise = 0.07
down_payment = 250000
epsilon = 100
low = 0
high = 10000
num_guesses = 0 
month_counter = 0 

if 3 * annual_salary < 250000:
    print("It is not possible to pay the down payment in three years with your current salary")
else:  
    while abs(current_savings - down_payment) >= epsilon: 
        portion_saved = (high + low)/(2*10000)
        num_guesses += 1
        while month_counter < 36:
            current_savings = current_savings + (((current_savings*r)/12) + ((annual_salary/12)*portion_saved)) 
            if month_counter%6 == 0:
                annual_salary = annual_salary*(1.0+semi_annual_raise)
            month_counter += 1
            if current_savings < down_payment:
                low = portion_saved*10000
            if current_savings > down_payment:
                high = portion_saved*10000
        print("num_guesses =", num_guesses)
        print("you will have to put aside" , (portion_saved*100) , "percent of your salary every month to achieve the mortgage payment" ) 
