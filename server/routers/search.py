from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..helpers.agent import build_intent
from ..helpers.elastic_search import build_search
from ..helpers.pdl import pdl_search
from ..helpers.email_validation import validate_email
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
        print(
            f"""
            search: {search.query}
            qty: {search.qty}
            """
        )

        intent = build_intent(query=search.query)
        if not intent["success"]:
            raise HTTPException(status_code=400, detail="build intent func failed")

        es_query = build_search(intent["data"])
        pdl_response = pdl_search(es_query=es_query, qty=search.qty)

        if not pdl_response["success"]:
            raise HTTPException(status_code=400, detail="pdl search func failed")

        print(pdl_response["data"])

        for person in pdl_response["data"]:
            email_check = validate_email(
                work_email=person.get("work_email"),
                first_name=person.get("first_name"), 
                last_name=person.get("last_name"), 
                domain=person.get("domain")
            )

            if email_check["success"]:
                prospect = OutreachProspect(
                    name=person.get("first_name"),
                    job_company_name=person.get("job_company_name"),
                    facebook_url=person.get("facebook_url"),
                    mobile_phone=person.get("mobile_phone"),
                    personal_emails=person.get("personal_emails"),
                    linkedin_url=person.get("linkedin_url"),
                    recommended_personal_email=person.get("recommended_personal_email"),
                    work_email=email_check["verified_work_email"],
                )

                db.add(prospect)
                db.commit()
                print(f"prospect added to database: {prospect}")

            else:
                prospect = OutreachProspect(
                    name=person.get("first_name"),
                    job_company_name=person.get("job_company_name"),
                    facebook_url=person.get("facebook_url"),
                    mobile_phone=person.get("mobile_phone"),
                    personal_emails=person.get("personal_emails"),
                    linkedin_url=person.get("linkedin_url"),
                    recommended_personal_email=person.get("recommended_personal_email"),
                    work_email=None,
                )

                db.add(prospect)
                db.commit()
                print(f"prospect added to database: {prospect}")

        return {
            "success": True,
            "data": pdl_response["data"],
            "message": f"{search.qty} candidates have been sent a message."
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))