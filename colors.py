import pandas as pd
import sqlite3
# заполнение таблицы colors из excel
# Подключение к базе данных
conn = sqlite3.connect('database.db')

# Загрузка данных из Excel файла
df = pd.read_excel('Цвета янв. 2023.xlsx')

# Переименование столбцов
df.columns = ['id', 'name', 'additionalCleaning', 'composite', 'colorMaterialHEX', 'colorPointHEX','markingDeletion']

# Преобразование столбцов 'colorMaterialHEX', 'colorPointHEX' к верхнему регистру
df['colorMaterialHEX'] = df['colorMaterialHEX'].str.upper()
df['colorPointHEX'] = df['colorPointHEX'].str.upper()

# Замена значений в столбце 'composite' на 1 или 0
df['composite'] = df['composite'].map({'Да': 'true', 'Нет': 'false'})

# Изменение названий столбцов в датафрейме, чтобы они соответствовали названиям столбцов в таблице colors
df.columns = ['id', 'name', 'additionalCleaning', 'composite', 'colorMaterialHEX', 'colorPointHEX','markingDeletion'
]

# Загрузка обновленных данных в базу данных SQLite
df.to_sql('colors', conn, if_exists='replace', index=False)

# Commit the transaction
conn.commit()

# Закрытие соединения с базой данных
conn.close()
