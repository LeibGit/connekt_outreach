import json
from peopledatalabs import PDLPY
import os
from dotenv import load_dotenv

load_dotenv()


def pdl_search(es_query, qty):
  # Create a client, specifying your API key
  try:
    print(os.environ.get("PDL_KEY"))
    print("PDL SEARCH HIT")
    CLIENT = PDLPY(
        api_key=os.environ.get("PDL_KEY"),
    )
        
    # Create an Elasticsearch query
    ES_QUERY = es_query

    # Create a parameters JSON object
    PARAMS = {
      'query': ES_QUERY,
      'size': qty,
      'pretty': True
    }

    # Pass the parameters object to the Person Search API
    response = CLIENT.person.search(**PARAMS).json()

    # Check for successful response
    if response["status"] == 200:
      data = response['data']
      
      return {
        "success": True,
        "data": data
      }
    
    else:
      print("NOTE: The carrier pigeons lost motivation in flight. See error and try again.")
      print("Error:", response)
  except Exception as e:
    print(f"PDL ERROR: {e}")