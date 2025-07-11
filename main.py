# main.py

from system_info import get_system_info, get_cpu_info, get_ram_info, get_disk_info, get_gpu_info, get_motherboard_info

def menu():
    print("\n=== ARKToolsPC - Información del Hardware ===")
    print("1. Información del Sistema")
    print("2. Información de la CPU")
    print("3. Información de la Memoria RAM")
    print("4. Información de los Discos")
    print("5. Información de la/s Tarjeta/s Gráfica/s")
    print("6. Información de la Placa Base")
    print("7. Salir")

def run_tool():
    while True:
        menu()
        try:
            choice = input("\nSelecciona una opción (1-7): ")
            match choice:
                case "1":
                    get_system_info()
                case "2":
                    get_cpu_info()
                case "3":
                    get_ram_info()
                case "4":
                    get_disk_info()
                case "5":
                    get_gpu_info()
                case "6":
                    get_motherboard_info()
                case "7":
                    print("Saliendo de ARKToolsPC...")
                    break
                case _:
                    print("Opción no válida. Inténtalo de nuevo.")
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    run_tool()