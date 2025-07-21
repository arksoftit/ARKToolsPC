# arktoolspc.py

import tkinter as tk
from tkinter import ttk, Menu
from ttkthemes import ThemedTk

# Importamos las funciones desde system_info.py
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
    get_regional_settings
    )

class ARKToolsPCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ARKToolsPC - Diagnóstico de Hardware")
        self.root.geometry("800x600")
        self.root.minsize(800, 600)
        self.root.resizable(True, True)

        # Estilo
        self.style = ttk.Style()
        self.style.configure("TButton", padding=10, font=("Segoe UI", 10))
        self.style.configure("Header.TButton", font=("Segoe UI", 10, "bold"), padding=10)
        
        # Estilo para botón de salida
        self.style.configure("Exit.TButton",
                            font=("Segoe UI", 10, "bold"),
                            padding=10,
                            background="#ADD8E6",   # Azul claro
                            foreground="black")

        # Opcional: Cambiar color al presionar
        self.style.map("Exit.TButton",
                    background=[('active', '#87CEEB')])

        # Crear menú principal (MainMenu)
        self.create_main_menu()

        # Frame principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Área de contenido
        self.content_text = tk.Text(self.main_frame, wrap="word", bg="black", fg="white", font=("Consolas", 10))        
        self.content_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Botón Salir (en el área principal)
        exit_button_frame = ttk.Frame(self.main_frame)
        exit_button_frame.pack(side="bottom", fill="x", padx=10, pady=10)

        exit_button = ttk.Button(
            exit_button_frame,
            text="Salir de la Aplicación",
            style="Exit.TButton",     # Aplica el estilo personalizado
            command=self.exit_app
        )
        exit_button.pack(side="right", anchor="e")

        # Crear footer
        self.create_footer()

    def create_main_menu(self):
        """Crea el menú principal estilo MainMenu (como en Lazarus)"""
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # Menú "Archivo"
        archivo_menu = Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Nuevo")
        archivo_menu.add_command(label="Abrir")
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.exit_app)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

        # Menú "Herramientas"
        herramientas_menu = Menu(menubar, tearoff=0)
        hardware_menu = Menu(herramientas_menu, tearoff=0)

        # Submenú: Información del Hardware
        hardware_menu.add_command(label="Sistema", command=lambda: self.show_content(get_system_info))
        hardware_menu.add_command(label="CPU", command=lambda: self.show_content(get_cpu_info))
        hardware_menu.add_command(label="Memoria RAM", command=lambda: self.show_content(get_ram_info))
        hardware_menu.add_command(label="Disco", command=lambda: self.show_content(get_disk_info))
        hardware_menu.add_command(label="GPU", command=lambda: self.show_content(get_gpu_info))
        hardware_menu.add_command(label="Placa Base", command=lambda: self.show_content(get_motherboard_info))
        hardware_menu.add_command(label="Tarjetas de Red", command=lambda: self.show_content(get_nic_info))
        hardware_menu.add_command(label="Tarjetas de Audio", command=lambda: self.show_content(get_audio_devices))
        hardware_menu.add_command(label="Puertos COM", command=lambda: self.show_content(get_com_ports))
        hardware_menu.add_command(label="Dispositivos USB", command=lambda: self.show_content(get_usb_devices))
        hardware_menu.add_command(label="Dispositivos Bluetooth", command=lambda: self.show_content(get_bluetooth_devices))

        herramientas_menu.add_cascade(label="Información del Hardware", menu=hardware_menu)
        #herramientas_menu.add_command(label="Otra herramienta (pendiente)", command=lambda: self.show_placeholder("Herramienta Pendiente"))
        herramientas_menu.add_command(label="Información de Red", command=lambda: self.show_content(get_network_info))
        herramientas_menu.add_command(label="Información del Sistema Operativo", command=lambda: self.show_content(get_os_info))
        herramientas_menu.add_command(label="Configuración Regional", command=lambda: self.show_content(get_regional_settings))
        menubar.add_cascade(label="Herramientas", menu=herramientas_menu)
        
        # Menú "Informes"
        informes_menu = Menu(menubar, tearoff=0)
        sub_informes_menu = Menu(informes_menu, tearoff=0)

        sub_informes_menu.add_command(label="Informe de Hardware", command=lambda: self.show_placeholder("Informe de Hardware"))

        informes_menu.add_cascade(label="Generar Informe", menu=sub_informes_menu)
        menubar.add_cascade(label="Informes", menu=informes_menu)


        # Menú "Ayuda"
        ayuda_menu = Menu(menubar, tearoff=0)
        ayuda_menu.add_command(label="Acerca de...", command=self.show_about)
        menubar.add_cascade(label="Ayuda", menu=ayuda_menu)

    def show_content(self, func):
        """Muestra el resultado de una función en el área de texto"""
        from io import StringIO
        import sys

        old_stdout = sys.stdout
        redirected_output = StringIO()
        sys.stdout = redirected_output

        try:
            func()  # Ejecutar función
        finally:
            sys.stdout = old_stdout

        output = redirected_output.getvalue()
        self.content_text.delete(1.0, tk.END)
        self.content_text.insert(tk.END, output)
        self.content_text.see(tk.END)

    def show_placeholder(self, tool_name):
        """Muestra un mensaje temporal para herramientas no implementadas"""
        self.content_text.delete(1.0, tk.END)
        self.content_text.insert(tk.END, f"[PENDIENTE] {tool_name} - Funcionalidad aún no implementada.")

    def show_about(self):
        """Muestra información 'Acerca de...'"""
        self.content_text.delete(1.0, tk.END)
        about_text = (
            "ARKToolsPC - Diagnóstico de Hardware\n"
            "Versión: 1.0\n"
            "Desarrollado por: Arksoft Integradores de Sistemas, C.A.\n"
            "© 2025 Todos los derechos reservados\n\n"
            "Esta herramienta permite obtener información detallada del hardware del sistema."
        )
        self.content_text.insert(tk.END, about_text)

    def create_footer(self):
        """Crea el pie de página con información corporativa"""
        footer_frame = ttk.Frame(self.root)
        footer_frame.pack(side="bottom", fill="x")

        footer_texto = (
            "© 2025 Arksoft Integradores de Sistemas, C.A. RIF: J310994692 - Todos los derechos reservados\n"
            "Contacto: +58 424-3672111 | arksoft.sistemas@gmail.com"
        )

        footer_label = ttk.Label(
            footer_frame,
            text=footer_texto,
            justify="center",
            font=("Segoe UI", 9),
            padding=10,
            background="#f0f0f0",
            relief="flat",
            anchor="center",
            width=100
        )
        footer_label.pack(fill="x", padx=10, pady=5)

    def exit_app(self):
        """Cerrar la aplicación"""
        self.root.destroy()


if __name__ == "__main__":
    app_root = ThemedTk(theme="arc")  # Tema claro y moderno
    app = ARKToolsPCApp(app_root)
    app_root.mainloop()