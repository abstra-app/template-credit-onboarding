import os
from abstra.forms import *
from abstra.tasks import send_task

display_markdown("""
<img src="https://abstracloud-webflow-assets.s3.amazonaws.com/5599illustration.gif" width="100" height="100" />

# Request a personal loan 🫰
### Simple, fast, no bureaucracy.

Fill out this form to apply for a loan and get a quick response!
""", button_text="Start")

personal_data = Page() \
    .display("Personal Info", size="large") \
    .read("Full name:", placeholder = "Michael Scott", key="name") \
    .read_email("Email:", placeholder = "michael.scott@dundermifflin.com", key="email") \
    .run()

income_data = Page() \
    .display("Income info", size="large") \
    .read_currency("Monthly income:", currency = "USD", placeholder = "10.000,00", key="income") \
    .read("Current employer, if applicable:", placeholder = "Dunder Mifflin", key="employer", required=False) \
    .run()

loan_data = Page() \
    .display("Loan info", size="large") \
    .read_currency("Loan amount:", currency="USD", placeholder = "10.000,00", key="loan_amount") \
    .read("Number of installments:", placeholder = "12", min=2, max=12, key="installments") \
    .run()

if not income_data["employer"]:
    employer = "Not provided"
else:
    employer = income_data["employer"]

payload = {
    "name": personal_data["name"],
    "email": personal_data["email"],
    "income": income_data["income"],
    "employer": employer,
    "loan_amount": loan_data["loan_amount"],
    "installments": loan_data["installments"],
    "review_email": os.environ.get("CREDIT_TEAM_EMAIL")
}

send_task("request_data", payload)

display_markdown("""
# ✨ Request received!
### Your evaluation will take up to 10 minutes. You'll receive an email with the result.
""", end_program=True, button_text=None)