import sqlite3

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('database.db')

# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Удаление всех записей из таблицы
cursor.execute('DELETE FROM materialsInPrinters') #materialsInPrinters colors  materials makers polymerBases

# Сохранение изменений и закрытие соединения с базой данных
conn.commit()
conn.close()
