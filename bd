from supabase import create_client

url = "https://YOUR_PROJECT.supabase.co"
key = "YOUR_SECRET_KEY"

supabase = create_client(url, key)

supabase.table("anpr").insert({
    "plate": latest_plate
}).execute()
