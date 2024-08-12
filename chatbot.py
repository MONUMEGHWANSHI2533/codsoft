# -*- coding: utf-8 -*-
"""chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13ls6sw5B3t0oMM_DBo09SrjnhRhmDh0s
"""

import nltk
from nltk.chat.util import Chat, reflections
import spacy

# Download necessary NLTK data files
nltk.download('punkt')

# Load the small English model in spaCy
nlp = spacy.load("en_core_web_sm")

# Define a set of patterns and responses for the NLTK part of the chatbot
pairs = [
    [r"my name is (.*)", ["Hello %1, how can I help you today?"]],
    [r"hi|hello|hey", ["Hello! How can I assist you?"]],
    [r"what is your name?", ["I'm a chatbot created by you."]],
    [r"how are you?", ["I'm just a bunch of code, but thanks for asking! How are you?"]],
    [r"what can you do?", ["I can help with simple queries. Ask me about the weather, time, or more."]],
    [r"quit|bye|exit", ["Goodbye! Have a great day!"]],
]

# Initialize the NLTK chatbot
nltk_chatbot = Chat(pairs, reflections)

def combined_chatbot():
    print("Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ").lower()

        # Check for exit condition
        if "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a nice day!")
            break

        # Process user input with spaCy
        doc = nlp(user_input)

        # Use spaCy for entity recognition and pattern matching
        if any(ent.label_ == "TIME" for ent in doc.ents):
            print("Chatbot: The current time is 2:30 PM.")
        elif "weather" in user_input:
            print("Chatbot: The weather today is sunny with a slight chance of rain in the afternoon.")
        elif "name" in user_input:
            print("Chatbot: I'm a chatbot created by you.")
        else:
            # Fall back to NLTK-based responses
            response = nltk_chatbot.respond(user_input)
            if response:
                print(f"Chatbot: {response}")
            else:
                print("Chatbot: I'm sorry, I didn't quite understand that. Can you please rephrase?")

# Run the combined chatbot
combined_chatbot()