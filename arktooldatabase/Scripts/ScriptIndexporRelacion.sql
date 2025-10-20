-- Relaciones en empleados
CREATE INDEX idx_employees_cargo ON ark_employees(emy_Cargo);
CREATE INDEX idx_employees_cliente ON ark_employees(emy_Cliente);

-- Relación entre usuarios y empleados
CREATE INDEX idx_users_employee ON ark_users(id_employee);

-- Relaciones en activos informáticos
CREATE INDEX idx_assets_functional_unit ON ark_it_assets(ita_functional_units);
CREATE INDEX idx_assets_employee ON ark_it_assets(ita_idemployees);

-- Relación entre acciones y categorías
CREATE INDEX idx_actions_category ON ark_actions(id_category);

-- Relación entre requerimientos y clientes
CREATE INDEX idx_requests_cliente ON ark_requests(req_CodigoCliente);

-- Relaciones en sesiones
CREATE INDEX idx_sessions_cliente ON ark_sessions(ses_clt_IDauto);
CREATE INDEX idx_sessions_usuario ON ark_sessions(ses_usr_IDauto);

-- Relaciones en detalles de sesión
CREATE INDEX idx_details_session ON ark_session_details(dts_ses_IDauto);
CREATE INDEX idx_details_action ON ark_session_details(dts_act_Codigo);
CREATE INDEX idx_details_request ON ark_session_details(dts_req_IDauto);