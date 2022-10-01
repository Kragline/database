import sqlite3


def start_base():
    global base, cursor

    base = sqlite3.connect('database.db')
    cursor = base.cursor()
    if base:
        print('Base connected!\n')

    base.execute('CREATE TABLE IF NOT EXISTS people(name, surname, age)')
    base.commit()


def sql_add():
    name = input('Enter name : ').capitalize()
    surname = input('Enter surname : ').capitalize()
    age = input('Enter age : ')

    cursor.execute('INSERT INTO people VALUES(?, ?, ?)', (name, surname, age))
    base.commit()
    print(f'{name} {surname} ({age} y.o.) was sucessfully added!')


def sql_delete():
    del_name = input('Enter name to delete : ').capitalize()
    names = cursor.execute('SELECT name FROM people WHERE name == ?', (del_name,)).fetchall()

    if len(names) == 1:
        cursor.execute('DELETE FROM people WHERE name == ?', (del_name,))
        print(f'{del_name} was sucessfully deleted!')

    elif len(names) > 1:
        del_surname = input('Enter surname to delete : ').capitalize()
        cursor.execute('DELETE FROM people WHERE name == ? AND surname == ?', (del_name, del_surname))
        print(f'{del_name} {del_surname} was sucessfully deleted!')

    else:
        print(f'No person named {del_name}')

    base.commit()


def sql_show():
    how_to_show = input('What do you want see : ').lower()
    results = cursor.execute('SELECT * FROM people').fetchall()

    if len(results) == 0:
        print('Database is empty')

    if how_to_show == 'all':
        results = cursor.execute('SELECT * FROM people').fetchall()
        for person in results:
            print(f'{person[0]} {person[1]} {person[2]} y.o.')

    elif how_to_show == 'by name':
        name = input('Enter name : ').capitalize()
        results = cursor.execute('SELECT * FROM people WHERE name == ?', (name,)).fetchall()
        for person in results:
            print(f'{person[0]} {person[1]} {person[2]} y.o.')

    elif how_to_show == 'by surname':
        surname = input('Enter surname : ').capitalize()
        results = cursor.execute('SELECT * FROM people WHERE surname == ?', (surname,)).fetchall()
        for person in results:
            print(f'{person[0]} {person[1]} {person[2]} y.o.')

    elif how_to_show == 'by age':
        age = input('Enter age : ').capitalize()
        results = cursor.execute('SELECT * FROM people WHERE age == ?', (age,)).fetchall()
        for person in results:
            print(f'{person[0]} {person[1]} {person[2]} y.o.')


def delete_base():
    base.execute('DROP TABLE IF EXISTS people')
    base.commit()
    base.close()


def main():
    start_base()

    while True:
        what_to_do = input('What do you want : ').lower()
        
        if what_to_do == 'add':
            sql_add()
        elif what_to_do == 'delete':
            sql_delete()
        elif what_to_do == 'show':
            sql_show()
        elif what_to_do == 'delete base':
            delete_base()
        elif what_to_do == 'exit':
            break
        else:
            print('Wrong command')    

if __name__ == '__main__':
    main()