# system_info.py Verision 1.0.6

from datetime import datetime
import platform
import psutil
import subprocess
import locale
import os
import winreg
import GPUtil

try:
    import wmi
except ImportError:
    wmi = None


import platform

def get_system_info():
    """
    Obtiene la información general del sistema y la retorna como una cadena de texto.
    """
    info_str = "\n=== INFORMACIÓN GENERAL DEL SISTEMA ===\n\n"
    try:
        import wmi
        c = wmi.WMI()
        
        # Información del Sistema
        system_info = c.Win32_ComputerSystem()[0]
        info_str += f"Nombre del Sistema: {system_info.Name}\n"
        info_str += f"Fabricante: {system_info.Manufacturer}\n"
        info_str += f"Modelo: {system_info.Model}\n"
        info_str += f"Tipo de Sistema: {system_info.SystemType}\n"
        info_str += f"Dominio/Grupo de Trabajo: {system_info.Domain}\n"
        info_str += f"Número de serie: {system_info.IdentifyingNumber}\n"
        info_str += "-" * 40 + "\n"
        
        # Información de la BIOS
        bios_info = c.Win32_BIOS()[0]
        info_str += f"Fabricante de BIOS: {bios_info.Manufacturer}\n"
        info_str += f"Versión: {bios_info.Version}\n"
        info_str += f"Número de Serie: {bios_info.SerialNumber}\n"
        info_str += f"Fecha de lanzamiento: {bios_info.ReleaseDate}\n"
        info_str += "-" * 40 + "\n"

    except Exception as e:
        info_str += f"Error al obtener información general del sistema: {e}"
        
    return info_str

# system_info.py

def get_cpu_info():
    """
    Obtiene la información detallada del procesador y la retorna como una cadena de texto.
    """
    info_str = "\n=== Información del Procesador ===\n\n"
    try:
        import wmi
        c = wmi.WMI()
        cpu_wmi = c.Win32_Processor()[0]
        
        info_str += f"Nombre: {cpu_wmi.Name.strip()}\n"
        info_str += f"Fabricante: {cpu_wmi.Manufacturer}\n"
        info_str += f"Arquitectura: {cpu_wmi.Architecture}\n"
        info_str += f"Núcleos lógicos: {cpu_wmi.NumberOfLogicalProcessors}\n"
        info_str += f"Núcleos físicos: {cpu_wmi.NumberOfCores}\n"
        info_str += f"Velocidad máxima: {cpu_wmi.MaxClockSpeed} MHz\n"
        info_str += f"Caché L2: {cpu_wmi.L2CacheSize} KB\n" if cpu_wmi.L2CacheSize else ""
        info_str += f"Caché L3: {cpu_wmi.L3CacheSize} KB\n" if cpu_wmi.L3CacheSize else ""
        info_str += f"Socket: {cpu_wmi.SocketDesignation}\n"
        info_str += "-" * 40 + "\n"
        
        # Uso de psutil para información adicional
        info_str += f"Uso actual: {psutil.cpu_percent(interval=1)}%\n"
        
    except Exception as e:
        info_str += f"No se pudo obtener información completa de la CPU: {e}"
        
    return info_str


def get_ram_info():
    """
    Obtiene la información de la memoria RAM y la retorna como una cadena de texto.
    """
    info_str = "\n=== Información de Memoria RAM ===\n\n"
    try:
        import wmi
        c = wmi.WMI()
        total_ram = psutil.virtual_memory().total
        info_str += f"Memoria total instalada: {round(total_ram / (1024**3), 2)} GB\n\n"
        
        for i, mem in enumerate(c.Win32_PhysicalMemory(), start=1):
            info_str += f"=== Módulo {i} ===\n"
            info_str += f"Banco: {mem.BankLabel}\n"
            info_str += f"Fabricante: {mem.Manufacturer}\n"
            info_str += f"Modelo: {mem.PartNumber.strip()}\n"
            info_str += f"Tamaño: {round(int(mem.Capacity) / (1024**3), 2)} GB\n"
            info_str += f"Velocidad: {mem.Speed} MHz\n"
            info_str += f"Número de Serie: {mem.SerialNumber.strip()}\n"
            info_str += "-" * 40 + "\n"
    except Exception as e:
        info_str += f"No se pudo obtener información de la RAM: {e}"
        
    return info_str

