{% macro concat(list_of_columns_to_concat, column_alias`) %}
    {%- for col in list_of_columns_to_concat %} ({{ col }}::text) {%- if not loop.last -%} || {%- endif -%} {%- endfor %} as {{ column_alias }}
{% endmacro %}