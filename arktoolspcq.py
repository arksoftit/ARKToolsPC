# ARKToolsPC - Diagnóstico de Hardware (PyQt6)
# Desarrollado por Juan Ernesto Páez Mujica 
# Fecha: 2025-07-17 
# Versión: 1.0.6
# Este script es una aplicación de escritorio que permite obtener información detallada del hardware del sistema.

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit,
    QMenuBar, QMenu, QPushButton, QMessageBox, QLabel, QHBoxLayout, QMessageBox
)
from PyQt6.QtGui import QAction, QTextCursor, QPalette, QColor
from PyQt6.QtCore import Qt

# Importa las funciones de system_info.py (igual que en tu versión original)
from system_info import (
    get_system_info, 
    get_cpu_info, 
    get_ram_info, 
    get_disk_info,
    get_gpu_info, 
    get_motherboard_info, 
    get_network_info,
    get_nic_info, 
    get_audio_devices, 
    get_com_ports,
    get_usb_devices, 
    get_bluetooth_devices, 
    get_os_info,
    get_regional_settings,
    set_regional_settings,
    show_current_datetime,
    show_regional_and_datetime    
)

class ARKToolsPCApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ARKToolsPC - Diagnóstico de Hardware (PyQt6)")
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumSize(800, 600)

        # Configurar paleta de colores
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(240, 240, 240))  # Fondo gris claro
        palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))    # Texto negro
        palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))    # Texto blanco (para QTextEdit)
        self.setPalette(palette)
        
        # Estilos CSS
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QTextEdit {
                background-color: black;
                color: white;
                font-family: Consolas;
                font-size: 10pt;
                border: 1px solid #ccc;
            }
            QMenuBar {
                background-color: #f0f0f0;
                color: black;
            }
            QMenuBar::item {
                padding: 5px 10px;
                background: transparent;
            }
            QMenuBar::item:selected {
                background: #d0d0d0;
            }
            QMenu {
                background-color: white;
                border: 1px solid #ccc;
            }
            QMenu::item {
                color: black;
                padding: 5px 25px;
            }
            QMenu::item:selected {
                background-color: #ADD8E6;
            }
            QPushButton#exitButton {
                background-color: #ADD8E6;
                color: black;
                border: 1px solid #87CEEB;
                padding: 10px;
                font: bold 10pt "Segoe UI";
            }
            QPushButton#exitButton:hover {
                background-color: #87CEEB;
            }
            QLabel#footerLabel {
                background-color: #f0f0f0;
                color: black;
                padding: 10px;
                font: 9pt "Segoe UI";
                border-top: 1px solid #d0d0d0;
            }
        """)

        # Crear menú principal
        self.create_menu_bar()

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(10, 10, 10, 10)

        # Área de texto
        self.content_text = QTextEdit()
        self.content_text.setReadOnly(True)
        layout.addWidget(self.content_text)

        # Contenedor para botones inferiores
        button_bottom_layout = QHBoxLayout()

        # Botón de limpiar
        clear_button = QPushButton("Limpiar")
        clear_button.setFixedHeight(30)
        clear_button.clicked.connect(self.clear_content)
        button_bottom_layout.addWidget(clear_button, alignment=Qt.AlignmentFlag.AlignLeft)

        # Espaciador para separar los botones
        button_bottom_layout.addStretch()

        # Botón de salir
        exit_button = QPushButton("Salir de la Aplicación")
        exit_button.setObjectName("exitButton")
        exit_button.clicked.connect(self.close)
        button_bottom_layout.addWidget(exit_button, alignment=Qt.AlignmentFlag.AlignRight)

        # Añadir el layout de botones al layout principal
        layout.addLayout(button_bottom_layout)
        
        # Footer
        self.create_footer()

    def create_menu_bar(self):
        menubar = self.menuBar()

        # Menú: Archivo
        file_menu = menubar.addMenu("Archivo")
        file_menu.addAction("Nuevo")
        file_menu.addAction("Abrir")
        file_menu.addSeparator()
        exit_action = QAction("Salir", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Menú: Acciones
        accion_menu = menubar.addMenu("Acciones")
        accion_menu.addAction("Cambiar Configuración Regional HB", lambda: self.confirm_action(
            "Configuración Regional",
            "¿Estás seguro de aplicar estos cambios de configuración regional?",
            set_regional_settings
        ))

        # Menú: Herramientas
        tools_menu = menubar.addMenu("Herramientas")
        
        # Submenú: Hardware
        hardware_menu = tools_menu.addMenu("Información del Hardware")
        hardware_actions = [
            ("Sistema", get_system_info),
            ("CPU", get_cpu_info),
            ("Memoria RAM", get_ram_info),
            ("Disco", get_disk_info),
            ("GPU", get_gpu_info),
            ("Placa Base", get_motherboard_info),
            ("Tarjetas de Red", get_nic_info),
            ("Tarjetas de Audio", get_audio_devices),
            ("Puertos COM", get_com_ports),
            ("Dispositivos USB", get_usb_devices),
            ("Dispositivos Bluetooth", get_bluetooth_devices)
        ]
        
        for text, func in hardware_actions:
            action = QAction(text, self)
            action.triggered.connect(lambda _, f=func: self.show_content(f))
            hardware_menu.addAction(action)

        # Otras herramientas
        tools_menu.addAction("Información de Red", lambda: self.show_content(get_network_info))
        tools_menu.addAction("Información del SO", lambda: self.show_content(get_os_info))
        tools_menu.addAction("Configuración Regional", lambda: self.show_content(get_regional_settings))
        

        # Menú: Informes
        reports_menu = menubar.addMenu("Informes")
        reports_menu.addAction("Informe de Hardware", lambda: self.show_placeholder("Informe de Hardware"))

        # Menú: Ayuda
        help_menu = menubar.addMenu("Ayuda")
        help_menu.addAction("Acerca de...", self.show_about)
        
    def show_notification(self, title, message, is_error=False):
        """
        Muestra un mensaje informativo o de error al usuario
        """
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)

        if is_error:
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        else:
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        msg.exec()
        
    def confirm_action(self, title, message, action):
        """
        Muestra un mensaje de confirmación antes de ejecutar una acción
        """
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        msg.setDefaultButton(QMessageBox.StandardButton.No)

        response = msg.exec()
        if response == QMessageBox.StandardButton.Yes:
            try:
                action()  # Ejecutar la función pasada como parámetro
                self.show_content(get_regional_settings)  # Mostrar la nueva configuración inmediatamente
                self.show_content(show_current_datetime)  # Ejemplos
                self.show_content(show_regional_and_datetime) 
                self.show_notification("Acción Confirmada", "La configuración se ha actualizado correctamente.")
            except Exception as e:
                self.show_notification("Error", f"No se pudo aplicar la configuración: {e}", is_error=True)

    def show_content(self, func):
        """Muestra el resultado de una función en el área de texto"""
        import io
        import sys
        from contextlib import redirect_stdout

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            func()  # Ejecutar la función del módulo system_info

        self.content_text.clear()
        self.content_text.setPlainText(buffer.getvalue())
        self.content_text.moveCursor(QTextCursor.MoveOperation.End)
    
    def clear_content(self):
        """Limpia el área de contenido (QTextEdit)"""
        self.content_text.clear()


    def show_placeholder(self, tool_name):
        """Muestra un mensaje para herramientas no implementadas"""
        self.content_text.clear()
        self.content_text.setPlainText(f"[PENDIENTE] {tool_name} - Funcionalidad aún no implementada.")

    def show_about(self):
        """Muestra el diálogo 'Acerca de'"""
        about_text = (
            "ARKToolsPC - Diagnóstico de Hardware\n"
            "Versión: 1.0.6 (PyQt6)\n"
            "Desarrollado por: Arksoft Integradores de Sistemas, C.A.\n"
            "© 2025 Todos los derechos reservados\n\n"
            "Esta herramienta permite obtener información detallada del hardware del sistema."
        )
        QMessageBox.information(self, "Acerca de...", about_text)

    def create_footer(self):
        """Crea el pie de página con información corporativa"""
        footer = QLabel()
        footer.setObjectName("footerLabel")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setText(
            "© 2025 Arksoft Integradores de Sistemas, C.A. RIF: J310994692 - Todos los derechos reservados\n"
            "Contacto: +58 424-3672111 | arksoft.sistemas@gmail.com"
        )
        self.centralWidget().layout().addWidget(footer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Estilo consistente en todos los sistemas
    window = ARKToolsPCApp()
    window.show()
    sys.exit(app.exec())