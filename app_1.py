from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

chat_response = chat.invoke("Hola, ¿cómo te llamas?")
print(chat_response.content)