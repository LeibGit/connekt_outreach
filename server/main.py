from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import search
from .database.database import create_db_and_tables, SessionDep
from fastapi_crons import Crons, get_cron_router
from .database.database import engine
from .database.models import OutreachProspect, AllProspect
from .emails.send import outreach_message_one, outreach_message_two, outreach_message_three
from sqlmodel import select, Session
from datetime import datetime, timezone, timedelta

app = FastAPI()

crons = Crons(app)

app.include_router(search.router)
app.include_router(get_cron_router(), prefix="/crons")


origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://connekt-outreach-two.vercel.app/", 
    "https://connekt-outreach-two.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    print("creating database and models")
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"Connekt": "Active"}  


@crons.cron("*/5 * * * *", name="periodic_cleanup")
def email_outreach():
    print("Running Cron for email sequence")
    with Session(engine) as db:
        print("session started...")
        statement = select(OutreachProspect).where(OutreachProspect.status == "active")
        prospects = db.exec(statement).all()
        print(f"found {len(prospects)} active prospects")

        prospect_list_statement = select(AllProspect)
        prospect_list = db.exec(prospect_list_statement).all()

        two_days_ago = datetime.now(timezone.utc) - timedelta(days=2)

        for prospect in prospects:
            if prospect.status == "active":
                if not prospect.outreach_one:
                    new_message = outreach_message_one(
                        company_name=prospect.job_company_name,
                        name=prospect.name,
                        email=prospect.recommended_personal_email
                    )
                    prospect.outreach_one = True
                    print("message one sent")
                    prospect.one_created_at = datetime.now(timezone.utc)
                elif not prospect.outreach_two:
                    if prospect.one_created_at < two_days_ago:
                        new_message = outreach_message_two(
                            company_name=prospect.job_company_name,
                            name=prospect.name, 
                            email=prospect.recommended_personal_email
                        )
                        prospect.outreach_two = True
                        print("message two sent")
                        prospect.two_created_at = datetime.now(timezone.utc)

                    else:
                        continue
                elif prospect.outreach_one and prospect.outreach_two and not prospect.outreach_three:
                    if prospect.two_created_at < two_days_ago:
                        new_message = outreach_message_three(
                            company_name=prospect.job_company_name,
                            name=prospect.name, 
                            email=prospect.recommended_personal_email
                        )
                        print("message three sent")
                        prospect.outreach_three = True
                        prospect.outreach_three_time = datetime.now(timezone.utc)
                        prospect_list.outreached_emails.append(prospect.recommended_personal_email)
                        prospect.status = "completed"
                    else:
                        continue
        db.commit() 