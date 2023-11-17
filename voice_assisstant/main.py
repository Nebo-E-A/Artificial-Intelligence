import difflib
import speech_recognition as sr
import json
import pyttsx3
import openai
#from gtts import gTTs
#from difflib import get_close_matches
#from . import Data

def user_input()->str:
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            audio = rec.listen(source)
            try:
                request = rec.recognize_google(audio)
                print(request)
                return request
            except:
                print("i didn't get that...")

def retrieval(request)->str:
    with open("Data.json","r") as file:
        data:dict = json.load(file)
    requests = list(data.keys())
    acc_request = difflib.get_close_matches(request, requests)
    text_response = data[acc_request[0]]
    print(text_response)
    return text_response

def gpt_retrieval(request)->str:
    openai.api_key = "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"
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[
                                                {"role": "system", "content": "Welcome to Vall-E"},
                                                {"role": "user", "content": request}])
    gpt_response = response.choices[0].message.content
    return gpt_response





def voice_assisstant():
    converter=pyttsx3.init()
    #converter.say("Hi I am all ears")
    while True:
        request:str=user_input()
        if(request == "exit" or request==" thank you"):
            break
        response:str = retrieval(request)
        converter.say(response)
        converter.runAndWait()














if __name__ == '__main__':
    voice_assisstant()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
