### Queries the RCSB PDB for structures with chemical component FAD
### returns a list PDB IDs 

import requests
import json
import pprint

jsonfilename = 'FAD_PDB_api_query.json'
json_query = json.load(open(jsonfilename))
qjson = json.dumps(json_query) ## converts to a JSON formatted str for url

front_of_url = "https://search.rcsb.org/rcsbsearch/v1/query?json="
full_url = front_of_url+qjson

r = requests.get(full_url)

status_code = r.status_code
print('Status Code: '+str(status_code))

content_json = json.loads(r.content) ## dictionary
## print(pprint.pprint(content_json))

result_set_list = content_json['result_set']
list_of_PDB_IDs_returned_by_query = []
for i in result_set_list:
    PDB_ID = i['identifier']
    list_of_PDB_IDs_returned_by_query.append(PDB_ID)
print(list(set(list_of_PDB_IDs_returned_by_query)))
