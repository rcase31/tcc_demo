import speech_recognition as sr
from pygame import mixer  # Load the popular external library


#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    frase = 'a'
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        audio = microfone.listen(source, phrase_time_limit=5)

    try:
        #Passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio, language='pt-BR')
        #Após alguns segundos, retorna a frase falada
        #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except:
        pass
    return frase


def aguarda_audio(palavras: list) -> tuple:
    if isinstance(palavras, str):
        palavras = [palavras]
    mixer.init()
    frase = ouvir_microfone()
    print(frase)
    for palavra in palavras:
        if palavra in frase:
            return palavra
    return None