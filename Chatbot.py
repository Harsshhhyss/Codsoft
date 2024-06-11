import nltk
from nltk.chat.util import Chat, reflections
#Pairs is a list of patterns and responses.
Conversation = [
    [
        r"(.*)bot",
        ["hi Human, how can I help you "]
    ],
    [
        r"(.*)What you can do?",
        ["I am here for your help"]
    ],
    
    [
        r"(.*)creator",
        ["Harsh created me using Python"]
    ],
    [
        r"(.*)alive ",
        ["I am Robot, I am just a computer program . Created by Harsh"]
    ],
    
    
    [
        r"(.*)name(.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["If you need any help. Just ask ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is AI Robot, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Harsh created me using Python's NLTK library ","Its top secret........... ;)",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
    
]

my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
}
chat = Chat(Conversation, reflections)
chat.converse()
