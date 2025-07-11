# system_info.py

import psutil
import platform
import socket
import psutil
import subprocess
import GPUtil
import wmi
from datetime import datetime


def get_system_info():
    uname = platform.uname()
    print("\n=== Información del Sistema ===")
    print(f"Sistema Operativo: {uname.system} {uname.release} ({uname.version})")
    print(f"Nombre del equipo: {uname.node}")
    print(f"Arquitectura: {uname.machine}")


# system_info.py

def get_cpu_info():
    try:
        import wmi
        c = wmi.WMI()

        print("\n=== Información Detallada del Procesador ===")
        for cpu in c.Win32_Processor():
            print(f"Nombre: {cpu.Name.strip()}")
            print(f"Fabricante: {cpu.Manufacturer}")
            print(f"Arquitectura: {cpu.Architecture}")
            print(f"Núcleos lógicos: {cpu.NumberOfLogicalProcessors}")
            print(f"Núcleos físicos: {cpu.NumberOfCores}")
            print(f"Velocidad máxima: {cpu.MaxClockSpeed} MHz")
            
            if cpu.L2CacheSize:
                print(f"Tamaño L2 Cache: {cpu.L2CacheSize} KB")
            if cpu.L3CacheSize:
                print(f"Tamaño L3 Cache: {cpu.L3CacheSize} KB")
                
            print(f"Socket: {cpu.SocketDesignation}")
            print(f"Versión: {cpu.ProcessorId}")
            print("-" * 40)

        # Información adicional con psutil
        print("=== Información adicional (uso actual) ===")
        print(f"Uso total de CPU: {psutil.cpu_percent(interval=1)}%")
        print(f"Tiempo de CPU (usuario/sistema/inactivo): {psutil.cpu_times().user:.2f}s usuario, "
              f"{psutil.cpu_times().system:.2f}s sistema, "
              f"{psutil.cpu_times().idle:.2f}s inactivo")

    except Exception as e:
        print(f"No se pudo obtener información completa de la CPU: {e}")


def get_ram_info():
    try:
        import wmi
        c = wmi.WMI()
        print("\n=== Información Detallada de Memoria RAM ===")

        total_ram = psutil.virtual_memory().total
        print(f"Memoria total instalada: {round(total_ram / (1024**3), 2)} GB\n")

        for mem in c.Win32_PhysicalMemory():
            print(f"Banco: {mem.BankLabel}")
            print(f"Fabricante: {mem.Manufacturer}")
            print(f"Modelo: {mem.PartNumber.strip()}")
            print(f"Tamaño: {round(int(mem.Capacity) / (1024**3), 2)} GB")
            print(f"Velocidad: {mem.Speed} MHz")
            print(f"Tipo: {'DDR4' if int(mem.SMBIOSMemoryType) == 24 else 'DDR3' if int(mem.SMBIOSMemoryType) == 21 else 'Otro'}")
            print(f"Número de Serie: {mem.SerialNumber.strip()}")
            print("-" * 40)

    except Exception as e:
        print(f"No se pudo obtener información completa de la RAM: {e}")

# Almacenamiento

def get_disk_info():
    try:
        import wmi
        c = wmi.WMI()
        print("\n=== INFORMACIÓN BÝSICA DE DISCOS FÝSICOS ===")

        disks = c.Win32_DiskDrive()
        total_storage_bytes = 0  # Acumulador para el tamaño total

        if not disks:
            print("No se encontraron discos físicos.")
            return

        for disk in disks:
            try:
                print(f"\nModelo: {disk.Model or 'Desconocido'}")
                print(f"Fabricante: {disk.Manufacturer or 'Desconocido'}")
                print(f"Interfaz: {disk.InterfaceType or 'Desconocida'}")

                size_gb = round(int(disk.Size) / (1024**3), 2) if disk.Size else 'N/A'
                print(f"Tamaño total: {size_gb} GB")

                print(f"Tipo: {'SSD' if 'SSD' in str(disk.Model) else 'HDD'}")
                print(f"Número de Serie: {disk.SerialNumber.strip() if disk.SerialNumber else 'No disponible'}")
                print("-" * 50)

                # Acumular solo si el disco tiene tamaño definido
                if disk.Size:
                    total_storage_bytes += int(disk.Size)

            except Exception as e:
                print(f"⚠︝ Error al procesar disco {disk.DeviceID}: {e}")
                print("-" * 50)
                continue

        # Mostrar resumen final del almacenamiento total
        if total_storage_bytes > 0:
            total_gb = round(total_storage_bytes / (1024**3), 2)
            print("\n=== RESUMEN DE ALMACENAMIENTO TOTAL ===")
            print(f"Almacenamiento total instalado: {total_gb} GB")
            print("=" * 50)

    except Exception as e:
        print(f"🚨 No se pudo obtener información completa de los discos: {e}")


def get_gpu_info():
    try:
        import wmi
        c = wmi.WMI()
        print("\n=== Información de Tarjeta(s) Gráfica(s) ===")
        for gpu in c.Win32_VideoController():
            print(f"Nombre: {gpu.Name}")
            print(f"Fabricante: {gpu.AdapterCompatibility}")
            print(f"Tipo de dispositivo: {gpu.VideoProcessor}")
            print(f"Versión del controlador: {gpu.DriverVersion}")
            print(f"Memoria dedicada: {round(int(gpu.AdapterRAM) / (1024**3), 2)} GB")
            print("-" * 40)
    except Exception as e:
        print(f"No se pudo obtener información de la GPU: {e}")

