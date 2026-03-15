from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mail_service import send_email

app = FastAPI()

# allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class MailRequest(BaseModel):
    name: str
    course: str
    message: str


@app.get("/")
def home():
    return {"status": "mail backend running"}


@app.post("/send-mail")
async def send_mail(data: MailRequest):

    email_body = f"""
New user interaction from website

Name: {data.name}
Course: {data.course}
Message: {data.message}
"""

    send_email(email_body)

    return {"status": "mail sent successfully"}