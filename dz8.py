import sqlite3
import os

# Удаляем существующий файл базы данных, если он есть
if os.path.exists('.venv/person.db'):
    os.remove('.venv/person.db')

with sqlite3.connect('.venv/person.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        DepartmentID INTEGER NOT NULL,
        FOREIGN KEY (DepartmentID) REFERENCES Departments (DepartmentID)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Departments (
        DepartmentID INTEGER PRIMARY KEY AUTOINCREMENT,
        DepartmentName TEXT NOT NULL
    )''')

    cursor.execute('''INSERT INTO Departments (DepartmentName) VALUES
        ('HR'),
        ('Sales'),
        ('IT')
    ''')

    cursor.execute('''INSERT INTO Employees (FirstName, LastName, DepartmentID) VALUES
        ('Вася', 'Пупкин', 1),
        ('Сакиш', 'Бопуш', 2),
        ('Джеймс', 'Бонд', 3),
        ('Стервелла', 'Де Виль', 1),
        ('Странствующий', 'Торговец', 2),
        ('Мамкин', 'Программист', 3)
    ''')

    conn.commit()

with sqlite3.connect('.venv/person.db') as conn:
    cursor = conn.cursor()

    # Вывод всех сотрудников
    cursor.execute('''
        SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
        FROM Employees
        JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
    ''')

    all_employees = cursor.fetchall()

    if all_employees:
        print('Список всех сотрудников:')
        for emp in all_employees:
            print(f'{emp[0]} {emp[1]} - {emp[2]}')
    else:
        print('Сотрудников не найдено.')

    print('\n' + '-' * 40 + '\n')  # Разделитель

    # Вывод сотрудников отдела IT
    cursor.execute('''
        SELECT Employees.FirstName, Employees.LastName
        FROM Employees
        JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
        WHERE Departments.DepartmentName = 'IT'
    ''')

    it_employees = cursor.fetchall()

    if it_employees:
        print('Список всех сотрудников, работающих в отделе "IT":')
        for emp in it_employees:
            print(f'{emp[0]} {emp[1]}')
    else:
        print('В отделе "IT" нет сотрудников.')
