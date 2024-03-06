import google.generativeai as genai
import env 

def ia_chat(user_msg):
  
    genai.configure(api_key= env.GOOGLE_API_KEY)
    
    for m in genai.list_models():
      if 'generateContent' in m.supported_generation_methods:
        print(m.name)
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_msg)
    msg = response.text
    
    return msg

