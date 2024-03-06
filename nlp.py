import google.generativeai as genai
# Módulo contendo variáveis de ambiente.
import env 

def ia_chat(user_msg):
  """
    Função para interagir com o modelo de IA para geração de conteúdo.

    Args:
        user_msg (str): Mensagem do usuário para ser processada pelo modelo.

    Returns:
        str: Resposta gerada pelo modelo.
    """
    
    # Configura a chave da API do Google AI
    genai.configure(api_key= env.GOOGLE_API_KEY)

    # Lista os modelos disponíveis e verifica se o método de geração de conteúdo é suportado
    for m in genai.list_models():
      if 'generateContent' in m.supported_generation_methods:
        print(m.name)

    # Inicializa o modelo específico ('gemini-pro') para geração de conteúdo
    model = genai.GenerativeModel('gemini-pro')
    # Gera uma resposta com base na mensagem do usuário
    response = model.generate_content(user_msg)
    msg = response.text
    
    return msg

