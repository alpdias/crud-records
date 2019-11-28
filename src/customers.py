# imported libraries
import os
import pymysql
from time import sleep
from datetime import date

# functions
connection = pymysql.connect(host = 'localhost', database = 'customers', user = 'root', passwd = '')
cursor = connection.cursor()

# main program
print('')
print('Records Registration CRUD')
print('')
menu = ['records list', 'records search', 'add new record', 'change record', 'export table', 'import table']
for index, listItems in enumerate(menu):
    print(f'[{index + 1}] {listItems}')
print('[0] exit the program')
print('')
selectOption = int(input('select an option to perform: '))

# records list
if selectOption == 1:
    print('')
    print('list of registered records')
    print('')
    nameTable = str(input('select table to view: '))
    print('')
    result = cursor.execute(f'SELECT * FROM {nameTable}')
    for result in cursor:
        print(result)

# records search

# add new record
if selectOption == 3:
    print('')
    print('fill in to add a new record')
    print('')
    numberID = str(input('ID: '))
    company = str(input('Company Name: '))
    register = str(input('Registration Number: '))
    tax = str(input('Tax: '))
    email = str(input('E-mail: '))
    telephone = str(input('Phone Number: '))
    office = str(input('Office Address: '))
    situation = str(input('Current Situation: '))
    cursor.execute("INSERT INTO registration (id, company, register, tax, email, telephone, office, situation) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (numberID, company, register, tax, email, telephone, office, situation))
    connection.commit()

# change record

# export table

# import table

print('')
