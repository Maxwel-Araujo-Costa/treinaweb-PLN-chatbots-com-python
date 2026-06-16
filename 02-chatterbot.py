from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    "BotTw"
)

sentenca = [
    "opa",
    "como vai?",
    "Qual seu nome?",
    "Sou o BotTw e vou te ajudar na carreira de tecnologia",
    "Qual formação você indica em python?",
    "Recomendo a Formação Flask",
    "Qual tecnologia está em alta no momento?",
    "Flutter"
]

treino = ListTrainer(chatbot)
treino.train(sentenca)

while True:
    mensagem = input("Envie uma mensagem \n")

    if mensagem.lower() == "sair":
        break

    resposta = chatbot.get_response(mensagem)

    if float(resposta.confidence) > 0.4:
        print("BotTw:", resposta)
    else:
        print("BotTw: Ainda não sei responder essa pergunta")