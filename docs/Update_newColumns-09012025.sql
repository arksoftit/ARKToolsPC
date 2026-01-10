-- 1. ark_company (emp_)
UPDATE ark_company SET 
    emp_systemdate=emp_FechaCreacion, 
    emp_systemtime=emp_FechaCreacion, 
    emp_namemachine='NIBIRUS', 
    emp_lastupdatedate=emp_FechaCreacion, 
    emp_lastupdatetime=emp_FechaCreacion, 
    emp_lastmachine='NIBIRUS', 
    emp_usercreator='juanep', 
    emp_userlastupdate='juanep' 
WHERE emp_systemdate IS NULL;

-- 2. ark_clients (clt_)
UPDATE ark_clients SET 
    clt_systemdate=clt_FechaCreacion, 
    clt_systemtime=clt_FechaCreacion, 
    clt_namemachine='NIBIRUS', 
    clt_lastupdatedate=clt_FechaCreacion, 
    clt_lastupdatetime=clt_FechaCreacion, 
    clt_lastmachine='NIBIRUS', 
    clt_usercreator='juanep', 
    clt_userlastupdate='juanep' 
WHERE clt_systemdate IS NULL;

-- 3. ark_actions (act_)
UPDATE ark_actions SET 
    act_systemdate=act_FechaCreacion, 
    act_systemtime=act_FechaCreacion, 
    act_namemachine='NIBIRUS', 
    act_lastupdatedate=act_FechaCreacion, 
    act_lastupdatetime=act_FechaCreacion, 
    act_lastmachine='NIBIRUS', 
    act_usercreator='juanep', 
    act_userlastupdate='juanep' 
WHERE act_systemdate IS NULL;

-- 4. ark_action_categories (cat_)
UPDATE ark_action_categories SET 
    cat_systemdate=cat_FechaCreacion, 
    cat_systemtime=cat_FechaCreacion, 
    cat_namemachine='NIBIRUS', 
    cat_lastupdatedate=cat_FechaCreacion, 
    cat_lastupdatetime=cat_FechaCreacion, 
    cat_lastmachine='NIBIRUS', 
    cat_usercreator='juanep', 
    cat_userlastupdate='juanep' 
WHERE cat_systemdate IS NULL;

-- 5. ark_currencies (mda_)
UPDATE ark_currencies SET 
    mda_systemdate=mda_FechaCreacion, 
    mda_systemtime=mda_FechaCreacion, 
    mda_namemachine='NIBIRUS', 
    mda_lastupdatedate=mda_FechaCreacion, 
    mda_lastupdatetime=mda_FechaCreacion, 
    mda_lastmachine='NIBIRUS', 
    mda_usercreator='juanep', 
    mda_userlastupdate='juanep' 
WHERE mda_systemdate IS NULL;

-- 6. ark_device_types (dty_)
UPDATE ark_device_types SET 
    dty_systemdate=dty_FechaCreacion, 
    dty_systemtime=dty_FechaCreacion, 
    dty_namemachine='NIBIRUS', 
    dty_lastupdatedate=dty_FechaCreacion, 
    dty_lastupdatetime=dty_FechaCreacion, 
    dty_lastmachine='NIBIRUS', 
    dty_usercreator='juanep', 
    dty_userlastupdate='juanep' 
WHERE dty_systemdate IS NULL;

-- 7. ark_employees (emy_)
UPDATE ark_employees SET 
    emy_systemdate=emy_FechaCreacion, 
    emy_systemtime=emy_FechaCreacion, 
    emy_namemachine='NIBIRUS', 
    emy_lastupdatedate=emy_FechaCreacion, 
    emy_lastupdatetime=emy_FechaCreacion, 
    emy_lastmachine='NIBIRUS', 
    emy_usercreator='juanep', 
    emy_userlastupdate='juanep' 
WHERE emy_systemdate IS NULL;

