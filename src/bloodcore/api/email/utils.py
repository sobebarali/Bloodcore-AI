from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from .constants import SMTP_CONFIG

conf = ConnectionConfig(
    MAIL_USERNAME=SMTP_CONFIG["username"],
    MAIL_PASSWORD=SMTP_CONFIG["password"],
    MAIL_FROM=SMTP_CONFIG["from_email"],
    MAIL_PORT=SMTP_CONFIG["port"],
    MAIL_SERVER=SMTP_CONFIG["server"],
    MAIL_SSL_TLS=True,  # Use SSL/TLS encryption
    MAIL_STARTTLS=False,  # Disable STARTTLS
    USE_CREDENTIALS=True,
)

async def send_email_async(email: str, subject: str, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[email],
        body=body,
        subtype="html",
    )
    fm = FastMail(conf)
    await fm.send_message(message)