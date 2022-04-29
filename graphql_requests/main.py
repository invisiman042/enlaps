from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import sys
sys.path.insert(1, r'C:\Users\nicol\Desktop\enlaps_python\enlaps')
import settings.settings as settings

# url = settings.url
# headers = settings.headers
# params = settings.params

staging_url = settings.staging_url
staging_headers = settings.staging_headers
# staging_params = settings.staging_params

transport = AIOHTTPTransport(url=staging_url, headers=staging_headers)
client = Client(transport=transport)

params_for_tikee_by_sn = {'search': [{'field': 'serial_number', 'value': '801911'}]}
params_tikee = {"id": 140}

def get_query_response(query_gql, query_params):
    # query_file = fr'C:\Users\33638\OneDrive\Bureau\PYTHON\enlaps\graphql_requests\graphql\{query_gql}.graphql'
    query_file = fr'C:\Users\nicol\Desktop\enlaps_python\enlaps\graphql_requests\graphql\{query_gql}.graphql'
    query = gql(open(query_file).read())
    response = client.execute(query, variable_values=query_params)
    return response