# Almacenamiento

def get_disk_info():
    """
    Obtiene la información de los discos físicos y la retorna como una cadena de texto.
    """
    info_str = "\n=== INFORMACION DE DISCOS FISICOS ===\n\n"
    try:
        import wmi
        c = wmi.WMI()
        disks = c.Win32_DiskDrive()
        total_storage_bytes = 0
        
        if not disks:
            info_str += "No se encontraron discos físicos."
            return info_str

        for disk in disks:
            try:
                info_str += f"\nModelo: {disk.Model or 'Desconocido'}\n"
                info_str += f"Fabricante: {disk.Manufacturer or 'Desconocido'}\n"
                info_str += f"Interfaz: {disk.InterfaceType or 'Desconocida'}\n"
                size_gb = round(int(disk.Size) / (1024**3), 2) if disk.Size else 'N/A'
                info_str += f"Tamaño total: {size_gb} GB\n"
                info_str += f"Tipo: {'SSD' if 'SSD' in str(disk.Model) else 'HDD'}\n"
                info_str += f"Número de Serie: {disk.SerialNumber.strip() if disk.SerialNumber else 'No disponible'}\n"
                info_str += "-" * 50 + "\n"
                if disk.Size:
                    total_storage_bytes += int(disk.Size)
            except Exception as e:
                info_str += f"⚠ Error al procesar disco {disk.DeviceID}: {e}\n"
                info_str += "-" * 50 + "\n"
                continue
                
        if total_storage_bytes > 0:
            total_gb = round(total_storage_bytes / (1024**3), 2)
            info_str += "\n=== RESUMEN DE ALMACENAMIENTO TOTAL ===\n"
            info_str += f"Almacenamiento total instalado: {total_gb} GB\n"
            info_str += "=" * 50 + "\n"

    except Exception as e:
        info_str += f"🚨 No se pudo obtener información completa de los discos: {e}"
        
    return info_str


def get_gpu_info():
    """
    Obtiene la información de la(s) tarjeta(s) gráfica(s) y la retorna como una cadena de texto.
    """
    info_str = "\n=== Información de Tarjeta(s) Gráfica(s) ===\n\n"
    try:
        import wmi
        c = wmi.WMI()
        for gpu in c.Win32_VideoController():
            info_str += f"Nombre: {gpu.Name}\n"
            info_str += f"Fabricante: {gpu.AdapterCompatibility}\n"
            info_str += f"Tipo de dispositivo: {gpu.VideoProcessor}\n"
            info_str += f"Versión del controlador: {gpu.DriverVersion}\n"
            pnp_id = getattr(gpu, 'PNPDeviceID', 'No disponible')
            info_str += f"Identificador Único (PNPDeviceID): {pnp_id}\n"
            ram_gb = round(int(gpu.AdapterRAM) / (1024**3), 2)
            info_str += f"Memoria dedicada: {ram_gb} GB\n"
            info_str += "-" * 40 + "\n"
    except Exception as e:
        info_str += f"No se pudo obtener información de la GPU: {e}"
    
    return info_str

def get_motherboard_info():
    """
    Obtiene la información de la placa base y la retorna como una cadena de texto.
    """
    info_str = "\n=== Información de la Placa Base ===\n\n"
    try:
        import wmi
        c = wmi.WMI()
        motherboard = c.Win32_BaseBoard()[0]
        
        info_str += f"Fabricante: {motherboard.Manufacturer}\n"
        info_str += f"Producto: {motherboard.Product}\n"
        info_str += f"Versión: {motherboard.Version}\n"
        info_str += f"Número de Serie: {motherboard.SerialNumber}\n"
        
    except IndexError:
        info_str += "No se pudo obtener información de la placa base."
    except Exception as e:
        info_str += f"Error al obtener información de la placa base: {e}"
        
    return info_str

