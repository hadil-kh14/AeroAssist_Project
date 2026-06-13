import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")

st.title("AeroAssist ✈️")
st.subheader("Assistant IA de Maintenance avec Grok")


llm = ChatOpenAI(
    openai_api_key=groq_key,
    openai_api_base="https://api.groq.com/openai/v1",  
    model_name="llama-3.3-70b-versatile"              
)


query = st.text_input("Exemple : Comment réparer une fuite de compresseur ?")

if query:
    st.write("🔄 Connexion à Llama-3 en cours...")
    
    try:
        reponse = llm.invoke(query)
        st.success("Réponse de l'assistant :")
        st.write(reponse.content)
    except Exception as e:
        st.error(f"Erreur de connexion : {e}")
