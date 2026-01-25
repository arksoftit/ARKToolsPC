-- 1. ACTUALIZACIÓN PARA TABLA ark_company (Prefijo: emp_)
-- ALTER TABLE ark_action_categories RENAME COLUMN cat_systemtime TO cat_SystemTime;
ALTER TABLE ark_company RENAME COLUMN emp_systemdate TO emp_SystemDate;
ALTER TABLE ark_company RENAME COLUMN emp_systemtime TO emp_SystemTime;
ALTER TABLE ark_company RENAME COLUMN emp_namemachine TO emp_NameMachine;
ALTER TABLE ark_company RENAME COLUMN emp_usercreator TO emp_UserCreator;
ALTER TABLE ark_company RENAME COLUMN emp_lastupdatedate TO emp_LastUpdateDate;
ALTER TABLE ark_company RENAME COLUMN emp_lastupdatetime TO emp_LastUpdateTime;
ALTER TABLE ark_company RENAME COLUMN emp_lastmachine TO emp_LastMachine;
ALTER TABLE ark_company RENAME COLUMN emp_userlastupdate TO emp_UserLastUpdate;

-- 2. ACTUALIZACIÓN PARA TABLA ark_clients (Prefijo: clt_)
ALTER TABLE ark_clients RENAME COLUMN clt_systemdate TO clt_SystemDate;
ALTER TABLE ark_clients RENAME COLUMN clt_systemtime TO clt_SystemTime;
ALTER TABLE ark_clients RENAME COLUMN clt_namemachine TO clt_NameMachine;
ALTER TABLE ark_clients RENAME COLUMN clt_usercreator TO clt_UserCreator;
ALTER TABLE ark_clients RENAME COLUMN clt_lastupdatedate TO clt_LastUpdateDate;
ALTER TABLE ark_clients RENAME COLUMN clt_lastupdatetime TO clt_LastUpdateTime;
ALTER TABLE ark_clients RENAME COLUMN clt_lastmachine TO clt_LastMachine;
ALTER TABLE ark_clients RENAME COLUMN clt_userlastupdate TO clt_UserLastUpdate;

-- 3. ACTUALIZACIÓN PARA TABLA ark_actions (Prefijo: act_)
ALTER TABLE ark_actions RENAME COLUMN act_systemdate TO act_SystemDate;
ALTER TABLE ark_actions RENAME COLUMN act_systemtime TO act_SystemTime;
ALTER TABLE ark_actions RENAME COLUMN act_namemachine TO act_NameMachine;
ALTER TABLE ark_actions RENAME COLUMN act_usercreator TO act_UserCreator;
ALTER TABLE ark_actions RENAME COLUMN act_lastupdatedate TO act_LastUpdateDate;
ALTER TABLE ark_actions RENAME COLUMN act_lastupdatetime TO act_LastUpdateTime;
ALTER TABLE ark_actions RENAME COLUMN act_lastmachine TO act_LastMachine;
ALTER TABLE ark_actions RENAME COLUMN act_userlastupdate TO act_UserLastUpdate;

-- 4. ACTUALIZACIÓN PARA TABLA ark_action_categories (Prefijo: cat_)
ALTER TABLE ark_action_categories RENAME COLUMN cat_systemdate TO cat_SystemDate;
ALTER TABLE ark_action_categories RENAME COLUMN cat_systemtime TO cat_SystemTime;
ALTER TABLE ark_action_categories RENAME COLUMN cat_namemachine TO cat_NameMachine;
ALTER TABLE ark_action_categories RENAME COLUMN cat_usercreator TO cat_UserCreator;
ALTER TABLE ark_action_categories RENAME COLUMN cat_lastupdatedate TO cat_LastUpdateDate;
ALTER TABLE ark_action_categories RENAME COLUMN cat_lastupdatetime TO cat_LastUpdateTime;
ALTER TABLE ark_action_categories RENAME COLUMN cat_lastmachine TO cat_LastMachine;
ALTER TABLE ark_action_categories RENAME COLUMN cat_userlastupdate TO cat_UserLastUpdate;

-- 5. ACTUALIZACIÓN PARA TABLA ark_currencies (Prefijo: mda_)
ALTER TABLE ark_currencies RENAME COLUMN mda_systemdate TO mda_SystemDate;
ALTER TABLE ark_currencies RENAME COLUMN mda_systemtime TO mda_SystemTime;
ALTER TABLE ark_currencies RENAME COLUMN mda_namemachine TO mda_NameMachine;
ALTER TABLE ark_currencies RENAME COLUMN mda_usercreator TO mda_UserCreator;
ALTER TABLE ark_currencies RENAME COLUMN mda_lastupdatedate TO mda_LastUpdateDate;
ALTER TABLE ark_currencies RENAME COLUMN mda_lastupdatetime TO mda_LastUpdateTime;
ALTER TABLE ark_currencies RENAME COLUMN mda_lastmachine TO mda_LastMachine;
ALTER TABLE ark_currencies RENAME COLUMN mda_userlastupdate TO mda_UserLastUpdate;

