🤖 Rule-Based AI Python ChatBot

A simple Rule-Based AI ChatBot built using Python. This chatbot interacts with users through predefined responses, greets them based on the current time, and answers basic questions using keyword matching.

📖 Project Overview

This project demonstrates the fundamentals of Artificial Intelligence and Natural Language Processing through a rule-based approach. The chatbot responds to user queries by matching keywords against a predefined set of responses.

It is designed for beginners learning Python and AI concepts.

✨ Features
Personalized user greeting
Time-based greetings (Morning, Afternoon, Evening, Night)
Interactive conversation loop
Predefined chatbot responses
Case-insensitive question handling
Exit command using "bye"
Simple rule-based AI implementation
🛠️ Technologies Used
Python 3
Dictionaries
Functions
Loops
Conditional Statements
Date and Time Module
📂 Project Structure
Rule-Based-AI-ChatBot/
│
├── chatbot.py
└── README.md
🚀 Getting Started
Prerequisites

Install Python 3 on your system.

Check Python version:

python --version
Run the Application
python chatbot.py
📋 Sample Interaction
Welcome, enter your name: Ankit

Good morning, Ankit

Welcome to Your ChatBot
You can ask me basic questions. Type 'bye' to exit from the bot

Please ask your question: hello
Bot Response: Hi, welcome. How can I help you?

Please ask your question: who are you
Bot Response: I am a smart AI chatbot

Please ask your question: motivate me
Bot Response: Keep going. Every bug in your project makes you a better developer

Please ask your question: bye
Bot Response: I am not able to answer that yet. I will learn this soon.
🧠 How It Works
Time-Based Greeting

The chatbot checks the current system time and greets the user accordingly.

presentHour = datetime.datetime.now().hour
Rule-Based Responses

The chatbot stores responses in a dictionary.

responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am doing very well. Thank you",
    "who are you": "I am a smart AI chatbot"
}
Keyword Matching

The chatbot searches user input for matching keywords and returns the associated response.

for eachKey in responses:
    if eachKey in userQuestion:
        return responses[eachKey]
🎯 Learning Objectives

This project helps in understanding:

Python Fundamentals
Functions and Dictionaries
String Manipulation
Rule-Based Artificial Intelligence
User Interaction in Console Applications
Basic NLP Concepts
🔮 Future Enhancements
Add more intelligent responses
Store conversation history
Use Machine Learning models
Integrate Speech Recognition
Add Text-to-Speech support
GUI using Tkinter
Connect with OpenAI APIs
Support multiple languages
📚 Concepts Demonstrated
Rule-Based Systems
Keyword Matching
Input Processing
AI Chatbot Basics
Decision Making Logic
