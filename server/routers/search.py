from fastapi import APIRouter, HTTPException
from pydantic import BaseModel 
import uuid
from ..helpers.agent import build_intent
from ..helpers.elastic_search import build_search
from ..helpers.pdl import pdl_search
from ..database.database import SessionDep
from ..database.models import OutreachProspect

router = APIRouter(
    prefix="/search", 
    tags=["search"]
)

class UserQuery(BaseModel):
    query: str
    qty: int

@router.post("/candidates")
async def candidate_search(
    db: SessionDep,
    search: UserQuery
):
    try:
        intent = build_intent(query=search.query)
        if not (intent["success"]):
            raise HTTPException(status_code=400, detail="build intent func failed")
        
        es_query = build_search(intent["data"]) 
        pdl_response = pdl_search(es_query=es_query, qty=search.qty)

        if not pdl_response["success"]:
            raise HTTPException(status_code=400, detail="pdl search func failed")

        print(pdl_response["data"])

        for person in pdl_response["data"]:
            unique_id = uuid.uuid4()
            for person in pdl_response["data"]:
                prospect = OutreachProspect(
                    name=person["first_name"], 
                    job_company_name=person["job_company_name"],
                    facebook_url=person["facebook_url"], 
                    mobile_phone=person["mobile_phone"],
                    personal_emails=person["personal_emails"],
                    linkedin_url=person["linkedin_url"],
                    recommended_personal_email=person["recommended_personal_email"],
                    work_email=person["work_email"], 
                )
                db.add(prospect)
                print(f"prospect added to database: {prospect}")
                db.commit()

        return {
            "success": True, 
            "data": pdl_response["data"]
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))