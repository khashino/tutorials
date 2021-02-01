https://apex.oracle.com/pls/apex/apexlessons/r/oracle-apex-office-hours/apex-collection?session=6992500904083

#1) DISABLE Procedure
This procedure stops the automation from executing automatically.

Syntax
```
APEX_AUTOMATION.DISABLE(
    p_application_id         IN NUMBER   DEFAULT wwv_flow.g_flow_id,
    p_static_id              IN VARCHAR2 );
Parameters
Parameter	Description
p_application_id	ID of the application which contains the automation.
p_static_id	Static ID of the automation to disable.
Examples
This example disables the automation request-approval in application 89243.


BEGIN
    apex_automation.disable(
        p_application_id  => 89243,
        p_static_id       => 'request-approval' );
END;
```
#2) ENABLE Procedure
This procedure enables the automation for normal execution.

Syntax
```
APEX_AUTOMATION.ENABLE(
    p_application_id         IN NUMBER   DEFAULT wwv_flow.g_flow_id,
    p_static_id              IN VARCHAR2 );
Parameters
Parameter	Description
p_application_id	ID of the application which contains the automation.
p_static_id	Static ID of the automation to disable.
Examples
This example enables the automation request-approval in application 89243.


BEGIN
    apex_automation.enable(
        p_application_id  => 89243,
        p_static_id       => 'request-approval' );
END;
```
#3) EXECUTE Procedure
This procedure executes an automation.

Syntax
```
APEX_AUTOMATION.EXECUTE(
    p_application_id    IN NUMBER                        DEFAULT wwv_flow.g_flow_id,
    p_static_id         IN VARCHAR2,
    p_filters           IN wwv_flow_exec_api.t_filters   DEFAULT wwv_flow_exec_api.c_empty_filters,
    p_order_bys         IN wwv_flow_exec_api.t_order_bys DEFAULT wwv_flow_exec_api.c_empty_order_bys );
Parameters
Parameter	Description
p_application_id	ID of the application which contains the automation.
p_static_id	Static ID of the automation to execute.
p_filters	Additional filters to apply to the automation query.
p_order_bys	ORDER BY clauses to apply to the automation query.
Examples
This example executes the automation request-approval.


BEGIN 
    apex_automation.execute(
        p_application_id  => 89243,
        p_static_id       => 'request-approval'  );
END;
```
