# login_dialog.py
import sys
from PySide6.QtWidgets import QDialog, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QFont
from database_manager import DatabaseManager
import logging

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.db_manager = DatabaseManager()
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        self.setWindowTitle("Inicio de Sesión - ARKToolsPC")
        self.setFixedSize(400, 250)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # --- CENTRAL WIDGET ---
        main_widget = QLabel(self)
        main_widget.setStyleSheet("""
            QLabel {
                background-color: #2C3E50;
                border-radius: 20px;
                border: 1px solid #34495E;
            }
        """)
        main_widget.setGeometry(10, 10, 380, 230)

        # --- LAYOUT ---
        layout = QVBoxLayout(main_widget)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # --- TITLE ---
        title_label = QLabel("ARKToolsPC")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: #ECF0F1; margin-bottom: 10px;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # --- USERNAME ---
        username_layout = QHBoxLayout()
        username_label = QLabel("Usuario:")
        username_label.setStyleSheet("color: #ECF0F1; font-size: 12px;")
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("""
            QLineEdit {
                padding: 8px 10px;
                border: 1px solid #3498DB;
                border-radius: 5px;
                color: #ECF0F1;
                background-color: #34495E;
            }
            QLineEdit:focus {
                border-color: #1ABC9C;
            }
        """)
        self.username_input.setPlaceholderText("Ingresa tu nombre de usuario")
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        layout.addLayout(username_layout)

        # --- PASSWORD ---
        password_layout = QHBoxLayout()
        password_label = QLabel("Contraseña:")
        password_label.setStyleSheet("color: #ECF0F1; font-size: 12px;")
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet("""
            QLineEdit {
                padding: 8px 10px;
                border: 1px solid #3498DB;
                border-radius: 5px;
                color: #ECF0F1;
                background-color: #34495E;
            }
            QLineEdit:focus {
                border-color: #1ABC9C;
            }
        """)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Ingresa tu contraseña")
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        layout.addLayout(password_layout)

        # --- BUTTONS ---
        buttons_layout = QHBoxLayout()
        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #1ABC9C;
                color: white;
                border-radius: 5px;
                padding: 8px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #16A085;
            }
            QPushButton:pressed {
                background-color: #138D75;
            }
        """)
        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C;
                color: white;
                border-radius: 5px;
                padding: 8px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
            QPushButton:pressed {
                background-color: #A93226;
            }
        """)
        buttons_layout.addWidget(self.login_button)
        buttons_layout.addWidget(self.cancel_button)
        layout.addLayout(buttons_layout)

        # --- STATUS LABEL ---
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("color: #E74C3C; font-size: 11px;")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

    def setup_connections(self):
        self.login_button.clicked.connect(self.validate_login)
        self.cancel_button.clicked.connect(self.reject)

    def validate_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            self.show_message("Por favor, ingrese usuario y contraseña.", error=True)
            return

        # Consulta directa a la tabla ark_users
        sql = "SELECT usr_Password FROM ark_users WHERE usr_Codigo = ? AND usr_Status = 0"
        result = self.db_manager.fetch_data(sql, (username,))
        
        if result:
            stored_password = result[0]['usr_Password']
            # Comparación directa (sin hashing por ahora)
            if password == stored_password:
                logging.info(f"Login exitoso para el usuario: {username}")
                self.accept()  # Cierra el diálogo con resultado aceptado
            else:
                logging.warning(f"Intento de login fallido para usuario: {username} - Contraseña incorrecta")
                self.show_message("Usuario o contraseña incorrectos.", error=True)
        else:
            logging.warning(f"Intento de login fallido para usuario no encontrado: {username}")
            self.show_message("Usuario o contraseña incorrectos.", error=True)

    def show_message(self, message, error=False):
        self.status_label.setText(message)
        if error:
            self.status_label.setStyleSheet("color: #E74C3C; font-size: 11px;")
            # Animación de error
            self.shake_widget(self.status_label)
        else:
            self.status_label.setStyleSheet("color: #1ABC9C; font-size: 11px;")

    def shake_widget(self, widget):
        animation = QPropertyAnimation(widget, b"geometry")
        animation.setDuration(200)
        start_geom = widget.geometry()
        animation.setKeyValueAt(0, start_geom)
        animation.setKeyValueAt(0.25, start_geom.adjusted(10, 0, 10, 0))
        animation.setKeyValueAt(0.5, start_geom)
        animation.setKeyValueAt(0.75, start_geom.adjusted(-10, 0, -10, 0))
        animation.setKeyValueAt(1, start_geom)
        animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginDialog()
    if login_window.exec() == QDialog.DialogCode.Accepted:
        print("Login exitoso. Abriendo aplicación principal...")
        # Aquí se abriría la ventana principal
    else:
        print("Login fallido o cancelado.")
        sys.exit(0) # Salir de la aplicación si no se logró el login
    sys.exit(app.exec())