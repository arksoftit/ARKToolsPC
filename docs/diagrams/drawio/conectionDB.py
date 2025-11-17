import os
import sqlite3

db_path = os.path.join("arktooldatabase", "ArkToolsDB.sqlite")

if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    # Aquí podrías ejecutar el script SQL desde un archivo externo
    conn.close()