# Netware

def get_network_info():
    """
    Obtiene y retorna la salida completa de 'ipconfig /all' como una cadena de texto.
    """
    output_text = "\n=== INFORMACIÓN COMPLETA DE RED ===\n\n"
    try:
        # Ejecutar el comando ipconfig /all
        result = subprocess.run(
            ["ipconfig", "/all"], 
            capture_output=True, 
            text=True, 
            encoding="cp850"
        )
        output_text += result.stdout
    except Exception as e:
        output_text += f"Error al obtener información de red: {e}"
        
    return output_text

# Hardware de red
def get_nic_info():
    """
    Obtiene y retorna información detallada sobre las tarjetas de red (NICs).
    """
    info_str = "\n=== TARJETAS DE RED (NICs) ===\n\n"
    try:
        import wmi
        c = wmi.WMI()

        nics = c.Win32_NetworkAdapter(PhysicalAdapter=True)

        # Diccionario de estados de conexión
        status_codes = {
            '1': 'Connecting',
            '2': 'Connected',
            '3': 'Disconnected',
            '4': 'Disconnecting',
            '5': 'Hardware not present',
            '6': 'Hardware disabled',
            '7': 'Hardware malfunction',
            '8': 'Media disconnected',
            '9': 'Authenticating',
            '10': 'Credential rejected',
            '11': 'Paused',
            '12': 'No Media',
            '13': 'Port blocked'
        }

        if not nics:
            info_str += "  No se encontraron tarjetas de red físicas.\n"
        else:
            for nic in nics:
                info_str += f"Tarjeta: {nic.NetConnectionID or 'Desconocido'}\n"
                info_str += f"  Modelo: {nic.Name}\n"
                info_str += f"  Fabricante: {nic.Manufacturer or 'Desconocido'}\n"
                info_str += f"  Dirección MAC: {nic.MACAddress or 'No disponible'}\n"
                info_str += f"  Tipo: {nic.AdapterType}\n"
                
                # Usamos el diccionario para traducir el código de estado
                status_code = str(nic.NetConnectionStatus)
                status_desc = status_codes.get(status_code, f"Desconocido ({status_code})")
                info_str += f"  Estado: {status_desc}\n"
                info_str += f"  Velocidad: {nic.Speed or 'Desconocida'} bps\n"
                info_str += "-" * 40 + "\n"

    except Exception as e:
        info_str += f"Error al obtener información de NICs: {e}\n"
        
    return info_str
        
# Hardware de audio

def get_audio_devices():
    """
    Obtiene la información de los dispositivos de audio y la retorna como una cadena de texto.
    """
    info_str = "\n=== Dispositivos de Audio ===\n\n"
    try:
        import wmi
        c = wmi.WMI()
        audio_devices = c.Win32_SoundDevice()
        if not audio_devices:
            info_str += "No se encontraron dispositivos de audio."
        else:
            for i, audio_device in enumerate(audio_devices):
                info_str += f"Dispositivo #{i+1}:\n"
                info_str += f"Nombre: {audio_device.Name}\n"
                info_str += f"Fabricante: {audio_device.Manufacturer}\n"
                info_str += f"ID de Producto: {audio_device.ProductName}\n"
                info_str += f"Estado: {audio_device.Status}\n"
                info_str += "-" * 40 + "\n"
    except Exception as e:
        info_str += f"No se pudo obtener la información de los dispositivos de audio: {e}"

    return info_str

# Puertos usb

