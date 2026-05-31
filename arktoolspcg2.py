# arktoolspcg2.py es el archivo Main de la aplicación PySide6 ARKToolsPCG2
# Version 2.0.8 - Integración de Base de Datos y Formularios de Gestión

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
        self.id_categoria_seleccionada = None
        self.selected_customer_id = None

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
        self.ui.btn_archives_menu.clicked.connect(self.toggle_archives_menu)
        self.ui.btn_systems_menu.clicked.connect(self.toggle_systems_menu)
        self.ui.btn_transactions_menu.clicked.connect(self.toggle_transactions_menu)
        self.ui.btn_reports_menu.clicked.connect(self.toggle_reports_menu)
        self.ui.zz_btn_Disponible_menu.clicked.connect(self.toggle_disponible_menu)
        self.ui.btn_log_out.clicked.connect(self.toggle_logout)

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
        self.ui.btn_settings_menu.clicked.connect(self.mostrar_inf_config)
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
        self.ui.btn_menu_repo_ppal.clicked.connect(self.volver_menu_principal)
        self.ui.btn_menu_arch_ppal.clicked.connect(self.volver_menu_principal)
        self.ui.btn_menu_sys_ppal.clicked.connect(self.volver_menu_principal)
        self.ui.btn_menu_ppal.clicked.connect(self.volver_menu_principal)
        self.ui.btn_menu_cnf_ppal.clicked.connect(self.volver_menu_principal)
        
        # Conexiones de botones de las barras de acciones
        # Conectar botón Incluir y Cancelar de company (Empresa)
        self.ui.btn_add_a_company.clicked.connect(self.action_include_company)
        self.ui.btn_save_a_company.clicked.connect(self.save_company)
        self.ui.btn_cancel_a_company.clicked.connect(self.action_cancel_company)

        # Conectar botón Incluir y Cancelar de actions (Acciones)
        self.ui.btn_add_action.clicked.connect(self.action_include_actions)
        self.ui.btn_save_action.clicked.connect(self.save_actions)
        self.ui.btn_cancel_action.clicked.connect(self.action_cancel_actions)

        # Categorias
        # Conectar botón Incluir, Guardar y Cancelar de categories (Categorias)
        self.ui.btn_add_actions_categories.clicked.connect(self.action_include_categories)
        self.ui.btn_save_actions_categories.clicked.connect(self.save_categories)
        self.ui.btn_cancel_actions_categories.clicked.connect(self.action_cancel_categories)
        
        # Clients
        # Conectar botón Incluir, Guardar y Cancelar de clients (Clients)
        self.ui.btn_add_clients.clicked.connect(self.action_include_clients)
        self.ui.btn_save_clients.clicked.connect(self.save_clients)
        self.ui.btn_cancel_clients.clicked.connect(self.action_cancel_clients)

        # Conectar botón Incluir y Cancelar de currencies (Monedas)
        self.ui.btn_add_currencies.clicked.connect(self.action_include_currencies)
        self.ui.btn_save_currencies.clicked.connect(self.save_currencies)
        self.ui.btn_cancel_currencies.clicked.connect(self.action_cancel_currencies)

        # Conectar botón Incluir y Cancelar de device_types (Tipo de Dispositivos)
        self.ui.btn_add_device_types.clicked.connect(self.action_include_types)
        self.ui.btn_save_device_types.clicked.connect(self.save_device_types)
        self.ui.btn_cancel_device_types.clicked.connect(self.action_cancel_types)

        # Conectar botón Incluir y Cancelar de employees (Empleados)
        self.ui.btn_add_employees.clicked.connect(self.action_include_employees)
        self.ui.btn_save_employees.clicked.connect(self.save_employees)
        self.ui.btn_cancel_employees.clicked.connect(self.action_cancel_employees)

        # Conectar botón Incluir y Cancelar de functional_units (Unidades Funcionales)
        self.ui.btn_add_functional_units.clicked.connect(self.action_include_units)
        self.ui.btn_save_functional_units.clicked.connect(self.save_functional_units)
        self.ui.btn_cancel_functional_units.clicked.connect(self.action_cancel_units)

        # Conectar botón Incluir y Cancelar de assets (Recursos)
        self.ui.btn_add_it_assets.clicked.connect(self.action_include_assets)
        self.ui.btn_save_it_assets.clicked.connect(self.save_it_assets)
        self.ui.btn_cancel_it_assets.clicked.connect(self.action_cancel_assets)

        # Conectar botón Incluir y Cancelar de job_titles (Profesiones)
        self.ui.btn_add_job_titles.clicked.connect(self.action_include_job_titles)
        self.ui.btn_cancel_job_titles.clicked.connect(self.action_cancel_job_titles)

        # Conectar botón Incluir y Cancelar de requests (Requerimientos)
        self.ui.btn_add_requests.clicked.connect(self.action_include_requests)
        self.ui.btn_cancel_requests.clicked.connect(self.action_cancel_requests)

        # Conectar botón Incluir y Cancelar de sessions (Sesiones)
        self.ui.btn_add_sessions.clicked.connect(self.action_include_sessions)
        self.ui.btn_cancel_sessions.clicked.connect(self.action_cancel_sessions)

        # Conectar botón Incluir y Cancelar de users (Usuarios)
        self.ui.btn_add_users.clicked.connect(self.action_include_users)
        self.ui.btn_cancel_users.clicked.connect(self.action_cancel_users)
        
        # Conectar botón para activar buscadores
        self.ui.btn_buscar_ita_functional_units.clicked.connect(self.open_search_functional_units)
        self.ui.btn_search_act_category.clicked.connect(self.open_search_categories)
        self.ui.btn_search_emy_client.clicked.connect(self.open_search_clients)
        self.ui.btn_search_req_client.clicked.connect(self.open_search_clients)
        self.ui.btn_search_ses_client.clicked.connect(self.open_search_clients)
        self.ui.btn_search_ita_id_employees.clicked.connect(self.open_search_employees)
        self.ui.btn_search_ses_employees.clicked.connect(self.open_search_employees)
        self.ui.btn_search_usr_job_titles.clicked.connect(self.open_search_job_titles)
        # -------------------------------------------------------------------------
                
        # LLAMADA OBLIGATORIA PARA QUE SE MUESTRE AL ABRIR
        self.actualizar_barra_estado()
        
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
                
    # --- ACTUALIZAR BARRA DE ESTADO CON INFO DEL SISTEMA ---
    
    def actualizar_barra_estado(self):
        try:
            # Extraemos los datos de tu sistema_info
            fecha   = system_info.get_date_audit()
            user = system_info.get_current_user()
            equipo  = system_info.get_machine_name()
            
            # Formateamos la cadena
            info_sesion = f" SESIÓN ACTIVA | Usuario: {user} | Equipo: {equipo} | Fecha: {fecha}"
            
            # Aplicamos al QLabel que mencionaste
            self.ui.pie_arkinfo.setText(info_sesion)
            
            # Log para verificar en consola/archivo si se ejecutó
            logging.info("Barra de estado actualizada correctamente.")
            
        except Exception as e:
            logging.error(f"Error al actualizar pie_arkinfo: {e}")
    
    # --- MÉTODOS DE ACCIÓN (SLOTS) ---
    # ============GESTION DE EMPRESAS============
    def action_include_company(self):
        """Habilita los campos del formulario de Empresa."""
        self.set_form_enabled(self.ui.frm_a_company, True)
        self.ui.lineEdit_emp_code.setFocus()
    def action_cancel_company(self):
        if self.confirmar_accion_cancelar():
            self.clear_form_company()
            self.set_form_enabled(self.ui.frm_a_company, False)
    # ============GESTION DE ACCIONES============
    def action_include_actions(self):
        self.set_form_enabled(self.ui.frm_actions, True)
        self.ui.lineEdit_act_code.setFocus()
    def action_cancel_actions(self):
        if self.confirmar_accion_cancelar():
            self.clear_form_categories()
            self.set_form_enabled(self.ui.frm_actions, False)
    # ============GESTION DE CATEGORIAS============
    def action_include_categories(self):
        self.set_form_enabled(self.ui.frm_actions_categories, True)
        self.ui.lineEdit_cat_code.setFocus()
    def action_cancel_categories(self):
        if self.confirmar_accion_cancelar():
            self.clear_form_categories()
            self.set_form_enabled(self.ui.frm_actions_categories, False)
    # ============GESTION DE CLIENTES============
    def action_include_clients(self):   
        self.set_form_enabled(self.ui.frm_clients, True)
        self.ui.lineEdit_clt_code.setFocus()
        logging.info("Formulario de clientes habilitado.")        
    def action_cancel_clients(self):
        if self.confirmar_accion_cancelar():
            self.clear_form_clients()
            self.set_form_enabled(self.ui.frm_clients, False)
        logging.info("Acción cancelar confirmada: Formulario limpiado y deshabilitado.")
    # ============GESTION DE MONEDAS============
    def action_include_currencies(self):
        self.set_form_enabled(self.ui.frm_currencies, True)
        self.ui.lineEdit_mda_code.setFocus()
        logging.info("Formulario de monedas habilitado.")      
    def action_cancel_currencies(self):
        if self.confirmar_accion_cancelar():
            self.clear_form_currencies()
            self.set_form_enabled(self.ui.frm_currencies, False)
        logging.info("Acción cancelar confirmada: Formulario limpiado y deshabilitado.")
    # ============GESTION DE TIPOS DE DISPOSITIVOS============
    def action_include_types(self):
        self.set_form_enabled(self.ui.frm_device_types, True)
        self.ui.lineEdit_dty_code.setFocus()
        logging.info("Formulario de tipos de dispositivos habilitado.")
    def action_cancel_types(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_device_types, False)
        logging.info("Acción cancelar confirmada: Formulario limpiado y deshabilitado.")
    # ============GESTION DE EMPLEADOS============
    def action_include_employees(self):
        self.set_form_enabled(self.ui.frm_employees, True)
        self.ui.lineEdit_emy_code.setFocus()
    def action_cancel_employees(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_employees, False)
    # ============GESTION DE UNIDADES FUNCIONALES============
    def action_include_units(self):
        self.set_form_enabled(self.ui.frm_functional_units, True)
        self.ui.lineEdit_fun_code.setFocus()
        logging.info("Formulario de unidades funcionales habilitado.")
    def action_cancel_units(self):
        if self.confirmar_accion_cancelar():
            self.clear_form_functional_units()
            self.set_form_enabled(self.ui.frm_functional_units, False)
        logging.info("Acción cancelar confirmada: Formulario limpiado y deshabilitado.")
    # ============GESTION DE RECURSOS============
    def action_include_assets(self):
        self.set_form_enabled(self.ui.frm_it_assets, True)
        self.ui.page_frm_it_assets.setFocus()
    def action_cancel_assets(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_it_assets, False)
    # ============GESTION DE PROFESIONES============
    def action_include_job_titles(self):
        self.set_form_enabled(self.ui.frm_job_titles, True)
        self.ui.page_frm_job_titles.setFocus()
    def action_cancel_job_titles(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_job_titles, False)
    # ============GESTION DE REQUERIMIENTOS============
    def action_include_requests(self):
        self.set_form_enabled(self.ui.frm_requests, True)
        self.ui.lineEdit_req_code.setFocus()
    def action_cancel_requests(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_requests, False)
    # ============GESTION DE SESIONES============
    def action_include_sessions(self):
        self.set_form_enabled(self.ui.frm_sessions, True)
        self.ui.lineEdit_ses_number.setFocus()
    def action_cancel_sessions(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_sessions, False)
    # ============GESTION DE USUARIOS============
    def action_include_users(self):
        self.set_form_enabled(self.ui.frm_users, True)
        self.ui.lineEdit_usr_code.setFocus()
    def action_cancel_users(self):
        if self.confirmar_accion_cancelar():
            self.set_form_enabled(self.ui.frm_users, False)
    
    # ============INSERT  DE DATOS
    
    # ============INSERT  DE DATOS EMPRESAS
    
    def save_company(self):
        """
        Recopila los datos del formulario frm_a_company e inserta
        un nuevo registro en la tabla ark_company.
        """
        try:
            # 1. Recolección de datos desde los widgets de PySide6
            # Nota: Usamos .strip() en textos para evitar espacios accidentales
            code            = self.ui.lineEdit_emp_code.text().strip()
            description     = self.ui.lineEdit_emp_description.text().strip()
            tax_id          = self.ui.lineEdit_emp_tax_id.text().strip()
            status          = self.ui.cmb_emp_ststus.currentIndex()             
            tax_address     = self.ui.textEdit_emp_tax_address.toPlainText().strip()
            local_address   = self.ui.textEdit_emp_local_address.toPlainText().strip()
            phone           = self.ui.lineEdit_emp_phone.text().strip()
            mobile          = self.ui.lineEdit_emp_mobile.text().strip()
            rep             = self.ui.lineEdit_emp_legal_representative.text().strip()
            id_rep          = self.ui.lineEdit_emp_legal_representative_id.text().strip()
            tel_rep         = self.ui.lineEdit_emp_contact_phone.text().strip()
            email_rep       = self.ui.lineEdit_emp_contact_email.text().strip()
            email_emp       = self.ui.lineEdit_emp_company_email.text().strip()
            tipo_taxpayer   = self.ui.cmb_emp_tipo_taxpayer.currentIndex()
            creation_date   = self.ui.dateEdit_creation_date.date().toString("yyyy-MM-dd")

            # Seccion de auditoría del sistema
            f_system  = system_info.get_date_audit()
            h_system  = system_info.get_time_audit()
            computer_name = system_info.get_machine_name()
            user    = system_info.get_current_user()
            last_f_systems = system_info.get_date_audit()
            last_h_systems = system_info.get_time_audit()
            last_computer_name = system_info.get_machine_name()
            last_user    = system_info.get_current_user()

            # 2. Validación básica de campos obligatorios
            if not code:
                QMessageBox.warning(self, "Validación", "El Código de la empresa es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_company (
                emp_Codigo, emp_Descripcion, emp_IDfiscal, emp_Status, emp_DireccionF, 
                emp_DireccionL, emp_Telefono1, emp_Telefono2, emp_Representante, emp_IDRepresentante, 
                emp_TelefonoContacto, emp_EmailContacto, emp_EmailEmpresa, emp_TipoContribuyente, emp_FechaCreacion,
                emp_SystemDate, emp_SystemTime, emp_NameMachine, emp_UserCreator,
                emp_LastUpdateDate, emp_LastUpdateTime, emp_LastMachine, emp_UserLastUpdate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = (
                code, description, tax_id, status, tax_address, local_address, phone, mobile, rep, id_rep, tel_rep, 
                email_rep, email_emp, tipo_taxpayer, creation_date, f_system, h_system, computer_name, user,
                last_f_systems, last_h_systems, last_computer_name, last_user
            )

            # 5. Ejecución mediante el DatabaseManager
            exito = self.db_manager.execute_query(sql, params)

            if exito:
                logging.info(f"Empresa guardada exitosamente: {code}")
                QMessageBox.information(self, "Éxito", f"La Empresa '{code}' ha sido registrada correctamente.")
                self.clear_form_clients() # Función que haremos a continuación
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el registro en la base de datos.")
        except Exception as e:
            logging.error(f"Error crítico en save_company: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")
    # ============LIMPEZA DE FORMULARIO EMPRESAS

    def clear_form_company(self):
        """
        Limpia todos los campos del formulario de clientes.
        """
        self.ui.lineEdit_emp_code.clear()
        self.ui.lineEdit_emp_description.clear()
        self.ui.lineEdit_emp_tax_id.clear()
        self.ui.cmb_emp_ststus.setCurrentIndex(0)
        self.ui.textEdit_emp_tax_address.clear()
        self.ui.textEdit_emp_local_address.clear()
        self.ui.lineEdit_emp_phone.clear()
        self.ui.lineEdit_emp_mobile.clear()
        self.ui.lineEdit_emp_legal_representative.clear()
        self.ui.lineEdit_emp_legal_representative_id.clear()
        self.ui.lineEdit_emp_contact_phone.clear()
        self.ui.lineEdit_emp_contact_email.clear()
        self.ui.lineEdit_emp_company_email.clear()
        self.ui.cmb_emp_tipo_taxpayer.setCurrentIndex(0)
        self.ui.dateEdit_creation_date.setDate(QDate.currentDate())
        self.ui.lineEdit_emp_code.setFocus()
        logging.info("Formulario de empresa limpiado.")
        
    # ============INSERT  DE DATOS CLIENTES
    def save_clients(self):
        """
        Recopila los datos del formulario frm_form_clients e inserta
        un nuevo registro en la tabla ark_clients.
        """
        try:
            # 1. Recolección de datos desde los widgets de PySide6
            # Nota: Usamos .strip() en textos para evitar espacios accidentales
            code         = self.ui.lineEdit_clt_code.text().strip()
            description  = self.ui.lineEdit_clt_description.text().strip()
            tax_id       = self.ui.lineEdit_clt_idfiscal.text().strip() # Según tu nombre con typo 'iscal'
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
            code_orig  = "" # Puedes vincularlo a un widget si lo creas luego
            creation_date   = self.ui.dateEdit_clt_fechacreacion.date().toString("yyyy-MM-dd")
            
            # Seccion de auditoría del sistema
            f_system  = system_info.get_date_audit()
            h_system  = system_info.get_time_audit()
            computer_name = system_info.get_machine_name()
            user    = system_info.get_current_user()
            last_f_systems = system_info.get_date_audit()
            last_h_systems = system_info.get_time_audit()
            last_computer_name = system_info.get_machine_name()
            last_user    = system_info.get_current_user()
            
            # 2. Validación básica de campos obligatorios
            if not code:
                QMessageBox.warning(self, "Validación", "El Código del cliente es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_clients (
                clt_Codigo, clt_Descripcion, clt_IDfiscal, clt_Status, clt_DireccionF, 
                clt_DireccionL, clt_Telefono1, clt_Telefono2, clt_Representante, clt_IDRepresentante, 
                clt_TelefonoContacto, clt_EmailContacto, clt_EmailEmpresa, clt_TipoContribuyente, clt_Origen, 
                clt_CodigoOrigen, clt_FechaCreacion,
                clt_SystemDate, clt_SystemTime, clt_NameMachine, clt_UserCreator,
                clt_LastUpdateDate, clt_LastUpdateTime, clt_LastMachine, clt_UserLastUpdate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = (
                    code, description, tax_id, status, direccion_f, 
                    direccion_l, tel1, tel2, rep, id_rep, 
                    tel_cont, email_cont, email_emp, tipo_cont, origen, 
                    code_orig, creation_date,
                    f_system, h_system, computer_name, user, # Creación
                    last_f_systems, last_h_systems, last_computer_name, last_user  # Última actualización
                )

            # 5. Ejecución mediante el DatabaseManager
            exito = self.db_manager.execute_query(sql, params)

            if exito:
                logging.info(f"Cliente guardado exitosamente: {code}")
                QMessageBox.information(self, "Éxito", f"El cliente '{code}' ha sido registrado correctamente.")
                self.clear_form_clients() # Función que haremos a continuación
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el registro en la base de datos.")

        except Exception as e:
            logging.error(f"Error crítico en save_clients: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")
    
    # ============LIMPEZA DE FORMULARIO CLIENTES
    
    def clear_form_clients(self):
        """
        Resetea todos los campos del formulario de clientes a sus valores iniciales.
        """
        # 1. Limpiar QLineEdits y QTextEdits
        self.ui.lineEdit_clt_code.clear()
        self.ui.lineEdit_clt_description.clear()
        self.ui.lineEdit_clt_idfiscal.clear()
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
        self.ui.lineEdit_clt_code.setFocus()
        
        logging.info("Formulario de clientes limpiado.")
    
    # ============INSERT  DE DATOS CATEGORIES
    
    def save_categories(self):
        """
        Recopila los datos del formulario frm_form_categories e inserta
        un nuevo registro en la tabla ark_action_categories.
        """
        try:
            # 1. Recolección de datos desde frm_actions_categories
            code            = self.ui.lineEdit_cat_code.text().strip()
            description     = self.ui.lineEdit_act_description.text().strip()
            status          = self.ui.cmb_cat_status.currentIndex()
            descriptiontec  = self.ui.textEdit_act_descriptiontec.toPlainText().strip()
            create_date     = self.ui.dateEdit_act_create_date.date().toString("yyyy-MM-dd")
            
            # Seccion de auditoría del sistema
            f_system            = system_info.get_date_audit()
            h_system            = system_info.get_time_audit()
            computer_name       = system_info.get_machine_name()
            user                = system_info.get_current_user()
            last_f_systems      = system_info.get_date_audit()
            last_h_systems      = system_info.get_time_audit()
            last_computer_name  = system_info.get_machine_name()
            last_user           = system_info.get_current_user()

            # 2. Validación básica de campos obligatorios
            if not code:
                QMessageBox.warning(self, "Validación", "El Código de la categoría es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_action_categories (
                cat_Codigo, cat_Descripcion, cat_Status, cat_DescripcionTec, cat_FechaCreacion,
                cat_SystemDate, cat_SystemTime, cat_NameMachine, cat_UserCreator,
                cat_LastUpdateDate, cat_LastUpdateTime, cat_LastMachine, cat_UserLastUpdate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = (
                code, description, status,
                descriptiontec, create_date, f_system, h_system, computer_name, user,
                last_f_systems, last_h_systems, last_computer_name, last_user   
            )

            # 5. Ejecución mediante el DatabaseManager
            # execute_query retorna el cursor si fue exitoso, o None si falló
            exito = self.db_manager.execute_query(sql, params)

            if exito:
                logging.info(f"Categoría guardada exitosamente: {code}")
                QMessageBox.information(self, "Éxito", f"La Categoría '{code}' ha sido registrada correctamente.")
                self.clear_form_categories() # Función que haremos a continuación
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el registro en la base de datos.")

        except Exception as e:
            logging.error(f"Error crítico en save_categories: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")

    # ============LIMPEZA DE FORMULARIO CATEGORIES

    def clear_form_categories(self):
        """
        Resetea todos los campos del formulario de categorías a sus valores iniciales.
        """
        # 1. Limpiar QLineEdits y QTextEdits
        self.ui.lineEdit_cat_code.clear()
        self.ui.lineEdit_cat_descripcion.clear()
        self.ui.textEdit_act_descriptiontec.clear()
        # 2. Resetear QComboBoxes al primer elemento (índice 0)
        self.ui.cmb_cat_status.setCurrentIndex(0)
        # 3. Resetear QDateEdit a la fecha actual
        self.ui.dateEdit_cat_fechacreacion.setDate(QDate.currentDate())

        # 4. (Opcional) Poner el foco de nuevo en el primer campo
        self.ui.lineEdit_cat_code.setFocus()
        
        logging.info("Formulario de categorías  limpiado.")  

    # ============INSERT  DE DATOS UNIDADES FUNCIONALES
    def save_functional_units(self):
        """
        Recopila los datos del formulario frm_functional_units e inserta
        un nuevo registro en la tabla ark_functional_units.
        """
        try:
            # 1. Recolección de datos desde frm_actions_categories
            code            = self.ui.lineEdit_fun_code.text().strip()
            description     = self.ui.lineEdit_fun_description.text().strip()
            status          = self.ui.cmb_fun_status.currentIndex()
            descriptiontec  = self.ui.textEdit_fun_descriptiontec.toPlainText().strip()
            create_date     = self.ui.dateEdit_fun_create_date.date().toString("yyyy-MM-dd")
            
            
            # Seccion de auditoría del sistema
            f_system  = system_info.get_date_audit()
            h_system  = system_info.get_time_audit()
            computer_name = system_info.get_machine_name()
            user    = system_info.get_current_user()
            last_f_systems = system_info.get_date_audit()
            last_h_systems = system_info.get_time_audit()
            last_computer_name = system_info.get_machine_name()
            last_user    = system_info.get_current_user()

            # 2. Validación básica de campos obligatorios
            if not code:
                QMessageBox.warning(self, "Validación", "El Código de la acción es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_functional_units (
                fun_Codigo, fun_Descripcion, fun_Status, fun_DescripcionTec, fun_FechaCreacion,
                fun_SystemDate, fun_SystemTime, fun_NameMachine, fun_UserCreator,
                fun_LastUpdateDate, fun_LastUpdateTime, fun_LastMachine, fun_UserLastUpdate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = (
                code, description, status, descriptiontec, create_date,
                f_system, h_system, computer_name, user,
                last_f_systems, last_h_systems, last_computer_name, last_user
            )

            # 5. Ejecución mediante el DatabaseManager
            # execute_query retorna el cursor si fue exitoso, o None si falló
            exito = self.db_manager.execute_query(sql, params)

            if exito:
                logging.info(f"Unidad guardada exitosamente: {code}")
                QMessageBox.information(self, "Éxito", f"La Unidad '{code}' ha sido registrada correctamente.")
                self.clear_form_functional_units() # Función que haremos a continuación
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el registro en la base de datos.")

        except Exception as e:
            logging.error(f"Error crítico en save_currencies: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")
    
    # ============LIMPEZA DE FORMULARIO UNIDADES FUNCIONALES
    def clear_form_functional_units(self):
        """
        Resetea todos los campos del formulario de monedas a sus valores iniciales.
        """
        # 1. Limpiar QLineEdits y QTextEdits
        self.ui.lineEdit_fun_code.clear()
        self.ui.lineEdit_fun_description.clear()
        self.ui.textEdit_fun_descriptiontec.clear()
        self.ui.cmb_fun_status.setCurrentIndex(0)
        self.ui.dateEdit_fun_create_date.setDate(QDate.currentDate())

        # 5. (Opcional) Poner el foco de nuevo en el primer campo
        self.ui.lineEdit_fun_code.setFocus()
        
        logging.info("Formulario de unidades limpiado.")
    
    # ============INSERT DE DATOS ACCIONES
    
    def save_actions(self):
        """
        Recopila los datos del formulario frm_actions e inserta
        un nuevo registro en la tabla ark_actions.
        """
        try:
            # 1. Recolección de datos desde frm_actions_categories
            code            = self.ui.lineEdit_act_code.text().strip()
            description     = self.ui.lineEdit_act_description.text().strip()
            status          = self.ui.cmb_act_status.currentIndex()
            descriptiontec  = self.ui.textEdit_act_descriptiontec.toPlainText().strip()
            categoria       = self.id_categoria_seleccionada  # ID de la categoría vinculada            
            create_date     = self.ui.dateEdit_act_create_date.date().toString("yyyy-MM-dd")
            
            # Seccion de auditoría del sistema
            f_system  = system_info.get_date_audit()
            h_system  = system_info.get_time_audit()
            computer_name = system_info.get_machine_name()
            user    = system_info.get_current_user()
            last_f_systems = system_info.get_date_audit()
            last_h_systems = system_info.get_time_audit()
            last_computer_name = system_info.get_machine_name()
            last_user    = system_info.get_current_user()

            # 2. Validación básica de campos obligatorios
            if not code:
                QMessageBox.warning(self, "Validación", "El Código de la acción es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_actions (
                act_Codigo, act_Descripcion, act_Status, act_DescripcionTec,
                id_category, act_FechaCreacion,
                act_SystemDate, act_SystemTime, act_NameMachine, act_UserCreator,
                act_LastUpdateDate, act_LastUpdateTime, act_LastMachine, act_UserLastUpdate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = (
                code, description, status,
                descriptiontec, categoria, create_date,
                f_system, h_system, computer_name, user,
                last_f_systems, last_h_systems, last_computer_name, last_user
            )

            # 5. Ejecución mediante el DatabaseManager
            # execute_query retorna el cursor si fue exitoso, o None si falló
            exito = self.db_manager.execute_query(sql, params)

            if exito:
                logging.info(f"Acción guardada exitosamente: {code}")
                QMessageBox.information(self, "Éxito", f"La Acción '{code}' ha sido registrada correctamente.")
                self.clear_form_action() # Función que haremos a continuación
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el registro en la base de datos.")

        except Exception as e:
            logging.error(f"Error crítico en save_categories: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")

    # ============LIMPEZA DE FORMULARIO ACCIONES

    def clear_form_action(self):
        """
        Resetea todos los campos del formulario de acciones a sus valores iniciales.
        """
        # 1. Limpiar QLineEdits y QTextEdits
        self.ui.lineEdit_act_code.clear()
        self.ui.lineEdit_act_description.clear()
        self.ui.textEdit_act_descriptiontec.clear()
        self.ui.lineEdit_id_category.clear()
        # 2. Resetear QComboBoxes al primer elemento (índice 0)
        self.ui.cmb_act_status.setCurrentIndex(0)
        # 3. Resetear QDateEdit a la fecha actual
        self.ui.label_act_create_date.setDate(QDate.currentDate())

        # 4. (Opcional) Poner el foco de nuevo en el primer campo
        self.ui.lineEdit_act_code.setFocus()
        
        logging.info("Formulario de acciones limpiado.")  
                  
    # ============INSERT  DE DATOS CURRENCIES
    def save_currencies(self):
        """
        Recopila los datos del formulario frm_currencies e inserta
        un nuevo registro en la tabla ark_currencies.
        """
        try:
            # 1. Recolección de datos desde frm_actions_categories
            code          = self.ui.lineEdit_mda_code.text().strip()
            description     = self.ui.lineEdit_mda_description.text().strip()
            status          = self.ui.cmb_mda_status.currentIndex()
            iso4217         = self.ui.cmb_mda_iso4217.currentIndex()
            symbol         = self.ui.cmb_mda_symbol.currentText()
            operator        = self.ui.cmb_mda_operator.currentIndex()
            creation_date      = self.ui.dateEdit_mda_creationdate.date().toString("yyyy-MM-dd")
            fecha_update    = self.ui.dateEdit_mda_update_date.date().toString("yyyy-MM-dd")
            fecha_lastup    = self.ui.dateEdit_mda_last_date.date().toString("yyyy-MM-dd")
            factor_activo   = self.ui.dsb_mda_activefactor.value()
            factor_pasivo   = self.ui.dsb_mda_passivefactor.value()
            
            # Seccion de auditoría del sistema
            f_system  = system_info.get_date_audit()
            h_system  = system_info.get_time_audit()
            computer_name = system_info.get_machine_name()
            user    = system_info.get_current_user()
            last_f_systems = system_info.get_date_audit()
            last_h_systems = system_info.get_time_audit()
            last_computer_name = system_info.get_machine_name()
            last_user    = system_info.get_current_user()
            

            # 2. Validación básica de campos obligatorios
            if not code:
                QMessageBox.warning(self, "Validación", "El Código de la acción es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_currencies (
                mda_Codigo, mda_Descripcion, mda_Status, mda_ISO4217, mda_Simbolo, 
                mda_OperadorCalculo, mda_FechaCreacion, mda_FechaActualizacion, mda_FechaUltima, mda_FactorActivo, 
                mda_FactorPasivo,
                mda_SystemDate, mda_SystemTime, mda_NameMachine, mda_UserCreator,
                mda_LastUpdateDate, mda_LastUpdateTime, mda_LastMachine, mda_UserLastUpdate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = (
                code, description, status, iso4217, symbol, operator,
                creation_date, fecha_update, fecha_lastup, factor_activo, factor_pasivo,
                f_system, h_system, computer_name, user,
                last_f_systems, last_h_systems, last_computer_name, last_user
            )

            # 5. Ejecución mediante el DatabaseManager
            # execute_query retorna el cursor si fue exitoso, o None si falló
            exito = self.db_manager.execute_query(sql, params)

            if exito:
                logging.info(f"Moneda guardada exitosamente: {code}")
                QMessageBox.information(self, "Éxito", f"La Moneda '{code}' ha sido registrada correctamente.")
                self.clear_form_currencies() # Función que haremos a continuación
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el registro en la base de datos.")

        except Exception as e:
            logging.error(f"Error crítico en save_currencies: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")
    
    # ============LIMPEZA DE FORMULARIO MONEDAS
    def clear_form_currencies(self):
        """
        Resetea todos los campos del formulario de monedas a sus valores iniciales.
        """
        # 1. Limpiar QLineEdits y QTextEdits
        self.ui.lineEdit_mda_code.clear()
        self.ui.lineEdit_mda_description.clear()
        # 2. Resetear QComboBoxes al primer elemento (índice 0)
        self.ui.cmb_mda_status.setCurrentIndex(0)
        self.ui.cmb_mda_iso4217.setCurrentIndex(0)
        self.ui.cmb_mda_symbol.setCurrentIndex(0)
        self.ui.cmb_mda_operator.setCurrentIndex(0)
        # 3. Resetear QDateEdit a la fecha actual
        self.ui.dateEdit_mda_creationdate.setDate(QDate.currentDate())
        self.ui.dateEdit_mda_update_date.setDate(QDate.currentDate())
        self.ui.dateEdit_mda_last_date.setDate(QDate.currentDate())

        # 4. Resetear QDoubleSpinBox a 0.00
        self.ui.dsb_mda_activefactor.setValue(0.00)
        self.ui.dsb_mda_passivefactor.setValue(0.00)

        # 5. (Opcional) Poner el foco de nuevo en el primer campo
        self.ui.lineEdit_mda_code.setFocus()
        
        logging.info("Formulario de monedas limpiado.")
         
    # ============INSERT  DE TIPOS DISPOSITIVOS
    def save_device_types(self):
        """
        Recopila los datos del formulario frm_device_types e inserta
        un nuevo registro en la tabla ark_device_types.
        """
        try:
            # 1. Recolección de datos desde frm_device_types
            code          = self.ui.lineEdit_dty_code.text().strip()
            description     = self.ui.lineEdit_dty_description.text().strip()
            status          = self.ui.cmb_dty_status.currentIndex()
            descriptiontec  = self.ui.textEdit_dty_descriptiontech.toPlainText().strip()
            creation_date      = self.ui.dateEdit_dty_creationdate.date().toString("yyyy-MM-dd")

            # Seccion de auditoría del sistema
            f_system  = system_info.get_date_audit()
            h_system  = system_info.get_time_audit()
            computer_name = system_info.get_machine_name()
            user    = system_info.get_current_user()
            last_f_systems = system_info.get_date_audit()
            last_h_systems = system_info.get_time_audit()
            last_computer_name = system_info.get_machine_name()
            last_user    = system_info.get_current_user()

            # 2. Validación básica de campos obligatorios
            if not code:
                QMessageBox.warning(self, "Validación", "El Código del tipo de dispositivo es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_device_types (
                dty_Codigo, dty_Descripcion, dty_Status, dty_DescripcionTec, dty_FechaCreacion, 
                dty_SystemDate, dty_SystemTime, dty_NameMachine, dty_UserCreator,
                dty_LastUpdateDate, dty_LastUpdateTime, dty_LastMachine, dty_UserLastUpdate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = ( code, description, status, descriptiontec, creation_date,
                f_system, h_system, computer_name, user,
                last_f_systems, last_h_systems, last_computer_name, last_user
            )   
            # 5. Ejecución mediante el DatabaseManager
            # execute_query retorna el cursor si fue exitoso, o None si falló
            exito = self.db_manager.execute_query(sql, params)
            if exito:
                logging.info(f"Tipo de dispositivo guardado exitosamente: {code}")
                QMessageBox.information(self, "Éxito", f"El Tipo de Dispositivo '{code}' ha sido registrado correctamente.")
                self.clear_form_device_types() # Función que haremos a continuación
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el registro en la base de datos.")  
        except Exception as e:
            logging.error(f"Error crítico en save_device_types: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")
                
    # ============LIMPEZA DE FORMULARIO TIPOS DISPOSITIVOS
    def clear_form_device_types(self):  
        """
        Resetea todos los campos del formulario de tipos de dispositivos a sus valores iniciales.
        """
        # 1. Limpiar QLineEdits y QTextEdits
        self.ui.lineEdit_dty_code.clear()
        self.ui.lineEdit_dty_description.clear()
        self.ui.textEdit_dty_descriptiontech.clear()
        # 2. Resetear QComboBoxes al primer elemento (índice 0)
        self.ui.cmb_dty_status.setCurrentIndex(0)
        # 3. Resetear QDateEdit a la fecha actual
        self.ui.dateEdit_dty_creationdate.setDate(QDate.currentDate())
        # 4. (Opcional) Poner el foco de nuevo en el primer campo
        self.ui.lineEdit_dty_code.setFocus()
        logging.info("Formulario de tipos de dispositivos limpiado.")
    
    # ============INSERT  DE EMPLEADOS
    def save_employees(self):
        """
        Recopila los datos del formulario frm_employees e inserta
        un nuevo registro en la tabla ark_employees.
        """
        try:
            # 1. Recolección de datos desde frm_employees
            code            = self.ui.lineEdit_emy_code.text().strip()
            description     = self.ui.lineEdit_emy_description.text().strip()
            status          = self.ui.cmb_emy_status.currentIndex()
            idemployees     = self.ui.lineEdit_emy_idemployees.text().strip()
            phone           = self.ui.lineEdit_emy_phone.text().strip()
            position        = self.ui.lineEdit_emy_position.text().strip()
            client          = self.selected_customer_id  # ID dek cliente vinculado
            role            = self.ui.lineEdit_emy_role.text().strip()   
            email           = self.ui.lineEdit_emy_emailemployees.text().strip()
            password        = self.ui.lineEdit_emy_password.text().strip()
            creation_date   = self.ui.dateEdit_emy_creationdate.date().toString("yyyy-MM-dd")

            # Seccion de auditoría del sistema
            f_system  = system_info.get_date_audit()
            h_system  = system_info.get_time_audit()
            computer_name = system_info.get_machine_name()
            user    = system_info.get_current_user()
            last_f_systems = system_info.get_date_audit()
            last_h_systems = system_info.get_time_audit()
            last_computer_name = system_info.get_machine_name()
            last_user    = system_info.get_current_user()

            # 2. Validación básica de campos obligatorios
            if not code:
                QMessageBox.warning(self, "Validación", "El Código del empleado es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_employees (
                emy_Codigo, emy_Descripcion, emy_Status, emy_IDEmployees, emy_Telefono1, 
                emy_Cargo, emy_Cliente, emy_Rol, emy_EmailUsuario, emy_Password, emy_FechaCreacion,
                emp_SystemDate, emp_SystemTime, emp_NameMachine, emp_UserCreator,
                emp_LastUpdateDate, emp_LastUpdateTime, emp_LastMachine, emp_UserLastUpdate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = ( code, description, status, idemployees, phone,  
                      position, client, role, email, password, creation_date,
                      f_system, h_system, computer_name, user,
                      last_f_systems, last_h_systems, last_computer_name, last_user
            )
            # 5. Ejecución mediante el DatabaseManager
            # execute_query retorna el cursor si fue exitoso, o None si falló   
            cursor = self.db_manager.execute_query(sql, params)
            if cursor:
                QMessageBox.information(self, "Éxito", "Empleado guardado correctamente.")
                logging.info("Empleado guardado exitosamente.")
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el empleado.")
                logging.error("Error al guardar el empleado.")
        except Exception as e:
            logging.error(f"Error crítico en guardar_employees: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")    
    # ============LIMPEZA DE FORMULARIO EMPLEADOS
    def clear_form_employees(self): 
        """
        Resetea todos los campos del formulario de empleados a sus valores iniciales.
        """
        # 1. Limpiar QLineEdits y QTextEdits
        self.ui.lineEdit_emy_code.clear()
        self.ui.lineEdit_emy_description.clear()
        self.ui.lineEdit_emy_idemployees.clear()
        self.ui.lineEdit_emy_phone.clear()
        self.ui.lineEdit_emy_position.clear()
        self.ui.lineEdit_emy_role.clear()
        self.ui.lineEdit_emy_emailemployees.clear()
        self.ui.lineEdit_emy_password.clear()
        self.ui.lineEdit_emy_id_client.clear()        
        # 2. Resetear QComboBoxes al primer elemento (índice 0)
        self.ui.cmb_emy_status.setCurrentIndex(0)
        # 3. Resetear QDateEdit a la fecha actual
        self.ui.dateEdit_emy_creationdate.setDate(QDate.currentDate())
        # 4. (Opcional) Poner el foco de nuevo en el primer campo
        self.ui.lineEdit_emy_code.setFocus()
        logging.info("Formulario de empleados limpiado.")
    
    # ============INSERT DE RECURSOS
    def save_it_assets(self):
        """
        Recopila los datos del formulario frm_it_assets e inserta
        un nuevo registro en la tabla ark_it_assets.
        """
        try:
            # 1. Recolección de datos desde frm_it_assets
            code            = self.ui.lineEdit_ita_code.text().strip()
            description     = self.ui.lineEdit_ita_description.text().strip()
            brand           = self.ui.lineEdit_ita_brand.text().strip()        
            descriptiontec  = self.ui.textEdit_ita_technical_description.toPlainText().strip()
            classification  = self.ui.cmb_ita_classification.currentIndex()
            status          = self.ui.cmb_ita_status.currentIndex()
            notestec        = self.ui.textEdit_ita_technical_description.toPlainText().strip()
            mac             = self.ui.lineEdit_ita_macadrees.text().strip()
            ip              = self.ui.lineEdit_ita_ipadrees.text().strip()
            units           = self.ui.lineEdit_ita_id_functional_units.text().strip()
            role            = self.ui.lineEdit_ita_role.text().strip()
            idRDP1          = self.ui.lineEdit_ita_idRDP1.text().strip()
            idRDP2          = self.ui.lineEdit_ita_idRDP2.text().strip()
            iprdp           = self.ui.lineEdit_ita_iprdp.text().strip()
            id_employees    = self.ui.lineEdit_ita_id_employees.text().strip()
            creation_date   = self.ui.dateEdit_ita_creationdate.date().toString("yyyy-MM-dd")

            # Seccion de auditoría del sistema
            f_system  = system_info.get_date_audit()
            h_system  = system_info.get_time_audit()
            computer_name = system_info.get_machine_name()
            user    = system_info.get_current_user()
            last_f_systems = system_info.get_date_audit()
            last_h_systems = system_info.get_time_audit()
            last_computer_name = system_info.get_machine_name()
            last_user    = system_info.get_current_user()

            # 2. Validación básica de campos obligatorios
            if not code:
                QMessageBox.warning(self, "Validación", "El Código del activo es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_it_assets (
                ita_Codigo, ita_Descripcion, ita_marca, ita_Clasificacion, ita_Status, 
                ita_DescripcionTec, ita_NotasTech, ita_macadrees, ita_ipadrees, ita_functional_units,
                ita_Rol, ita_idRDP1, ita_idRDP2, ita_iprdp, ita_idemployees, ita_FechaCreacion,
                res_SystemDate, res_SystemTime, res_NameMachine, res_UserCreator,
                res_LastUpdateDate, res_LastUpdateTime, res_LastMachine, res_UserLastUpdate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
        # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = ( code, description, brand, descriptiontec, classification, status, notestec, mac,  
                      ip, units, role, idRDP1, idRDP2, iprdp, id_employees, creation_date,
                      f_system, h_system, computer_name, user,
                      last_f_systems, last_h_systems, last_computer_name, last_user
            )
            # 5. Ejecución mediante el DatabaseManager
            # execute_query retorna el cursor si fue exitoso, o None si falló   
            cursor = self.db_manager.execute_query(sql, params)
            if cursor:
                QMessageBox.information(self, "Éxito", "Activo guardado correctamente.")
                logging.info("Activo guardado exitosamente.") 
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar el activo.")
                logging.error("Error al guardar el activo.")
        except Exception as e:
            logging.error(f"Error crítico en save_assets: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")
    # ============LIMPEZA DE FORMULARIO RECURSOS
    def clear_form_assets(self): 
        """
        Resetea todos los campos del formulario de recursos a sus valores iniciales.
        """
        # 1. Limpiar QLineEdits y QTextEdits
        self.ui.lineEdit_ita_code.clear()
        self.ui.lineEdit_ita_description.clear()
        self.ui.lineEdit_ita_brand.clear()        
        self.ui.textEdit_ita_technical_description.clear()
        self.ui.lineEdit_ita_macadrees.clear()
        self.ui.lineEdit_ita_ipadrees.clear()
        self.ui.lineEdit_ita_id_functional_units.clear()
        self.ui.lineEdit_ita_role.clear()
        self.ui.lineEdit_ita_idRDP1.clear()
        self.ui.lineEdit_ita_idRDP2.clear()
        self.ui.lineEdit_ita_iprdp.clear()
        self.ui.lineEdit_ita_id_employees.clear()        
        # 2. Resetear QComboBoxes al primer elemento (índice 0)
        self.ui.cmb_ita_classification.setCurrentIndex(0)
        self.ui.cmb_ita_status.setCurrentIndex(0)
        # 3. Resetear QDateEdit a la fecha actual
        self.ui.dateEdit_ita_creationdate.setDate(QDate.currentDate())
        # 4. (Opcional) Poner el foco de nuevo en el primer campo
        self.ui.lineEdit_ita_code.setFocus()
        logging.info("Formulario de activos limpiado.")
        
    # ============INSERT DE JOB TITLES 
    
    def save_job_titles(self):
        """
        Recopila los datos del formulario frm_job_titles e inserta
        un nuevo registro en la tabla ark_job_titles.
        """
        try:
            # 1. Recolección de datos desde frm_job_titles
            code            = self.ui.lineEdit_job_code.text().strip()
            description     = self.ui.lineEdit_job_description.text().strip()
            status          = self.ui.cmb_job_status.currentIndex()
            description_tec = self.ui.textEdit_job_descriptiontec.toPlainText().strip()
            create_date     = self.ui.dateEdit_job_creationdate.date().toString("yyyy-MM-dd")

            # Seccion de auditoría del sistema
            f_system  = system_info.get_date_audit()
            h_system  = system_info.get_time_audit()
            computer_name = system_info.get_machine_name()
            user    = system_info.get_current_user()
            last_f_systems = system_info.get_date_audit()
            last_h_systems = system_info.get_time_audit()
            last_computer_name = system_info.get_machine_name()
            last_user    = system_info.get_current_user()

            # 2. Validación básica de campos obligatorios
            if not code:
                QMessageBox.warning(self, "Validación", "El Código de la profesión es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_job_titles (
                job_Codigo, job_Descripcion, job_Status, job_DescripcionTec, job_FechaCreacion,
                job_SystemDate, job_SystemTime, job_NameMachine, job_UserCreator,
                job_LastUpdateDate, job_LastUpdateTime, job_LastMachine, job_UserLastUpdate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = ( code, description, status, description_tec, create_date,
                       f_system, h_system, computer_name, user,
                       last_f_systems, last_h_systems, last_computer_name, last_user)
    
           # 5. Ejecución mediante el DatabaseManager
           # execute_query retorna el cursor si fue exitoso, o None si falló   
            cursor = self.db_manager.execute_query(sql, params)
            if cursor:
                QMessageBox.information(self, "Éxito", "Profesión guardada correctamente.")
                logging.info("Profesión guardada exitosamente.")
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar la profesión.")
                logging.error("Error al guardar la profesión.")
        except Exception as e:
            logging.error(f"Error crítico en save_job_titles: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")
    
    # ============LIMPEZA DE FORMULARIO PROFESSION
    
    def clear_form_job_titles(self): 
        """
        Resetea todos los campos del formulario de profesiones a sus valores iniciales.
        """
        # 1. Limpiar QLineEdits y QTextEdits
        self.ui.lineEdit_job_code.clear()
        self.ui.lineEdit_job_description.clear()
        self.ui.textEdit_job_descriptiontec.clear()       
        # 2. Resetear QComboBoxes al primer elemento (índice 0)
        self.ui.cmb_job_status.setCurrentIndex(0)
        # 3. Resetear QDateEdit a la fecha actual
        self.ui.dateEdit_job_creationdate.setDate(QDate.currentDate())
        # 4. (Opcional) Poner el foco de nuevo en el primer campo
        self.ui.lineEdit_job_code.setFocus()
        logging.info("Formulario de profesiones limpiado.")
    
    # ============INSERT DE REQUESTS
    
    def save_requests(self):
        """
        Recopila los datos del formulario frm_requests e inserta
        un nuevo registro en la tabla ark_requests.
        """
        try:
            # 1. Recolección de datos desde frm_requests
            code            = self.ui.lineEdit_req_code.text().strip()
            description     = self.ui.lineEdit_req_description.text().strip()
            status          = self.ui.cmb_req_status.currentIndex()
            description_tec = self.ui.textEdit_req_descriptiontec.toPlainText().strip()
            client          = self.selected_customer_id  # ID del cliente vinculado
            create_date     = self.ui.dateEdit_req_creationdate.date().toString("yyyy-MM-dd")
            # Seccion de auditoría del sistema
            f_system  = system_info.get_date_audit()     
            h_system  = system_info.get_time_audit()
            computer_name = system_info.get_machine_name()
            user    = system_info.get_current_user()
            last_f_systems = system_info.get_date_audit()
            last_h_systems = system_info.get_time_audit()
            last_computer_name = system_info.get_machine_name()
            last_user    = system_info.get_current_user()
            
            # 2. Validación básica de campos obligatorios
            if not code:
                QMessageBox.warning(self, "Validación", "El Código de la solicitud es obligatorio.")
                return
            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_requests (
                req_Code, req_Description, req_Status, req_DescriptionTec, req_CodigoCliente,
                req_CreationDate, f_system, h_system, computer_name, user,
                last_f_systems, last_h_systems, last_computer_name, last_user
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = ( code, description, status, description_tec, client, create_date, 
                       f_system, h_system, computer_name, user,
                       last_f_systems, last_h_systems, last_computer_name, last_user)
              # 5. Ejecución mediante el DatabaseManager
            # execute_query retorna el cursor si fue exitoso, o None si falló
            cursor = self.db_manager.execute_query(sql, params)
            if cursor:
                QMessageBox.information(self, "Éxito", "Solicitud guardada correctamente.")
                logging.info("Solicitud guardada exitosamente.")    
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar la solicitud.")
                logging.error("Error al guardar la solicitud.")
        except Exception as e:
            logging.error(f"Error crítico en save_requests: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")
    
    # ============LIMPEZA DE FORMULARIO REQUESTS
    def clear_form_requests(self): 
        """
        Resetea todos los campos del formulario de solicitudes a sus valores iniciales.
        """
        # 1. Limpiar QLineEdits y QTextEdits
        self.ui.lineEdit_req_code.clear()
        self.ui.lineEdit_req_description.clear()
        self.ui.textEdit_req_descriptiontec.clear()       
        # 2. Resetear QComboBoxes al primer elemento (índice 0)
        self.ui.cmb_req_status.setCurrentIndex(0)
        # 3. Resetear QDateEdit a la fecha actual
        self.ui.dateEdit_req_creationdate.setDate(QDate.currentDate())
        # 4. (Opcional) Poner el foco de nuevo en el primer campo
        self.ui.lineEdit_req_code.setFocus()
        logging.info("Formulario de solicitudes limpiado.")
    # ============INSERT DE SESSIONS
    def save_sessions(self):
        """
        Recopila los datos del formulario frm_sessions e inserta
        un nuevo registro en la tabla ark_sessions.
        """
        try:
            # 1. Recolección de datos desde frm_sessions
            code            = self.ui.lineEdit_ses_number.text().strip()
            description     = self.ui.lineEdit_ses_clt_description.text().strip()
            clt_idfiscal    = self.ui.lineEdit_ses_clt_fiscal_id.text().strip()
            clt_code        = self.ui.lineEdit_ses_clt_code.text().strip()
            fiscaladdress   = self.ui.textEdit_ses_fiscaladdress.toPlainText().strip()
            clt_phone       = self.ui.lineEdit_ses_clt_phone.text().strip()
            clt_mobile      = self.ui.lineEdit_ses_clt_mobile.text().strip()
            status          = self.ui.cmb_ses_status.currentIndex()
            clt_employees   = self.ui.lineEdit_ses_clt_employees.text().strip()
            session_date    = self.ui.dateEdit_ses_sessionsdate.date().toString("yyyy-MM-dd")
            date_of_issue   = self.ui.dateEdit_ses_date_of_issue.date().toString("yyyy-MM-dd")
            start_time      = self.ui.timeEdit_ses_start_time.time().toString("HH:mm:ss")
            end_time        = self.ui.timeEdit_ses_end_time.time().toString("HH:mm:ss")
            total_hours     = self.ui.lineEdit_ses_total_time.text().strip()

            # Seccion de auditoría del sistema
            f_system  = system_info.get_date_audit()
            h_system  = system_info.get_time_audit()
            computer_name = system_info.get_machine_name()
            user    = system_info.get_current_user()
            last_f_systems = system_info.get_date_audit()
            last_h_systems = system_info.get_time_audit()
            last_computer_name = system_info.get_machine_name()
            last_user    = system_info.get_current_user()

            # 2. Validación básica de campos obligatorios
            if not code:
                QMessageBox.warning(self, "Validación", "El Código de la sesión es obligatorio.")
                return

            # 3. Preparación de la consulta SQL
            sql = """
            INSERT INTO ark_sessions (
                ses_numero, ses_clt_Descripcion, ses_clt_IDfiscal, ses_clt_Codigo, ses_clt_DireccionF, 
                ses_clt_Telefono1, ses_clt_Telefono2, ses_usr_Descripcion, ses_Status, ses_FechaSesion,
                ses_HoraInicial, ses_HoraFinal, ses_TotalHora
                ses_SystemDate, ses_SystemTime, ses_NameMachine, ses_UserCreator,
                ses_LastUpdateDate, ses_LastUpdateTime, ses_LastMachine, ses_UserLastUpdate
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            # 4. Tupla de parámetros (DEBE seguir el mismo orden que el INSERT)
            params = (code, description, clt_idfiscal, clt_code, fiscaladdress, clt_phone, 
                      clt_mobile, clt_employees,  status, session_date, date_of_issue,
                      start_time, end_time, total_hours,
                      f_system, h_system, computer_name, user,
                      last_f_systems, last_h_systems, last_computer_name, last_user)
            # 5. Ejecución mediante el DatabaseManager
            # execute_query retorna el cursor si fue exitoso, o None si falló
            cursor = self.db_manager.execute_query(sql, params)
            if cursor:  
                QMessageBox.information(self, "Éxito", "Sesión guardada correctamente.")
                logging.info("Sesión guardada exitosamente.")
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar la sesión.")
                logging.error("Error al guardar la sesión.")
        except Exception as e:
            logging.error(f"Error crítico en save_sessions: {str(e)}")
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error inesperado:\n{e}")
    # ============LIMPEZA DE FORMULARIO SESSIONS
    def clear_form_sessions(self):
        self.ui.lineEdit_ses_code.clear()
        self.ui.lineEdit_ses_description.clear()
        self.ui.cmb_ses_status.setCurrentIndex(0)
        self.ui.dateEdit_ses_creationdate.setDate(QDate.currentDate())
        self.ui.lineEdit_ses_code.setFocus()
        logging.info("Formulario de sesiones limpiado.")
        

    

    # ==================================FIN INSERT DE DATOS==================================
    
    # ==============================ACTIVACION DE BUSCADORES=================================
    
    def run_search_tool(self, titulo, sql, columnas):
        """
        Lógica centralizada para abrir cualquier buscador tipo lupa.
        Retorna una tupla (ID, Texto_Combinado) o (None, None)
        """
        dialogo = BuscadorBaseDialog(self.db_manager, titulo, sql, columnas)
        
        if dialogo.exec():
            return dialogo.id_seleccionado, dialogo.texto_combinado
        
        return None, None
    
    def open_search_categories(self):
        # 1. Definimos la configuración específica
        sql = "SELECT cat_IDauto, cat_Codigo, cat_Descripcion FROM ark_action_categories WHERE cat_Status = 0"
        columnas = ["ID", "Código", "Descripción"]
        
        # 2. Llamamos al motor genérico
        id_sel, texto_sel = self.run_search_tool("Categorías de Acciones", sql, columnas)
        
        # 3. Si el user eligió algo, actualizamos la App
        if id_sel is not None:
            self.id_categoria_selecconada = id_sel
            self.ui.lineEdit_act_id_category.setText(texto_sel)
            logging.info(f"Buscador: Seleccionado ID {id_sel}")
    
    def open_search_clients(self):
        # 1. Definimos la configuración específica
        sql = "SELECT clt_IDauto, clt_Codigo, clt_Descripcion FROM ark_clients WHERE clt_Status = 0"
        columnas = ["ID", "Código", "Descripción"]
        
        # 2. Llamamos al motor genérico
        id_sel, texto_sel = self.run_search_tool("Clients", sql, columnas)
        
        # 3. Si el user eligió algo, actualizamos la App
        if id_sel is not None:
            self.selected_customer_id = id_sel
            self.ui.lineEdit_emy_id_client.setText(texto_sel)
            logging.info(f"Buscador: Seleccionado ID {id_sel}")
    
    def open_search_functional_units(self):
        # 1. Definimos la configuración específica
        sql = "SELECT fun_IDauto, fun_Codigo, fun_Descripcion FROM ark_functional_units WHERE fun_Status = 0"
        columnas = ["ID", "Código", "Descripción"]
        
        # 2. Llamamos al motor genérico
        id_sel, texto_sel = self.run_search_tool("Functional Units", sql, columnas)
        
        # 3. Si el user eligió algo, actualizamos la App
        if id_sel is not None:
            self.selected_functional_unit_id = id_sel
            self.ui.lineEdit_ita_id_functional_units.setText(texto_sel)
            logging.info(f"Buscador: Seleccionado ID {id_sel}")
    
    def open_search_employees(self):
        # 1. Definimos la configuración específica
        sql = "SELECT emy_IDauto, emy_Codigo, emy_Descripcion FROM ark_employees WHERE emy_Status = 0"
        columnas = ["ID", "Código", "Descripción"]
        
        # 2. Llamamos al motor genérico
        id_sel, texto_sel = self.run_search_tool("Employees", sql, columnas)
        
        # 3. Si el user eligió algo, actualizamos la App
        if id_sel is not None:
            self.selected_employee_id = id_sel
            self.ui.lineEdit_ita_id_employees.setText(texto_sel)
            logging.info(f"Buscador: Seleccionado ID {id_sel}") 
                
    def open_search_job_titles(self):
        # 1. Definimos la configuración específica
        sql = "SELECT job_IDauto, job_Codigo, job_Descripcion FROM ark_job_titles WHERE job_Status = 0"
        columnas = ["ID", "Código", "Descripción"]
        
        # 2. Llamamos al motor genérico
        id_sel, texto_sel = self.run_search_tool("Job Titles", sql, columnas)
        
        # 3. Si el user eligió algo, actualizamos la App
        if id_sel is not None:
            self.selected_job_title_id = id_sel
            self.ui.lineEdit_emy_position.setText(texto_sel)
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
        Muestra un mensaje informativo o de error al user.
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
        """Muestra el cuadro de diálogo y retorna True si el user confirma."""
        respuesta = QMessageBox.question(
            self, 
            "Confirmar Cancelación", 
            "¿Está seguro de cancelar la operación actual? Se perderán los cambios no guardados.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        return respuesta == QMessageBox.StandardButton.Yes

    # ------------------ MOSTRAR MENÚ PRINCIPAL ------------------
    def mover_menu(self):
        """Muestra u oculta el menú principal (frame_menu_main)."""
        # 1. Cerrar submenús para evitar conflictos visuales
        self.ui.frame_sub_hardware.setMaximumWidth(0)
        self.ui.frame_menu_transactions.setMaximumWidth(0)
        self.ui.frame_menu_archives.setMaximumWidth(0)
        self.ui.frame_menu_reports.setMaximumWidth(0)
        
        # 2. Determinar estado actual y objetivo
        width = self.ui.frame_menu_main.maximumWidth()
        target_width = 0 if width > 0 else 200  # Si está visible (200), ocultar (0). Si está oculto (0), mostrar (200).
        
        # 3. Crear y ejecutar animación
        self.animacion_menu = QPropertyAnimation(self.ui.frame_menu_main, b'maximumWidth')
        self.animacion_menu.setDuration(300)
        self.animacion_menu.setStartValue(width)
        self.animacion_menu.setEndValue(target_width)
        self.animacion_menu.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_menu.start()

    # ------------------ MOSTRAR SUBMENÚ DE HARDWARE ------------------
    def toggle_sub_hardware_menu(self):
        """Alterna la visibilidad del submenú de hardware (frame_sub_hardware)."""
        current_width_sub = self.ui.frame_sub_hardware.maximumWidth()
        
        # Definir anchos: Si abrimos submenú, cerramos menú principal (y viceversa)
        if current_width_sub == 0:
            end_width_sub = 200  # Mostrar submenú
            end_width_menu = 0   # Ocultar menú principal
        else:
            end_width_sub = 0    # Ocultar submenú
            end_width_menu = 200 # Mostrar menú principal

        # Animación submenú
        self.animacion_sub_hardware = QPropertyAnimation(self.ui.frame_sub_hardware, b'maximumWidth')
        self.animacion_sub_hardware.setDuration(300)
        self.animacion_sub_hardware.setStartValue(current_width_sub)
        self.animacion_sub_hardware.setEndValue(end_width_sub)
        self.animacion_sub_hardware.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_sub_hardware.start()
        
        # Animación menú principal
        self.animacion_menu = QPropertyAnimation(self.ui.frame_menu_main, b'maximumWidth')
        self.animacion_menu.setDuration(300)
        self.animacion_menu.setStartValue(self.ui.frame_menu_main.maximumWidth())
        self.animacion_menu.setEndValue(end_width_menu)
        self.animacion_menu.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_menu.start()
    # ------------------ MOSTRAR SUBMENÚ DE ARCHIVES ------------------
    def toggle_archives_menu(self):
        """
        Alterna la visibilidad del submenú de archivos (frame_menu_archives).
        Si el submenú está visible, lo oculta y muestra el menú principal.
        Si el submenú está oculto, lo muestra y oculta el menú principal.
        """
        current_width_archives = self.ui.frame_menu_archives.maximumWidth()
        
        if current_width_archives == 0:
            end_width_archives = 200  # Mostrar submenú
            end_width_menu = 0        # Ocultar menú principal
        else:
            end_width_archives = 0    # Ocultar submenú
            end_width_menu = 200      # Mostrar menú principal

        self.animacion_archives = QPropertyAnimation(self.ui.frame_menu_archives, b'maximumWidth')
        self.animacion_archives.setDuration(300)
        self.animacion_archives.setStartValue(current_width_archives)
        self.animacion_archives.setEndValue(end_width_archives)
        self.animacion_archives.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_archives.start()

        self.animacion_menu = QPropertyAnimation(self.ui.frame_menu_main, b'maximumWidth')
        self.animacion_menu.setDuration(300)
        self.animacion_menu.setStartValue(self.ui.frame_menu_main.maximumWidth())
        self.animacion_menu.setEndValue(end_width_menu)
        self.animacion_menu.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_menu.start()
    # ------------------ MOSTRAR SUBMENÚ DE SYSTEMS  ------------------
    def toggle_systems_menu(self):
        """
        Alterna la visibilidad del submenú de sistemas (frame_menu_systems).
        Si el submenú está visible, lo oculta y muestra el menú principal (frame_menu_main).
        Si el submenú está oculto, lo muestra y oculta el menú principal.
        """
        current_width_systems = self.ui.frame_menu_systems.maximumWidth()
        
        if current_width_systems == 0:
            end_width_systems = 200  # Mostrar submenú
            end_width_menu = 0       # Ocultar menú principal
        else:
            end_width_systems = 0    # Ocultar submenú
            end_width_menu = 200     # Mostrar menú principal

        self.animacion_systems = QPropertyAnimation(self.ui.frame_menu_systems, b'maximumWidth')
        self.animacion_systems.setDuration(300)
        self.animacion_systems.setStartValue(current_width_systems)
        self.animacion_systems.setEndValue(end_width_systems)
        self.animacion_systems.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_systems.start()

        self.animacion_menu = QPropertyAnimation(self.ui.frame_menu_main, b'maximumWidth')
        self.animacion_menu.setDuration(300)
        self.animacion_menu.setStartValue(self.ui.frame_menu_main.maximumWidth())
        self.animacion_menu.setEndValue(end_width_menu)
        self.animacion_menu.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_menu.start()
    
    # ------------------ MOSTRAR SUBMENÚ DE TRANSACTIONS  ------------------
    def toggle_transactions_menu(self):
        """
        Alterna la visibilidad del submenú de transacciones (frame_menu_transactions).
        Si el submenú está visible, lo oculta y muestra el menú principal (frame_menu_main).
        Si el submenú está oculto, lo muestra y oculta el menú principal.
        """
        # Obtener el ancho actual del submenú de transacciones
        current_width_transactions = self.ui.frame_menu_transactions.maximumWidth()
        
        # Definir el ancho de la animación
        if current_width_transactions == 0:
            end_width_transactions = 200  # Mostrar el submenú
            end_width_menu = 0            # Ocultar el menú principal
        else:
            end_width_transactions = 0    # Ocultar el submenú
            end_width_menu = 200          # Mostrar el menú principal

        # Animación para el submenú de transacciones
        self.animacion_transactions = QPropertyAnimation(self.ui.frame_menu_transactions, b'maximumWidth')
        self.animacion_transactions.setDuration(300)
        self.animacion_transactions.setStartValue(current_width_transactions)
        self.animacion_transactions.setEndValue(end_width_transactions)
        self.animacion_transactions.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_transactions.start()

        # Animación para el menú principal
        self.animacion_menu = QPropertyAnimation(self.ui.frame_menu_main, b'maximumWidth')
        self.animacion_menu.setDuration(300)
        self.animacion_menu.setStartValue(self.ui.frame_menu_main.maximumWidth())
        self.animacion_menu.setEndValue(end_width_menu)
        self.animacion_menu.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_menu.start()
    # ------------------ MOSTRAR SUBMENÚ DE REPORTS  ------------------
    def toggle_reports_menu(self):
        """
        Alterna la visibilidad del submenú de reportes (frame_menu_reports).
        Si el submenú está visible, lo oculta y muestra el menú principal (frame_menu_main).
        Si el submenú está oculto, lo muestra y oculta el menú principal.
        """
        # Obtener el ancho actual del submenú de reportes
        current_width_reports = self.ui.frame_menu_reports.maximumWidth()
        
        # Definir el ancho de la animación
        if current_width_reports == 0:
            end_width_reports = 200  # Mostrar el submenú
            end_width_menu = 0       # Ocultar el menú principal
        else:
            end_width_reports = 0    # Ocultar el submenú
            end_width_menu = 200     # Mostrar el menú principal

        # Animación para el submenú de reportes
        self.animacion_reports = QPropertyAnimation(self.ui.frame_menu_reports, b'maximumWidth')
        self.animacion_reports.setDuration(300)
        self.animacion_reports.setStartValue(current_width_reports)
        self.animacion_reports.setEndValue(end_width_reports)
        self.animacion_reports.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_reports.start()

        # Animación para el menú principal
        self.animacion_menu = QPropertyAnimation(self.ui.frame_menu_main, b'maximumWidth')
        self.animacion_menu.setDuration(300)
        self.animacion_menu.setStartValue(self.ui.frame_menu_main.maximumWidth())
        self.animacion_menu.setEndValue(end_width_menu)
        self.animacion_menu.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_menu.start()
    # ------------------ MOSTRAR SUBMENÚ DE DISPONIBLE ------------------
    def toggle_disponible_menu(self):
        """
        Alterna la visibilidad del submenú de disponible (frame_disponible).
        Si el submenú está visible, lo oculta y muestra el menú principal.
        Si el submenú está oculto, lo muestra y oculta el menú principal.
        """
        # Obtener el ancho actual del submenú
        current_width_disponible = self.ui.frame_disponible.maximumWidth()
        
        # Definir el ancho de la animación (0 para ocultar, 200 para mostrar)
        if current_width_disponible == 0:
            end_width_disponible = 200  # Mostrar el submenú
            end_width_menu = 0          # Ocultar el menú principal
        else:
            end_width_disponible = 0    # Ocultar el submenú
            end_width_menu = 200         # Mostrar el menú principal

        # Animación para el submenú de disponible
        self.animacion_disponible = QPropertyAnimation(self.ui.frame_disponible, b'maximumWidth')
        self.animacion_disponible.setDuration(300)
        self.animacion_disponible.setStartValue(current_width_disponible)
        self.animacion_disponible.setEndValue(end_width_disponible)
        self.animacion_disponible.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_disponible.start()

        # Animación para el menú principal
        self.animacion_menu = QPropertyAnimation(self.ui.frame_menu_main, b'maximumWidth')
        self.animacion_menu.setDuration(300)
        self.animacion_menu.setStartValue(self.ui.frame_menu_main.maximumWidth())
        self.animacion_menu.setEndValue(end_width_menu)
        self.animacion_menu.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_menu.start()
    # ------------------ MOSTRAR SUBMENÚ DE SETTINGS ------------------
    def toggle_settings_menu(self):
        """
        Alterna la visibilidad del submenú de configuración (frame_settings).
        Si el submenú está visible, lo oculta y muestra el menú principal.
        Si el submenú está oculto, lo muestra y oculta el menú principal.
        """
        # Obtener el ancho actual del submenú
        current_width_settings = self.ui.frame_settings.maximumWidth()
        
        # Definir el ancho de la animación (0 para ocultar, 200 para mostrar)
        if current_width_settings == 0:
            end_width_settings = 200  # Mostrar el submenú
            end_width_menu = 0         # Ocultar el menú principal
        else:
            end_width_settings = 0     # Ocultar el submenú
            end_width_menu = 200       # Mostrar el menú principal

        # Animación para el submenú de configuración
        self.animacion_settings = QPropertyAnimation(self.ui.frame_settings, b'maximumWidth')
        self.animacion_settings.setDuration(300)
        self.animacion_settings.setStartValue(current_width_settings)
        self.animacion_settings.setEndValue(end_width_settings)
        self.animacion_settings.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_settings.start()

        # Animación para el menú principal
        self.animacion_menu = QPropertyAnimation(self.ui.frame_menu_main, b'maximumWidth')
        self.animacion_menu.setDuration(300)
        self.animacion_menu.setStartValue(self.ui.frame_menu_main.maximumWidth())
        self.animacion_menu.setEndValue(end_width_menu)
        self.animacion_menu.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animacion_menu.start()
    # ------------------ Cerrar Sesión  ------------------
    def toggle_logout(self):
        """
        Gestiona el cierre seguro de la aplicación con confirmación interactiva.
        """
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Cerrar Sesión")
        msg_box.setText("¿Estás seguro que deseas cerrar la aplicación?")
        msg_box.setInformativeText("Se perderán los cambios no guardados.")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)

        respuesta = msg_box.exec()

        if respuesta == QMessageBox.StandardButton.Yes:
            logging.info("El usuario ha confirmado el cierre de la aplicación.")
            self.close()

    # Función para volver al menú principal
    def volver_menu_principal(self):
        """
        Cierra todos los submenús y muestra el menú principal (frame_menu_main) con animaciones.
        """
        # Cerrar submenú de hardware
        if self.ui.frame_sub_hardware.maximumWidth() > 0:
            self.animacion_sub_hardware = QPropertyAnimation(self.ui.frame_sub_hardware, b'maximumWidth')
            self.animacion_sub_hardware.setDuration(300)
            self.animacion_sub_hardware.setStartValue(self.ui.frame_sub_hardware.maximumWidth())
            self.animacion_sub_hardware.setEndValue(0)
            self.animacion_sub_hardware.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animacion_sub_hardware.start()

        # Cerrar submenú de archivos
        if self.ui.frame_menu_archives.maximumWidth() > 0:
            self.animacion_archives = QPropertyAnimation(self.ui.frame_menu_archives, b'maximumWidth')
            self.animacion_archives.setDuration(300)
            self.animacion_archives.setStartValue(self.ui.frame_menu_archives.maximumWidth())
            self.animacion_archives.setEndValue(0)
            self.animacion_archives.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animacion_archives.start()

        # Cerrar submenú de transacciones
        if self.ui.frame_menu_transactions.maximumWidth() > 0:
            self.animacion_transactions = QPropertyAnimation(self.ui.frame_menu_transactions, b'maximumWidth')
            self.animacion_transactions.setDuration(300)
            self.animacion_transactions.setStartValue(self.ui.frame_menu_transactions.maximumWidth())
            self.animacion_transactions.setEndValue(0)
            self.animacion_transactions.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animacion_transactions.start()

        # Cerrar submenú de reportes
        if self.ui.frame_menu_reports.maximumWidth() > 0:
            self.animacion_reports = QPropertyAnimation(self.ui.frame_menu_reports, b'maximumWidth')
            self.animacion_reports.setDuration(300)
            self.animacion_reports.setStartValue(self.ui.frame_menu_reports.maximumWidth())
            self.animacion_reports.setEndValue(0)
            self.animacion_reports.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animacion_reports.start()

        # Cerrar submenú de sistemas
        if self.ui.frame_menu_systems.maximumWidth() > 0:
            self.animacion_systems = QPropertyAnimation(self.ui.frame_menu_systems, b'maximumWidth')
            self.animacion_systems.setDuration(300)
            self.animacion_systems.setStartValue(self.ui.frame_menu_systems.maximumWidth())
            self.animacion_systems.setEndValue(0)
            self.animacion_systems.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animacion_systems.start()

        # Mostrar menú principal si está oculto
        if self.ui.frame_menu_main.maximumWidth() == 0:
            self.animacion_menu = QPropertyAnimation(self.ui.frame_menu_main, b'maximumWidth')
            self.animacion_menu.setDuration(300)
            self.animacion_menu.setStartValue(0)
            self.animacion_menu.setEndValue(200)
            self.animacion_menu.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animacion_menu.start()

        # Cambiar a la página de inicio
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
        Permite mover la ventana cuando el user arrastra el mouse sobre el frame superior.
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
        Muestra la página de configuración del sistema y oculta el menú principal.
        """
        # 1. Si el menú principal está abierto, lo cerramos con animación
        if self.ui.frame_menu_main.maximumWidth() > 0:
            self.animacion_menu = QPropertyAnimation(self.ui.frame_menu_main, b'maximumWidth')
            self.animacion_menu.setDuration(300)
            self.animacion_menu.setStartValue(self.ui.frame_menu_main.maximumWidth())
            self.animacion_menu.setEndValue(0)
            self.animacion_menu.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animacion_menu.start()
            
        # 2. Cambiamos a la página de configuración
        self.ui.sw_consolas.setCurrentWidget(self.ui.page_inf_config)
        
    def aplicar_config_regional(self):
        """
        Llama al método de confirmación antes de aplicar la configuración regional.
        """
        logging.info("Se ha solicitado cambiar la configuración regional.")
        # Define una función anónima (lambda) para la acción.
        # Esta es la función que confirm_action ejecutará si el user dice "Sí".
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
        Es llamada por confirm_action después de que el user confirma.
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