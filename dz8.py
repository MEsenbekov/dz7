import sqlite3

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

with sqlite3.connect('.venv/person.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Departments (DepartmentName) VALUES
        ('HR'),
        ('Engineering'),
        ('Marketing')
    ''')

    cursor.execute('''INSERT INTO Employees (FirstName, LastName, DepartmentID) VALUES
        ('John', 'Doe', 1),
        ('Jane', 'Smith', 2),
        ('Emily', 'Jones', 3)
    ''')

    conn.commit()

with sqlite3.connect('.venv/person.db') as conn:
    cursor = conn.cursor()

    department_id = int(input('Введите ID отдела (числа от 1 до 9) для получения информации: '))

    cursor.execute('''SELECT DepartmentName FROM Departments WHERE DepartmentID = ?''', (department_id,))
    department_name = cursor.fetchone()

    if department_name:
        print(f'Отдел: {department_name[0]}')

        cursor.execute('''SELECT FirstName, LastName FROM Employees WHERE DepartmentID = ?''', (department_id,))
        employees = cursor.fetchall()

        if employees:
            print('Сотрудники:')
            for emp in employees:
                print(f'{emp[0]} {emp[1]}')
        else:
            print('В этом отделе нет сотрудников.')
    else:
        print('Отдел с таким ID не найден.')