def get_usb_devices():
    """
    Obtiene y retorna la información de dispositivos USB conectados.
    """
    info_str = "\n=== DISPOSITIVOS USB CONECTADOS ===\n\n"
    try:
        import wmi
        c = wmi.WMI()
        devices = c.Win32_PnPEntity()

        usb_devices = [d for d in devices if "USB" in str(d.Description or "")]

        if not usb_devices:
            info_str += "  No hay dispositivos USB conectados.\n"
        else:
            for device in usb_devices:
                info_str += f"Dispositivo: {device.Description}\n"
                if device.Name:
                    info_str += f"  Nombre: {device.Name}\n"
                if device.DeviceID:
                    info_str += f"  ID del dispositivo: {device.DeviceID}\n"
                if device.Status:
                    info_str += f"  Estado: {device.Status}\n"
                info_str += "-" * 40 + "\n"

    except Exception as e:
        info_str += f"Error al obtener información de dispositivos USB: {e}\n"
        
    return info_str
        
# Puertos COM
        
def get_com_ports():
    """
    Obtiene los puertos COM del sistema y la retorna como una cadena de texto.
    """
    info_str = "\n=== Información de Puertos COM ===\n\n"
    try:
        from serial.tools import list_ports
        com_ports = list(list_ports.comports())
        if not com_ports:
            info_str += "No se encontraron puertos COM activos."
        else:
            for port in com_ports:
                info_str += f"Dispositivo: {port.device}\n"
                info_str += f"Descripción: {port.description}\n"
                info_str += f"Hardware ID: {port.hwid}\n"
                info_str += "-" * 40 + "\n"
    except Exception as e:
        info_str += f"No se pudo obtener la información de los puertos COM: {e}"
        
    return info_str

# Dispositivos Bluetooth

def get_bluetooth_devices():
    """
    Obtiene y retorna información de dispositivos Bluetooth emparejados.
    """
    info_str = "\n=== DISPOSITIVOS BLUETOOTH ===\n\n"
    try:
        import wmi
        c = wmi.WMI()
        devices = c.Win32_PnPEntity()

        bluetooth_devices = [d for d in devices if "bluetooth" in str(d.Description or "").lower()]

        if not bluetooth_devices:
            info_str += "  No hay dispositivos Bluetooth activos o emparejados.\n"
        else:
            for device in bluetooth_devices:
                info_str += f"Dispositivo: {device.Description}\n"
                if device.Name:
                    info_str += f"  Nombre: {device.Name}\n"
                if device.DeviceID:
                    info_str += f"  ID del dispositivo: {device.DeviceID}\n"
                if device.Status:
                    info_str += f"  Estado: {device.Status}\n"
                info_str += "-" * 40 + "\n"

    except Exception as e:
        info_str += f"Error al obtener información de dispositivos Bluetooth: {e}\n"

    info_str += "=" * 40 + "\n"
    return info_str

