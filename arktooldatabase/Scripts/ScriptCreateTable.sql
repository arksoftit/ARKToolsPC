PRAGMA foreign_keys = ON;

-- Empresas
CREATE TABLE ark_company (
    emp_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_Codigo TEXT NOT NULL,
    emp_Descripcion TEXT,
    emp_IDfiscal TEXT,
    emp_Status INTEGER DEFAULT 1,
    emp_DireccionF TEXT,
    emp_DireccionL TEXT,
    emp_Telefono1 TEXT,
    emp_Telefono2 TEXT,
    emp_Representante TEXT,
    emp_TelefonoContacto TEXT,
    emp_EmailContacto TEXT,
    emp_EmailEmpresa TEXT,
    emp_TipoContribuyente INTEGER,
    emp_FechaCreacion TEXT DEFAULT (datetime('now'))
);

-- Clientes
CREATE TABLE ark_clients (
    clt_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    clt_Codigo TEXT NOT NULL,
    clt_Descripcion TEXT,
    clt_IDfiscal TEXT,
    clt_Status INTEGER DEFAULT 1,
    clt_DireccionF TEXT,
    clt_DireccionL TEXT,
    clt_Telefono1 TEXT,
    clt_Telefono2 TEXT,
    clt_Representante TEXT,
    clt_TelefonoContacto TEXT,
    clt_EmailContacto TEXT,
    clt_EmailEmpresa TEXT,
    clt_TipoContribuyente INTEGER,
    clt_Origen TEXT,
    clt_CodigoOrigen TEXT,
    clt_FechaCreacion TEXT DEFAULT (datetime('now'))
);

-- Cargos
CREATE TABLE ark_job_titles (
    job_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    job_Codigo TEXT NOT NULL,
    job_Descripcion TEXT,
    job_Status INTEGER DEFAULT 1,
    job_DescripcionTec TEXT,
    job_FechaCreacion TEXT DEFAULT (datetime('now'))
);

-- Unidades funcionales
CREATE TABLE ark_functional_units (
    fun_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    fun_Codigo TEXT NOT NULL,
    fun_Descripcion TEXT,
    fun_Status INTEGER DEFAULT 1,
    fun_FechaCreacion TEXT DEFAULT (datetime('now'))
);

-- Empleados
CREATE TABLE ark_employees (
    emy_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    emy_Codigo TEXT NOT NULL,
    emy_Descripcion TEXT,
    emy_Status INTEGER DEFAULT 1,
    emy_Telefono2 TEXT,
    emy_Cargo INTEGER,
    emy_Cliente INTEGER,
    emy_Rol TEXT,
    emy_EmailUsuario TEXT,
    emy_Password TEXT,
    emy_FechaCreacion TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (emy_Cargo) REFERENCES ark_job_titles(job_IDauto),
    FOREIGN KEY (emy_Cliente) REFERENCES ark_clients(clt_IDauto)
);

-- Usuarios
CREATE TABLE ark_users (
    usr_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    usr_Codigo TEXT NOT NULL,
    usr_Descripcion TEXT,
    usr_Status INTEGER DEFAULT 1,
    usr_Telefono2 TEXT,
    usr_Cargo TEXT,
    usr_Rol TEXT,
    usr_EmailUsuario TEXT,
    usr_Password TEXT,
    usr_FechaCreacion TEXT DEFAULT (datetime('now')),
    id_employee INTEGER,
    FOREIGN KEY (id_employee) REFERENCES ark_employees(emy_IDauto)
);

-- Tipos de equipos
CREATE TABLE ark_device_types (
    dty_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    dty_Codigo TEXT NOT NULL,
    dty_Descripcion TEXT,
    dty_Status INTEGER DEFAULT 1,
    dty_DescripcionTec TEXT,
    dty_FechaCreacion TEXT DEFAULT (datetime('now'))
);

-- Equipos informáticos
CREATE TABLE ark_it_assets (
    ita_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    ita_Codigo TEXT NOT NULL,
    ita_Descripcion TEXT,
    ita_marca TEXT,
    ita_Status INTEGER DEFAULT 1,
    ita_DescripcionTec TEXT,
    ita_DireccionL TEXT,
    ita_macadrees TEXT,
    ita_ipadrees TEXT,
    ita_functional_units INTEGER,
    ita_Rol TEXT,
    ita_idRustDesk TEXT,
    ita_idAnyDesk TEXT,
    ita_iprdp TEXT,
    ita_idemployees INTEGER,
    ita_FechaCreacion TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (ita_functional_units) REFERENCES ark_functional_units(fun_IDauto),
    FOREIGN KEY (ita_idemployees) REFERENCES ark_employees(emy_IDauto)
);

