from openai import OpenAI
from dotenv import load_dotenv
import os
from tools import carrega
from tools import salva

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"

def analisador_sentimentos(produto):
    prompt_sistema = f"""
        Você é um analisador de sentimentos de avaliações de produtos.
        Escreva um parágrafo com até 50 palavras resumindo as avaliações e 
        depois atribua qual o sentimento geral para o produto.
        Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

        # Formato de Saída

        Nome do Produto:
        Resumo das Avaliações:
        Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
        Ponto fortes: lista com três bullets
        Pontos fracos: lista com três bullets
    """

    prompt_usuario = carrega(f"dados/avaliacoes-{produto}.txt")

    lista_mensagens = [
        {
            "role" : "system",
            "content" : prompt_sistema
        },
        {
            "role" : "user",
            "content" : prompt_usuario
        }
    ]

    resposta = cliente.chat.completions.create(
        model=modelo,
        messages=lista_mensagens
    )
    
    texto_resposta = resposta.choices[0].message.content
    salva(f"dados/analise-{produto}.txt", texto_resposta)


lista_produtos = ["smartphone", "notebook"]
for nome_produto in lista_produtos:
    analisador_sentimentos(nome_produto)