def get_os_info():
    """
    Obtiene y retorna la información detallada del sistema operativo como una cadena.
    """
    info_str = "\n=== INFORMACIÓN DEL SISTEMA OPERATIVO ===\n\n"

    # Información básica del sistema
    info_str += f"Sistema Operativo: {platform.system()}\n"
    info_str += f"Nombre del Equipo: {platform.node()}\n"
    info_str += f"Versión del SO: {platform.version()}\n"
    info_str += f"Edición: {platform.win32_edition() if platform.system() == 'Windows' else 'N/A'}\n"
    info_str += f"Arquitectura: {platform.machine()}\n"
    info_str += f"Procesador: {platform.processor()}\n"
    info_str += f"Plataforma: {platform.platform()}\n"
    info_str += f"Número de procesadores lógicos: {os.cpu_count()}\n"
    info_str += f"Versión de Python: {platform.python_version()}\n"
    ahora = datetime.now()
    info_str += f"Fecha de consulta: {ahora.strftime('%d/%m/%Y')}\n"
    info_str += f"Hora de consulta: {ahora.strftime('%H:%M:%S')}\n"
    info_str += "-" * 50 + "\n"

    # Información adicional en Windows
    if platform.system() == "Windows":
        try:
            import wmi
            c = wmi.WMI()
            os_info = c.Win32_OperatingSystem()[0]
            
            info_str += "=== Información específica de Windows ===\n"
            info_str += f"Versión completa: {os_info.Caption} {os_info.Version}\n"
            info_str += f"ID del producto: {os_info.SerialNumber}\n"
            info_str += f"Tipo de instalación: {os_info.OSArchitecture} - {os_info.CodeSet}\n"
            info_str += f"Idioma del sistema: {os_info.OSLanguage}\n"
            info_str += f"País/Región: {os_info.CountryCode}-{os_info.Locale}\n"
            info_str += f"Organización registrada: {os_info.Organization or 'Desconocido'}\n"
            info_str += f"Registrado a nombre de: {os_info.RegisteredUser}\n"
            
            # Formateo de fecha
            try:
                install_date = os_info.InstallDate
                if isinstance(install_date, str) and install_date.startswith(('20', '10')):
                    date_str = install_date.split('.')[0]
                    install_datetime = datetime.strptime(date_str, "%Y%m%d%H%M%S")
                    info_str += f"Instalado: {install_datetime.strftime('%Y-%m-%d %H:%M:%S')}\n"
                else:
                    info_str += f"Instalado: {install_date}\n"
            except Exception as e:
                info_str += f"  No se pudo parsear la fecha de instalación: {e}\n"
            info_str += "-" * 50 + "\n"
            
            # Dominio o grupo de trabajo
            comp_info = c.Win32_ComputerSystem()[0]
            domain = comp_info.Domain if comp_info.Domain else "No pertenece a un dominio"
            workgroup = comp_info.Workgroup if not comp_info.PartOfDomain else "Dominio activo"
            info_str += f"Pertenece a dominio: {'Sí' if comp_info.PartOfDomain else 'No'}\n"
            info_str += f"  Dominio: {domain}\n"
            info_str += f"  Grupo de trabajo: {workgroup}\n"
            info_str += "-" * 50 + "\n"
            
            # Acceso remoto (RDP)
            result = subprocess.run(
                ["powershell", "(Get-WmiObject -Class Win32_TerminalServiceSetting -Namespace root\\CIMv2\\TerminalServices).AllowTSConnections"],
                capture_output=True, text=True, encoding="latin-1", errors="replace"
            )
            output = result.stdout.strip()
            rdp_status = "Habilitado" if output == "1" else "Deshabilitado"
            info_str += f"Acceso remoto (RDP): {rdp_status}\n"
            info_str += "-" * 50 + "\n"
            
        except Exception as e:
            info_str += f"Error al obtener info avanzada de Windows: {e}\n"

    # Para Linux/macOS
    else:
        info_str += "Para sistemas no Windows, puedes usar comandos como:\n"
        info_str += "  uname -a\n"
        info_str += "  lsb_release -a\n"
        info_str += "  sw_vers (en macOS)\n"
        info_str += "-" * 50 + "\n"

    # Configuración regional
    lang, encoding = locale.getdefaultlocale()
    info_str += f"Configuración regional predeterminada: {lang}\n"
    info_str += f"Codificación del sistema: {encoding}\n"
    
    return info_str

