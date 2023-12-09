from openai import OpenAI
from dotenv import load_dotenv
import os
from tools import carrega
from tools import salva

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"

contexto = carrega("dados/contexto.txt")

def responder(mensaegm):
    prompt_sistema = f"""
        Você é um chatbot de um e-commerce de produtos de skate. Não responda 
        nada relacionado a outros temas.
        Utilize o contexto para responder ao usuário.

        # Contexto
        {contexto}
    """


    lista_mensagens = [
        {
            "role" : "system",
            "content" : prompt_sistema
        },
        {
            "role" : "user",
            "content" : mensaegm
        }
    ]

    resposta = cliente.chat.completions.create(
        model=modelo,
        messages=lista_mensagens
    )
    
    texto_resposta = resposta.choices[0].message.content
    return texto_resposta

print(responder("Quais os produtos disponíveis?"))