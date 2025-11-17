INSERT INTO ark_sessions (ses_clt_IDauto, ses_usr_IDauto, ses_FechaSesion, ses_TotalHora)
VALUES 
(1, 1, '2025-10-18', 2),
(2, 2, '2025-10-18', 3);

INSERT INTO ark_session_details (dts_ses_IDauto, dts_act_Codigo, dts_req_IDauto, dts_description, dts_result, dts_time_spent)
VALUES 
(1, 1, 1, 'Se limpió el equipo y se verificó el rendimiento.', 'Equipo operativo', 1.5),
(2, 2, 2, 'Se instaló software y se configuró acceso remoto.', 'Configuración exitosa', 2.0);