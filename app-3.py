from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)
chat_history = []

def main():
    while True:
        question = input("Dime tu pregunta: ")
        chat_history.append(HumanMessage(content=question))
        chat_response = chat.invoke(chat_history)
        print("Respuesta: ", chat_response.content)
        chat_history.append(AIMessage(chat_response.content))

main()