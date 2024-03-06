**Instruções para Configuração do ChatBot**

Este é um guia passo a passo para configurar o ambiente e as dependências necessárias para o projeto do ChatBot.

**Pré-requisitos**
* Python instalado no seu sistema
* Acesso à internet

**Passos**
 1. **Criar Ambiente Virtual:** Crie um ambiente virtual para isolar as dependências do seu projeto. Isso garante que as bibliotecas necessárias não interfiram com outros projetos

    * Instale o virtualenv (caso não tenha): 
      ~~~Python
      pip install virtualenv
      ~~~
   * Cria uma máquina virtual:
      ~~~Python
      python -m venv vm
      ~~~
     * Ativar maquina Virtual:
      ~~~Python
      vm\Scripts\activate
      ~~~
OBS: O passo a passo está correto para o windows. Outros sistemas operacionais podem apresentar diferenças. 

 3. **Instalar Dependências:** Utilize o pip para instalar as bibliotecas necessárias, executando o seguinte comando:
   ~~~Python
   pip install telepot
   ~~~
 3. **Gerar Token do ChatBot:**
     * Acesse o aplicativo Telegram e procure por @BotFather. Inicie uma conversa clicando sobre ele.
     * No chat, envie o comando: /newbot.
     * Siga as instruções fornecidas pelo BotFather para configurar um nome para o seu bot.
     * Você receberá um token único e um link para o seu bot.

 4.**Obter Chave da API Gemini:** Acesse o link: https://aistudio.google.com/app/apikey para gerar a chave da API Gemini.
 
 5. **Criar Arquivo 'env.py':**
   * Crie um arquivo chamado env.py no diretório raiz do seu projeto.
   * Adicione o token do Telegram e a chave da API Gemini no seguinte formato:
       ~~~Python
       TOKEN = 'INSIRA AQUI O TOKEN QUE VOCÊ GEROU NO TELEGRAM' 
       GOOGLE_API_KEY =  'INSIRA AQUI A CHAVE GERADA NA API GEMINI'
       ~~~
 6. **Executar o Programa:**
   * Rode o arquivo main.py para iniciar a execução do ChatBot.
   * Abra o Bot no telegram e inicie a conversa. 

= )
