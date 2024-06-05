from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage

load_dotenv()
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)
chat_history = ChatMessageHistory()
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="Eres un experto en desarrollo de software. Dame tus respuestas como si lo leyera un niño de 10 años."),
    MessagesPlaceholder(variable_name="messages"),
])
chain = prompt | chat

def main():
    while True:
        question = input("Dime tu pregunta: ")
        chat_history.add_user_message(question)
        chat_response = chain.invoke({"messages": chat_history.messages})
        print("Respuesta: ", chat_response.content)
        chat_history.add_ai_message(chat_response.content)
        
main()