
        {{
            config(
                materialized = 'table'
                    )
        }}

    select 
        * 
    from {{ source("random_source_1", "random_source_table_1") }}