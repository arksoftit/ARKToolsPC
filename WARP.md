# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Environment and dependencies

- This is a Windows-focused desktop application built with Python and PySide6; it relies heavily on Windows-specific APIs such as WMI (`WMI` package), `winreg`, and commands like `ipconfig` and PowerShell.
- Python dependencies are defined in `requirements.txt` (PySide6, psutil, pyserial, pywin32, WMI, etc.). Install them into an environment before running the app.
- The SQLite database file is created relative to the current working directory under `arktooldatabase/ArkToolsBD.sqlite`. Running the app from a different directory will create/use a different database path.

## Common commands

All commands assume the repository root (`ARKToolsPC`) as the working directory and a standard Python installation on Windows.

### Set up a virtual environment and install dependencies

- Create and activate a virtual environment (PowerShell):
  - `python -m venv .venv`
  - `./.venv/Scripts/Activate.ps1`
- Install dependencies:
  - `pip install -r requirements.txt`

### Run the application (GUI)

- From the repo root, launch the main window:
  - `python arktoolspcg2.py`

### Linting and tests

- There is currently no configured linting or automated test suite in this repository (no `pytest.ini`, `tox.ini`, `pyproject.toml`, or `tests/` directory). If you introduce linting or tests (e.g., via `pytest` or `ruff`), also update this `WARP.md` with the canonical commands.

## High-level architecture

### Main application entrypoint: `arktoolspcg2.py`

- Defines `MiApp(QMainWindow)`, the primary window class that wires the generated Qt UI (`Ui_MainWindow` from `ui_arktoolspcg2.py`) to application logic.
- On startup, it:
  - Instantiates `DatabaseManager` and calls `setup_database()` to ensure the SQLite schema exists.
  - Configures the window as frameless and handles custom resize/move behavior via `QSizeGrip` and mouse events on `frame_superior`.
  - Connects top-bar buttons (`btn_minimizar`, `btn_maximizar`, `btn_restaurar`, `btn_cerrar`) to window state management methods.
  - Manages the left-side navigation and submenus (`frame_menu`, `frame_sub_hardware`, `frame_operations`) via animated show/hide functions (`mover_menu`, `toggle_sub_hardware_menu`, `toggle_operations_menu`, `volver_menu_principal`).
  - Routes navigation buttons (e.g., `btn_info_red`, `btn_info_so`, `btn_info_regional`, `btn_info_mbd`, `btn_info_cpu`, `btn_info_gpu`, `btn_info_ram`, `btn_info_hdd`, `btn_info_nic`, `btn_info_com`, `btn_info_bth`, `btn_info_audio`, `btn_info_sistema`, `btn_info_usb`) to corresponding `system_info` functions and updates the main `QStackedWidget` (`sw_consolas`) to show the appropriate page.
  - Uses QPixmaps (icons and illustrations) to update `label_info_hw` depending on the selected hardware category.
- Provides a small messaging helper layer over `QMessageBox` (`show_notification`, `confirm_action`) to standardize confirmations and error dialogs.
- Encapsulates configuration and localization flows:
  - `mostrar_inf_config()` switches to the configuration page.
  - `aplicar_config_regional()` requests user confirmation and, if accepted, delegates to `ejecutar_cambios_y_notificar()`.
  - `ejecutar_cambios_y_notificar()` calls `system_info.set_regional_settings()`, writes progress and results to `textEdit_info_config`, and shows success/error popups.
- Integrates with the database for configuration inspection:
  - `consultar_configuracion_db()` executes a read-only `SELECT` on the `ark_company` table through `DatabaseManager.fetch_data()`, formats the results into a human-readable report, and writes it into `textEdit_info_config`.

The `if __name__ == "__main__":` block at the bottom of `arktoolspcg2.py` is the canonical entrypoint used when running the app from this repository.

### Legacy main window: `arktoolspcg2-Mal.py`

- Contains an older/alternate `MiApp` implementation that uses a `stackedWidget` name and a simpler menu structure.
- It appears to be a previous iteration kept for reference; the current application code uses `arktoolspcg2.py` and `sw_consolas`. Prefer modifying `arktoolspcg2.py` going forward.

### Qt UI definitions: `arktoolspcg2.ui` and `ui_arktoolspcg2.py`

- `arktoolspcg2.ui` is the Qt Designer XML source for the main window. It defines:
  - A top bar (`frame_superior`) with the menu button and window control buttons.
  - A main frame (`frm_principal`) with a left navigation area and a central content area.
  - A `QStackedWidget` used to switch between pages: the start page, hardware info, network info, OS info, regional settings, configuration, etc.
