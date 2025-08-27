# ARKToolsPC - Diagnóstico de Hardware (PyQt6)
# Desarrollado por Juan Ernesto Páez Mujica 
# Fecha: 2025-08-17 
# Versión: 1.0.7
# Configuración pantalla de prueba en PySide6 arktoolspc_gui
# Este script es una aplicación de escritorio que permite obtener información detallada del hardware del sistema.

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader # <--- Importación corregida
from PySide6.QtCore import QFile, QIODevice

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # 1. Cargas el archivo .ui de forma segura
        loader = QUiLoader()
        path = "arktoolspcg.ui"
        ui_file = QFile(path)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {path}: {ui_file.errorString()}")
            return
            
        # 2. Creas la instancia de la interfaz
        self.ui = loader.load(ui_file, self)
        ui_file.close()        
        self.resize(1000, 700)
        
        # Centrar la ventana en la pantalla
        qr = self.frameGeometry() 
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # 3. Muestras la interfaz
        self.setCentralWidget(self.ui)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())