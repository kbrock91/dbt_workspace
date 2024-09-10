{% macro log_results(results) %}

  {% if execute %}
  {{ log("========== Begin Summary ==========", info=True) }}
  {% for res in results -%}
    {% set line -%}
        {% if'rows_affected' in res.adapter_response  %}
            node: {{ res.node.unique_id }};  rows_affected: {{ res.adapter_response.rows_affected }}
        {% endif %}

    {%- endset %}

    {{ log(line, info=True) }}
  {% endfor %}
  {{ log("========== End Summary ==========", info=True) }}
  {% endif %}

{% endmacro %}
