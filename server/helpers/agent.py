import os
import anthropic
from dotenv import load_dotenv
from ..schema.person import PersonSearch
from ..schema.search import SearchIntent
from ..helpers.elastic_search import build_search

load_dotenv()

outreach_key = os.environ.get("OUTREACH_KEY")

client = anthropic.Anthropic(api_key=outreach_key)

tools = [
    {
        "name": "pdl_search_intent",
        "description": "Given a user query pull the PDL search intent behind the query",
        "input_schema": SearchIntent.model_json_schema()
    }
]

def build_intent(query: str = None):
    try:
        response = client.messages.create(
            model="claude-opus-5",
            max_tokens=1000,
            tools=tools,
            tool_choice={"type": "tool", "name": "pdl_search_intent"},
            messages=[{
                    "role": "user",
                    "content": f"Your job is to take in the query: {query} and match search intent",
            }]
        )

        intent = SearchIntent(**response.content[0].input)
        print(intent)
        
        return {
            "success": True,
            "data": intent
        }
    
    except Exception as e:
        print(f"An error occured: {e}")
        return {
            "success": False,
            "error": e
        }