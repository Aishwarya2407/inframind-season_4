import speech_recognition as sr1
r1 = sr1.Recognizer()
with sr1.Microphone() as source:
    print("Speak Anything :")
    audio = r1.listen(source)
    try:
        text = r1.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")


