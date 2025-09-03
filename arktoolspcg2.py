import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QSizeGrip, QMessageBox
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint
from PySide6.QtGui import QPixmap
from ui_arktoolspcg2 import Ui_MainWindow
import system_info
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
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
        # Conectar el botón de Sistema
        self.ui.btn_info_so.clicked.connect(self.mostrar_info_os)
        # Conectar el botón de Configuración Regional
        self.ui.btn_info_regional.clicked.connect(self.mostrar_info_regional)
        # Conectar el botón de Placa Base (Motherboard)
        self.ui.btn_info_mbd.clicked.connect(self.mostrar_info_mbd)
        # Conectar el botón de CPU
        self.ui.btn_info_cpu.clicked.connect(self.mostrar_info_cpu_hw)
        # Conectar el botón de GPU
        self.ui.btn_info_gpu.clicked.connect(self.mostrar_info_gpu)
        # Conectar el botón de RAM
        self.ui.btn_info_ram.clicked.connect(self.mostrar_info_ram)
        # Conectar el botón de HDD
        self.ui.btn_info_hdd.clicked.connect(self.mostrar_info_hdd)
        # Conectar el botón de NIC
        self.ui.btn_info_nic.clicked.connect(self.mostrar_info_nic)
        # Conectar el botón de COM
        self.ui.btn_info_com.clicked.connect(self.mostrar_info_com)
        # Conectar el botón de Bluetooth
        self.ui.btn_info_bth.clicked.connect(self.mostrar_info_bth)
        # Conectar el botón de Audio
        self.ui.btn_info_audio.clicked.connect(self.mostrar_info_audio)
        # Conectar el botón de Sistema General
        self.ui.btn_info_sistema.clicked.connect(self.mostrar_info_sistema_gen)
        # Conectar el botón de USB
        self.ui.btn_info_usb.clicked.connect(self.mostrar_info_usb)
        # Mostrar la página de inicio al iniciar la aplicación        
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio)
        # Conectar el botón de limpiar textos
        self.ui.btn_limpiar.clicked.connect(self.limpiar_textos)
        # Conectar el botón de regresar al menú principal
        self.ui.btn_regresar_menu.clicked.connect(self.volver_menu_principal)
        # Conectar el botón de Configuración
        self.ui.btn_config.clicked.connect(self.mostrar_inf_config)
        # Conectar el botón de Configuración Regional
        self.ui.btn_cambio_regional.clicked.connect(self.aplicar_config_regional)
        # Conectar el botón de Herramientas
        #self.ui.btn_config_tools.clicked.connect(self.mostrar_info_regional)
        

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

    # ------------------ MOSTRAR MENSAJE DE CONFIRMACIÓN ------------------
    def show_notification(self, title, message, is_error=False):
        """
        Muestra un mensaje informativo o de error al usuario.
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
        Muestra un mensaje de confirmación antes de ejecutar una acción.
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
            except Exception as e:
                self.show_notification("Error", f"No se pudo aplicar la configuración: {e}", is_error=True)

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
    
    def limpiar_textos(self):
        """
        Limpia el contenido de todos los QTextEdit en las páginas relevantes.
        """
        self.ui.textEdit_info_red.clear()
        self.ui.textEdit_info_so.clear()
        self.ui.textEdit_info_regional.clear()
        self.ui.textEdit_info_hw.clear()
        self.ui.textEdit_info_config.clear()
        
        # Vuelve a la página de inicio
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio)
    
    # ------------------ MOSTRAR INFORMACIÓN DE RED ------------------
    
    def mostrar_info_red(self):
        """
        Muestra la información de la Red en textEdit_info_hw y cambia la imagen.
        """
        info_red = system_info.get_network_info()
        self.ui.textEdit_info_red.setText(info_red)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_red)
        
    # ------------------ MOSTRAR INFORMACIÓN DEL SISTEMA OPERATIVO ------------------
    
    def mostrar_info_os(self):
        """
        Muestra la información del Sistema Operativo en textEdit_info_hw y cambia la imagen.
        """
        info_os = system_info.get_os_info()
        self.ui.textEdit_info_so.setText(info_os)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_so)

    # ------------------ MOSTRAR INFORMACIÓN REGIONAL ------------------

    def mostrar_info_regional(self):
        """
        Muestra la información Regional en textEdit_info_hw y cambia la imagen.
        """
        info_regional = system_info.get_regional_settings()
        self.ui.textEdit_info_regional.setText(info_regional)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_regional)
    
    def mostrar_info_mbd(self):
        """
        Muestra la información de la placa base en textEdit_info_hw y cambia la imagen.
        """
        self.ui.textEdit_info_hw.clear()
        pixmap_mbd = QPixmap("imagen/mbd_02.png")
        self.ui.label_info_hw.setPixmap(pixmap_mbd)
        info_mbd = system_info.get_motherboard_info()
        self.ui.textEdit_info_hw.setText(info_mbd)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_hardware)

    def mostrar_info_cpu_hw(self):
        """
        Muestra la información de la CPU en textEdit_info_hw y cambia la imagen.
        """
        self.ui.textEdit_info_hw.clear()
        pixmap_cpu = QPixmap("imagen/cpu02.svg")
        self.ui.label_info_hw.setPixmap(pixmap_cpu)
        info_cpu = system_info.get_cpu_info()
        self.ui.textEdit_info_hw.setText(info_cpu)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_hardware)
    
    def mostrar_info_gpu(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_gpu = QPixmap("imagen/Grafica01.svg")
        self.ui.label_info_hw.setPixmap(pixmap_gpu)
        info_gpu = system_info.get_gpu_info()
        self.ui.textEdit_info_hw.setText(info_gpu)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_hardware)

    def mostrar_info_ram(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_ram = QPixmap("imagen/Ram01.svg")
        self.ui.label_info_hw.setPixmap(pixmap_ram)
        info_ram = system_info.get_ram_info()
        self.ui.textEdit_info_hw.setText(info_ram)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_hardware)

    def mostrar_info_hdd(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_hdd = QPixmap("imagen/hdd03.svg")
        self.ui.label_info_hw.setPixmap(pixmap_hdd)
        info_hdd = system_info.get_disk_info()
        self.ui.textEdit_info_hw.setText(info_hdd)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_hardware)
        
    def mostrar_info_nic(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_nic = QPixmap("imagen/nic01.svg")
        self.ui.label_info_hw.setPixmap(pixmap_nic)
        info_nic = system_info.get_nic_info()
        self.ui.textEdit_info_hw.setText(info_nic)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_hardware)

    def mostrar_info_com(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_com = QPixmap("imagen/com02.svg")
        self.ui.label_info_hw.setPixmap(pixmap_com)
        info_com = system_info.get_com_ports()
        self.ui.textEdit_info_hw.setText(info_com)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_hardware)
        
    def mostrar_info_bth(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_bth = QPixmap("imagen/bluetooth02.svg")
        self.ui.label_info_hw.setPixmap(pixmap_bth)
        info_bth = system_info.get_bluetooth_devices()
        self.ui.textEdit_info_hw.setText(info_bth)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_hardware)

    def mostrar_info_audio(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_audio = QPixmap("imagen/audio01.svg")
        self.ui.label_info_hw.setPixmap(pixmap_audio)
        info_audio = system_info.get_audio_devices()
        self.ui.textEdit_info_hw.setText(info_audio)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_hardware)

    def mostrar_info_sistema_gen(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_sistema = QPixmap("imagen/sys01.svg")
        self.ui.label_info_hw.setPixmap(pixmap_sistema)
        info_sistema = system_info.get_system_info()
        self.ui.textEdit_info_hw.setText(info_sistema)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_hardware)
        
    def mostrar_info_usb(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_usb = QPixmap("imagen/usb03.svg")
        self.ui.label_info_hw.setPixmap(pixmap_usb)
        info_usb = system_info.get_usb_devices()
        self.ui.textEdit_info_hw.setText(info_usb)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_hardware)
    
    def mostrar_inf_config(self):
        """
        Muestra la página de configuración del sistema.
        """
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inf_config)
        
    def aplicar_config_regional(self):
        """
        Llama al método de confirmación antes de aplicar la configuración regional.
        """
        logging.info("Se ha solicitado cambiar la configuración regional.")
        # Define una función anónima (lambda) para la acción.
        # Esta es la función que confirm_action ejecutará si el usuario dice "Sí".
        accion_a_ejecutar = lambda: self.ejecutar_cambios_y_notificar()
        
        # Llama a la función de confirmación, pasando el mensaje y la acción
        self.confirm_action(
            "Confirmar Configuración",
            "¿Estás seguro de que quieres aplicar la nueva configuración regional? Esto puede requerir reiniciar algunas aplicaciones para que los cambios surtan efecto.",
            accion_a_ejecutar
        )

    def ejecutar_cambios_y_notificar(self):
        """
        Esta función realiza los cambios y notifica el resultado.
        Es llamada por confirm_action después de que el usuario confirma.
        """
        try:
            logging.info("Iniciando proceso de cambio de configuración regional.")
            
            # Limpiar el área de texto inicialmente
            self.ui.textEdit_info_config.clear()
            self.ui.textEdit_info_config.setText("Aplicando la configuración regional. Por favor, espera...")
            
            # Aplicar los cambios regionales
            resultado = system_info.set_regional_settings()
            
            # Concatenar el resultado al contenido existente
            contenido_actual = self.ui.textEdit_info_config.toPlainText()
            nuevo_contenido = f"{contenido_actual}\n{resultado}"
            
            # Agregar mensajes adicionales si la operación fue exitosa
            if "✅" in resultado:
                advertencia_permisos = (
                    "\n\n⚠️ ADVERTENCIA: La modificación del Registro requiere permisos elevados. "
                    "Asegúrate de que la aplicación se ejecute como administrador para evitar errores."
                )
                mensaje_reinicio = (
                    "\n\nℹ️ INFORMACIÓN: Algunos cambios en la configuración regional pueden requerir reiniciar "
                    "aplicaciones o incluso el sistema para que surtan efecto."
                )
                nuevo_contenido += advertencia_permisos + mensaje_reinicio
                
                logging.info("Configuración regional actualizada correctamente.")
                self.show_notification("Éxito", "La configuración regional ha sido actualizada correctamente.")
            else:
                logging.error(f"Error al actualizar la configuración regional: {resultado}")
                self.show_notification("Error", "Ocurrió un error al actualizar la configuración.", is_error=True)
            
            # Actualizar el contenido del QTextEdit
            self.ui.textEdit_info_config.setText(nuevo_contenido)
        
        except Exception as e:
            logging.error(f"Excepción no manejada: {e}")
            self.show_notification("Error", f"Ocurrió un error inesperado: {e}", is_error=True)
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec())