from contextlib import asynccontextmanager
from datetime import datetime, timedelta

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_crons import Crons, get_cron_router
from sqlmodel import select, Session

from .routers import search
from .database.database import create_db_and_tables, SessionDep, engine
from .database.models import OutreachProspect, AllProspect
from .emails.send import outreach_message_one, outreach_message_two, outreach_message_three


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("creating database and models")
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

crons = Crons(app)

app.include_router(search.router)
app.include_router(get_cron_router(), prefix="/crons")


origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://connekt-outreach-two.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.api_route("/", methods=["GET", "HEAD"])
def read_root():
    return {"Connekt": "Active"}


@crons.cron("*/5 * * * *", name="email_sequence")
def email_outreach():
    print("Running Cron for email sequence")
    with Session(engine) as db:
        print("session started...")
        statement = select(OutreachProspect).where(OutreachProspect.status == "active")
        prospects = db.exec(statement).all()
        print(f"found {len(prospects)} active prospects")

        prospect_list_statement = select(AllProspect)
        prospect_list = db.exec(prospect_list_statement).all()

        two_days_ago = datetime.utcnow() - timedelta(days=2)

        for prospect in prospects:
            if prospect.status == "active" and prospect.work_email:
                if not prospect.outreach_one:
                    new_message = outreach_message_one(
                        company_name=prospect.job_company_name,
                        name=prospect.name,
                        email=prospect.work_email
                    )
                    prospect.outreach_one = True
                    print("message one sent")
                    prospect.one_created_at = datetime.utcnow()
                elif not prospect.outreach_two:
                    if prospect.one_created_at < two_days_ago:
                        new_message = outreach_message_two(
                            company_name=prospect.job_company_name,
                            name=prospect.name,
                            email=prospect.work_email
                        )
                        prospect.outreach_two = True
                        print("message two sent")
                        prospect.two_created_at = datetime.utcnow()
                    else:
                        continue
                elif prospect.outreach_one and prospect.outreach_two and not prospect.outreach_three:
                    if prospect.two_created_at < two_days_ago:
                        new_message = outreach_message_three(
                            company_name=prospect.job_company_name,
                            name=prospect.name,
                            email=prospect.work_email
                        )
                        print("message three sent")
                        prospect.outreach_three = True
                        prospect.outreach_three_time = datetime.utcnow()
                        prospect_list.append(prospect.work_email)
                        prospect.status = "completed"
                    else:
                        continue
        db.commit()