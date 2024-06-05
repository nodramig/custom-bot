from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

def main():
    while True:
        question = input("Dime tu pregunta: ")
        chat_response = chat.invoke(question)
        print("Respuesta: ", chat_response.content)

main()