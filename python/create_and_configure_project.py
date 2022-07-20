from dbtc import dbtCloudClient

client = dbtCloudClient()

accounts = client.cloud.list_accounts()

account_id = accounts['data'][0]['id']
customer_name = "Customer3"
project_name = 'Snowflake - ' + customer_name

snowflake_account = 'zna84829'
snowflake_role = 'transformer'
snowflake_database = 'kbrock_'+customer_name
snowflake_warehouse = 'transforming'
git_clone_url = 'git@github.com:kbrock91/dbt-snowflake-demo.git'

print(project_name)

projects = client.cloud.list_projects(account_id)

project_exists = False

for project in projects['data']:
    if project['name'] == project_name:
        project_exists = True

if not project_exists:

    project_payload = {
        'id': None,
        'name': project_name,
        'dbt_project_subdirectory': None,
        'account_id': account_id,
        'connection_id': None,
        'repository_id': None
    }


    create_project = client.cloud.create_project(account_id, project_payload) 

    project_id = create_project['data']['id']

else: 
    project_id = project['id']

#create snowflake connection
conn_payload = {
    'id': None,
    'name': 'Snowflake',
    'type': 'snowflake',
    'details': {
        'account': snowflake_account,
        'role': snowflake_role,
        'database': snowflake_database,
        'warehouse': snowflake_warehouse,
        'oauth_client_id': None,
        'oauth_client_secret': None,
        'client_session_keep_alive': False,
        'allow_sso': False,
    },
    'state': 1,
    'account_id': account_id,
    'project_id': project_id
}

create_conn = client.cloud.create_connection(account_id, project_id, conn_payload) 

conn_id = create_conn['data']['id']

#create repository
repo_payload = {
    'account_id': 1,
    'project_id': 1,
    'remote_url': git_clone_url,
    'git_clone_strategy': 'deploy_key',
    'github_installation_id': None,
    'token_str': None
}


create_repo = client.cloud.create_repository(account_id, project_id, repo_payload) 

repo_id = create_repo['data']['id']

#update project to associate the snowflake and repository details
update_project_payload = {
    "name": project_name,
    "account_id": account_id,
    "repository_id": repo_id,
    "connection_id": conn_id,
    "id": project_id
}


update_project = client.cloud.update_project(account_id, project_id, update_project_payload)