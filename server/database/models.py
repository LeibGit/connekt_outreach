from sqlmodel import Field, Session, SQLModel, Column, JSON
from typing import List
from datetime import datetime, timezone
from sqlalchemy import DateTime

class OutreachProspect(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str | None
    work_email: str | None
    personal_emails: List[str] | None = Field(default=None, sa_column=Column(JSON))
    recommended_personal_email: str | None
    mobile_phone: str | None
    job_company_name: str | None
    
    linkedin_url: str | None
    facebook_url: str | None
    outreach_one: bool = False
    one_created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), nullable=False)
    )
    outreach_two: bool = False
    two_created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), nullable=False)
    )
    outreach_three: bool = False
    outreach_three_time: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), nullable=False)
    )
    status: str = "active"

class AllProspect(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    outreached_emails: List[str] | None = Field(default=None, sa_column=Column(JSON))