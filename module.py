# -*- coding: utf-8 -*-
"""test module for colab
"""
from requests import Request, Session

# meta for discovery
# discovery by id: GET http://api.us.socrata.com/api/catalog/v1?ids=ydr8-5enu
# discovery by domain: GET http://api.us.socrata.com/api/catalog/v1?domains=data.cityofchicago.org&search_context=data.cityofchicago.org

DISCOVERY_API_URL = 'http://api.us.socrata.com/api/catalog/v1'
CHICAGO_RESOURCE_URL = 'data.cityofchicago.org'

# socrata authorization key
# SOCRATA_API_TOKEN_FILE    = '/home/alxfed/credo/socrata_api_token.txt'
# token_file = open(SOCRATA_API_TOKEN_FILE, 'r')
# socrata_api_token = token_file.read()
# token_file.close()
# socrata_api_token = input('Enter the API token: ')

# header for authenticated requests
# socrata_authorization_header = {'Content-Type': 'application/json', 'X-App-Token': socrata_api_token}

# all Chicago datasets
def all_chicago_datasets():
    session = Session()
    # both, the domain and the context should be the same URI here
    params = {'domains': CHICAGO_RESOURCE_URL, 'search_context': CHICAGO_RESOURCE_URL}
    request = Request(method='GET', url=DISCOVERY_API_URL, params=params)
    prepped = request.prepare()
    response = session.send(prepped)
    return response.json()['results']

