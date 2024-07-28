from .config import url, key
from supabase import create_client, Client
from supabase.client import ClientOptions

supabase_url: str = url
supabase_key: str = key
auth_header = {'Authorization': f'Bearer {key}'}

client_options = ClientOptions(
    headers=auth_header,
    # Set other optional fields as needed
    auto_refresh_token=True,
    persist_session=True,
)

supabase: Client = create_client(supabase_url, supabase_key, options=client_options)
