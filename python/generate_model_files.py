import json

with open('python/table_metadata.json', 'r') as f:
  data = json.load(f)

for x in data['models']:
    model_name = x['model_name']
    source_name = x['source_name']
    source_table = x['source_table']
    fields = x['fields']
    materialization = x['materialization']

    config_text = f"""
        {{{{ 
            config(
                materialized = '{materialization}'
                    )

        }}}}"""
    
    select_text = f"""
    select 
        {fields} 
    from """ + "{{" + f" source(\"{source_name}\", \"{source_table}\") " +"}}"
    

    model_text =  config_text + "\n"+ select_text
 
    with open(f"dbt/models/demos/generated_models/{model_name}.sql", "w") as f:
            f.write(model_text)
            f.close()