"""
    1. provide input to user to enter a questions and answer the question
"""
def process(question):
    print("You asked :",question)

while True:
    question = input("Hi,welcome to bot chat, enter quit to end talk:")
    if(question == 'quit'):
        exit()
    else:
        process(question)

