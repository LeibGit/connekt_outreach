import os
from dotenv import load_dotenv
from zerobouncesdk import ZeroBounce, ZBApiUrl

load_dotenv()

zero_bounce = ZeroBounce(
    api_key=os.environ.get("ZEROBOUNCE_KEY"),
    base_url=ZBApiUrl.API_USA_URL
)

credit_response = zero_bounce.get_credits()
print(f"ZeroBounce credits: {credit_response}")

VALID_STATUSES = {"valid", "catch-all"}
ACCEPTABLE_GUESS_CONFIDENCE = {"high", "medium"}


def _domain_from_email(email: str) -> str | None:
    if email and "@" in email:
        return email.split("@", 1)[1]
    return None


def validate_email(work_email: str, first_name: str = None, last_name: str = None, domain: str = None):
    """Validate a person's work email for business outreach.

    Returns
    -------
    dict
        {"success": bool, "verified_work_email": str | None}
    """
    domain = domain or _domain_from_email(work_email)

    # first check if the given work email is valid
    if work_email:
        try:
            response = zero_bounce.validate(work_email)
            status = getattr(response, "status", None)
            print(f"ZeroBounce validated {work_email}: {status}")

            if status in VALID_STATUSES:
                return {"success": True, "verified_work_email": work_email}
        except Exception as e:
            print(f"ZeroBounce validation error: {e}")

    # work email missing or invalid — try to find the correct one
    if not domain or not first_name:
        return {"success": False, "verified_work_email": None}

    try:
        guess = zero_bounce.find_email_format(
            first_name=first_name,
            last_name=last_name,
            domain=domain,
        )

        confidence = getattr(guess, "email_confidence", None)
        confidence_value = getattr(confidence, "value", confidence)
        guessed_email = getattr(guess, "email", None)

        print(f"ZeroBounce guessed format for {domain}: {guessed_email} ({confidence_value})")

        if not guessed_email or confidence_value not in ACCEPTABLE_GUESS_CONFIDENCE:
            return {"success": False, "verified_work_email": None}

        confirm = zero_bounce.validate(guessed_email)
        confirm_status = getattr(confirm, "status", None)
        print(f"ZeroBounce validated guess {guessed_email}: {confirm_status}")

        if confirm_status in VALID_STATUSES:
            return {"success": True, "verified_work_email": guessed_email}

        return {"success": False, "verified_work_email": None}

    except Exception as e:
        print(f"ZeroBounce find_email_format error: {e}")
        return {"success": False, "verified_work_email": None}