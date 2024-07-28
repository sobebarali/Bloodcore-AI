from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from .constants import SMTP_CONFIG
from typing import Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

conf = ConnectionConfig(
    MAIL_USERNAME=SMTP_CONFIG["username"],
    MAIL_PASSWORD=SMTP_CONFIG["password"],
    MAIL_FROM=SMTP_CONFIG["from_email"],
    MAIL_PORT=SMTP_CONFIG["port"],
    MAIL_SERVER=SMTP_CONFIG["server"],
    MAIL_SSL_TLS=False,  # Disable implicit SSL/TLS
    MAIL_STARTTLS=True,  # Enable STARTTLS
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)

async def send_email_async(email: str, subject: str, body: str, attachment: Optional[bytes] = None):
    try:
        message = MessageSchema(
            subject=subject,
            recipients=[email],
            body=body,
            subtype="html",
        )

        if attachment:
            message.attachments = [(attachment, "application/pdf")]

        fm = FastMail(conf)
        await fm.send_message(message, template_name=None)
        logger.info("Email sent successfully")
    except Exception as e:
        logger.error(f"An error occurred while sending the email: {e}")
        raise
