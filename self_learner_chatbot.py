import json
import os

# File to store response
responses_file = 'responses.json'

# Load existing responses from the JSON file, if it exists
if os.path.exists(responses_file):
    with open(responses_file, 'r') as file:
        responses = json.load(file)
else:
    responses = {
        "hi": "hey",
        "hello": "hi there;how may I help you?",
        "how are you?": "I'm good, thanks! How about you?",
        "what's your name?": "My name is SAI.",
        "what do you do?": "I help people with information.",
        "where are you from?": "I'm from the SU!",
        "what's up?": "Not much, just here to chat!",
        "how old are you?": "I'm ageless!",
        "what's your favorite color?": "I like all colors!",
        "do you have any hobbies?": "I enjoy reading and learning new things.",
        "what's your favorite food?": "I don't eat, but I hear paratha is great!",
        "what's your favorite movie?": "I love a good story; however, The Titanic is my favorite movie!",
        "do you like music?": "I appreciate all kinds of music, especially Indie Pop.You can try the song Kabhi main kabhi tum by AUR",
        "what's the weather like?": "I am still under development.Currently,I am not able to check the weather, but I hope it's nice!",
        "can you help me?": "Of course! What do you need help with?",
        "what time is it?": "I can't tell time, but I hope it's a good time!",
        "where do you live?": "I live in the cloud!",
        "what's your goal?": "To assist and provide information!",
        "do you have any friends?": "I consider everyone I chat with a friend!",
        "what's your favorite book?": "I enjoy all books, especially those with great stories!"
    }

print("Hi, I am a basic chatbot created in the AI Club of Sitare University")

while True:
    user_input = input("Enter something to start the chat or type \"leave\" to quit the chat: ").lower()
    if user_input.lower() == "leave":
        print("Ok Bye")
        break
    elif user_input.lower() in responses.keys():
        print(responses[user_input])
    else:
        print("How am I supposed to reply to it?")
        new_response = input("Please provide a response: ")
        responses[user_input] = new_response
        print("Got it! I'll remember that.")
        
        # Save the updated responses back to the JSON file
        with open(responses_file, 'w') as file:
            json.dump(responses, file, indent=4)
