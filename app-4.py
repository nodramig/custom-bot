from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ChatMessageHistory

load_dotenv()
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)
chat_history = ChatMessageHistory()

def main():
    while True:
        question = input("Dime tu pregunta: ")
        chat_history.add_user_message(question)
        chat_response = chat.invoke(chat_history.messages)
        print("Respuesta: ", chat_response.content)
        chat_history.add_ai_message(chat_response.content)

main()