from __future__ import print_function
import time
import v3client
from v3client.rest import ApiException
from pprint import pprint
import API_KEY

# Configure API key authorization: apiKey
v3client.configuration.api_key['X-TBA-Auth-Key'] = API_KEY.key
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# v3client.configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'
# create an instance of the API class
api_instance = v3client.TBAApi()
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

try:
    api_response = api_instance.get_status(if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TBAApi->get_status: %s\n" % e)
