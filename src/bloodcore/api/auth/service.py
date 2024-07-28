from .client import supabase
from .utils import normalize_email
from .exceptions import EmailAlreadyExistsError, InvalidCredentialsError
from .constants import EMAIL_ALREADY_EXISTS, INVALID_CREDENTIALS
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def create_user(email: str, password: str) -> dict:
    email = normalize_email(email)
    try:
        sign_up =  supabase.auth.sign_up(credentials={"email": email, "password": password})
        logger.info(f"User created with email: {email}")
        return sign_up
    except Exception as e:
        if "User already registered" in str(e):
            logger.warning(f"Attempt to create an already registered user with email: {email}")
            raise EmailAlreadyExistsError(EMAIL_ALREADY_EXISTS)
        logger.error(f"Failed to create user: {str(e)}")
        raise e

async def login_user(email: str, password: str) -> dict:
    email = normalize_email(email)
    try:
        login = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        logger.info(f"User logged in with email: {email}")
        return login
    except Exception as e:
        if "Invalid login credentials" in str(e):
            logger.warning(f"Invalid login attempt for email: {email}")
            raise InvalidCredentialsError(INVALID_CREDENTIALS)
        logger.error(f"Failed to log in user: {str(e)}")
        raise e

async def get_user() -> dict:
    try:
        # Refresh the session to get a new session token
        res = supabase.auth.refresh_session()
      
        # Retrieve the logged-in user using the current session
        user = supabase.auth.get_user()
        logger.info(f"Retrieved user information: {user}")
        return user
    except Exception as e:
        logger.error(f"Failed to retrieve user information: {str(e)}")
        raise e
async def logout_user() -> dict:
    try:
        logout = supabase.auth.sign_out()
        logger.info("User logged out successfully")
        return logout
    except Exception as e:
        logger.error(f"Failed to log out user: {str(e)}")
        raise e
    


