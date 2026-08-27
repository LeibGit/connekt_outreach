from fastapi import APIRouter, HTTPException
from pydantic import BaseModel 
from ..helpers.agent import get_intent

router = APIRouter(
    prefix="/search", 
    tags=["search"]
)

class UserQuery(BaseModel):
    query: str

@router.post("/candidates")
async def candidate_search(
    query: UserQuery
):
    try:
        response = await get_intent(query=query)
        print(response["success"])

        if (response["success"]):
            data = response.json()
            print(data)
            return {
                "success": True, 
                "data": data["data"]
            }
        
    except Exception as e:
        HTTPException(status_code=400, detail=e)