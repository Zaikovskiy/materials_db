import sqlite3
import random

conn = sqlite3.connect('database.db')
cur = conn.cursor()

materials_for_printers = {
    1: {
        'main': ['ABS Standart', 'ABS GF-4', 'Titan GF-12', 'FormaX', 'ABS Standart'],
        'additional': ['PETG', 'HIPS', 'PETG', 'HIPS', 'PETG']
    },
    2: {
        'main': ['ABS/PA', 'PA66 GF-30', 'UltraX', 'TERMAX GF-40','UltraX'],
        'additional': ['PLA', 'PVA', 'PLA', 'PVA', 'PLA']
    },
    3: {
        'main': ['PLA', 'PETG', 'TOTAL GF-30', 'TOTAL CF-5', 'PETG'],
        'additional': ['TPU A93', 'WAX 3D Base', 'TPU A93', 'WAX 3D Base', 'TPU A93']
    }
}

cur.execute("SELECT id FROM colors")
colors = [color[0] for color in cur.fetchall()]

for printer_id, materials in materials_for_printers.items():
    for type, material_names in materials.items():
        for i, material_name in enumerate(material_names, start=1 if type == 'main' else 6):
            cur.execute("SELECT id FROM materials WHERE name = ?", (material_name,))
            material_id = cur.fetchone()

            if material_id is None:
                print(f"Материал {material_name} не найден в таблице 'materials'.")
                continue

            material_id = material_id[0]
            color_id = random.choice(colors)

            cur.execute(
                "INSERT INTO materialsInPrinters (idPrinter, idMaterial, cell, idColor, idPackage, materialQuantity, period) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (printer_id, material_id, i, color_id, 4, 1000, '2023-06-06 14:15:06')
            )

conn.commit()
cur.close()
conn.close()
