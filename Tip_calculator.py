# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:13:46 2021

@author: SRI
"""

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print('Welcome! to the tip calculator!!')

total_bill = float(input('Enter the bill amount: \n$ '))

people = int(input ('enter the no. of bill for lunch: \n'))

tip = int(input('Enter the tip % 10,12 or 15 : \n'))

bill_with_tip = (total_bill*tip/100)+total_bill

per_person = bill_with_tip/people
per_person_format = "{:.2f}".format(per_person)

print(f'Total bill each person needs to be pay: ${per_person_format}')

    