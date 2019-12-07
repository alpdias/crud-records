'''
@Autor: Paulo https://github.com/alpdias
'''
# imported libraries
import os
import pymysql
from time import sleep
from datetime import date

# connection
try:
    connection = pymysql.connect(host = 'localhost', database = 'people', user = 'root', passwd = '')
    cursor = connection.cursor()
    print('connection established')
    established = 1
except:
    print('')
    print('error connecting database')
    established = 0

if established == 1:

    # main program
    print('')
    print('CRUD - Records List')
    print('')
    menu = ['records list', 'records search', 'add new record', 'change record', 'delete record', 'export table', 'import table']
    for index, listItems in enumerate(menu):
        print(f'[{index + 1}] {listItems}')
    print('[0] exit the program')
    print('')
    selectOption = int(input('select an option to perform: '))

    # records list
    if selectOption == 1:
        print('')
        print('record list')
        print('')
        result = cursor.execute('SELECT * FROM people')
        for result in cursor:
            print(result)

    # records search
    if selectOption == 2:
        print('')
        searchRecord = int(input('select ID to search: '))
        print('')
        searchID = cursor.execute(f'SELECT * FROM people WHERE id = {searchRecord}')
        connection.commit()
        resultSearch = cursor.fetchone()
        if resultSearch == None:
            print('record not found see record list')
        else:
            print(resultSearch)

    # add new record
    if selectOption == 3:
        print('')
        print('fill in to add a new record')
        print('')
        numberID = str(input('ID (empty to self fill):  '))
        fullName = str(input('full Name: '))
        profession = str(input('profession: '))
        birth = str(input('birth [yyyy-mm-dd]: '))
        genre = str(input('genre [M/F]: '))
        bodyweight = str(input('body Weight: '))
        height = str(input('height: '))
        nationality = str(input('nationality: '))
        try:
            cursor.execute("INSERT INTO people (id, fullname, profession, birth, genre, bodyweight, height, nationality)   \
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (numberID, fullName, profession, birth, genre, bodyweight, height, nationality))
            connection.commit()
            print('')
            print('successful inclusion')
        except:
            print('')
            print('not done inclusion, check your input or connection')

    # change record
    if selectOption == 4:
        print('')
        print('select ID to change a record')
        print('')
        changeID = int(input('ID to change: ')) # add except to 'None' result in SQL
        print('')
        listOptions = ['id', 'fullname', 'profession', 'birth', 'genre', 'bodyweight', 'height', 'nationality']
        for index, listItems in enumerate(listOptions):
            print(f'[{index + 1}] {listItems}')
        print('')
        changeColumn = int(input('select the column number you wish to modify: '))
        if changeColumn == 1:
            changeColumn = 'id'
        elif changeColumn == 2:
            changeColumn = 'fullname'
        elif changeColumn == 3:
            changeColumn = 'profession'
        elif changeColumn == 4:
            changeColumn = 'birth'
        elif changeColumn == 5:
            changeColumn = 'genre'
        elif changeColumn == 6:
            changeColumn = 'bodyweight'
        elif changeColumn == 7:
            changeColumn = 'height'
        elif changeColumn == 8:
            changeColumn = 'nationality'
        newChange = str(input('new value: '))
        try:
            changeModify = cursor.execute(f"UPDATE people SET {changeColumn} = '{newChange}' WHERE id = {changeID}")
            connection.commit()
            print('')
            print('successful modification')
        except:
            print('')
            print('error trying to modify, check table or connection')

    # delete record
    if selectOption == 5:
        print('')
        print('select ID to delete a record')
        print('')
        deleteID = int(input('ID to delete: '))
        deletedID = cursor.execute(f'SELECT * FROM people WHERE id = {deleteID}')
        print('')
        print('selected record:')
        print('')
        print(cursor.fetchone()) # add except to 'None' result in SQL
        print('')
        confirmDelete = str(input('Do you really want to delete this record? [Y/N] ')).strip().upper()
        if confirmDelete == 'Y':
            try:
                deletedID = cursor.execute(f'DELETE FROM people WHERE id = {deleteID}')
                connection.commit()
                print('')
                print('successfully deleted record, see list of records to view')
            except:
                print('')
                print('error deleting record, check input or connection')

    # export table

    # import table

elif established == 0:
    print('check database connection and try again')

print('')
