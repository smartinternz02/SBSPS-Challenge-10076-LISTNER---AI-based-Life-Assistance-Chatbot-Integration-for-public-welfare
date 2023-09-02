import json
import re
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

# Load the responses from a JSON file
with open('responses.json', 'r') as file:
    responses = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()
 # Tokenize the user input
    tokens = word_tokenize(user_input)

    # Check for specific user inputs and provide corresponding responses
    for pattern, response in responses.items():
        pattern_tokens = word_tokenize(pattern)
        if all(token in tokens for token in pattern_tokens):
            return response

    # Default response if no specific pattern is matched
    return "I'm sorry, I don't understand that. Please ask something else."

# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    bot_response = get_response(user_input)
    print("jack:", bot_response)