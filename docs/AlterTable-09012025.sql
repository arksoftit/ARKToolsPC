-- 1. ACTUALIZACIÓN PARA TABLA ark_company (Prefijo: emp_)
ALTER TABLE ark_company ADD COLUMN emp_systemdate TEXT;
ALTER TABLE ark_company ADD COLUMN emp_systemtime TEXT;
ALTER TABLE ark_company ADD COLUMN emp_namemachine TEXT;
ALTER TABLE ark_company ADD COLUMN emp_usercreator TEXT;
ALTER TABLE ark_company ADD COLUMN emp_lastupdatedate TEXT;
ALTER TABLE ark_company ADD COLUMN emp_lastupdatetime TEXT;
ALTER TABLE ark_company ADD COLUMN emp_lastmachine TEXT;
ALTER TABLE ark_company ADD COLUMN emp_userlastupdate TEXT;

-- 2. ACTUALIZACIÓN PARA TABLA ark_clients (Prefijo: clt_)
ALTER TABLE ark_clients ADD COLUMN clt_systemdate TEXT;
ALTER TABLE ark_clients ADD COLUMN clt_systemtime TEXT;
ALTER TABLE ark_clients ADD COLUMN clt_namemachine TEXT;
ALTER TABLE ark_clients ADD COLUMN clt_usercreator TEXT;
ALTER TABLE ark_clients ADD COLUMN clt_lastupdatedate TEXT;
ALTER TABLE ark_clients ADD COLUMN clt_lastupdatetime TEXT;
ALTER TABLE ark_clients ADD COLUMN clt_lastmachine TEXT;
ALTER TABLE ark_clients ADD COLUMN clt_userlastupdate TEXT;

-- 3. ACTUALIZACIÓN PARA TABLA ark_actions (Prefijo: act_)
ALTER TABLE ark_actions ADD COLUMN act_systemdate TEXT;
ALTER TABLE ark_actions ADD COLUMN act_systemtime TEXT;
ALTER TABLE ark_actions ADD COLUMN act_namemachine TEXT;
ALTER TABLE ark_actions ADD COLUMN act_usercreator TEXT;
ALTER TABLE ark_actions ADD COLUMN act_lastupdatedate TEXT;
ALTER TABLE ark_actions ADD COLUMN act_lastupdatetime TEXT;
ALTER TABLE ark_actions ADD COLUMN act_lastmachine TEXT;
ALTER TABLE ark_actions ADD COLUMN act_userlastupdate TEXT;

-- 4. ACTUALIZACIÓN PARA TABLA ark_action_categories (Prefijo: cat_)
ALTER TABLE ark_action_categories ADD COLUMN cat_systemdate TEXT;
ALTER TABLE ark_action_categories ADD COLUMN cat_systemtime TEXT;
ALTER TABLE ark_action_categories ADD COLUMN cat_namemachine TEXT;
ALTER TABLE ark_action_categories ADD COLUMN cat_usercreator TEXT;
ALTER TABLE ark_action_categories ADD COLUMN cat_lastupdatedate TEXT;
ALTER TABLE ark_action_categories ADD COLUMN cat_lastupdatetime TEXT;
ALTER TABLE ark_action_categories ADD COLUMN cat_lastmachine TEXT;
ALTER TABLE ark_action_categories ADD COLUMN cat_userlastupdate TEXT;

-- 5. ACTUALIZACIÓN PARA TABLA ark_currencies (Prefijo: mda_)
ALTER TABLE ark_currencies ADD COLUMN mda_systemdate TEXT;
ALTER TABLE ark_currencies ADD COLUMN mda_systemtime TEXT;
ALTER TABLE ark_currencies ADD COLUMN mda_namemachine TEXT;
ALTER TABLE ark_currencies ADD COLUMN mda_usercreator TEXT;
ALTER TABLE ark_currencies ADD COLUMN mda_lastupdatedate TEXT;
ALTER TABLE ark_currencies ADD COLUMN mda_lastupdatetime TEXT;
ALTER TABLE ark_currencies ADD COLUMN mda_lastmachine TEXT;
ALTER TABLE ark_currencies ADD COLUMN mda_userlastupdate TEXT;