-- 8. ark_functional_units (fun_)
UPDATE ark_functional_units SET 
    fun_systemdate=fun_FechaCreacion, 
    fun_systemtime=fun_FechaCreacion, 
    fun_namemachine='NIBIRUS', 
    fun_lastupdatedate=fun_FechaCreacion, 
    fun_lastupdatetime=fun_FechaCreacion, 
    fun_lastmachine='NIBIRUS', 
    fun_usercreator='juanep', 
    fun_userlastupdate='juanep' 
WHERE fun_systemdate IS NULL;


-- 9. ark_it_assets (ita_)
UPDATE ark_it_assets SET 
    ita_systemdate=ita_FechaCreacion, 
    ita_systemtime=ita_FechaCreacion, 
    ita_namemachine='NIBIRUS', 
    ita_lastupdatedate=ita_FechaCreacion, 
    ita_lastupdatetime=ita_FechaCreacion, 
    ita_lastmachine='NIBIRUS', 
    ita_usercreator='juanep', 
    ita_userlastupdate='juanep' 
WHERE ita_systemdate IS NULL;

-- 10. ark_job_titles (job_)
UPDATE ark_job_titles SET 
    job_systemdate=job_FechaCreacion, 
    job_systemtime=job_FechaCreacion, 
    job_namemachine='NIBIRUS', 
    job_lastupdatedate=job_FechaCreacion, 
    job_lastupdatetime=job_FechaCreacion, 
    job_lastmachine='NIBIRUS', 
    job_usercreator='juanep', 
    job_userlastupdate='juanep' 
WHERE job_systemdate IS NULL;

-- 11. ark_requests (req_)
UPDATE ark_requests SET 
    req_systemdate=req_FechaCreacion, 
    req_systemtime=req_FechaCreacion, 
    req_namemachine='NIBIRUS', 
    req_lastupdatedate=req_FechaCreacion, 
    req_lastupdatetime=req_FechaCreacion, 
    req_lastmachine='NIBIRUS', 
    req_usercreator='juanep', 
    req_userlastupdate='juanep' 
WHERE req_systemdate IS NULL;

-- 12. ark_sessions_details (dts_)
UPDATE ark_sessions_details SET 
    dts_systemdate=dts_FechaSesion, 
    dts_systemtime=dts_FechaSesion, 
    dts_namemachine='NIBIRUS', 
    dts_lastupdatedate=dts_FechaSesion, 
    dts_lastupdatetime=dts_FechaSesion, 
    dts_lastmachine='NIBIRUS', 
    dts_usercreator='juanep', 
    dts_userlastupdate='juanep' 
WHERE dts_systemdate IS NULL;   

-- 13. ark_sessions (ses_)
UPDATE ark_sessions SET 
    ses_systemdate=ses_FechaCreacion, 
    ses_systemtime=ses_FechaCreacion, 
    ses_namemachine='NIBIRUS', 
    ses_lastupdatedate=ses_FechaCreacion, 
    ses_lastupdatetime=ses_FechaCreacion, 
    ses_lastmachine='NIBIRUS', 
    ses_usercreator='juanep', 
    ses_userlastupdate='juanep' 
WHERE ses_systemdate IS NULL;

-- 14. ark_tasks_completed (tsc_)
UPDATE ark_tasks_completed SET 
    tsc_systemdate=tsc_FechaCreacion, 
    tsc_systemtime=tsc_FechaCreacion, 
    tsc_namemachine='NIBIRUS', 
    tsc_lastupdatedate=tsc_FechaCreacion, 
    tsc_lastupdatetime=tsc_FechaCreacion, 
    tsc_lastmachine='NIBIRUS', 
    tsc_usercreator='juanep', 
    tsc_userlastupdate='juanep' 
WHERE tsc_systemdate IS NULL;

-- 15. ark_users (usr_)
UPDATE ark_users SET 
    usr_systemdate=usr_FechaCreacion, 
    usr_systemtime=usr_FechaCreacion, 
    usr_namemachine='NIBIRUS', 
    usr_lastupdatedate=usr_FechaCreacion, 
    usr_lastupdatetime=usr_FechaCreacion, 
    usr_lastmachine='NIBIRUS', 
    usr_usercreator='juanep', 
    usr_userlastupdate='juanep' 
WHERE usr_systemdate IS NULL;