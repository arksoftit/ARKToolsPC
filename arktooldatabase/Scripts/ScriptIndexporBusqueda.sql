-- Códigos únicos
CREATE INDEX idx_clients_codigo ON ark_clients(clt_Codigo);
CREATE INDEX idx_users_codigo ON ark_users(usr_Codigo);
CREATE INDEX idx_employees_codigo ON ark_employees(emy_Codigo);
CREATE INDEX idx_assets_codigo ON ark_it_assets(ita_Codigo);
CREATE INDEX idx_actions_codigo ON ark_actions(act_Codigo);
CREATE INDEX idx_requests_codigo ON ark_requests(req_Codigo);
CREATE INDEX idx_sessions_codigo ON ark_sessions(ses_clt_Codigo);

-- Fechas
CREATE INDEX idx_clients_fecha ON ark_clients(clt_FechaCreacion);
CREATE INDEX idx_users_fecha ON ark_users(usr_FechaCreacion);
CREATE INDEX idx_employees_fecha ON ark_employees(emy_FechaCreacion);
CREATE INDEX idx_assets_fecha ON ark_it_assets(ita_FechaCreacion);
CREATE INDEX idx_sessions_fecha ON ark_sessions(ses_FechaSesion);
CREATE INDEX idx_details_fecha ON ark_session_details(dts_date_logged);