-- 6. ACTUALIZACIÓN PARA TABLA ark_device_types (Prefijo: dty_)
ALTER TABLE ark_device_types RENAME COLUMN dty_systemdate TO dty_SystemDate;
ALTER TABLE ark_device_types RENAME COLUMN dty_systemtime TO dty_SystemTime;
ALTER TABLE ark_device_types RENAME COLUMN dty_namemachine TO dty_NameMachine;
ALTER TABLE ark_device_types RENAME COLUMN dty_usercreator TO dty_UserCreator;
ALTER TABLE ark_device_types RENAME COLUMN dty_lastupdatedate TO dty_LastUpdateDate;
ALTER TABLE ark_device_types RENAME COLUMN dty_lastupdatetime TO dty_LastUpdateTime;
ALTER TABLE ark_device_types RENAME COLUMN dty_lastmachine TO dty_LastMachine;
ALTER TABLE ark_device_types RENAME COLUMN dty_userlastupdate TO dty_UserLastUpdate;

-- 7. ACTUALIZACIÓN PARA TABLA ark_employees (Prefijo: emy_)
ALTER TABLE ark_employees RENAME COLUMN emy_systemdate TO emy_SystemDate;
ALTER TABLE ark_employees RENAME COLUMN emy_systemtime TO emy_SystemTime;
ALTER TABLE ark_employees RENAME COLUMN emy_namemachine TO emy_NameMachine;
ALTER TABLE ark_employees RENAME COLUMN emy_usercreator TO emy_UserCreator;
ALTER TABLE ark_employees RENAME COLUMN emy_lastupdatedate TO emy_LastUpdateDate;
ALTER TABLE ark_employees RENAME COLUMN emy_lastupdatetime TO emy_LastUpdateTime;
ALTER TABLE ark_employees RENAME COLUMN emy_lastmachine TO emy_LastMachine;
ALTER TABLE ark_employees RENAME COLUMN emy_userlastupdate TO emy_UserLastUpdate;

-- 8. ACTUALIZACIÓN PARA TABLA ark_functional_units (Prefijo: fun_)
ALTER TABLE ark_functional_units RENAME COLUMN fun_systemdate TO fun_SystemDate;
ALTER TABLE ark_functional_units RENAME COLUMN fun_systemtime TO fun_SystemTime;
ALTER TABLE ark_functional_units RENAME COLUMN fun_namemachine TO fun_NameMachine;
ALTER TABLE ark_functional_units RENAME COLUMN fun_usercreator TO fun_UserCreator;
ALTER TABLE ark_functional_units RENAME COLUMN fun_lastupdatedate TO fun_LastUpdateDate;
ALTER TABLE ark_functional_units RENAME COLUMN fun_lastupdatetime TO fun_LastUpdateTime;
ALTER TABLE ark_functional_units RENAME COLUMN fun_lastmachine TO fun_LastMachine;
ALTER TABLE ark_functional_units RENAME COLUMN fun_userlastupdate TO fun_UserLastUpdate;

-- 9. ACTUALIZACIÓN PARA TABLA ark_it_assets (Prefijo: ita_)
ALTER TABLE ark_it_assets RENAME COLUMN ita_systemdate TO ita_SystemDate;
ALTER TABLE ark_it_assets RENAME COLUMN ita_systemtime TO ita_SystemTime;
ALTER TABLE ark_it_assets RENAME COLUMN ita_namemachine TO ita_NameMachine;
ALTER TABLE ark_it_assets RENAME COLUMN ita_usercreator TO ita_UserCreator;
ALTER TABLE ark_it_assets RENAME COLUMN ita_lastupdatedate TO ita_LastUpdateDate;
ALTER TABLE ark_it_assets RENAME COLUMN ita_lastupdatetime TO ita_LastUpdateTime;
ALTER TABLE ark_it_assets RENAME COLUMN ita_lastmachine TO ita_LastMachine;
ALTER TABLE ark_it_assets RENAME COLUMN ita_userlastupdate TO ita_UserLastUpdate;

-- 10. ACTUALIZACIÓN PARA TABLA ark_job_titles (Prefijo: job_)
ALTER TABLE ark_job_titles RENAME COLUMN job_systemdate TO job_SystemDate;
ALTER TABLE ark_job_titles RENAME COLUMN job_systemtime TO job_SystemTime;
ALTER TABLE ark_job_titles RENAME COLUMN job_namemachine TO job_NameMachine;
ALTER TABLE ark_job_titles RENAME COLUMN job_usercreator TO job_UserCreator;
ALTER TABLE ark_job_titles RENAME COLUMN job_lastupdatedate TO job_LastUpdateDate;
ALTER TABLE ark_job_titles RENAME COLUMN job_lastupdatetime TO job_LastUpdateTime;
ALTER TABLE ark_job_titles RENAME COLUMN job_lastmachine TO job_LastMachine;
ALTER TABLE ark_job_titles RENAME COLUMN job_userlastupdate TO job_UserLastUpdate;

