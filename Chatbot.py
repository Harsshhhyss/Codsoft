#responses are the fixed pattern and responses of the chatbot
responses={
"greet": "Hello! How can I assist you today?",
"goodbye": "Goodbye! Have a great day!",
"hi":"Hi there! I'm here to assist you?",
"hello":"Hello! How can I help you today?",    
"thanks": "You're welcome!",
"options": "Here are a few things I can help with: [list of options]",
"fallback": "I'm sorry, I didn't quite catch that. Could you please repeat?",
"confirm_action": "Are you sure you want to proceed with this action?",
"provide_help': "How can I assist you further?",
"not_understood': "I'm sorry, I'm not sure I understand what you mean.",
"confirm_end': "Are you sure you want to end this session?",
"tell_more': "Please tell me more about your issue.",
"offer_help': "Would you like me to help you with anything else?",
"verify_details': "Let me verify your details.",    
"what's your name":"I'm just a chatbot,creates by Harsh.",
"where are you from":"I'm from the new AI world!",
"how are you":"I'm doin good. What About You",
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
#calling the function back (callback)
    response=get_response(user_data)
    print("Harsh's Chatbot:",response)
#End    
