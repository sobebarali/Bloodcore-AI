import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY") 

url: str = os.environ.get("SUPABASE_URL") or "https://dcvktiepcsteonwljsqy.supabase.co"
key: str = os.environ.get("SUPABASE_KEY") or "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRjdmt0aWVwY3N0ZW9ud2xqc3F5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTY3OTkwOTIsImV4cCI6MjAzMjM3NTA5Mn0.uMO5cBMBqn_b5VD_At2hdimdnKCgxo5JwjG2tWyRFLI"

# Debug: Print the loaded environment variables
print(f"SUPABASE_URL: {url}")
print(f"SUPABASE_KEY: {key}")