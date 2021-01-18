import random
import pyttsx3
import speech_recognition as sr
import time
from subprocess import Popen

idlemovie = 'media/idle_screen.mp4'
welcomemovie = 'media/welcome_screen_loop.mp4'
eye1movie = 'media/eyes_open.mp4'
eye2movie = 'media/eyes_close.mp4'
fortune1movie = 'media/fortune_1.mp4'
fortune2movie = 'media/fortune_2.mp4'

## "sudo vlc " + idlemovie +" --no-video-title --loop --fullscreen" 



# omxp = Popen(['omxplayer',idlemovie])

##play idle sequence

maindelay = 5  #delay for main loop

r = sr.Recognizer()


def getSpeech():
    text = "human"
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return text

def speak(sentence):
    eng = pyttsx3.init()
    eng.setProperty('rate', 130) 
    eng.say(sentence)
    eng.runAndWait()
    print(sentence)
    eng.stop() 

# name = input('what is your name?')
# n1 = len(name)

# name = getname()
count = 1


while (1) :
    count -=1

    ##detect user with distance/motion

    ##led flash


    ## play opening sequence
    # omxp = Popen(['omxplayer', eye1movie])
    
    speak("what is your name, human?")
    name = getSpeech()
    if " " in name:
        word_list = name.split()
        name = word_list[-1]
    
    if name != "human":
        speak("greetings, ..." + name)

    # name = "human"

    # omxp = Popen(['omxplayer', eye1movie])

    fortunes = ['You will become very rich!',
                'You will fall into a big hole!',
                'You will find a worm in your next apple!',
                'You will lose your umbrella!',
                'You will dig up some treasure at the beach!',
                'You will turn into a newt!',
                'You will get no homework tomorrow!',
                'You will get eaten by a dragon!']


    # omxp = Popen(['omxplayer', fortune1movie])

    fortune1 = random.choice(fortunes)

    # print()
    # print(fortune1)
    # print()


    with open('wisdom.txt') as f:
        lines = f.readlines()
        advice = random.choice(lines)
        # print(random.choice(lines))


    with open('fortunes.txt', encoding="utf8") as f2:
        lines = f2.readlines()
        fortune2 = random.choice(lines)
        # print(random.choice(lines))


    sentence = "the robotic fortune teller says..... " + fortune1
    speak(sentence)

    time.sleep(1)


    sentence = name + ", .....  here is some advice from the robot who knows all ...... " + advice
    speak(sentence)

    time.sleep(1)


    sentence = "finally,... " + name + " ... hear this, ....." + fortune2
    speak(sentence)

    choice = random.randrange(0,2)


    q1 ="may the force be with you"
    q2 = "the needs of the many outweigh the needs of the few"
    q3 = "so say we all"

    if choice == 0:
        cquote = q1

    if choice == 1:
        cquote = q2

    if choice == 2:
        cquote = q3
        

    sentence = "I have spoken, ...." + name + " ... goodbye, ....." + cquote
    speak(sentence)


    ## play ending sequence


    ## play idle sequence

    time.sleep(maindelay)

    if count == 0:
        break