-- 11. ACTUALIZACIÓN PARA TABLA ark_requests (Prefijo: req_)
ALTER TABLE ark_requests RENAME COLUMN req_systemdate TO req_SystemDate;
ALTER TABLE ark_requests RENAME COLUMN req_systemtime TO req_SystemTime;
ALTER TABLE ark_requests RENAME COLUMN req_namemachine TO req_NameMachine;
ALTER TABLE ark_requests RENAME COLUMN req_usercreator TO req_UserCreator;
ALTER TABLE ark_requests RENAME COLUMN req_lastupdatedate TO req_LastUpdateDate;
ALTER TABLE ark_requests RENAME COLUMN req_lastupdatetime TO req_LastUpdateTime;
ALTER TABLE ark_requests RENAME COLUMN req_lastmachine TO req_LastMachine;
ALTER TABLE ark_requests RENAME COLUMN req_userlastupdate TO req_UserLastUpdate;

-- 12. ACTUALIZACIÓN PARA TABLA ark_session_details (Prefijo: dts_)
ALTER TABLE ark_sessions_details RENAME COLUMN dts_systemdate TO dts_SystemDate;
ALTER TABLE ark_sessions_details RENAME COLUMN dts_systemtime TO dts_SystemTime;
ALTER TABLE ark_sessions_details RENAME COLUMN dts_namemachine TO dts_NameMachine;
ALTER TABLE ark_sessions_details RENAME COLUMN dts_usercreator TO dts_UserCreator;
ALTER TABLE ark_sessions_details RENAME COLUMN dts_lastupdatedate TO dts_LastUpdateDate;
ALTER TABLE ark_sessions_details RENAME COLUMN dts_lastupdatetime TO dts_LastUpdateTime;
ALTER TABLE ark_sessions_details RENAME COLUMN dts_lastmachine TO dts_LastMachine;
ALTER TABLE ark_sessions_details RENAME COLUMN dts_userlastupdate TO dts_UserLastUpdate;

-- 13. ACTUALIZACIÓN PARA TABLA ark_sessions (Prefijo: ses_)
ALTER TABLE ark_sessions RENAME COLUMN ses_systemdate TO ses_SystemDate;
ALTER TABLE ark_sessions RENAME COLUMN ses_systemtime TO ses_SystemTime;
ALTER TABLE ark_sessions RENAME COLUMN ses_namemachine TO ses_NameMachine;
ALTER TABLE ark_sessions RENAME COLUMN ses_usercreator TO ses_UserCreator;
ALTER TABLE ark_sessions RENAME COLUMN ses_lastupdatedate TO ses_LastUpdateDate;
ALTER TABLE ark_sessions RENAME COLUMN ses_lastupdatetime TO ses_LastUpdateTime;
ALTER TABLE ark_sessions RENAME COLUMN ses_lastmachine TO ses_LastMachine;
ALTER TABLE ark_sessions RENAME COLUMN ses_userlastupdate TO ses_UserLastUpdate;

-- 14. ACTUALIZACIÓN PARA TABLA ark_tasks_completed (Prefijo: tsc_)
ALTER TABLE ark_tasks_completed RENAME COLUMN tsc_systemdate TO tsc_SystemDate;
ALTER TABLE ark_tasks_completed RENAME COLUMN tsc_systemtime TO tsc_SystemTime;
ALTER TABLE ark_tasks_completed RENAME COLUMN tsc_namemachine TO tsc_NameMachine;
ALTER TABLE ark_tasks_completed RENAME COLUMN tsc_usercreator TO tsc_UserCreator;
ALTER TABLE ark_tasks_completed RENAME COLUMN tsc_lastupdatedate TO tsc_LastUpdateDate;
ALTER TABLE ark_tasks_completed RENAME COLUMN tsc_lastupdatetime TO tsc_LastUpdateTime;
ALTER TABLE ark_tasks_completed RENAME COLUMN tsc_lastmachine TO tsc_LastMachine;
ALTER TABLE ark_tasks_completed RENAME COLUMN tsc_userlastupdate TO tsc_UserLastUpdate;

-- 15. ACTUALIZACIÓN PARA TABLA ark_users (Prefijo: usr_)
ALTER TABLE ark_users RENAME COLUMN usr_systemdate TO usr_SystemDate;
ALTER TABLE ark_users RENAME COLUMN usr_systemtime TO usr_SystemTime;
ALTER TABLE ark_users RENAME COLUMN usr_namemachine TO usr_NameMachine;
ALTER TABLE ark_users RENAME COLUMN usr_usercreator TO usr_UserCreator;
ALTER TABLE ark_users RENAME COLUMN usr_lastupdatedate TO usr_LastUpdateDate;
ALTER TABLE ark_users RENAME COLUMN usr_lastupdatetime TO usr_LastUpdateTime;
ALTER TABLE ark_users RENAME COLUMN usr_lastmachine TO usr_LastMachine;
ALTER TABLE ark_users RENAME COLUMN usr_userlastupdate TO usr_UserLastUpdate;
-- FIN DE LAS ACTUALIZACIONES DE ESQUEMA DE BASE DE DATOS