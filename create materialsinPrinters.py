import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('database.db')

# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Создание таблицы materialsInPrinters
cursor.execute('''
    CREATE TABLE IF NOT EXISTS materialsInPrinters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        idPrinter INTEGER,
        idMaterial INTEGER,
        cell INTEGER,
        idColor INTEGER,
        idPackage INTEGER,
        materialQuantity NUMERIC(5, 1),
        period TIMESTAMP
    )
''')

# Сохранение изменений и закрытие соединения с базой данных
conn.commit()
conn.close()