-- 6. ACTUALIZACIÓN PARA TABLA ark_device_types (Prefijo: dty_)
ALTER TABLE ark_device_types ADD COLUMN dty_systemdate TEXT;
ALTER TABLE ark_device_types ADD COLUMN dty_systemtime TEXT;
ALTER TABLE ark_device_types ADD COLUMN dty_namemachine TEXT;
ALTER TABLE ark_device_types ADD COLUMN dty_usercreator TEXT;
ALTER TABLE ark_device_types ADD COLUMN dty_lastupdatedate TEXT;
ALTER TABLE ark_device_types ADD COLUMN dty_lastupdatetime TEXT;
ALTER TABLE ark_device_types ADD COLUMN dty_lastmachine TEXT;
ALTER TABLE ark_device_types ADD COLUMN dty_userlastupdate TEXT;

-- 7. ACTUALIZACIÓN PARA TABLA ark_employees (Prefijo: emy_)
ALTER TABLE ark_employees ADD COLUMN emy_systemdate TEXT;
ALTER TABLE ark_employees ADD COLUMN emy_systemtime TEXT;
ALTER TABLE ark_employees ADD COLUMN emy_namemachine TEXT;
ALTER TABLE ark_employees ADD COLUMN emy_usercreator TEXT;
ALTER TABLE ark_employees ADD COLUMN emy_lastupdatedate TEXT;
ALTER TABLE ark_employees ADD COLUMN emy_lastupdatetime TEXT;
ALTER TABLE ark_employees ADD COLUMN emy_lastmachine TEXT;
ALTER TABLE ark_employees ADD COLUMN emy_userlastupdate TEXT;

-- 8. ACTUALIZACIÓN PARA TABLA ark_functional_units (Prefijo: fun_)
ALTER TABLE ark_functional_units ADD COLUMN fun_systemdate TEXT;
ALTER TABLE ark_functional_units ADD COLUMN fun_systemtime TEXT;
ALTER TABLE ark_functional_units ADD COLUMN fun_namemachine TEXT;
ALTER TABLE ark_functional_units ADD COLUMN fun_usercreator TEXT;
ALTER TABLE ark_functional_units ADD COLUMN fun_lastupdatedate TEXT;
ALTER TABLE ark_functional_units ADD COLUMN fun_lastupdatetime TEXT;
ALTER TABLE ark_functional_units ADD COLUMN fun_lastmachine TEXT;
ALTER TABLE ark_functional_units ADD COLUMN fun_userlastupdate TEXT;

-- 9. ACTUALIZACIÓN PARA TABLA ark_it_assets (Prefijo: ita_)
ALTER TABLE ark_it_assets ADD COLUMN ita_systemdate TEXT;
ALTER TABLE ark_it_assets ADD COLUMN ita_systemtime TEXT;
ALTER TABLE ark_it_assets ADD COLUMN ita_namemachine TEXT;
ALTER TABLE ark_it_assets ADD COLUMN ita_usercreator TEXT;
ALTER TABLE ark_it_assets ADD COLUMN ita_lastupdatedate TEXT;
ALTER TABLE ark_it_assets ADD COLUMN ita_lastupdatetime TEXT;
ALTER TABLE ark_it_assets ADD COLUMN ita_lastmachine TEXT;
ALTER TABLE ark_it_assets ADD COLUMN ita_userlastupdate TEXT;

-- 10. ACTUALIZACIÓN PARA TABLA ark_job_titles (Prefijo: job_)
ALTER TABLE ark_job_titles ADD COLUMN job_systemdate TEXT;
ALTER TABLE ark_job_titles ADD COLUMN job_systemtime TEXT;
ALTER TABLE ark_job_titles ADD COLUMN job_namemachine TEXT;
ALTER TABLE ark_job_titles ADD COLUMN job_usercreator TEXT;
ALTER TABLE ark_job_titles ADD COLUMN job_lastupdatedate TEXT;
ALTER TABLE ark_job_titles ADD COLUMN job_lastupdatetime TEXT;
ALTER TABLE ark_job_titles ADD COLUMN job_lastmachine TEXT;
ALTER TABLE ark_job_titles ADD COLUMN job_userlastupdate TEXT;

