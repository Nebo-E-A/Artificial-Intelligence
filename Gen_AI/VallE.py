import speech_recognition as sr 
import openai 
ear = sr.Recognizer()
with sr.Microphone() as sourse:
    print("listening...")
    audio = ear.listen(sourse)
    text = ear.recognize_google(audio)
    print("Question",text)
    openai.api_key = "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"
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[
                                                {"role": "system", "content": "Welcome to Vall-E"},
                                                {"role": "user", "content": text}])
    message = response.choices[0].message.content
    print("Answer",message)
    #except:
        #print("i didn't get that...")






