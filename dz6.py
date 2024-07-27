import sqlite3 as sq

with sq.connect('students.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user(
        fullname TEXT NOT NULL,
        birthday DATE,
        points INT
    )''')

    cursor.execute('''SELECT rowid, fullname, birthday, points FROM user''')
    print("Все студенты:", cursor.fetchall())

    cursor.execute('''SELECT rowid, fullname, birthday, points FROM user WHERE LENGTH(fullname) > 10''')
    print("Студенты с фамилией больше 10 символов:", cursor.fetchall())

    cursor.execute('''UPDATE user SET fullname = 'genius' WHERE points > 10''')
    connection.commit()

    cursor.execute('''SELECT rowid, fullname, birthday, points FROM user WHERE fullname = 'genius' ''')
    print("Студенты с именем 'genius':", cursor.fetchall())

    cursor.execute('''DELETE FROM user WHERE rowid % 2 = 0''')
    connection.commit()

    cursor.execute('''SELECT rowid, fullname, birthday, points FROM user''')
    print("Оставшиеся студенты:", cursor.fetchall())