def get_motherboard_info():
    try:
        import wmi
        c = wmi.WMI()
        motherboard = c.Win32_BaseBoard()[0]  # Generalmente hay solo una placa base
        print("\n=== Información de la Placa Base ===")
        print(f"Fabricante: {motherboard.Manufacturer}")
        print(f"Producto: {motherboard.Product}")
        print(f"Versión: {motherboard.Version}")
        print(f"Número de Serie: {motherboard.SerialNumber}")
    except IndexError:
        print("No se pudo obtener información de la placa base.")
    except Exception as e:
        print(f"Error al obtener información de la placa base: {e}")

# Netware

def get_network_info():
    """
      Muestra la salida completa de 'ipconfig /all' del sistema
    """
    print("\n=== INFORMACIÓN COMPLETA DE RED ===\n")
    try:
        # Ejecutar el comando ipconfig /all
        result = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True, encoding="latin-1")

        # Mostrar la salida completa
        print(result.stdout)

    except Exception as e:
        print(f"Error al obtener información de red: {e}")

# Hardware de red
def get_nic_info():
    """
    Muestra información detallada sobre las tarjetas de red (NICs)
    """
    print("\n=== TARJETAS DE RED (NICs) ===\n")
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
            print("  No se encontraron tarjetas de red físicas.")

        for nic in nics:
            print(f"Tarjeta: {nic.NetConnectionID or 'Desconocido'}")
            print(f"  Modelo: {nic.Name}")
            print(f"  Fabricante: {nic.Manufacturer or 'Desconocido'}")
            print(f"  Dirección MAC: {nic.MACAddress or 'No disponible'}")
            print(f"  Tipo: {nic.AdapterType}")
            
            # Usamos el diccionario para traducir el código de estado
            status_code = str(nic.NetConnectionStatus)
            status_desc = status_codes.get(status_code, f"Desconocido ({status_code})")
            print(f"  Estado: {status_desc}")
            
            print(f"  Velocidad: {nic.Speed or 'Desconocida'} bps")
            print("-" * 40)

    except Exception as e:
        print(f"Error al obtener información de NICs: {e}")
        
# Hardware de audio

def get_audio_devices():
    """
    Muestra información sobre dispositivos de audio
    """
    print("\n=== TARJETAS DE AUDIO ===\n")
    try:
        import wmi
        c = wmi.WMI()
        for i, device in enumerate(c.Win32_SoundDevice(), start=1):
            print(f"{i}. Nombre: {device.Name}")
            print(f"   Fabricante: {device.Manufacturer}")
            print(f"   Estado: {device.Status}")
            print("-" * 40)
    except Exception as e:
        print(f"Error al obtener información de audio: {e}")
        
# Puertos COM
        
def get_com_ports():
    """
    Muestra los puertos COM detectados en el sistema
    """
    print("\n=== PUERTOS COM ACTIVOS ===\n")
    try:
        from serial.tools import list_ports
        ports = list_ports.comports()
        if not ports:
            print("  No se encontraron puertos COM.")
        for port, desc, hwid in sorted(ports):
            print(f"Puerto: {port}")
            print(f"  Descripción: {desc}")
            print(f"  HWID: {hwid}")
            print("-" * 40)
    except Exception as e:
        print(f"Error al obtener información de puertos COM: {e}")

# Dispositivos USB

def get_usb_devices():
    """
    Muestra información de dispositivos USB conectados (versión más estable)
    """
    print("\n=== DISPOSITIVOS USB CONECTADOS ===\n")
    try:
        import wmi
        c = wmi.WMI()
        devices = c.Win32_PnPEntity()

        usb_devices = [d for d in devices if "USB" in str(d.Description or "")]

        if not usb_devices:
            print("  No hay dispositivos USB conectados.")
            return

        for device in usb_devices:
            print(f"Dispositivo: {device.Description}")
            if device.Name:
                print(f"  Nombre: {device.Name}")
            if device.DeviceID:
                print(f"  ID del dispositivo: {device.DeviceID}")
            if device.Status:
                print(f"  Estado: {device.Status}")
            print("-" * 40)

    except Exception as e:
        print(f"Error al obtener información de dispositivos USB: {e}")

# Dispositivos Bluetooth

def get_bluetooth_devices():
    """
    Muestra información de dispositivos Bluetooth emparejados
    """
    print("\n=== DISPOSITIVOS BLUETOOTH ===\n")
    try:
        import wmi
        c = wmi.WMI()
        devices = c.Win32_PnPEntity()

        bluetooth_devices = [d for d in devices if "bluetooth" in str(d.Description or "").lower()]

        if not bluetooth_devices:
            print("  No hay dispositivos Bluetooth activos o emparejados.")

        for device in bluetooth_devices:
            print(f"Dispositivo: {device.Description}")
            if device.Name:
                print(f"  Nombre: {device.Name}")
            if device.DeviceID:
                print(f"  ID del dispositivo: {device.DeviceID}")
            if device.Status:
                print(f"  Estado: {device.Status}")
            print("-" * 40)

    except Exception as e:
        print(f"Error al obtener información de dispositivos Bluetooth: {e}")

    print("=" * 40)