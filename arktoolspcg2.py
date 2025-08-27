import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QSizeGrip
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint
from ui_arktoolspcg2 import Ui_MainWindow

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

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Eliminar barra de título y aplicar opacidad
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)

        # SizeGrip (control para redimensionar la ventana)
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Mover ventana (con PySide6, el evento debe ser conectado a un método de la clase)
        self.ui.frame_superior.mouseMoveEvent = self.mover_ventana

        # Conectar botones de la barra superior
        self.ui.btn_minimizar.clicked.connect(self.control_bt_minimizar)
        self.ui.btn_restaurar.clicked.connect(self.control_bt_normal)
        self.ui.btn_maximizar.clicked.connect(self.control_bt_maximizar)
        self.ui.btn_cerrar.clicked.connect(lambda: self.close())
        
        # Ocultar el botón de restaurar al inicio
        self.ui.btn_restaurar.hide()

        # Conectar el botón del menú lateral
        self.ui.btn_menu.clicked.connect(self.mover_menu)

        # Conectar los botones del menú a las páginas del stackedWidget
        self.ui.btn_info_hardware.clicked.connect(self.toggle_sub_hardware_menu)
        # Conectar el botón de red
        self.ui.btn_info_red.clicked.connect(self.mostrar_info_red)
        self.ui.btn_inf_so.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_so))
        self.ui.btn_inf_regional.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_regional))
        self.ui.btn_regresar_menu.clicked.connect(self.volver_menu_principal)
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio)
        # Puedes añadir conexiones para otros botones aquí, como el de limpiar o el de configuración.
        # Por ejemplo:
        # self.ui.btn_limpiar.clicked.connect(...)
        # self.ui.btn_config.clicked.connect(...)

    def control_bt_minimizar(self):
        self.showMinimized()

    def control_bt_normal(self):
        self.showNormal()
        self.ui.btn_restaurar.hide()
        self.ui.btn_maximizar.show()

    def control_bt_maximizar(self):
        self.showMaximized()
        self.ui.btn_maximizar.hide()
        self.ui.btn_restaurar.show()

    # ------------------ MOSTRAR MENÚ DE HARDWARE ------------------
    def mover_menu(self):
        # Asegurarse de que el submenú de hardware está cerrado antes de abrir el menú principal
        self.ui.frame_sub_hardware.setMaximumWidth(0)

        width = self.ui.frame_menu.maximumWidth()
        if width == 0:
            extender = 200
        else:
            extender = 0
        
        self.animacion = QPropertyAnimation(self.ui.frame_menu, b'maximumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion.start()

    # ------------------ MOSTRAR SUBMENÚ DE HARDWARE ------------------
    def toggle_sub_hardware_menu(self):
        # Obtener el ancho actual del submenú
        current_width_sub = self.ui.frame_sub_hardware.maximumWidth()
        
        # Definir el ancho de la animación (0 para ocultar, 200 para mostrar)
        if current_width_sub == 0:
            # Si el submenú está oculto, lo mostramos y ocultamos el menú principal
            end_width_sub = 200
            end_width_menu = 0
        else:
            # Si el submenú está visible, lo ocultamos y mostramos el menú principal
            end_width_sub = 0
            end_width_menu = 200

        # Animación para el submenú
        self.animacion_sub_hardware = QPropertyAnimation(self.ui.frame_sub_hardware, b'maximumWidth')
        self.animacion_sub_hardware.setDuration(300)
        self.animacion_sub_hardware.setStartValue(current_width_sub)
        self.animacion_sub_hardware.setEndValue(end_width_sub)
        self.animacion_sub_hardware.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_sub_hardware.start()

        # Animación para el menú principal
        self.animacion_menu = QPropertyAnimation(self.ui.frame_menu, b'maximumWidth')
        self.animacion_menu.setDuration(300)
        self.animacion_menu.setStartValue(self.ui.frame_menu.maximumWidth())
        self.animacion_menu.setEndValue(end_width_menu)
        self.animacion_menu.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_menu.start()
    # ---------------------------------------------------
    
    # Función para volver al menú principal
    def volver_menu_principal(self):
        # Contrae el submenú de hardware y despliega el menú principal
        self.toggle_sub_hardware_menu()

    # SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    # Mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()

    def mover_ventana(self, event):
        if not self.isMaximized():
            if event.buttons() == Qt.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.clickPosition)
                self.clickPosition = event.globalPosition().toPoint()
                event.accept()

        if event.globalPosition().y() <= 20:
            self.showMaximized()
        else:
            self.showNormal()
    
    def mostrar_info_red(self):
        # Llama a la función del módulo system_info para obtener los datos
        info_red = get_network_info()

        # Actualiza el QTextEdit con la información
        # Asegúrate de que tu QTextEdit se llame 'textEdit_info_red' en tu UI
        self.ui.textEdit_info_red.setText(info_red)
        
        # Finalmente, cambia al QWidget correspondiente a la página de red
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_red)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec())