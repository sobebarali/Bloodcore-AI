import os

# The SMTP_CONFIG dictionary contains the configuration for the SMTP server.
# The username and password are the credentials for the SMTP server.
# The from_email is the email address that will be used to send the email.
# The port and server are the port and server address of the SMTP server.
# The values are set to the credentials provided by Mailtrap.

username: str = os.environ.get("SMTP_USERNAME")
password: str = os.environ.get("SMTP_PASSWORD")
from_email: str = os.environ.get("SMTP_FROM_EMAIL")
port: int = int(os.environ.get("SMTP_PORT"))
server: str = os.environ.get("SMTP_SERVER")

SMTP_CONFIG = {
    "username": username,
    "password": password,
    "from_email": from_email,
    "port": port,
    "server": server
}