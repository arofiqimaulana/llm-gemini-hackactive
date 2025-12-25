import os
import getpass
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

GROQ_API_KEY = os.getenv("TOKEN_GROQ", "").strip()
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

llm =  ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

st.title("Chatbotku")

# Membuat chat history kosong jika belum ada di session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Tampilkan chat history yang ada sampai sekarang
for chat in st.session_state["chat_history"]:
    role = "User" if type(chat) is HumanMessage else "AI"
    with st.chat_message(role):
        st.markdown(chat.content)

# Minta input dari user
user_chat = st.chat_input("Chat With AI")
if user_chat is None:
    st.stop()

# Tampilkan input user jika sudah ada
with st.chat_message("User"):
    st.markdown(user_chat)

# Masukkan input user ke chat history
if user_chat:
    st.session_state["chat_history"].append(HumanMessage(user_chat))
    response=llm.invoke(st.session_state["chat_history"]) # berfungsi untuk memanggil (mengeksekusi) model LLM dengan input berupa riwayat percakapan (chat history), lalu menghasilkan satu respons dari model berdasarkan konteks tersebut.
    st.session_state["chat_history"].append(response)

    # Tampilkan response LLM
    with st.chat_message("AI"):
        st.markdown(response.content)

