import sqlite3

# установите соединение с базой данных
conn = sqlite3.connect('database.db')

cur = conn.cursor()

# данные для вставки
data = (83, 'Titan GF-12', 1, 1, 2, 1.16, 280, 290, 110, 0, 80, 30, 99, 100, 10, 50, 10, 50, 100, 3.3, 0)

# вставьте данные в таблицу
cur.execute(
    "INSERT INTO materials (id, name, idPolymerBase, composite, idMaker, density, printingTemp, maxRadiatorTemp, "
    "tableTemp, blowingParts, chamberTemp, timeSwitchCoolingMode, coolingModeTemp, materialUnloadSpeed, "
    "materialUnloadTemp, materialUnloadLength, materialLoadSpeed, materialCleanLength, materialServeCoef, "
    "gramsCost, markingDeletion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    data
)

# закройте соединение
conn.commit()
cur.close()
conn.close()