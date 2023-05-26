import sqlite3
# создает insert скрипты для всех таблиц в бд
# Подключение к базе данных
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Получение списка таблиц
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()

with open('output.txt', 'w', encoding='utf-8') as f:  # Указываем кодировку 'utf-8'
    for table in tables:
        table = table[0]
        c.execute(f"PRAGMA table_info({table})")
        columns_info = c.fetchall()

        # исключаем id из списка столбцов
        columns = ', '.join([info[1] for info in columns_info if info[1] != 'id'])

        c.execute(f"SELECT * FROM {table}")
        rows = c.fetchall()

        values_list = []
        for row in rows:
            # Делаем преобразование, чтобы правильно обрабатывать строковые значения и None
            # исключаем первое значение (id) из строки
            row = list(row)[1:]
            # обрабатываем столбцы composite и markingDeletion
            for i, value in enumerate(row):
                if columns_info[i+1][1] == 'composite' or columns_info[i+1][1] == 'markingDeletion':
                    if value == 1:
                        row[i] = "true"
                    elif value == 0:
                        row[i] = "false"

            values = '(' + ', '.join(['NULL' if value is None else f"'{value}'" if isinstance(value, str) else str(value) for value in row]) + ')'
            values_list.append(values)

        all_values = ', '.join(values_list)

        if all_values:
            f.write(f"INSERT INTO public.\"{table}\" ({columns}) VALUES {all_values};\n")

# Закрытие соединения с базой данных
conn.close()
