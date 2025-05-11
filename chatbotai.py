import nltk
import random
import string
import nltk
nltk.data.path.append("C:/Users/rajajikps/AppData/Roaming/nltk_data")


# Download required NLTK packages (first time only)
nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

# Responses
greetings = ["hello", "hi", "hey", "good morning", "good evening"]
greeting_responses = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Hi! How can I help you?"]

farewell = ["bye", "goodbye", "see you", "take care"]
farewell_responses = ["Goodbye!", "See you soon!", "Take care!", "Bye! Have a nice day!"]

qa_pairs = {
    "what is your name": "I'm ChatGPT Bot!",
    "how old are you": "I'm timeless! But let's say I'm 1 day old 😄",
    "what is your favorite color": "I love all colors equally 🌈",
    "date of birth": "I was created in 2025!",
    "country": "I'm from the cloud ☁️",
    "state": "I'm stateless, but happy!",
    "father name": "OpenAI is my creator.",
    "mother name": "Also OpenAI 😄"
}

default_responses = [
    "I'm not sure I understand. Can you tell me more?",
    "Interesting... tell me more.",
    "Let's talk about something else.",
    "Can you explain that a bit?"
]

def preprocess(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

def check_greeting(tokens):
    for token in tokens:
        if token in greetings:
            return random.choice(greeting_responses)
    return None

def check_farewell(tokens):
    for token in tokens:
        if token in farewell:
            return random.choice(farewell_responses)
    return None

def check_question(user_input):
    for question in qa_pairs.keys():
        if question in user_input.lower():
            return qa_pairs[question]
    return None

def chatbot_response(user_input):
    tokens = preprocess(user_input)
    
    greet = check_greeting(tokens)
    if greet:
        return greet

    bye = check_farewell(tokens)
    if bye:
        return bye

    answer = check_question(user_input)
    if answer:
        return answer

    return random.choice(default_responses)

# Main chatbot loop
print("🤖 Chatbot: Hello! I'm your chatbot. Ask me anything, or type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print(f"🤖 Chatbot: {response}")
    
    if user_input.lower() in farewell:
        break
