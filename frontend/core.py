from supabase import create_client

url = "https://postgres.zuovjoaizcggcllzpjsz.supabase.co"
key = "sb_secret_z1c3SwaLG-RKSaIA_iwJ-A_qOQH_SlJ"

supabase = create_client(url, key)

supabase.table("anpr").insert({
    "plate": latest_plate
}).execute()
