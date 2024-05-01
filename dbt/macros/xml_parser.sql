/*
    <element>value</element>
*/

{% macro get_elements( relation, column ) %}
    {% set xml_query %}
        with keys as (
        select object_keys( dept_employee_xml.xmldata ) key
        from dept_employee_xml
        limit 1
        )
        select value
        from keys, table(flatten(keys.key))
    {% endset %}

    {% set results = run_query( xml_query ) %}

    {% if execute %}
    {# Return the first column #}
    {% set results_list = results.columns[0].values() %}
    {% else %}
    {% set results_list = [] %}
    {% endif %}

    {{ return(results_list) }}    
{% endmacro %}
