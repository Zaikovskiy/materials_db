import pandas as pd
import sqlite3
import numpy as np
# заполнение таблицы materials из excel
# Подключение к базе данных
conn = sqlite3.connect('database.db')

# Загрузка данных из Excel файла
df = pd.read_excel('Материалы янв. 2023.xlsx')

# Генерация случайных значений для столбца 'gramsCost' и округление до одной десятичной цифры

# Переименование столбцов
df.columns = ['id','name', 'idPolymerBase', 'composite', 'idMaker', 'density', 'printingTemp', 'maxRadiatorTemp',
              'tableTemp', 'blowingParts', 'chamberTemp', 'timeSwitchCoolingMode', 'coolingModeTemp',
              'materialUnloadSpeed', 'materialUnloadTemp', 'materialUnloadLength', 'materialLoadSpeed',
              'materialCleanLength', 'materialServeCoef', 'gramsCost', 'markingDeletion']

# Переупорядочивание столбцов
df = df[['id','name', 'idPolymerBase', 'composite', 'idMaker', 'density', 'printingTemp', 'maxRadiatorTemp',
         'tableTemp', 'blowingParts', 'chamberTemp', 'timeSwitchCoolingMode', 'coolingModeTemp',
         'materialUnloadSpeed', 'materialUnloadTemp', 'materialUnloadLength', 'materialLoadSpeed',
         'materialCleanLength', 'materialServeCoef', 'gramsCost', 'markingDeletion']]
df['gramsCost'] = np.round(np.random.uniform(1, 3, df.shape[0]), 1)
# Замена значений в столбце 'Полимерная основа' на их соответствующие идентификаторы
polymer_query = "SELECT id FROM polymerBases WHERE name = ?"
polymer_insert_query = "INSERT INTO polymerBases (name) VALUES (?)"
df['idPolymerBase'] = df['idPolymerBase'].apply(lambda x: conn.execute(polymer_query, (x,)).fetchone()[0]
                        if conn.execute(polymer_query, (x,)).fetchone() is not None
                        else conn.execute(polymer_insert_query, (x,)).lastrowid)

conn.commit()  # Добавьте эту строку для коммита изменений

# Замена значений в столбце 'Производитель' на их соответствующие идентификаторы
maker_query = "SELECT id FROM makers WHERE shortName = ?"
maker_insert_query = "INSERT INTO makers (name, shortName) VALUES (?, ?)"
df['idMaker'] = df['idMaker'].apply(lambda x: conn.execute(maker_query, (x,)).fetchone()[0]
                        if conn.execute(maker_query, (x,)).fetchone() is not None
                        else conn.execute(maker_insert_query, (x, x)).lastrowid)

conn.commit()  # Добавьте эту строку для коммита изменений

# Замена значений в столбце 'Композит' на 1 или 0
df['composite'] = df['composite'].map({'Да': 1, 'Нет': 0})

# Изменение названий столбцов в датафрейме, чтобы они соответствовали названиям столбцов в таблице materials

df.columns = ['id','name', 'idPolymerBase', 'composite', 'idMaker', 'density', 'printingTemp', 'maxRadiatorTemp',
         'tableTemp', 'blowingParts', 'chamberTemp', 'timeSwitchCoolingMode', 'coolingModeTemp',
         'materialUnloadSpeed', 'materialUnloadTemp', 'materialUnloadLength', 'materialLoadSpeed',
         'materialCleanLength', 'materialServeCoef', 'gramsCost', 'markingDeletion']
# Загрузка обновленных данных в базу данных SQLite
df.to_sql('materials', conn, if_exists='replace', index=False)

conn.commit()  # Добавьте эту строку для коммита изменений

# Закрытие соединения с базой данных
conn.close()
