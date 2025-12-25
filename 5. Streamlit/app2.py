import os
import getpass
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("TOKEN_GROQ", "").strip()
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

llm =  ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

chat_history = []

while True:
    user_chat = input("User : ")
    chat_history.append(
        HumanMessage(user_chat)
    )
    response = llm.invoke(user_chat)
    chat_history.append(response)
    print(response)