def get_regional_settings():
    """
    Obtiene la configuración regional desde el Registro de Windows y la retorna como una cadena.
    """
    info_str = "\n=== CONFIGURACIÓN REGIONAL (INTERNACIONAL) ===\n\n"
    try:
        import winreg

        key_path = r"Control Panel\International"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            def get_value(name):
                try:
                    return winreg.QueryValueEx(key, name)[0]
                except FileNotFoundError:
                    return "No definido"

            s_decimal       = get_value("sDecimal")
            s_thousand      = get_value("sThousand")
            s_mon_decimal   = get_value("sMonDecimalSep")
            s_mon_thousand  = get_value("sMonThousandSep")
            s_short_date    = get_value("sShortDate")
            s_time_format   = get_value("sTimeFormat")
            s_currency      = get_value("sCurrency")

            info_str += f"S. Decimal (sDecimal): {s_decimal}\n"
            info_str += f"S. Miles (sThousand): {s_thousand}\n"
            info_str += f"S. Moneda Decimal (sMonDecimalSep): {s_mon_decimal}\n"
            info_str += f"S. Moneda Miles (sMonThousandSep): {s_mon_thousand}\n"
            info_str += f"Formato Fecha Corta (sShortDate): {s_short_date}\n"
            info_str += f"Formato de Hora (sTimeFormat): {s_time_format}\n"
            info_str += f"Símbolo de Moneda (sCurrency): {s_currency}\n"

    except Exception as e:
        info_str += f"Error al obtener información de configuración regional: {e}\n"
        
    return info_str
        
def set_regional_settings():
    """
    Establece la configuración regional del sistema en el Registro de Windows y retorna un mensaje.
    """
    import winreg
    info_str = ""
    key_path = r"Control Panel\International"
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "sDecimal", 0, winreg.REG_SZ, ".")
        winreg.SetValueEx(key, "sThousand", 0, winreg.REG_SZ, ",")
        winreg.SetValueEx(key, "sMonDecimalSep", 0, winreg.REG_SZ, ".")
        winreg.SetValueEx(key, "sMonThousandSep", 0, winreg.REG_SZ, ",")
        winreg.SetValueEx(key, "sShortDate", 0, winreg.REG_SZ, "dd/MM/yyyy")
        winreg.SetValueEx(key, "sTimeFormat", 0, winreg.REG_SZ, "hh:mm")
        winreg.SetValueEx(key, "sCurrency", 0, winreg.REG_SZ, "Bs.")
        info_str = "✅ Configuración regional actualizada correctamente."
        winreg.CloseKey(key)

    except Exception as e:
        info_str = f"❌ Error al modificar configuración regional: {e}"
    
    return info_str

    
    return info_str

def show_current_datetime():
    """
    Obtiene y retorna la fecha y hora actual usando formatos del sistema (locale).
    """
    import time
    import locale
    info_str = "\n=== FECHA Y HORA ACTUAL SEGÚN EL LOCALE DEL SISTEMA ===\n\n"
    try:
        locale.setlocale(locale.LC_ALL, '')
        fecha_local = time.strftime("%x")
        hora_local = time.strftime("%X")
        fecha_hora_local = time.strftime("%c")

        info_str += f"Fecha local (%x): {fecha_local}\n"
        info_str += f"Hora local (%X): {hora_local}\n"
        info_str += f"Fecha/hora completa (%c): {fecha_hora_local}\n"

    except Exception as e:
        info_str += f"Error al obtener formato local: {e}"

    info_str += "-" * 50 + "\n"
    info_str += "Este ejemplo muestra CÓMO EL SISTEMA interpreta los formatos tras el cambio regional."
    return info_str
    
# Regional and Datetime

def show_regional_and_datetime():
    """
    Combina la información de la configuración regional y la fecha/hora actual en un solo texto.
    """
    info_regional = get_regional_settings()
    info_datetime = show_current_datetime()
    return info_regional + info_datetime

# --- FUNCIONES DE AUDITORÍA PARA BASE DE DATOS ---

def get_machine_name():
    """Retorna el nombre de red del equipo."""
    return platform.node()

def get_current_user():
    """Retorna el usuario actual de la sesión de OS."""
    return os.getlogin()

def get_date_audit():
    """Retorna la fecha actual en formato YYYY-MM-DD para SQLite."""
    return datetime.now().strftime("%Y-%m-%d")

def get_time_audit():
    """Retorna la hora actual en formato HH:MM:SS para SQLite."""
    return datetime.now().strftime("%H:%M:%S")