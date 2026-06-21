print("Simple Chatbot Started...\n")

while True:
    message = input("You: ")
    message = message.lower()

    if message == "hello" or message == "hi" or message == "hey":
        print("Bot: Hi there!")
        
        name = input("Bot: What's your name? ")
        print(f"Bot: Nice to meet you, {name}!")

    elif message == "bye":
        print("Bot: Goodbye! See you later.")
        break

    elif message == "how are you":
        print("Bot: I'm fine, thanks for asking!")

    else:
        print("Bot: Sorry, I don't understand that.")