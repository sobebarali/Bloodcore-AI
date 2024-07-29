import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# The SMTP_CONFIG dictionary contains the configuration for the SMTP server.
# The username and password are the credentials for the SMTP server.
# The from_email is the email address that will be used to send the email.
# The port and server are the port and server address of the SMTP server.
# The values are set to the credentials provided by Mailtrap.

username: str = os.getenv("SMTP_USERNAME")
password: str = os.getenv("SMTP_PASSWORD")
from_email: str = os.getenv("SMTP_FROM_EMAIL")
port: int = int(os.getenv("SMTP_PORT", "587"))  # Default to 587 if not set
server: str = os.getenv("SMTP_SERVER")

SMTP_CONFIG = {
    "username": username,
    "password": password,
    "from_email": from_email,
    "port": port,
    "server": server
}

# Debug: Print the loaded environment variables
print(f"SMTP_USERNAME: {username}")
print(f"SMTP_PASSWORD: {password}")
print(f"SMTP_FROM_EMAIL: {from_email}")
print(f"SMTP_PORT: {port}")
print(f"SMTP_SERVER: {server}")