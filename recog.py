import audio
import speech_recognition as sr
r=sr.Recognizer()
def initspeech():
    with sr.Microphone() as source:
        print("Listening...")
        audio.play_audio("E:/PROGRAMMING/python programming/sounds/clearly.wav")
        user_audio=r.listen(source)
    command=""
    try:
        command=r.recognize_google(user_audio)
        audio.play_audio("E:/PROGRAMMING/python programming/sounds/when.wav")
        print("Your command : "+command)
        initiate()
    except:
        print("Could'nt Understand the command : "+command)
        audio.play_audio("E:/PROGRAMMING/python programming/sounds/deduction.wav")
        initiate()
        
def initiate():        
    while True:
        with sr.Microphone() as source:
            user_audio=r.listen(source)
            try:
                command=r.recognize_google(user_audio)
                if(command == 'jarvis' or 'Jarvis' or'JARVIS'):
                    print('Your command : '+command)
                    initspeech()
                elif(command == 'exit'):
                    print(" okay Bye sir!.")
                    exit(1)
            except:
                print('Hold')
initiate()
