import sqlite3
# Вывод записей из каждой таблицы
# Подключение к базе данных
conn = sqlite3.connect('database.db')

# Получение списка таблиц в базе данных
tables_query = "SELECT name FROM sqlite_master WHERE type='table'"
tables = conn.execute(tables_query).fetchall()

# Вывод записей из каждой таблицы
for table in tables:
    table_name = table[0]
    print("Таблица:", table_name)

    # Получение списка столбцов таблицы
    columns_query = f"PRAGMA table_info({table_name})"
    columns = conn.execute(columns_query).fetchall()

    # Формирование строки с названиями столбцов
    column_names = [column[1] for column in columns]
    columns_string = ", ".join(column_names)
    print("Названия столбцов:", columns_string)

    # Получение всех записей из таблицы
    select_query = f"SELECT * FROM {table_name}"
    rows = conn.execute(select_query).fetchall()

    # Вывод записей
    for row in rows:
        print(row)

    print("\n")

# Закрытие соединения с базой данных
conn.close()