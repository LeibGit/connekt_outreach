import os
from dotenv import load_dotenv
from pathlib import Path
from mailgun.client import Client


load_dotenv()

key: str = os.environ.get("MAILGUN_API_KEY")
domain: str = os.environ.get("DOMAIN")
client: Client = Client(auth=("api", key))

def outreach_message_one(name: str, company_name: str) -> dict:
    data = {
        "from": "support@tryconnekt.com",
        "to": "leibnroth@gmail.com",
        "subject": "",
        "html": f"""
        <html>
            <body>
                <p style="margin-bottom: 20px;">
                    Hey Jane, I hope you are well!<br>
                </p>
                <p style="margin-bottom: 20px;">
                    I saw Acme Corp on Linkedin and figured you would be my best point of contact.
                    Quick context: I built <a href="https://tryconnekt.com">Connekt</a> for HR teams of 1-2 people who 
                    are doing their own sourcing and screening without a dedicated 
                    recruiting org backing them up, or those getting killed by recruiter/onboarding fees.<br>
                    It offers intelligent candidate search/filtering from a pool of 1.5+ Billion potential
                    candidates from 40 different platforms and outreach sequencing so you're not doing it all 
                    manually in LinkedIn Recruiter + spreadsheets. Curious how you're currently handling sourcing 
                    at Acme Corp worth a quick <a href="https://calendly.com/leibnroth/15-minute-meeting">15 min</a> to show you what we've built?
                </p>
                <p style="margin-bottom: 8px;">I look forward to hearing from you!</p>
                <p> 
                    Best,<br>
                    Leib Roth,<br>
                    Founder <a href="https://tryconnekt.com">@Connekt</a><br>
                </p>
            </body>
        </html>
        """,
        "o:tag": "Python test",
    }
    req = client.messages.create(data=data, domain=domain)
    return req.json()



def outreach_message_two(name: str, company_name: str) -> dict:
    data = {
        "from": "support@tryconnekt.com",
        "to": "leibnroth@gmail.com",
        "subject": "",
        "html": f"""
        <html>
            <body>
                <p style="margin-bottom: 20px;">
                    Hey Jane, I hope you are well!<br>
                </p>
                <p style="margin-bottom: 20px;">
                    I saw Acme Corp on Linkedin and figured you would be my best point of contact.
                    Quick context: I built <a href="https://tryconnekt.com">Connekt</a> for HR teams of 1-2 people who 
                    are doing their own sourcing and screening without a dedicated 
                    recruiting org backing them up, or those getting killed by recruiter/onboarding fees.<br>
                    It offers intelligent candidate search/filtering from a pool of 1.5+ Billion potential
                    candidates from 40 different platforms and outreach sequencing so you're not doing it all 
                    manually in LinkedIn Recruiter + spreadsheets. Curious how you're currently handling sourcing 
                    at Acme Corp worth a quick <a href="https://calendly.com/leibnroth/15-minute-meeting">15 min</a> to show you what we've built?
                </p>
                <p style="margin-bottom: 8px;">I look forward to hearing from you!</p>
                <p> 
                    Best,<br>
                    Leib Roth,<br>
                    Founder <a href="https://tryconnekt.com">@Connekt</a><br>
                </p>
            </body>
        </html>
        """,
        "o:tag": "Python test",
    }
    req = client.messages.create(data=data, domain=domain)
    return req.json()




def outreach_message_three(name: str, company_name: str) -> dict:
    data = {
        "from": "support@tryconnekt.com",
        "to": "leibnroth@gmail.com",
        "subject": "",
        "html": f"""
        <html>
            <body>
                <p style="margin-bottom: 20px;">
                    Hey Jane, I hope you are well!<br>
                </p>
                <p style="margin-bottom: 20px;">
                    I saw Acme Corp on Linkedin and figured you would be my best point of contact.
                    Quick context: I built <a href="https://tryconnekt.com">Connekt</a> for HR teams of 1-2 people who 
                    are doing their own sourcing and screening without a dedicated 
                    recruiting org backing them up, or those getting killed by recruiter/onboarding fees.<br>
                    It offers intelligent candidate search/filtering from a pool of 1.5+ Billion potential
                    candidates from 40 different platforms and outreach sequencing so you're not doing it all 
                    manually in LinkedIn Recruiter + spreadsheets. Curious how you're currently handling sourcing 
                    at Acme Corp worth a quick <a href="https://calendly.com/leibnroth/15-minute-meeting">15 min</a> to show you what we've built?
                </p>
                <p style="margin-bottom: 8px;">I look forward to hearing from you!</p>
                <p> 
                    Best,<br>
                    Leib Roth,<br>
                    Founder <a href="https://tryconnekt.com">@Connekt</a><br>
                </p>
            </body>
        </html>
        """,
        "o:tag": "Python test",
    }
    req = client.messages.create(data=data, domain=domain)
    return req.json()