- `ui_arktoolspcg2.py` is the auto-generated Python wrapper for the `.ui` file and defines the `Ui_MainWindow` class (widgets, layouts, and styling). The header explicitly warns that changes will be overwritten when regenerating from the `.ui` file.
- Regeneration pattern (do not run unless you intend to overwrite `ui_arktoolspcg2.py`):
  - `pyside6-uic arktoolspcg2.ui -o ui_arktoolspcg2.py`
- There are backup variants (`arktoolspcg2-bk.ui`, `ui_arktoolspcg2-BK.py`) representing an earlier layout. Unless you have a specific reason, keep them as historical references and update the non-`BK` versions for the active UI.

### Database layer: `database_manager.py`

- Encapsulates all SQLite database access via the `DatabaseManager` class.
- Key behaviors:
  - Builds an absolute database path as `[current working directory]/arktooldatabase/ArkToolsBD.sqlite` and ensures the `arktooldatabase` folder exists before connecting.
  - Defines a large `sql_script` string containing `CREATE TABLE IF NOT EXISTS` statements for the domain:
    - Companies, clients, job titles, functional units, employees, users.
    - Device types and IT assets (with foreign keys to functional units and employees).
    - Currencies, action categories, actions.
    - Client requests, completed tasks, work sessions, and session details.
  - `setup_database()` opens a connection and executes the full script via `executescript` to create any missing tables.
  - `execute_query(sql_query, params=())` and `fetch_data(sql_query, params=())` provide generic helpers for mutating and read-only operations. `fetch_data` configures `row_factory = sqlite3.Row` so callers can access columns by name.
- The only in-repo consumer at present is `MiApp.consultar_configuracion_db()` in `arktoolspcg2.py`, but the schema is broader and ready for future entities and management screens.

### System inspection and configuration: `system_info.py`

- Acts as a collection of Windows system introspection helpers, grouped by concern:
  - General system and BIOS: `get_system_info()` via WMI.
  - CPU, RAM, disks, GPU, motherboard: `get_cpu_info()`, `get_ram_info()`, `get_disk_info()`, `get_gpu_info()`, `get_motherboard_info()` using WMI and `psutil`.
  - Network stack and hardware: `get_network_info()` (shells out to `ipconfig /all`), `get_nic_info()` (physical NICs via WMI).
  - Peripherals: `get_audio_devices()`, `get_usb_devices()`, `get_com_ports()` (via `serial.tools.list_ports`), `get_bluetooth_devices()`.
  - OS and locale: `get_os_info()` mixes Python `platform` plus WMI to report Windows edition, licensing info, domain/workgroup, RDP status, and locale.
  - Regional settings utilities:
    - `get_regional_settings()` reads current user locale-related registry keys under `HKCU\Control Panel\International`.
    - `set_regional_settings()` writes a fixed set of numeric, date, time, and currency formatting values into the same key and returns a status string (used from `MiApp.ejecutar_cambios_y_notificar()`).
    - `show_current_datetime()` and `show_regional_and_datetime()` display locale-formatted date and time as a sanity check after changes.
- All of the `MiApp.mostrar_info_*` methods in `arktoolspcg2.py` are thin wrappers that call one of these functions, update the relevant `QTextEdit`, change the informational image, and set the `QStackedWidget` page.
- This module assumes a Windows host; on non-Windows platforms, many functions will either be no-ops or raise exceptions despite having some basic cross-platform fallbacks in `get_os_info()`.

### Assets and diagrams

- Visual assets live under `assets/`:
  - `assets/icons/` contains SVG/PNG icons for hardware categories, OS, menus, and custom graphics referenced by both the `.ui` file and `ui_arktoolspcg2.py`.
  - `assets/images/` contains application-level branding images and icons (e.g., app icon `.ico` files).
- There is a documentation-only script at `docs/diagrams/drawio/conectionDB.py` that demonstrates how to create an SQLite file named `ArkToolsDB.sqlite`. This script is not imported by the main application and uses a slightly different database filename than `DatabaseManager`.

## Notes for future changes

- Prefer extending `arktoolspcg2.py`, `database_manager.py`, and `system_info.py` rather than editing auto-generated files like `ui_arktoolspcg2.py`. When UI changes are needed, modify `arktoolspcg2.ui` in Qt Designer and regenerate the Python wrapper.
- When adding new views or pages to the main window, follow the existing pattern: add widgets and buttons in the `.ui`, wire them in `Ui_MainWindow`, then connect signals in `MiApp.__init__` to small methods that delegate to the appropriate helper in `system_info` or the database layer.
