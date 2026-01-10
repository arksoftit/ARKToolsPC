# dialogos.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHeaderView, QTableWidget, QTableWidgetItem, QLineEdit, QLabel
from PySide6.QtCore import Qt

class BuscadorBaseDialog(QDialog):
    def __init__(self, db_manager, titulo, sql_base, columnas):
        super().__init__()
        self.db_manager = db_manager
        self.sql_base = sql_base
        
        self.id_seleccionado = None
        self.texto_combinado = None
        
        self.setWindowTitle(titulo)
        self.setMinimumSize(500, 400)
        
        layout = QVBoxLayout(self)
        
        self.txt_buscar = QLineEdit()
        self.txt_buscar.setPlaceholderText("Escriba para filtrar...")
        self.txt_buscar.textChanged.connect(self.cargar_datos)
        layout.addWidget(self.txt_buscar)
        
        self.tabla = QTableWidget()
        # --- MEJORA VISUAL: Ocultar números de fila ---
        self.tabla.verticalHeader().setVisible(False)
        
        self.tabla.setColumnCount(len(columnas))
        self.tabla.setHorizontalHeaderLabels(columnas)
        self.tabla.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.cellDoubleClicked.connect(self.seleccionar_y_cerrar)
        layout.addWidget(self.tabla)
        
        self.cargar_datos()

    def cargar_datos(self):
        # Por ahora cargamos el SQL tal cual viene para evitar errores de sintaxis al filtrar
        datos = self.db_manager.fetch_data(self.sql_base)
        self.tabla.setRowCount(0)
        if datos:
            for fila in datos:
                pos = self.tabla.rowCount()
                self.tabla.insertRow(pos)
                for i in range(len(fila)):
                    if i < self.tabla.columnCount():
                        self.tabla.setItem(pos, i, QTableWidgetItem(str(fila[i])))

    def seleccionar_y_cerrar(self, row, column):
        # Columna 0 siempre es el ID
        self.id_seleccionado = int(self.tabla.item(row, 0).text())
        
        # Recopilamos el resto para el "Texto Combinado" (Código - Descripción)
        partes = []
        for c in range(1, self.tabla.columnCount()):
            partes.append(self.tabla.item(row, c).text())
        
        self.texto_combinado = " - ".join(partes)
        self.accept()