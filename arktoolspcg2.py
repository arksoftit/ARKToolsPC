# arktoolspcg2.py es el archivo Main de la aplicación PySide6 ARKToolsPCG2

import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QSizeGrip, QMessageBox, QWidget,
                               QLineEdit, QComboBox, QTextEdit, QDateEdit, QTimeEdit)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint, QDate, QTime
from PySide6.QtGui import QPixmap
from ui_arktoolspcg2 import Ui_MainWindow
from database_manager import DatabaseManager
import system_info
from dialogos import BuscadorBaseDialog 
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

        # --- NUEVA INTEGRACIÓN DE BASE DE DATOS (Solo Inicialización) ---
        self.db_manager = DatabaseManager()
        self.db_manager.setup_database() # Crea la BD y las tablas si no existen
        logging.info("Base de datos ArkToolsBD.sqlite inicializada y tablas verificadas.")
        # -----------------------------------------------------------------
        
        # ------------INICIALIZACION DE VARIABLES PARA GESTION DE BASE DE DATOS------------
        self.id_categoria_actual = None
        
        
        # Eliminar barra de título y aplicar opacidad
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)

        # SizeGrip (control para redimensionar la ventana)
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Mover ventana (con PySide6, el evento debe ser conectado a un método de la clase)
        self.ui.frame_superior.mouseMoveEvent = self.mover_ventana
        self.ui.frame_superior.mousePressEvent = self.mousePressEvent

        # Conectar botones de la barra superior
        self.ui.btn_minimizar.clicked.connect(self.control_bt_minimizar)
        self.ui.btn_restaurar.clicked.connect(self.control_bt_normal)
        self.ui.btn_maximizar.clicked.connect(self.control_bt_maximizar)
        self.ui.btn_cerrar.clicked.connect(lambda: self.close())
        
        # Ocultar el botón de restaurar al inicio
        self.ui.btn_restaurar.hide()

        # Conectar el botón del menú lateral
        self.ui.btn_menu.clicked.connect(self.mover_menu)
        self.ui.btn_info_hardware.clicked.connect(self.toggle_sub_hardware_menu)
        self.ui.btn_operations.clicked.connect(self.toggle_operations_menu)
        
       # --- ESTADO INICIAL: DESHABILITAR FORMULARIOS ---
        self.set_form_enabled(self.ui.frm_a_company, False)
        self.set_form_enabled(self.ui.frm_actions_categories, False)
        self.set_form_enabled(self.ui.frm_actions, False)
        self.set_form_enabled(self.ui.frm_clients, False)
        self.set_form_enabled(self.ui.frm_currencies, False)
        self.set_form_enabled(self.ui.frm_device_types, False)
        self.set_form_enabled(self.ui.frm_employees, False)
        self.set_form_enabled(self.ui.frm_functional_units, False)
        self.set_form_enabled(self.ui.frm_it_assets, False)
        self.set_form_enabled(self.ui.frm_job_titles, False)
        self.set_form_enabled(self.ui.frm_requests, False)
        self.set_form_enabled(self.ui.frm_sessions, False)
        self.set_form_enabled(self.ui.frm_users, False)
    # --- VALORES POR DEFECTO: FECHA Y HORA ---
    # Esto busca todos los QDateEdit y QTimeEdit en toda la ventana y los actualiza
        for de in self.findChildren(QDateEdit):
            de.setDate(QDate.currentDate())

        for te in self.findChildren(QTimeEdit):
            te.setTime(QTime.currentTime())
        

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
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inicio)
        # Conectar el botón de limpiar textos
        self.ui.btn_limpiar.clicked.connect(self.limpiar_textos)
        # Conectar el botón de regresar al menú principal
        self.ui.btn_regresar_menu.clicked.connect(self.volver_menu_principal)
        #self.ui.btn_menu_ppal.clicked.connect(self.volver_menu_principal)
        # Conectar el botón de Configuración
        self.ui.btn_config.clicked.connect(self.mostrar_inf_config)
        # Conectar el botón de Configuración Regional
        self.ui.btn_cambio_regional.clicked.connect(self.aplicar_config_regional)
        # Conectar el botón de Herramientas
        # self.ui.btn_config_tools.clicked.connect(self.mostrar_info_regional)
        self.ui.btn_config_tools.clicked.connect(self.mostrar_configuracion)
        # Conectar el botón de Herramientas para CONSULTAR DATOS DE LA BD (Ejemplo)
        self.ui.btn_config_sql_tools.clicked.connect(self.consultar_configuracion_db)
        
        # Conexiones para formularios de gestion de datos
        self.ui.btn_ark_actions.clicked.connect(lambda: self.mostrar_pagina("page_frm_actions"))
        self.ui.btn_ark_categories.clicked.connect(lambda: self.mostrar_pagina("page_frm_actions_categories"))
        self.ui.btn_ark_clients.clicked.connect(lambda: self.mostrar_pagina("page_frm_clients"))
        # self.ui.btn_ark_company.clicked.connect(lambda: self.mostrar_pagina("page_frm_company"))
        self.ui.btn_ark_company.clicked.connect(lambda: self.mostrar_pagina("page_frm_a_company"))
        self.ui.btn_ark_currencies.clicked.connect(lambda: self.mostrar_pagina("page_frm_currencies"))
        self.ui.btn_ark_categories.clicked.connect(lambda: self.mostrar_pagina("page_frm_action_categories"))
        self.ui.btn_ark_device_types.clicked.connect(lambda: self.mostrar_pagina("page_frm_device_types"))
        self.ui.btn_ark_employees.clicked.connect(lambda: self.mostrar_pagina("page_frm_employees"))
        self.ui.btn_ark_functional_units.clicked.connect(lambda: self.mostrar_pagina("page_frm_functional_units"))
        self.ui.btn_ark_it_assets.clicked.connect(lambda: self.mostrar_pagina("page_frm_it_assets"))
        self.ui.btn_ark_job_titles.clicked.connect(lambda: self.mostrar_pagina("page_frm_job_titles"))
        self.ui.btn_ark_requests.clicked.connect(lambda: self.mostrar_pagina("page_frm_requests"))
        self.ui.btn_ark_sessions.clicked.connect(lambda: self.mostrar_pagina("page_frm_sessions"))
        self.ui.btn_ark_users.clicked.connect(lambda: self.mostrar_pagina("page_frm_users"))
        self.ui.btn_menu_ppal.clicked.connect(self.volver_menu_principal)
        
        # Conexiones de botones de las barras de acciones
        # Conectar botón Incluir y Cancelar de company (Empresa)
        self.ui.btn_add_a_company.clicked.connect(self.accion_incluir_empresa)
        self.ui.btn_save_a_company.clicked.connect(self.guardar_company)
        self.ui.btn_cancel_a_company.clicked.connect(self.accion_cancelar_empresa)

        # Conectar botón Incluir y Cancelar de actions (Acciones)
        self.ui.btn_add_action.clicked.connect(self.accion_incluir_acciones)
        self.ui.btn_save_action.clicked.connect(self.guardar_acciones)
        self.ui.btn_cancel_action.clicked.connect(self.accion_cancelar_acciones)

        # Categorias
        # Conectar botón Incluir, Guardar y Cancelar de categories (Categorias)
        self.ui.btn_add_actions_categories.clicked.connect(self.accion_incluir_categorias)
        self.ui.btn_save_actions_categories.clicked.connect(self.guardar_categories)
        self.ui.btn_cancel_actions_categories.clicked.connect(self.accion_cancelar_categorias)
        
        # Clientes
        # Conectar botón Incluir, Guardar y Cancelar de clients (Clientes)
        self.ui.btn_add_clients.clicked.connect(self.accion_incluir_clientes)
        self.ui.btn_save_clients.clicked.connect(self.guardar_cliente)
        self.ui.btn_cancel_clients.clicked.connect(self.accion_cancelar_clientes)

        # Conectar botón Incluir y Cancelar de currencies (Monedas)
        self.ui.btn_add_currencies.clicked.connect(self.accion_incluir_monedas)
        self.ui.btn_cancel_currencies.clicked.connect(self.accion_cancelar_monedas)

        # Conectar botón Incluir y Cancelar de device_types (Tipo de Dispositivos)
        self.ui.btn_add_device_types.clicked.connect(self.accion_incluir_tipos)
        self.ui.btn_cancel_device_types.clicked.connect(self.accion_cancelar_tipos)

        # Conectar botón Incluir y Cancelar de employees (Empleados)
        self.ui.btn_add_employees.clicked.connect(self.accion_incluir_empleados)
        self.ui.btn_cancel_employees.clicked.connect(self.accion_cancelar_empleados)

        # Conectar botón Incluir y Cancelar de functional_units (Unidades Funcionales)
        self.ui.btn_add_functional_units.clicked.connect(self.accion_incluir_unidades)
        self.ui.btn_cancel_functional_units.clicked.connect(self.accion_cancelar_unidades)

        # Conectar botón Incluir y Cancelar de assets (Recursos)
        self.ui.btn_add_it_assets.clicked.connect(self.accion_incluir_recursos)
        self.ui.btn_cancel_it_assets.clicked.connect(self.accion_cancelar_recursos)

        # Conectar botón Incluir y Cancelar de job_titles (Profesiones)
        self.ui.btn_add_job_titles.clicked.connect(self.accion_incluir_profesiones)
        self.ui.btn_cancel_job_titles.clicked.connect(self.accion_cancelar_profesiones)

        # Conectar botón Incluir y Cancelar de requests (Requerimientos)
        self.ui.btn_add_requests.clicked.connect(self.accion_incluir_requerimientos)
        self.ui.btn_cancel_requests.clicked.connect(self.accion_cancelar_requerimientos)

        # Conectar botón Incluir y Cancelar de sessions (Sesiones)
        self.ui.btn_add_sessions.clicked.connect(self.accion_incluir_sesiones)
        self.ui.btn_cancel_sessions.clicked.connect(self.accion_cancelar_sesiones)

        # Conectar botón Incluir y Cancelar de users (Usuarios)
        self.ui.btn_add_users.clicked.connect(self.accion_incluir_usuarios)
        self.ui.btn_cancel_users.clicked.connect(self.accion_cancelar_usuarios)
        
        # Conectar botón para activar buscadores
        self.ui.btn_buscar_categoria.clicked.connect(self.abrir_buscador_categorias)
        

        # ===***===***===***===***===***===***===***===***===***===***===***===***===***===***===***===***===***===
        
    # --- MÉTODOS DE UTILIDAD DE INTERFAZ ---
    def set_form_enabled(self, container, enabled=True):
        """Habilita o deshabilita widgets de entrada en un contenedor."""
        # Buscamos TODOS los widgets hijos que heredan de QWidget
        all_widgets = container.findChildren(QWidget)
        
        # Definimos la tupla de tipos que queremos controlar
        tipos_entrada = (QLineEdit, QComboBox, QTextEdit, QDateEdit, QTimeEdit)
        
        for widget in all_widgets:
            if isinstance(widget, tipos_entrada):
                widget.setEnabled(enabled)

    # --- MÉTODOS DE ACCIÓN (SLOTS) ---
    # ============GESTION DE EMPRESAS============
    def accion_incluir_empresa(self):
        """Habilita los campos del formulario de Empresa."""
        self.set_form_enabled(self.ui.frm_a_company, True)
        self.ui.lineEdit_emp_codigo.setFocus()
    
    def accion_cancelar_empresa(self):
        if self.confirmar_accion_cancelar():
            self.limpiar_formulario_company()
            self.set_form_enabled(self.ui.frm_a_company, False)
    # ============GESTION DE ACCIONES============
    def accion_incluir_acciones(self):
        self.set_form_enabled(self.ui.frm_actions, True)
        self.ui.lineEdit_act_codigo.setFocus()

    def accion_cancelar_acciones(self):
        if self.confirmar_accion_cancelar():
            self.limpiar_formulario_categories()
            self.set_form_enabled(self.ui.frm_actions, False)
    # ============GESTION DE CATEGORIAS============
    def accion_incluir_categorias(self):
        self.set_form_enabled(self.ui.frm_actions_categories, True)
        self.ui.lineEdit_cat_codigo.setFocus()
          
    def accion_cancelar_categorias(self):
        if self.confirmar_accion_cancelar():
            self.limpiar_formulario_categories()
            self.set_form_enabled(self.ui.frm_actions_categories, False)
    # ============GESTION DE CLIENTES============
    def accion_incluir_clientes(self):   
        self.set_form_enabled(self.ui.frm_clients, True)
        self.ui.lineEdit_clt_codigo.setFocus()
        logging.info("Formulario de clientes habilitado.")
    def accion_cancelar_clientes(self):
        if self.confirmar_accion_cancelar():
            self.limpiar_formulario_clientes()
            self.set_form_enabled(self.ui.frm_clients, False)
        logging.info("Acción cancelar confirmada: Formulario limpiado y deshabilitado.")
    # ============GESTION DE MONEDAS============
    def accion_incluir_monedas(self):
        self.set_form_enabled(self.ui.frm_currencies, True)
        self.ui.lineEdit_mda_codigo.setFocus()
    def accion_cancelar_monedas(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_currencies, False)
    # ============GESTION DE TIPOS DE DISPOSITIVOS============
    def accion_incluir_tipos(self):
        self.set_form_enabled(self.ui.frm_device_types, True)
        self.ui.lineEdit_dty_vodigo.setFocus()
    def accion_cancelar_tipos(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_device_types, False)
    # ============GESTION DE EMPLEADOS============
    def accion_incluir_empleados(self):
        self.set_form_enabled(self.ui.frm_employees, True)
        self.ui.lineEdit_emy_codigo.setFocus()
    def accion_cancelar_empleados(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_employees, False)
    # ============GESTION DE UNIDADES FUNCIONALES============
    def accion_incluir_unidades(self):
        self.set_form_enabled(self.ui.frm_functional_units, True)
        self.ui.lineEdit_fun_codigo.setFocus()
    def accion_cancelar_unidades(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_functional_units, False)
    # ============GESTION DE RECURSOS============
    def accion_incluir_recursos(self):
        self.set_form_enabled(self.ui.frm_it_assets, True)
        self.ui.page_frm_it_assets.setFocus()
    def accion_cancelar_recursos(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_it_assets, False)
    # ============GESTION DE PROFESIONES============
    def accion_incluir_profesiones(self):
        self.set_form_enabled(self.ui.frm_job_titles, True)
        self.ui.page_frm_job_titles.setFocus()
    def accion_cancelar_profesiones(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_job_titles, False)
    # ============GESTION DE REQUERIMIENTOS============
    def accion_incluir_requerimientos(self):
        self.set_form_enabled(self.ui.frm_requests, True)
        self.ui.lineEdit_req_codigo.setFocus()
    def accion_cancelar_requerimientos(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_requests, False)
    # ============GESTION DE SESIONES============
    def accion_incluir_sesiones(self):
        self.set_form_enabled(self.ui.frm_sessions, True)
        self.ui.lineEdit_ses_numero.setFocus()
    def accion_cancelar_sesiones(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_sessions, False)
    # ============GESTION DE USUARIOS============
    def accion_incluir_usuarios(self):
        self.set_form_enabled(self.ui.frm_users, True)
        self.ui.lineEdit_usr_codigo.setFocus()
    def accion_cancelar_usuarios(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_users, False)
    
    # ============INSERT  DE DATOS============

    # ============INSERT  DE DATOS EMPRESAS============
    
    def guardar_company(self):
        """
        Recopila los datos del formulario frm_a_company e inserta
        un nuevo registro en la tabla ark_company.
        """
        try:
            # 1. Recolección de datos desde los widgets de PySide6
            # Nota: Usamos .strip() en textos para evitar espacios accidentales
            codigo       = self.ui.lineEdit_emp_codigo.text().strip()
            descripcion  = self.ui.lineEdit_emp_descripcion.text().strip()
            id_fiscal    = self.ui.lineEdit_emp_idfiscal.text().strip()
            status       = self.ui.cmb_emp_ststus.currentIndex()             
            direccion_f  = self.ui.textEdit_emp_direccionf.toPlainText().strip()
            direccion_l  = self.ui.textEdit_emp_direccionl.toPlainText().strip()
            tel1         = self.ui.lineEdit_emp_telefono1.text().strip()
            tel2         = self.ui.lineEdit_emp_telefono2.text().strip()
            rep          = self.ui.lineEdit_emp_representante.text().strip()
            id_rep       = self.ui.lineEdit_emp_idrepresentante.text().strip()
            tel_rep     = self.ui.lineEdit_emp_TelefonoContacto.text().strip()
            email_rep   = self.ui.lineEdit_emp_EmailContacto.text().strip()
            email_emp    = self.ui.lineEdit_emp_EmailEmpresa.text().strip()
            tipo_cont    = self.ui.cmb_emp_tipo_contribuyente.currentIndex()
            fecha_crea   = self.ui.dateEdit_creation_company.date().toString("yyyy-MM-dd")

            # 2. Validación básica de campos obligatorios
            if not codigo:
                QMessageBox.warning(self, "Validación", "El Código de la empresa es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_company (
                emp_Codigo, emp_Descripcion, emp_IDfiscal, emp_Status, emp_DireccionF, emp_DireccionL, emp_Telefono1, emp_Telefono2, emp_Representante, emp_IDRepresentante, emp_TelefonoContacto, emp_EmailContacto, emp_EmailEmpresa, emp_TipoContribuyente, emp_FechaCreacion
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = (
                codigo, descripcion, id_fiscal, status, direccion_f, direccion_l, tel1, tel2, rep, id_rep, tel_rep, email_rep, email_emp, tipo_cont, fecha_crea
            )

            # 5. Ejecución mediante el DatabaseManager
            exito = self.db_manager.execute_query(sql, params)

            if exito:
                logging.info(f"Empresa guardada exitosamente: {codigo}")
                QMessageBox.information(self, "Éxito", f"La Empresa '{codigo}' ha sido registrada correctamente.")
                self.limpiar_formulario_clientes() # Función que haremos a continuación
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el registro en la base de datos.")
        except Exception as e:
            logging.error(f"Error crítico en guardar_company: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")
    # ============LIMPEZA DE FORMULARIO EMPRESAS============

    def limpiar_formulario_company(self):
        """
        Limpia todos los campos del formulario de clientes.
        """
        self.ui.lineEdit_emp_codigo.clear()
        self.ui.lineEdit_emp_descripcion.clear()
        self.ui.lineEdit_emp_idfiscal.clear()
        self.ui.cmb_emp_ststus.setCurrentIndex(0)
        self.ui.textEdit_emp_direccionf.clear()
        self.ui.textEdit_emp_direccionl.clear()
        self.ui.lineEdit_emp_telefono1.clear()
        self.ui.lineEdit_emp_telefono2.clear()
        self.ui.lineEdit_emp_representante.clear()
        self.ui.lineEdit_emp_idrepresentante.clear()
        self.ui.lineEdit_emp_TelefonoContacto.clear()
        self.ui.lineEdit_emp_EmailContacto.clear()
        self.ui.lineEdit_emp_EmailEmpresa.clear()
        self.ui.cmb_emp_tipo_contribuyente.setCurrentIndex(0)
        self.ui.dateEdit_creation_company.setDate(QDate.currentDate())
        self.ui.lineEdit_emp_codigo.setFocus()
        logging.info("Formulario de empresa limpiado.")
        

    # ============INSERT  DE DATOS CLIENTES============
    
    def guardar_cliente(self):
        """
        Recopila los datos del formulario frm_form_clients e inserta
        un nuevo registro en la tabla ark_clients.
        """
        try:
            # 1. Recolección de datos desde los widgets de PySide6
            # Nota: Usamos .strip() en textos para evitar espacios accidentales
            codigo       = self.ui.lineEdit_clt_codigo.text().strip()
            descripcion  = self.ui.lineEdit_clt_descripcion.text().strip()
            id_fiscal    = self.ui.lineEdit_clt_idfiscaliscal.text().strip() # Según tu nombre con typo 'iscal'
            status       = self.ui.cmb_clt_status.currentIndex()             # INTEGER
            direccion_f  = self.ui.textEdit_clt_direccionF.toPlainText().strip()
            direccion_l  = self.ui.textEdit_clt_direccionL.toPlainText().strip()
            tel1         = self.ui.lineEdit_clt_telefono1.text().strip()
            tel2         = self.ui.lineEdit_clt_telefono2.text().strip()
            rep          = self.ui.lineEdit_clt_representante.text().strip()
            id_rep       = self.ui.lineEdit_clt_idrepresentante.text().strip()
            tel_cont     = self.ui.lineEdit_clt_telefonocontacto.text().strip()
            email_cont   = self.ui.lineEdit_clt_emailcontacto.text().strip()
            email_emp    = self.ui.lineEdit_clt_emailempresa.text().strip()
            tipo_cont    = self.ui.cmb_clt_tipocontribuyente.currentIndex()  # INTEGER
            origen       = self.ui.cmb_clt_origen.currentText()              # TEXT
            codigo_orig  = "" # Puedes vincularlo a un widget si lo creas luego
            fecha_crea   = self.ui.dateEdit_clt_fechacreacion.date().toString("yyyy-MM-dd")

            # 2. Validación básica de campos obligatorios
            if not codigo:
                QMessageBox.warning(self, "Validación", "El Código del cliente es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_clients (
                clt_Codigo, clt_Descripcion, clt_IDfiscal, clt_Status,
                clt_DireccionF, clt_DireccionL, clt_Telefono1, clt_Telefono2,
                clt_Representante, clt_IDRepresentante, clt_TelefonoContacto,
                clt_EmailContacto, clt_EmailEmpresa, clt_TipoContribuyente,
                clt_Origen, clt_CodigoOrigen, clt_FechaCreacion
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = (
                codigo, descripcion, id_fiscal, status,
                direccion_f, direccion_l, tel1, tel2,
                rep, id_rep, tel_cont,
                email_cont, email_emp, tipo_cont,
                origen, codigo_orig, fecha_crea
            )

            # 5. Ejecución mediante el DatabaseManager
            exito = self.db_manager.execute_query(sql, params)

            if exito:
                logging.info(f"Cliente guardado exitosamente: {codigo}")
                QMessageBox.information(self, "Éxito", f"El cliente '{codigo}' ha sido registrado correctamente.")
                self.limpiar_formulario_clientes() # Función que haremos a continuación
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el registro en la base de datos.")

        except Exception as e:
            logging.error(f"Error crítico en guardar_cliente: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")
    
    # ============LIMPEZA DE FORMULARIO CLIENTES============
    
    def limpiar_formulario_clientes(self):
        """
        Resetea todos los campos del formulario de clientes a sus valores iniciales.
        """
        # 1. Limpiar QLineEdits y QTextEdits
        self.ui.lineEdit_clt_codigo.clear()
        self.ui.lineEdit_clt_descripcion.clear()
        self.ui.lineEdit_clt_idfiscaliscal.clear()
        self.ui.lineEdit_clt_telefono1.clear()
        self.ui.lineEdit_clt_telefono2.clear()
        self.ui.lineEdit_clt_representante.clear()
        self.ui.lineEdit_clt_idrepresentante.clear()
        self.ui.lineEdit_clt_telefonocontacto.clear()
        self.ui.lineEdit_clt_emailcontacto.clear()
        self.ui.lineEdit_clt_emailempresa.clear()
        
        self.ui.textEdit_clt_direccionF.clear()
        self.ui.textEdit_clt_direccionL.clear()

        # 2. Resetear QComboBoxes al primer elemento (índice 0)
        self.ui.cmb_clt_status.setCurrentIndex(0)
        self.ui.cmb_clt_tipocontribuyente.setCurrentIndex(0)
        self.ui.cmb_clt_origen.setCurrentIndex(0)

        # 3. Resetear QDateEdit a la fecha actual
        self.ui.dateEdit_clt_fechacreacion.setDate(QDate.currentDate())

        # 4. (Opcional) Poner el foco de nuevo en el primer campo
        self.ui.lineEdit_clt_codigo.setFocus()
        
        logging.info("Formulario de clientes limpiado.")
    
    # ============INSERT  DE DATOS CATEGORIES============
    
    def guardar_categories(self):
        """
        Recopila los datos del formulario frm_form_categories e inserta
        un nuevo registro en la tabla ark_action_categories.
        """
        try:
            # 1. Recolección de datos desde frm_actions_categories
            codigo       = self.ui.lineEdit_cat_codigo.text().strip()
            descripcion  = self.ui.lineEdit_cat_descripcion.text().strip()
            status       = self.ui.cmb_cat_status.currentIndex()
            descripciontec  = self.ui.textEdit_cat_descripciontec.toPlainText().strip()
            fecha_crea   = self.ui.dateEdit_cat_fechacreacion.date().toString("yyyy-MM-dd")

            # 2. Validación básica de campos obligatorios
            if not codigo:
                QMessageBox.warning(self, "Validación", "El Código de la categoría es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_action_categories (
                cat_Codigo, cat_Descripcion, cat_Status,
                cat_DescripcionTec, cat_FechaCreacion
            ) VALUES (?, ?, ?, ?, ?)
            """

            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = (
                codigo, descripcion, status,
                descripciontec, fecha_crea
            )

            # 5. Ejecución mediante el DatabaseManager
            # execute_query retorna el cursor si fue exitoso, o None si falló
            exito = self.db_manager.execute_query(sql, params)

            if exito:
                logging.info(f"Categoría guardada exitosamente: {codigo}")
                QMessageBox.information(self, "Éxito", f"La Categoría '{codigo}' ha sido registrada correctamente.")
                self.limpiar_formulario_categories() # Función que haremos a continuación
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el registro en la base de datos.")

        except Exception as e:
            logging.error(f"Error crítico en guardar_categories: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")

    # ============LIMPEZA DE FORMULARIO CATEGORIES============

    def limpiar_formulario_categories(self):
        """
        Resetea todos los campos del formulario de categorías a sus valores iniciales.
        """
        # 1. Limpiar QLineEdits y QTextEdits
        self.ui.lineEdit_cat_codigo.clear()
        self.ui.lineEdit_cat_descripcion.clear()
        self.ui.textEdit_cat_descripciontec.clear()
        # 2. Resetear QComboBoxes al primer elemento (índice 0)
        self.ui.cmb_cat_status.setCurrentIndex(0)
        # 3. Resetear QDateEdit a la fecha actual
        self.ui.dateEdit_cat_fechacreacion.setDate(QDate.currentDate())

        # 4. (Opcional) Poner el foco de nuevo en el primer campo
        self.ui.lineEdit_cat_codigo.setFocus()
        
        logging.info("Formulario de categorías  limpiado.")  

    # ============INSERT DE DATOS ACCIONES============
    
    def guardar_acciones(self):
        """
        Recopila los datos del formulario frm_actions e inserta
        un nuevo registro en la tabla ark_actions.
        """
        try:
            # 1. Recolección de datos desde frm_actions_categories
            codigo       = self.ui.lineEdit_act_codigo.text().strip()
            descripcion  = self.ui.lineEdit_act_descripcion.text().strip()
            status       = self.ui.cmb_act_status.currentIndex()
            descripciontec  = self.ui.textEdit_act_descripciontec.toPlainText().strip()
            categoria    = self.id_categoria_actual  # ID de la categoría vinculada            
            fecha_crea   = self.ui.dateEdit_act_fechacreacion.date().toString("yyyy-MM-dd")

            # 2. Validación básica de campos obligatorios
            if not codigo:
                QMessageBox.warning(self, "Validación", "El Código de la acción es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_actions (
                act_Codigo, act_Descripcion, act_Status,
                act_DescripcionTec, id_category, act_FechaCreacion
            ) VALUES (?, ?, ?, ?, ?, ?)
            """

            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = (
                codigo, descripcion, status,
                descripciontec, categoria, fecha_crea
            )

            # 5. Ejecución mediante el DatabaseManager
            # execute_query retorna el cursor si fue exitoso, o None si falló
            exito = self.db_manager.execute_query(sql, params)

            if exito:
                logging.info(f"Acción guardada exitosamente: {codigo}")
                QMessageBox.information(self, "Éxito", f"La Acción '{codigo}' ha sido registrada correctamente.")
                self.limpiar_formulario_accion() # Función que haremos a continuación
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el registro en la base de datos.")

        except Exception as e:
            logging.error(f"Error crítico en guardar_categories: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")

    # ============LIMPEZA DE FORMULARIO ACCIONES============

    def limpiar_formulario_accion(self):
        """
        Resetea todos los campos del formulario de acciones a sus valores iniciales.
        """
        # 1. Limpiar QLineEdits y QTextEdits
        self.ui.lineEdit_act_codigo.clear()
        self.ui.lineEdit_act_descripcion.clear()
        self.ui.textEdit_act_descripciontec.clear()
        self.ui.lineEdit_id_category.clear()
        # 2. Resetear QComboBoxes al primer elemento (índice 0)
        self.ui.cmb_act_status.setCurrentIndex(0)
        # 3. Resetear QDateEdit a la fecha actual
        self.ui.dateEdit_act_fechacreacion.setDate(QDate.currentDate())

        # 4. (Opcional) Poner el foco de nuevo en el primer campo
        self.ui.lineEdit_act_codigo.setFocus()
        
        logging.info("Formulario de acciones limpiado.")  
                  
    # ==================================FIN INSERT DE DATOS==================================
    
    # ==============================ACTIVACION DE BUSCADORES=================================
    
    def ejecutar_buscador_generico(self, titulo, sql, columnas):
        """
        Lógica centralizada para abrir cualquier buscador tipo lupa.
        Retorna una tupla (ID, Texto_Combinado) o (None, None)
        """
        dialogo = BuscadorBaseDialog(self.db_manager, titulo, sql, columnas)
        
        if dialogo.exec():
            return dialogo.id_seleccionado, dialogo.texto_combinado
        
        return None, None
    
    def abrir_buscador_categorias(self):
        # 1. Definimos la configuración específica
        sql = "SELECT cat_IDauto, cat_Codigo, cat_Descripcion FROM ark_action_categories WHERE cat_Status = 0"
        columnas = ["ID", "Código", "Descripción"]
        
        # 2. Llamamos al motor genérico
        id_sel, texto_sel = self.ejecutar_buscador_generico("Categorías de Acciones", sql, columnas)
        
        # 3. Si el usuario eligió algo, actualizamos la App
        if id_sel is not None:
            self.id_categoria_actual = id_sel
            self.ui.lineEdit_id_category.setText(texto_sel)
            logging.info(f"Buscador: Seleccionado ID {id_sel}")
                
       
    # ------------------ CONTROLES DE LA BARRA SUPERIOR ------------------      
    
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
    def consultar_configuracion_db(self):
        """
        Función conectada a btn_config_sql_tools que lee datos de la tabla ark_company 
        y los muestra en el área de texto de configuración (textEdit_info_config).
        ESTA FUNCIÓN ES EXCLUSIVAMENTE PARA CONSULTA (SELECT).
        """
        # Consulta SQL para obtener los datos de la empresa
        sql = "SELECT emp_IDauto, emp_Codigo, emp_Descripcion, emp_IDfiscal, emp_FechaCreacion FROM ark_company ORDER BY emp_IDauto DESC;"
        
        self.ui.textEdit_info_config.clear() 
        filas = self.db_manager.fetch_data(sql)
        output = "--- RESULTADO DE CONSULTA SQL (ark_company) ---\n\n"
        
        # Verificar si hay registros en la tabla
        if filas:
            # Obtener la primera empresa registrada (la más reciente según el ORDER BY)
            empresa_registrada = filas[0]['emp_Descripcion']
            output += f"La operadora Empresa registrada en la aplicación \"ArkToolsPC\" es: {empresa_registrada}.\n\n"
            
            # Mostrar el resto de los registros
            for i, fila in enumerate(filas):
                output += f"Registro {i+1} (ID: {fila['emp_IDauto']}):\n"
                output += f"  Código: {fila['emp_Codigo']}\n"
                output += f"  Descripción: {fila['emp_Descripcion']}\n"
                output += f"  RIF/ID Fiscal: {fila['emp_IDfiscal']}\n"
                output += f"  Creación: {fila['emp_FechaCreacion']}\n\n"
        else:
            output += "No se encontraron registros en la tabla 'ark_company'.\n"
            output += "Utiliza la sección de gestión (que definiremos más tarde) para insertar datos."
        
        # Mostrar el resultado en el QTextEdit
        self.ui.textEdit_info_config.setText(output)
        logging.info("Consulta a ark_company ejecutada y resultados mostrados.")
    
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
    
    def confirmar_accion_cancelar(self):
        """Muestra el cuadro de diálogo y retorna True si el usuario confirma."""
        respuesta = QMessageBox.question(
            self, 
            "Confirmar Cancelación", 
            "¿Está seguro de cancelar la operación actual? Se perderán los cambios no guardados.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        return respuesta == QMessageBox.StandardButton.Yes

    # ------------------ MOSTRAR MENÚ DE HARDWARE ------------------
    def mover_menu(self):
        """
        Muestra u oculta el menú principal (frame_menu).
        Asegura que los submenús (frame_sub_hardware y frame_operations) estén cerrados antes de abrir el menú principal.
        """
        # Cerrar los submenús antes de abrir el menú principal
        self.ui.frame_sub_hardware.setMaximumWidth(0)
        self.ui.frame_operations.setMaximumWidth(0)

        width = self.ui.frame_menu.maximumWidth()
        if width == 0:
            extender = 200  # Mostrar el menú principal
        else:
            extender = 0  # Ocultar el menú principal

        # Animación para el menú principal
        self.animacion = QPropertyAnimation(self.ui.frame_menu, b'maximumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion.start()

    # ------------------ MOSTRAR SUBMENÚ DE HARDWARE ------------------
    def toggle_sub_hardware_menu(self):
        """
        Alterna la visibilidad del submenú de hardware (frame_sub_hardware).
        Si el submenú está visible, lo oculta y muestra el menú principal.
        Si el submenú está oculto, lo muestra y oculta el menú principal.
        """
        # Obtener el ancho actual del submenú
        current_width_sub = self.ui.frame_sub_hardware.maximumWidth()
        
        # Definir el ancho de la animación (0 para ocultar, 200 para mostrar)
        if current_width_sub == 0:
            end_width_sub = 200  # Mostrar el submenú
            end_width_menu = 0   # Ocultar el menú principal
        else:
            end_width_sub = 0    # Ocultar el submenú
            end_width_menu = 200 # Mostrar el menú principal

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

    # ------------------ MOSTRAR SUBMENÚ DE OPERACIONES ------------------
    def toggle_operations_menu(self):
        """
        Alterna la visibilidad del submenú de operaciones (frame_operations).
        Si el submenú está visible, lo oculta y muestra el menú principal.
        Si el submenú está oculto, lo muestra y oculta el menú principal.
        """
        # Obtener el ancho actual del submenú
        current_width_operations = self.ui.frame_operations.maximumWidth()
        
        # Definir el ancho de la animación (0 para ocultar, 200 para mostrar)
        if current_width_operations == 0:
            end_width_operations = 200  # Mostrar el submenú
            end_width_menu = 0         # Ocultar el menú principal
        else:
            end_width_operations = 0   # Ocultar el submenú
            end_width_menu = 200       # Mostrar el menú principal

        # Animación para el submenú de operaciones
        self.animacion_operations = QPropertyAnimation(self.ui.frame_operations, b'maximumWidth')
        self.animacion_operations.setDuration(300)
        self.animacion_operations.setStartValue(current_width_operations)
        self.animacion_operations.setEndValue(end_width_operations)
        self.animacion_operations.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_operations.start()

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
        """
        Cierra todos los submenús y muestra el menú principal (frame_menu) con animaciones.
        """
        # Animación para cerrar el submenú de hardware
        if self.ui.frame_sub_hardware.maximumWidth() > 0:
            self.animacion_sub_hardware = QPropertyAnimation(self.ui.frame_sub_hardware, b'maximumWidth')
            self.animacion_sub_hardware.setDuration(300)
            self.animacion_sub_hardware.setStartValue(self.ui.frame_sub_hardware.maximumWidth())
            self.animacion_sub_hardware.setEndValue(0)
            self.animacion_sub_hardware.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animacion_sub_hardware.start()

        # Animación para cerrar el submenú de operaciones
        if self.ui.frame_operations.maximumWidth() > 0:
            self.animacion_operations = QPropertyAnimation(self.ui.frame_operations, b'maximumWidth')
            self.animacion_operations.setDuration(300)
            self.animacion_operations.setStartValue(self.ui.frame_operations.maximumWidth())
            self.animacion_operations.setEndValue(0)
            self.animacion_operations.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animacion_operations.start()

        # Animación para mostrar el menú principal
        if self.ui.frame_menu.maximumWidth() == 0:
            self.animacion_menu = QPropertyAnimation(self.ui.frame_menu, b'maximumWidth')
            self.animacion_menu.setDuration(300)
            self.animacion_menu.setStartValue(self.ui.frame_menu.maximumWidth())
            self.animacion_menu.setEndValue(200)
            self.animacion_menu.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animacion_menu.start()
        # Cambiar a la página de inicio en el QStackedWidget
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inicio)

    # SizeGrip
    def resizeEvent(self, event):
        """
        Maneja el evento de redimensionamiento de la ventana.
        Ajusta automáticamente los elementos según el tamaño de la ventana.
        """
        # Llama al método padre para mantener la funcionalidad original
        super().resizeEvent(event)
        
        # Ajustar los formularios según el nuevo tamaño
        self.ajustar_formularios_según_tamaño()
        
        # Mover el SizeGrip si es necesario
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def ajustar_formularios_según_tamaño(self):
        """
        Ajusta los formularios según el tamaño actual de la ventana.
        """
        # Obtener el tamaño actual de la ventana
        tamaño_ventana = self.size()
        
        # Ajustar según el ancho de la ventana
        ancho_ventana = tamaño_ventana.width()
        
        # Ajustar el tamaño de los formularios según el tamaño de la ventana
        if hasattr(self.ui, 'frm_bar_company') and hasattr(self.ui, 'frm_form_company'):
            if ancho_ventana > 1200:
                # Ventana grande - usar tamaño completo
                self.ui.frm_bar_company.setMaximumWidth(250)
                self.ui.frm_bar_company.setMinimumWidth(200)
                self.ui.frm_form_company.setMinimumWidth(800)
                
            elif ancho_ventana > 800:
                # Ventana mediana
                self.ui.frm_bar_company.setMaximumWidth(200)
                self.ui.frm_bar_company.setMinimumWidth(150)
                self.ui.frm_form_company.setMinimumWidth(600)
                
            else:
                # Ventana pequeña - ajuste compacto
                self.ui.frm_bar_company.setMaximumWidth(150)
                self.ui.frm_bar_company.setMinimumWidth(100)
                self.ui.frm_form_company.setMinimumWidth(400)
            
    # Mover ventana
    def mousePressEvent(self, event):
        """
        Guarda la posición inicial del mouse cuando se presiona el botón del mouse.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.clickPosition = event.globalPosition().toPoint()

    def mover_ventana(self, event):
        """
        Permite mover la ventana cuando el usuario arrastra el mouse sobre el frame superior.
        """
        if not self.isMaximized():
            if event.buttons() == Qt.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.clickPosition)
                self.clickPosition = event.globalPosition().toPoint()
                event.accept()

        # Maximizar/restaurar la ventana si el mouse está cerca de la parte superior
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
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inicio)
    
    # ------------------ MOSTRAR INFORMACIÓN DE RED ------------------
    
    def mostrar_info_red(self):
        """
        Muestra la información de la Red en textEdit_info_hw y cambia la imagen.
        """
        info_red = system_info.get_network_info()
        self.ui.textEdit_info_red.setText(info_red)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_red)
        
    # ------------------ MOSTRAR INFORMACIÓN DEL SISTEMA OPERATIVO ------------------
    
    def mostrar_info_os(self):
        """
        Muestra la información del Sistema Operativo en textEdit_info_hw y cambia la imagen.
        """
        info_os = system_info.get_os_info()
        self.ui.textEdit_info_so.setText(info_os)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_so)
        
    # ------------------ MOSTRAR FORMULARIOS DE GESTION DE DATOS ------------------
    
    def mostrar_pagina(self, nombre_pagina):
        """
        Muestra la página correspondiente en el QStackedWidget (qsw_forms).
        
        :param nombre_pagina: Nombre de la página o widget a mostrar (str).
        """
        # Cambiar a page_forms si es necesario
        if nombre_pagina.startswith("page_frm_"):
            self.ui.sw_consolas.setCurrentWidget(self.ui.page_forms)
        
        # Obtener el widget correspondiente
        pagina = getattr(self.ui, nombre_pagina, None)
        if pagina:
            logging.info(f"Página encontrada: {nombre_pagina}")
            self.ui.qsw_forms.setCurrentWidget(pagina)  # Usa el QStackedWidget dentro de page_forms
        else:
            logging.error(f"Página no encontrada: {nombre_pagina}")

    # ------------------ MOSTRAR INFORMACIÓN TECNICA DEL DISPOSITIVO ------------------

    def mostrar_info_regional(self):
        """
        Muestra la información Regional en textEdit_info_hw y cambia la imagen.
        """
        info_regional = system_info.get_regional_settings()
        self.ui.textEdit_info_regional.setText(info_regional)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_regional)
    
    def mostrar_configuracion(self):
        """
        Muestra la configuración regional en textEdit_info_config y cambia a page_inf_config.
        """
        info_regional = system_info.get_regional_settings()
        self.ui.textEdit_info_config.setText(info_regional)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_config)
    
    def mostrar_info_mbd(self):
        """
        Muestra la información de la placa base en textEdit_info_hw y cambia la imagen.
        """
        self.ui.textEdit_info_hw.clear()
        pixmap_mbd = QPixmap("imagen/mbd_02.png")
        self.ui.label_info_hw.setPixmap(pixmap_mbd)
        info_mbd = system_info.get_motherboard_info()
        self.ui.textEdit_info_hw.setText(info_mbd)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_hardware)

    def mostrar_info_cpu_hw(self):
        """
        Muestra la información de la CPU en textEdit_info_hw y cambia la imagen.
        """
        self.ui.textEdit_info_hw.clear()
        pixmap_cpu = QPixmap("imagen/cpu02.svg")
        self.ui.label_info_hw.setPixmap(pixmap_cpu)
        info_cpu = system_info.get_cpu_info()
        self.ui.textEdit_info_hw.setText(info_cpu)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_hardware)
    
    def mostrar_info_gpu(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_gpu = QPixmap("imagen/Grafica01.svg")
        self.ui.label_info_hw.setPixmap(pixmap_gpu)
        info_gpu = system_info.get_gpu_info()
        self.ui.textEdit_info_hw.setText(info_gpu)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_hardware)

    def mostrar_info_ram(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_ram = QPixmap("imagen/Ram01.svg")
        self.ui.label_info_hw.setPixmap(pixmap_ram)
        info_ram = system_info.get_ram_info()
        self.ui.textEdit_info_hw.setText(info_ram)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_hardware)

    def mostrar_info_hdd(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_hdd = QPixmap("imagen/hdd03.svg")
        self.ui.label_info_hw.setPixmap(pixmap_hdd)
        info_hdd = system_info.get_disk_info()
        self.ui.textEdit_info_hw.setText(info_hdd)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_hardware)
        
    def mostrar_info_nic(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_nic = QPixmap("imagen/nic01.svg")
        self.ui.label_info_hw.setPixmap(pixmap_nic)
        info_nic = system_info.get_nic_info()
        self.ui.textEdit_info_hw.setText(info_nic)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_hardware)

    def mostrar_info_com(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_com = QPixmap("imagen/com02.svg")
        self.ui.label_info_hw.setPixmap(pixmap_com)
        info_com = system_info.get_com_ports()
        self.ui.textEdit_info_hw.setText(info_com)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_hardware)
        
    def mostrar_info_bth(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_bth = QPixmap("imagen/bluetooth02.svg")
        self.ui.label_info_hw.setPixmap(pixmap_bth)
        info_bth = system_info.get_bluetooth_devices()
        self.ui.textEdit_info_hw.setText(info_bth)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_hardware)

    def mostrar_info_audio(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_audio = QPixmap("imagen/audio01.svg")
        self.ui.label_info_hw.setPixmap(pixmap_audio)
        info_audio = system_info.get_audio_devices()
        self.ui.textEdit_info_hw.setText(info_audio)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_hardware)

    def mostrar_info_sistema_gen(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_sistema = QPixmap("imagen/sys01.svg")
        self.ui.label_info_hw.setPixmap(pixmap_sistema)
        info_sistema = system_info.get_system_info()
        self.ui.textEdit_info_hw.setText(info_sistema)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_hardware)
        
    def mostrar_info_usb(self):
        self.ui.textEdit_info_hw.clear()
        pixmap_usb = QPixmap("imagen/usb03.svg")
        self.ui.label_info_hw.setPixmap(pixmap_usb)
        info_usb = system_info.get_usb_devices()
        self.ui.textEdit_info_hw.setText(info_usb)
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_hardware)
    
    def mostrar_inf_config(self):
        """
        Muestra la página de configuración del sistema.
        """
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_config)
        
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