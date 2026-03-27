import streamlit as st
import os
from supabase import create_client
from dotenv import load_dotenv

# 1. On charge les clés secrètes du fichier .env
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# 2. On se connecte à Supabase
supabase = create_client(url, key)

# 3. On crée l'interface visuelle
st.set_page_config(page_title="FOODROP", page_icon="🍎")
st.title("🍎 Bienvenue sur FOODROP")
st.write("Connexion à Supabase réussie !")

# 4. On affiche les catégories pour tester la base de données
st.subheader("Nos catégories de produits :")
try:
    response = supabase.table("T_Catégories").select("*").execute()
    for cat in response.data:
        st.write(f"- {cat['libelle']}")
except Exception as e:
    st.error(f"Erreur de connexion : {e}")
