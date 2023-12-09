
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-3.5-turbo"

prompt_sistema = """
    Assuma que você está classificando sentimentos em reviews.
    Você deve classificar os sentimentos entre positivo, negativo e
    neutro.

    Além disso, de justificar, como chegou a este sentimento.

    # Saída esperada
    Sentimento: [colocar sentimento aqui]
    Parecer: [colocar parecer aqui]

    # Exemplo
    Comentário avaliado: Comprei uma base nova da Lush, e a tampa era péssima.

    Sentimento: negativo
    Parecer: O usuário reclamou da embalagem do produto, sugerindo que era frágil
"""

resposta = cliente.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "system",
            "content" : prompt_sistema
        },
        {
            "role" : "user",
            "content" : "Faça a análise deste comentário: Fiz uma péssima compra"
        }
    ]
)

print("\nResposta: ", resposta.choices[0].message.content)

#https://github.com/ALMSantana/Workshop_PADS