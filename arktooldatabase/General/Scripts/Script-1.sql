-- REQ-20260116-005
-- Script de creacion de tablas en MariaDB - Base de datos NAUTILUS

-- Tabla: nau_company
CREATE TABLE IF NOT EXISTS nau_company (
    emp_IDauto            INTEGER PRIMARY KEY AUTO_INCREMENT,
    emp_Codigo            VARCHAR(255) NOT NULL,
    emp_Descripcion       TEXT,
    emp_IDfiscal          VARCHAR(255),
    emp_Status            TINYINT DEFAULT 1,
    emp_DireccionF        TEXT,
    emp_DireccionL        TEXT,
    emp_Telefono1         VARCHAR(50),
    emp_Telefono2         VARCHAR(50),
    emp_Representante     VARCHAR(255),
    emp_IdRepresentante   VARCHAR(255),
    emp_TelefonoContacto  VARCHAR(50),
    emp_EmailContacto     VARCHAR(255),
    emp_EmailEmpresa      VARCHAR(255),
    emp_TipoContribuyente INTEGER,
    emp_FechaCreacion     DATETIME DEFAULT CURRENT_TIMESTAMP,
    emp_SystemDate        DATE,
    emp_SystemTime        TIME,
    emp_NameMachine       VARCHAR(255),
    emp_UserCreator       VARCHAR(255),
    emp_LastUpdateDate    DATE,
    emp_LastUpdateTime    TIME,
    emp_LastMachine       VARCHAR(255),
    emp_UserLastUpdate    VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: nau_clients
CREATE TABLE IF NOT EXISTS nau_clients (
    clt_IDauto            INTEGER PRIMARY KEY AUTO_INCREMENT,
    clt_Codigo            VARCHAR(255) NOT NULL,
    clt_Descripcion       TEXT,
    clt_IDfiscal          VARCHAR(255),
    clt_Status            TINYINT DEFAULT 1,
    clt_DireccionF        TEXT,
    clt_DireccionL        TEXT,
    clt_Telefono1         VARCHAR(50),
    clt_Telefono2         VARCHAR(50),
    clt_Representante     VARCHAR(255),
    clt_IDRepresentante   VARCHAR(255),
    clt_TelefonoContacto  VARCHAR(50),
    clt_EmailContacto     VARCHAR(255),
    clt_EmailEmpresa      VARCHAR(255),
    clt_TipoContribuyente INTEGER,
    clt_Origen            VARCHAR(255),
    clt_CodigoOrigen      VARCHAR(255),
    clt_FechaCreacion     DATETIME DEFAULT CURRENT_TIMESTAMP,
    clt_SystemDate        DATE,
    clt_SystemTime        TIME,
    clt_NameMachine       VARCHAR(255),
    clt_UserCreator       VARCHAR(255),
    clt_LastUpdateDate    DATE,
    clt_LastUpdateTime    TIME,
    clt_LastMachine       VARCHAR(255),
    clt_UserLastUpdate    VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: nau_currencies
CREATE TABLE IF NOT EXISTS nau_currencies (
    mda_IDauto             INTEGER PRIMARY KEY AUTO_INCREMENT,
    mda_Codigo             VARCHAR(255) NOT NULL,
    mda_Descripcion        TEXT,
    mda_Status             TINYINT DEFAULT 1,
    mda_ISO4217            CHAR(3),
    mda_Simbolo            VARCHAR(10),
    mda_FactorActivo       DECIMAL(18,6),
    mda_FactorPasivo       DECIMAL(18,6),
    mda_OperadorCalculo    INTEGER,
    mda_AplicaImp          TINYINT DEFAULT 0,
    mda_FechaCreacion      DATETIME DEFAULT CURRENT_TIMESTAMP,
    mda_FechaActualizacion DATE,
    mda_FechaUltima        DATE,
    mda_SystemDate         DATE,
    mda_SystemTime         TIME,
    mda_NameMachine        VARCHAR(255),
    mda_UserCreator        VARCHAR(255),
    mda_LastUpdateDate     DATE,
    mda_LastUpdateTime     TIME,
    mda_LastMachine        VARCHAR(255),
    mda_UserLastUpdate     VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: nau_functional_units
CREATE TABLE IF NOT EXISTS nau_functional_units (
    fun_IDauto         INTEGER PRIMARY KEY AUTO_INCREMENT,
    fun_Codigo         VARCHAR(255) NOT NULL,
    fun_Descripcion    TEXT,
    fun_DescripcionTec TEXT,
    fun_Status         TINYINT DEFAULT 1,
    fun_FechaCreacion  DATETIME DEFAULT CURRENT_TIMESTAMP,
    fun_SystemDate     DATE,
    fun_SystemTime     TIME,
    fun_NameMachine    VARCHAR(255),
    fun_UserCreator    VARCHAR(255),
    fun_LastUpdateDate DATE,
    fun_LastUpdateTime TIME,
    fun_LastMachine    VARCHAR(255),
    fun_UserLastUpdate VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: nau_job_titles
CREATE TABLE IF NOT EXISTS nau_job_titles (
    job_IDauto         INTEGER PRIMARY KEY AUTO_INCREMENT,
    job_Codigo         VARCHAR(255) NOT NULL,
    job_Descripcion    TEXT,
    job_Status         TINYINT DEFAULT 1,
    job_DescripcionTec TEXT,
    job_FechaCreacion  DATETIME DEFAULT CURRENT_TIMESTAMP,
    job_SystemDate     DATE,
    job_SystemTime     TIME,
    job_NameMachine    VARCHAR(255),
    job_UserCreator    VARCHAR(255),
    job_LastUpdateDate DATE,
    job_LastUpdateTime TIME,
    job_LastMachine    VARCHAR(255),
    job_UserLastUpdate VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: nau_employees
CREATE TABLE IF NOT EXISTS nau_employees (
    emy_IDauto         INTEGER PRIMARY KEY AUTO_INCREMENT,
    emy_Codigo         VARCHAR(255) NOT NULL,
    emy_Descripcion    TEXT,
    emy_Status         TINYINT DEFAULT 1,
    emy_IDEmployees    VARCHAR(255),
    emy_Telefono1      VARCHAR(50),
    emy_Cargo          INTEGER,
    emy_Cliente        INTEGER,
    emy_Rol            VARCHAR(255),
    emy_EmailUsuario   VARCHAR(255),
    emy_Password       TEXT,
    emy_FechaCreacion  DATETIME DEFAULT CURRENT_TIMESTAMP,
    emy_SystemDate     DATE,
    emy_SystemTime     TIME,
    emy_NameMachine    VARCHAR(255),
    emy_UserCreator    VARCHAR(255),
    emy_LastUpdateDate DATE,
    emy_LastUpdateTime TIME,
    emy_LastMachine    VARCHAR(255),
    emy_UserLastUpdate VARCHAR(255),
    FOREIGN KEY (emy_Cargo) REFERENCES nau_job_titles (job_IDauto)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (emy_Cliente) REFERENCES nau_clients (clt_IDauto)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: nau_users
CREATE TABLE IF NOT EXISTS nau_users (
    usr_IDauto         INTEGER PRIMARY KEY AUTO_INCREMENT,
    usr_Codigo         VARCHAR(255) NOT NULL,
    usr_Descripcion    TEXT,
    usr_Status         TINYINT DEFAULT 1,
    usr_Telefono       VARCHAR(50),
    usr_Cargo          VARCHAR(255),
    usr_Rol            VARCHAR(255),
    usr_EmailUsuario   VARCHAR(255),
    usr_Password       TEXT,
    usr_FechaCreacion  DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_employee        INTEGER,
    usr_SystemDate     DATE,
    usr_SystemTime     TIME,
    usr_NameMachine    VARCHAR(255),
    usr_UserCreator    VARCHAR(255),
    usr_LastUpdateDate DATE,
    usr_LastUpdateTime TIME,
    usr_LastMachine    VARCHAR(255),
    usr_UserLastUpdate VARCHAR(255),
    FOREIGN KEY (id_employee) REFERENCES nau_employees (emy_IDauto)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
