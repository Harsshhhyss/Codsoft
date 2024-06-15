#responses are the fixed pattern and responses of the chatbot
responses={
"hi":"Hi there! I'm here to assist you?",
"hello":"Hello! How can I help you today?",
"what's your name":"I'm just a chatbot,creates by Harsh.",
"where are you from":"I'm from the digital world!",
"how are you":"I'm doin good. What About You",
"do you have any hobbies or interests?":"I'm always busy helping users, and my interest is helping people in need",
"what did you eat today?":"I don't eat. I'm a bot",
"what's your favorite color?":"I'm a chatbot",
"do you enjoy listening to music?":"I dont listen to music",
"bye":"Bye! Take care!",
}
#Using function
def get_response(user_data):
    for pattern,response in responses.items():
        if pattern in user_data:
            return response
    return "I'm sorry,I didn't get it."
print("Harsh's Chatbot: Hi! I'm a chatbot,How can I help you!")
#Using while loop
while True:
    user_data=input("Me: ")
    
    
    if user_data=='bye':
       print("Chatbot: Goodbye!")
       break
#calling the function
    response=get_response(user_data)
    print("Harsh's Chatbot:",response)
#End    
