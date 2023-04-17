{% macro concat(column_name, list_of_columns_to_concat, column_alias`) %}
    {{ column_name }}::text {%- for col in list_of_columns_to_concat %} ({{ col }}) {%- if not loop.last -%} || {%- endif -%} {%- endfor %} as {{ column_alias }}
{% endmacro %}