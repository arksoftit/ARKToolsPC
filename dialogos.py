# dialogos.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHeaderView, QTableWidget, QTableWidgetItem, QLineEdit, QLabel
from PySide6.QtCore import Qt

class BuscadorBaseDialog(QDialog):
    """Clase base para todos los buscadores tipo 'Lupa' de ArkToolsPC."""
    def __init__(self, db_manager, titulo, sql_base, columnas):
        super().__init__()
        self.db_manager = db_manager
        self.sql_base = sql_base
        self.columnas = columnas # Lista de nombres para las cabeceras
        
        self.id_seleccionado = None
        self.nombre_seleccionado = None
        
        self.setWindowTitle(titulo)
        self.setMinimumSize(500, 400)
        
        # Layout principal
        layout = QVBoxLayout(self)
        
        # Instrucciones y Buscador
        layout.addWidget(QLabel(f"Buscar en {titulo}:"))
        self.txt_buscar = QLineEdit()
        self.txt_buscar.setPlaceholderText("Escriba para filtrar...")
        self.txt_buscar.textChanged.connect(self.cargar_datos)
        layout.addWidget(self.txt_buscar)
        
        # Tabla de resultados
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(len(columnas))
        self.tabla.setHorizontalHeaderLabels(columnas)
        self.tabla.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.cellDoubleClicked.connect(self.seleccionar_y_cerrar)
        layout.addWidget(self.tabla)
        
        self.cargar_datos()

    def cargar_datos(self):
        filtro = self.txt_buscar.text().strip()
        sql = self.sql_base
        
        # Nota: El filtrado dinámico es complejo si el SQL es genérico.
        # Por ahora, ejecutamos el SQL base.
        datos = self.db_manager.fetch_data(sql)
        
        self.tabla.setRowCount(0)
        
        if datos:
            for fila in datos:
                pos = self.tabla.rowCount()
                self.tabla.insertRow(pos)
                
                # 'fila' es un objeto sqlite3.Row. 
                # Podemos convertirlo a lista o iterar sobre él directamente.
                for i in range(len(fila)):
                    if i < self.tabla.columnCount():
                        valor = fila[i]
                        self.tabla.setItem(pos, i, QTableWidgetItem(str(valor)))

    def seleccionar_y_cerrar(self, row, column):
        # 1. El ID siempre lo tomamos de la columna 0
        self.id_seleccionado = int(self.tabla.item(row, 0).text())
        
        # 2. El nombre para el lineEdit (Código) está en la columna 1
        self.nombre_seleccionado = self.tabla.item(row, 1).text()
        
        # 3. La descripción (para mostrar en el formulario) está en la columna 2
        # Verificamos si existe la columna 2 para no dar error
        if self.tabla.columnCount() > 2:
            self.valor_adicional = self.tabla.item(row, 2).text()
        else:
            self.valor_adicional = self.nombre_seleccionado
            
        self.accept()