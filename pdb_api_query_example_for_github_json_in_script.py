### Queries the RCSB PDB for all structures with the word "flavin" in the structure title
### returns a pretty printed json dictionary of the first 10 results 

import requests
import json
import pprint

json_query = {
  "query": {
    "type": "terminal",
    "service": "text",
    "parameters": {
      "attribute": "struct.title",
      "operator": "contains_words",
      "value": "flavin"
    }
  },
  "return_type": "entry"
}

qjson = json.dumps(json_query) ## converts to a JSON formatted str for url

front_of_url = "https://search.rcsb.org/rcsbsearch/v1/query?json="
full_url = front_of_url+qjson

r = requests.get(full_url)

status_code = r.status_code
print('Status Code: '+str(status_code))

content_json = json.loads(r.content) ## dictionary
print(pprint.pprint(content_json))