-- Monedas
CREATE TABLE ark_currencies (
    mda_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    mda_Codigo TEXT NOT NULL,
    mda_Descripcion TEXT,
    mda_Status INTEGER DEFAULT 1,
    mda_Simbolo TEXT,
    mda_FactorCambio1 REAL,
    mda_FactorCambio2 REAL,
    mda_OperadorCalculo INTEGER,
    mda_AplicaImp INTEGER DEFAULT 0,
    mda_FechaCreacion TEXT DEFAULT (datetime('now'))
);

-- Categorías de acciones
CREATE TABLE ark_action_categories (
    cat_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    cat_Codigo TEXT NOT NULL,
    cat_Descripcion TEXT,
    cat_Status INTEGER DEFAULT 1,
    cat_DescripcionTec TEXT,
    cat_FechaCreacion TEXT DEFAULT (datetime('now'))
);

-- Acciones frecuentes
CREATE TABLE ark_actions (
    act_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    act_Codigo TEXT NOT NULL,
    act_Descripcion TEXT,
    act_Status INTEGER DEFAULT 1,
    act_DescripcionTec TEXT,
    act_FechaCreacion TEXT DEFAULT (datetime('now')),
    id_category INTEGER,
    FOREIGN KEY (id_category) REFERENCES ark_action_categories(cat_IDauto)
);

-- Requerimientos del cliente
CREATE TABLE ark_requests (
    req_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    req_Codigo TEXT NOT NULL,
    req_Descripcion TEXT,
    req_Status INTEGER DEFAULT 1,
    req_DescripcionTec TEXT,
    req_FechaCreacion TEXT DEFAULT (datetime('now')),
    req_CodigoCliente INTEGER,
    FOREIGN KEY (req_CodigoCliente) REFERENCES ark_clients(clt_IDauto)
);

-- Tareas realizadas
CREATE TABLE ark_tasks_completed (
    tsc_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    tsc_Codigo TEXT NOT NULL,
    tsc_Descripcion TEXT,
    tsc_Status INTEGER DEFAULT 1,
    tsc_DescripcionTec TEXT,
    tsc_FechaCreacion TEXT DEFAULT (datetime('now'))
);

-- Sesiones de trabajo
CREATE TABLE ark_sessions (
    ses_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    ses_clt_IDauto INTEGER,
    ses_clt_Codigo TEXT,
    ses_clt_Descripcion TEXT,
    ses_clt_IDfiscal TEXT,
    ses_clt_Status INTEGER DEFAULT 1,
    ses_clt_DireccionF TEXT,
    ses_clt_DireccionA TEXT,
    ses_clt_Telefono1 TEXT,
    ses_clt_Telefono2 TEXT,
    ses_usr_IDauto INTEGER,
    ses_usr_Codigo TEXT,
    ses_usr_Descripcion TEXT,
    ses_FechaSesion TEXT,
    ses_HoraInicial TEXT,
    ses_HoraFinal TEXT,
    ses_TotalHora INTEGER,
    FOREIGN KEY (ses_clt_IDauto) REFERENCES ark_clients(clt_IDauto),
    FOREIGN KEY (ses_usr_IDauto) REFERENCES ark_users(usr_IDauto)
);

-- Detalle de sesiones
CREATE TABLE ark_session_details (
    dts_IDauto INTEGER PRIMARY KEY AUTOINCREMENT,
    dts_ses_IDauto INTEGER,
    dts_act_Codigo INTEGER,
    dts_req_IDauto INTEGER,
    dts_description TEXT,
    dts_result TEXT,
    dts_time_spent REAL,
    dts_date_logged TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (dts_ses_IDauto) REFERENCES ark_sessions(ses_IDauto),
    FOREIGN KEY (dts_act_Codigo) REFERENCES ark_actions(act_IDauto),
    FOREIGN KEY (dts_req_IDauto) REFERENCES ark_requests(req_IDauto)
);