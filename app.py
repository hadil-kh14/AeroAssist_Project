import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Charger la clé API depuis le fichier .env
load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")

st.title("AeroAssist ✈️")
st.subheader("Assistant IA de Maintenance avec Grok")

# Connexion à l'API Grok (via l'interface compatible OpenAI)
llm = ChatOpenAI(
    openai_api_key=groq_key,
    openai_api_base="https://api.groq.com/openai/v1",  # Serveur Groq
    model_name="llama-3.3-70b-versatile"              # Modèle gratuit ultra-performant
)

# Simulation du bouton de recherche
query = st.text_input("Exemple : Comment réparer une fuite de compresseur ?")

if query:
    st.write("🔄 Connexion à Llama-3 en cours...")
    # Ici LangChain enverra la question à Grok
    try:
        reponse = llm.invoke(query)
        st.success("Réponse de l'assistant :")
        st.write(reponse.content)
    except Exception as e:
        st.error(f"Erreur de connexion : {e}")