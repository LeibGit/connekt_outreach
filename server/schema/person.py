from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class PersonSearch(BaseModel):
    """Flat representation of the People Data Labs person schema.

    Every field is optional so this can double as a query/filter template:
    populate only the fields relevant to a given search, leave the rest None.
    """

    # --- identity -----------------------------------------------------
    id: Optional[str] = None
    full_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_initial: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    last_initial: Optional[str] = None
    name_aliases: Optional[List[str]] = None
    sex: Optional[str] = None
    birth_year: Optional[str] = None
    birth_date: Optional[str] = None

    # --- social / web profiles -----------------------------------------
    linkedin_url: Optional[str] = None
    linkedin_url_percent_encoded: Optional[str] = None
    linkedin_username: Optional[str] = None
    linkedin_id: Optional[str] = None
    linkedin_connections: Optional[int] = None
    facebook_url: Optional[str] = None
    facebook_username: Optional[str] = None
    facebook_id: Optional[str] = None
    facebook_friends: Optional[int] = None
    twitter_url: Optional[str] = None
    twitter_username: Optional[str] = None
    github_url: Optional[str] = None
    github_username: Optional[str] = None

    # --- contact ---------------------------------------------------------
    work_email: Optional[str] = None
    personal_emails: Optional[List[str]] = None
    recommended_personal_email: Optional[str] = None
    mobile_phone: Optional[str] = None
    phone_numbers: Optional[List[str]] = None

    # --- current job -----------------------------------------------------
    industry: Optional[str] = None
    job_title: Optional[str] = None
    job_title_class: Optional[str] = None
    job_title_role: Optional[str] = None
    job_title_sub_role: Optional[str] = None
    job_title_levels: Optional[List[str]] = None
    job_company_id: Optional[str] = None
    job_company_name: Optional[str] = None
    job_company_website: Optional[str] = None
    job_company_size: Optional[str] = None
    job_company_industry: Optional[str] = None
    job_company_industry_v2: Optional[str] = None
    job_company_founded: Optional[str] = None
    job_company_linkedin_url: Optional[str] = None
    job_company_linkedin_id: Optional[str] = None
    job_company_facebook_url: Optional[str] = None
    job_company_twitter_url: Optional[str] = None
    job_company_type: Optional[str] = None
    job_company_ticker: Optional[str] = None
    job_company_location_name: Optional[str] = None
    job_company_location_locality: Optional[str] = None
    job_company_location_region: Optional[str] = None
    job_company_location_metro: Optional[str] = None
    job_company_location_country: Optional[str] = None
    job_company_location_continent: Optional[str] = None
    job_company_location_street_address: Optional[str] = None
    job_company_location_address_line_2: Optional[str] = None
    job_company_location_postal_code: Optional[str] = None
    job_company_location_geo: Optional[str] = None
    job_company_employee_count: Optional[int] = None
    job_company_inferred_revenue: Optional[str] = None
    job_company_12mo_employee_growth_rate: Optional[float] = None
    job_company_total_funding_raised: Optional[float] = None
    job_last_verified: Optional[str] = None
    job_last_changed: Optional[str] = None
    job_start_date: Optional[str] = None
    job_summary: Optional[str] = None
    job_onet_code: Optional[str] = None
    job_onet_major_group: Optional[str] = None
    job_onet_minor_group: Optional[str] = None
    job_onet_broad_occupation: Optional[str] = None
    job_onet_specific_occupation: Optional[str] = None
    job_onet_specific_occupation_detail: Optional[str] = None

    # --- location -------------------------------------------------------
    location_name: Optional[str] = None
    location_locality: Optional[str] = None
    location_region: Optional[str] = None
    location_metro: Optional[str] = None
    location_country: Optional[str] = None
    location_continent: Optional[str] = None
    location_full_address: Optional[str] = None
    location_street_address: Optional[str] = None
    location_address_line_2: Optional[str] = None
    location_postal_code: Optional[str] = None
    location_geo: Optional[str] = None
    location_last_updated: Optional[str] = None
    location_names: Optional[List[str]] = None
    possible_location_names: Optional[List[str]] = None
    regions: Optional[List[str]] = None
    countries: Optional[List[str]] = None

    # --- profile signals --------------------------------------------------
    inferred_salary: Optional[str] = None
    inferred_years_experience: Optional[int] = None
    summary: Optional[str] = None
    headline: Optional[str] = None
    interests: Optional[List[str]] = None
    skills: Optional[List[str]] = None
    num_sources: Optional[int] = None
    profile_score: Optional[str] = None
    activity_score: Optional[str] = None
    num_records: Optional[int] = None
    first_seen: Optional[str] = None
    dataset_version: Optional[str] = None

    # --- structured / nested history (kept generic — see docstring) -----
    phones: Optional[List[Dict[str, Any]]] = None
    possible_phones: Optional[List[Dict[str, Any]]] = None
    emails: Optional[List[Dict[str, Any]]] = None
    possible_emails: Optional[List[Dict[str, Any]]] = None
    street_addresses: Optional[List[Dict[str, Any]]] = None
    possible_street_addresses: Optional[List[Dict[str, Any]]] = None
    experience: Optional[List[Dict[str, Any]]] = None
    job_history: Optional[List[Dict[str, Any]]] = None
    education: Optional[List[Dict[str, Any]]] = None
    profiles: Optional[List[Dict[str, Any]]] = None
    possible_profiles: Optional[List[Dict[str, Any]]] = None
    certifications: Optional[List[Dict[str, Any]]] = None
    languages: Optional[List[Dict[str, Any]]] = None
    profile_score_factors: Optional[Dict[str, Any]] = None
    activity_score_factors: Optional[Dict[str, Any]] = None