-- 11. ACTUALIZACIÓN PARA TABLA ark_requests (Prefijo: req_)
ALTER TABLE ark_requests ADD COLUMN req_systemdate TEXT;
ALTER TABLE ark_requests ADD COLUMN req_systemtime TEXT;
ALTER TABLE ark_requests ADD COLUMN req_namemachine TEXT;
ALTER TABLE ark_requests ADD COLUMN req_usercreator TEXT;
ALTER TABLE ark_requests ADD COLUMN req_lastupdatedate TEXT;
ALTER TABLE ark_requests ADD COLUMN req_lastupdatetime TEXT;
ALTER TABLE ark_requests ADD COLUMN req_lastmachine TEXT;
ALTER TABLE ark_requests ADD COLUMN req_userlastupdate TEXT;

-- 12. ACTUALIZACIÓN PARA TABLA ark_session_details (Prefijo: dts_)
ALTER TABLE ark_session_details ADD COLUMN dts_systemdate TEXT;
ALTER TABLE ark_session_details ADD COLUMN dts_systemtime TEXT;
ALTER TABLE ark_session_details ADD COLUMN dts_namemachine TEXT;
ALTER TABLE ark_session_details ADD COLUMN dts_usercreator TEXT;
ALTER TABLE ark_session_details ADD COLUMN dts_lastupdatedate TEXT;
ALTER TABLE ark_session_details ADD COLUMN dts_lastupdatetime TEXT;
ALTER TABLE ark_session_details ADD COLUMN dts_lastmachine TEXT;
ALTER TABLE ark_session_details ADD COLUMN dts_userlastupdate TEXT;

-- 13. ACTUALIZACIÓN PARA TABLA ark_sessions (Prefijo: ses_)
ALTER TABLE ark_sessions ADD COLUMN ses_systemdate TEXT;
ALTER TABLE ark_sessions ADD COLUMN ses_systemtime TEXT;
ALTER TABLE ark_sessions ADD COLUMN ses_namemachine TEXT;
ALTER TABLE ark_sessions ADD COLUMN ses_usercreator TEXT;
ALTER TABLE ark_sessions ADD COLUMN ses_lastupdatedate TEXT;
ALTER TABLE ark_sessions ADD COLUMN ses_lastupdatetime TEXT;
ALTER TABLE ark_sessions ADD COLUMN ses_lastmachine TEXT;
ALTER TABLE ark_sessions ADD COLUMN ses_userlastupdate TEXT;

-- 14. ACTUALIZACIÓN PARA TABLA ark_tasks_completed (Prefijo: tsc_)
ALTER TABLE ark_tasks_completed ADD COLUMN tsc_systemdate TEXT;
ALTER TABLE ark_tasks_completed ADD COLUMN tsc_systemtime TEXT;
ALTER TABLE ark_tasks_completed ADD COLUMN tsc_namemachine TEXT;
ALTER TABLE ark_tasks_completed ADD COLUMN tsc_usercreator TEXT;
ALTER TABLE ark_tasks_completed ADD COLUMN tsc_lastupdatedate TEXT;
ALTER TABLE ark_tasks_completed ADD COLUMN tsc_lastupdatetime TEXT;
ALTER TABLE ark_tasks_completed ADD COLUMN tsc_lastmachine TEXT;
ALTER TABLE ark_tasks_completed ADD COLUMN tsc_userlastupdate TEXT;

-- 15. ACTUALIZACIÓN PARA TABLA ark_users (Prefijo: usr_)
ALTER TABLE ark_users ADD COLUMN usr_systemdate TEXT;
ALTER TABLE ark_users ADD COLUMN usr_systemtime TEXT;
ALTER TABLE ark_users ADD COLUMN usr_namemachine TEXT;
ALTER TABLE ark_users ADD COLUMN usr_usercreator TEXT;
ALTER TABLE ark_users ADD COLUMN usr_lastupdatedate TEXT;
ALTER TABLE ark_users ADD COLUMN usr_lastupdatetime TEXT;
ALTER TABLE ark_users ADD COLUMN usr_lastmachine TEXT;
ALTER TABLE ark_users ADD COLUMN usr_userlastupdate TEXT;
-- FIN DE LAS ACTUALIZACIONES DE ESQUEMA DE BASE DE DATOS
