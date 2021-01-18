from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse
import random


def getFortune():
    fortunes = ['You will become very rich!',
                'You will fall into a big hole, and start a great adventure!',
                'You will find a golden ticket in your next apple!',
                'You will find your umbrella!',
                'You will dig up some treasure at the beach!',
                'You will turn into a unicorn!',
                'You will get no homework tomorrow!',
                'You will get to ride a giant dragon!']

    fortune1 = random.choice(fortunes)

    with open('wisdom.txt') as f:
        lines = f.readlines()
        advice = random.choice(lines)
        # print(random.choice(lines))


    with open('fortunes.txt', encoding="utf8") as f2:
        lines = f2.readlines()
        fortune2 = random.choice(lines)
        # print(random.choice(lines))


    sentence1 = "the robotic fortune teller says..... " + fortune1

    sentence2 = ", hello human, here is some advice from the robot who knows all ...... " + advice
    
    sentence3 = "finally, hear this, " + fortune2
    
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
        

    sentence4 = "I have spoken, human, goodbye, and remember" + cquote

    return sentence1, sentence2, sentence3, sentence4


app = Flask(__name__)



@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    body = request.values.get('Body', None)

    s1, s2, s3, s4 = getFortune()

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if 'fortune' in body.lower():
        resp.message(s1 + " " + s4)
    if 'random' in body.lower():
        resp.message(s3 + " " + s4)
    if 'advice' in body.lower():
        resp.message(s2 + " " + s4)

    elif body == 'test':
        resp.message("Goodbye")


    return str(resp)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a fortune message"""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    s1, s2, s3, s4 = getFortune()
    resp.say(s1, voice='alice')
    resp.say(s2, voice='alice')
    resp.say(s3, voice='alice')
    resp.say(s4, voice='alice')

    return str(resp)

if __name__ == "__main__":
    app.run(host =  'localhost', debug=True, port = 8003)