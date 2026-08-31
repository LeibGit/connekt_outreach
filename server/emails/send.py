import os
from dotenv import load_dotenv
from pathlib import Path
from mailgun.client import Client


load_dotenv()

key: str = os.environ.get("MAILGUN_API_KEY")
domain: str = os.environ.get("DOMAIN")
client: Client = Client(auth=("api", key))

def outreach_message_one(name: str, company_name: str, email: str) -> dict:
    data = {
        "from": "support@tryconnekt.com",
        "to": f"{email}",
        "subject": f"Sourcing at {company_name}",
        "html": f"""
        <html>
            <body>
                <p style="margin-bottom: 20px;">
                    Hey {name}, I hope you are well!<br>
                </p>
                <p style="margin-bottom: 20px;">
                    I saw {company_name} on Linkedin and figured you would be my best point of contact.
                    Quick context: I built <a href="https://tryconnekt.com">Connekt</a> for HR teams of 1-2 people who 
                    are doing their own sourcing and screening without a dedicated 
                    recruiting org backing them up, or those getting killed by recruiter/onboarding fees.<br>
                    It offers intelligent candidate search/filtering from a pool of 1.5+ Billion potential
                    candidates from 40 different platforms and outreach sequencing so you're not doing it all 
                    manually in LinkedIn Recruiter + spreadsheets. Curious how you're currently handling sourcing 
                    at {company_name} worth a quick <a href="https://calendly.com/leibnroth/15-minute-meeting">15 min</a> to show you what we've built?
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



def outreach_message_two(name: str, company_name: str, email: str) -> dict:
    data = {
        "from": "support@tryconnekt.com",
        "to": f"{email}",
        "subject": f"Re: Sourcing at {company_name}",
        "html": f"""
        <html>
            <body>
                <p style="margin-bottom: 20px;">
                    Hey {name}, following up on my note from a couple days ago.<br>
                </p>
                <p style="margin-bottom: 20px;">
                    Most solo HR/recruiting folks we talk to are spending 10-15 hours a week 
                    stitching together LinkedIn Recruiter, spreadsheets, and cold outreach by hand — 
                    or handing it off to a recruiter and eating a 20%+ placement fee.<br>
                    <a href="https://tryconnekt.com">Connekt</a> replaces that with one search: 
                    tell it who you're looking for, and it pulls matches from 1.5+ Billion profiles 
                    across 40 platforms and starts a personalized outreach sequence automatically.
                </p>
                <p style="margin-bottom: 20px;">
                    If sourcing at {company_name} is eating more time than it should, I'd love to 
                    show you in <a href="https://calendly.com/leibnroth/15-minute-meeting">15 minutes</a>.
                </p>
                <p style="margin-bottom: 8px;">Let me know either way!</p>
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


def outreach_message_three(name: str, company_name: str, email: str) -> dict:
    data = {
        "from": "support@tryconnekt.com",
        "to": f"{email}",
        "subject": f"Last note — {company_name} sourcing",
        "html": f"""
        <html>
            <body>
                <p style="margin-bottom: 20px;">
                    Hey {name}, I'll keep this short — last note from me on this.<br>
                </p>
                <p style="margin-bottom: 20px;">
                    If sourcing and outreach at {company_name} isn't a pain point right now, no worries 
                    at all, and I won't keep filling up your inbox.<br>
                    But if you're still doing candidate search manually or paying recruiter fees to 
                    get it off your plate, <a href="https://tryconnekt.com">Connekt</a> might be worth 
                    a look — happy to show you in <a href="https://calendly.com/leibnroth/15-minute-meeting">15 minutes</a>, 
                    no pressure either way.
                </p>
                <p style="margin-bottom: 8px;">Wishing you and the team well!</p>
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