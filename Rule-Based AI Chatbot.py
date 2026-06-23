# Rule-Based AI Python ChatBot 

import datetime
import time

name = input("Welcome, enter your name: ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11: 
    print("Good morning, ", name)
elif 11 <= presentHour <= 17:
    print("Good afternoon, ", name)
elif 17 <= presentHour <= 20:
    print("Good evening, ", name)
else:
    print("Good night, ", name)



print("Welcome to Your ChatBot")
print("You can ask me basic questions. Type 'bye' to exit from the bot")

# Chatbot Memory Creation [ dictionary of responses ]

responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am doing very well. Thank you",
    "who are you": "I am a smart AI chatbot",
    "motivate me": "Keep going. Every bug in your project makes you a better developer",
    "happy": "Great to hear that",
    "what are functions": "I don't Know"
} 

# Method/Function to get response of ChatBot 

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to answer that yet. I will learn this soon."    
    

# Take user input 


while True:
    userInput = input("Please ask your question: ")
    reply = getResponseOfBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
        break