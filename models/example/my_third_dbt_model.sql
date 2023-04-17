
-- Use the `source` function to select from one source

select *
from {{ source('schema', 'my_data') }}

