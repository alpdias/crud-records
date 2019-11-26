# imported libraries
import os
import pymysql
from time import sleep
from datetime import date
# functions
def returnConnection():
    connection = pymysql.connect(
        host = 'localhost',
        database = 'customers',
        user = 'root',
        passwd = '',
    )
    cursor = connection.cursor()
    return cursor


# main program
print('')
print('customer base')
print('')
menu = ['customers', 'search', 'include', 'changes', 'export']
for index, listItems in enumerate(menu):
    print(f'[{index + 1}] {listItems}')
print('[0] to quit')
print('')
selectOption = int(input('select an option: '))
# customers
if selectOption == 1:
    print('')
    print('list of registered records')
    print('')
    cursor = returnConnection()
    result = cursor.execute('SELECT * FROM registration')
    for result in cursor:
        print(result)
#search

# include
if selectOption == 3:
    print('')
    print('to add a new record')
    print('')
    numberID = int(input('ID: '))
    company = str(input('Company Name: '))
    register = str(input('Registration Number: '))
    tax = str(input('Tax: '))
    email = str(input('E-mail: '))
    telephone = str(input('Phone Number: '))
    office = str(input('Office Address: '))
    situation = str(input('Current Situation: '))

#changes

#export

print('')
