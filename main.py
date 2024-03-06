import sys
import time
import telepot
from telepot.loop import MessageLoop
# "ia_chat" é uma função que será importada do arquivo nlp para processamento de linguagem natural.
from nlp import ia_chat 
# Módulo contendo variáveis de ambiente.
import env

def handle(msg):
    """
    Função para lidar com as mensagens recebidas pelo bot.

    Args:
        msg (dict): Mensagem recebida pelo bot.

    Returns:
        None
    """       
    # Extrai informações da mensagem
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    # Processa a mensagem usando o módulo de processamento de linguagem natural
    nlp_response = ia(msg['text'])
    
    # Se o tipo de conteúdo for texto, envia a resposta processada de volta ao usuário
    if content_type == 'text':
        bot.sendMessage(chat_id, nlp_response)

# Obtém o token do arquivo de ambiente
TOKEN = env.TOKEN
bot = telepot.Bot(TOKEN)

# Inicia o loop de mensagens do bot
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Mantém o programa em execução
while 1:
    time.sleep(10)
