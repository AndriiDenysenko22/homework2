from faker import Faker
import sqlite3
import random
faker = Faker()


def create_pers():
    con = sqlite3.connect('pers.db')
    cur = con.cursor()
    sql = '''
        CREATE TABLE IF NOT EXISTS person(
        personid INTEGER NOT NULL PRIMARY KEY,
        first_name VARCHAR(128) NOT NULL,
        last_name VARCHAR(128) NOT NULL,
        Address VARCHAR(1024) NOT NULL,
        job VARCHAR(128),
        Age INTEGER NOT NULL
        )
        '''

    cur.execute(sql)
    con.close()


def insrt():
    con = sqlite3.connect('pers.db')
    cur = con.cursor()
    for i in range(11):
        i = 0
        sql = f'''
            INSERT INTO person (first_name, last_name, Address, job, Age)  
            VALUES
                ("{faker.first_name()}", 
                "{faker.last_name()}",
                "{faker.address()}", 
                "{faker.job()}", 
                {random.randint(18,100)})            
        '''
        i += 1
        cur.execute(sql)
    con.commit()
    con.close()


def print_persons():
    con = sqlite3.connect('pers.db')
    cur = con.cursor()
    sql = '''
        SELECT personid, first_name, last_name, Address, job, Age FROM person ORDER BY personid
        '''
    person = cur.execute(sql)
    for m in person:
        print(m)
    con.close()


def delete_person_by_id(personid):
    con = sqlite3.connect('pers.db')
    cur = con.cursor()
    sql = f'''
        DELETE FROM person WHERE personid = {personid}
        '''
    cur.execute(sql)
    con.commit()
    con.close()


def update_pers_by_id(person_id):
    print('5: Update Age')
    print('4: Update job')
    print('3: Update Address')
    print('2: Update last_name')
    print('1: Update first_name')
    upd_data = input('Choose the value you wish to update: ')
    if upd_data == '1':
        new_first_name = input('Please, enter new first name: ')
        con = sqlite3.connect('pers.db')
        cur = con.cursor()
        sql = f'''
            UPDATE person
            SET first_name="{new_first_name}"
            WHERE personid = {person_id}
            '''
        cur.execute(sql)
        con.commit()
        con.close()
    elif upd_data == '2':
        new_last_name = input('Please, enter new last name: ')
        con = sqlite3.connect('pers.db')
        cur = con.cursor()
        sql = f'''
                    UPDATE person
                    SET last_name="{new_last_name}"
                    WHERE personid = {person_id}
                    '''
        cur.execute(sql)
        con.commit()
        con.close()
    elif upd_data == '3':
        new_address = input('Please, enter new Address: ')
        con = sqlite3.connect('pers.db')
        cur = con.cursor()
        sql = f'''
                    UPDATE person
                    SET Address="{new_address}"
                    WHERE personid = {person_id}
                    '''
        cur.execute(sql)
        con.commit()
        con.close()
    elif upd_data == '4':
        new_job = input('Please, enter new job: ')
        con = sqlite3.connect('pers.db')
        cur = con.cursor()
        sql = f'''
                    UPDATE person
                    SET job ="{new_job}"
                    WHERE personid = {person_id}
                    '''
        cur.execute(sql)
        con.commit()
        con.close()

    elif upd_data == '5':
        new_age = input('Please, enter new Age: ')
        con = sqlite3.connect('pers.db')
        cur = con.cursor()
        sql = f'''
                    UPDATE person
                    SET Age ="{new_age}"
                    WHERE personid = {person_id}
                    '''
        cur.execute(sql)
        con.commit()
        con.close()

    else:
        print('Wrong input')


while True:
    print('4: Update person by id')
    print('3: Delete person by id')
    print('2: Input information about 11 random persons each time')
    print('1: Create table one time')
    print('0: Exit')

    ch = int(input('Select operation: '))

    if ch == 4:
        person_id = input('Please, enter id of the person that you wish to update')
        update_pers_by_id(person_id)
        print_persons()

    if ch == 3:
        personid = input('Please, enter id of the person that you wish to delete:')
        delete_person_by_id(personid)
        print_persons()

    if ch == 2:
        insrt()
        print_persons()

    if ch == 1:
        create_pers()

    if ch == 0:
        break
