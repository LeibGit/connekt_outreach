from ..schema.search import SearchIntent

def build_search(intent: SearchIntent) -> dict:
    must = []
    if intent.job_company_industry:
        must.append({"term": {"job_company_industry": intent.job_company_industry.lower()}})
    if intent.job_company_name:
        must.append({"term": {"job_company_name": intent.job_company_name.lower()}})
    if intent.job_company_size:
        must.append({"term": {"job_company_size": intent.job_company_size.lower()}})
    if intent.location_country:
        must.append({"term": {"location_country": intent.location_country.lower()}})
    if intent.job_title:
        must.append({"match": {"job_title.text": intent.job_title}})
    if intent.job_title_role:
        normalized = intent.job_title_role.lower().replace(" ", "_")
        must.append({"term": {"job_title_role": normalized}})

    return {"query": {"bool": {"must": must}}}