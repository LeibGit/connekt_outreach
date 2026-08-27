from __future__ import annotations
from typing import Optional
from pydantic import BaseModel


class SearchIntent(BaseModel):
    # find key pdl things to target here
    job_company_industry: Optional[str] = None
    job_company_name: Optional[str] = None
    job_company_size: Optional[str] = None
    location_country: Optional[str] = "united states"
    job_title: Optional[str] = None
    job_title_role: Optional[str] = None 