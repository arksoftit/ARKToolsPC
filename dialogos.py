# dialogos.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHeaderView, QTableWidget, QTableWidgetItem, QLineEdit
from PySide6.QtCore import Qt
import logging

class BuscadorBaseDialog(QDialog):
    def __init__(self, db_manager, titulo, sql_base, columnas):
        super().__init__()
        self.db_manager = db_manager
        self.sql_base = sql_base
        self.columnas = columnas          # Nombres de las columnas para los encabezados
        self.datos_originales = []        # Almacena todos los registros sin filtrar
        self.id_seleccionado = None
        self.texto_combinado = None

        self.setWindowTitle(titulo)
        self.setMinimumSize(500, 400)

        layout = QVBoxLayout(self)

        # Campo de búsqueda
        self.txt_buscar = QLineEdit()
        self.txt_buscar.setPlaceholderText("🔍 Escriba para filtrar...")
        self.txt_buscar.textChanged.connect(self.filtrar_datos)
        layout.addWidget(self.txt_buscar)

        # Tabla de resultados
        self.tabla = QTableWidget()
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.cellDoubleClicked.connect(self.seleccionar_y_cerrar)
        layout.addWidget(self.tabla)

        # Cargar datos iniciales
        self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self):
        """Carga todos los registros de la BD y los guarda en memoria."""
        self.datos_originales = self.db_manager.fetch_data(self.sql_base)
        self.mostrar_datos_en_tabla(self.datos_originales)

    def mostrar_datos_en_tabla(self, datos):
        """Llena la tabla con la lista de filas (cada fila es sqlite3.Row o tupla)."""
        if not datos:
            self.tabla.setRowCount(0)
            self.tabla.setColumnCount(len(self.columnas))
            self.tabla.setHorizontalHeaderLabels(self.columnas)
            return

        num_filas = len(datos)
        num_cols = len(self.columnas)
        self.tabla.setRowCount(num_filas)
        self.tabla.setColumnCount(num_cols)
        self.tabla.setHorizontalHeaderLabels(self.columnas)

        for i, fila in enumerate(datos):
            for j in range(num_cols):
                # Soporta tanto sqlite3.Row (acceso por índice) como tuplas/listas
                valor = fila[j] if hasattr(fila, '__getitem__') else fila[j]
                self.tabla.setItem(i, j, QTableWidgetItem(str(valor)))

        self.tabla.resizeColumnsToContents()

    def filtrar_datos(self):
        """Filtra los datos en memoria según el texto ingresado y actualiza la tabla."""
        texto = self.txt_buscar.text().strip().lower()
        if not texto:
            self.mostrar_datos_en_tabla(self.datos_originales)
            return

        filtrados = []
        for fila in self.datos_originales:
            # Construir un string con todas las columnas de la fila
            valores = [str(fila[i]) for i in range(len(self.columnas)) if i < len(fila)]
            texto_fila = " ".join(valores).lower()
            if texto in texto_fila:
                filtrados.append(fila)

        self.mostrar_datos_en_tabla(filtrados)

    def seleccionar_y_cerrar(self, row, column):
        """Toma el ID (columna 0) y construye el texto combinado (col1 - col2 - ...)."""
        self.id_seleccionado = int(self.tabla.item(row, 0).text())
        partes = []
        for c in range(1, self.tabla.columnCount()):
            item = self.tabla.item(row, c)
            if item is not None and item.text():
                partes.append(item.text())
        self.texto_combinado = " - ".join(partes)
        self.accept()