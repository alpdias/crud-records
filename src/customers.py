# imported libraries
import os
import pymysql
from time import sleep
from datetime import date
# main program
print('')
print('customer base')
print('')
menu = ['customers', 'search', 'include', 'changes', 'export']
for index, listItems in enumerate(menu):
    print(f'[{index}] {listItems}')

'''
numberID = int(input('ID: '))
company = str(input('Company Name: '))
register = str(input('Registration Number: '))
tax = str(input('Tax: '))
email = str(input('E-mail: '))
telephone = str(input('Phone Number: '))
address = str(input('Address: '))
situation = str(input('Current Situation: '))
''' 
print('')
