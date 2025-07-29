def simple_chatbot():
    print("ChatBot: Hello! Type something to chat (type 'bye' to exit)")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("ChatBot: Hi!")
        elif user_input == "how are you":
            print("ChatBot: I'm fine, thanks!")
        elif user_input == "bye":
            print("ChatBot: Goodbye!")
            break
        else:
            print("ChatBot: I don't understand that.")

simple_chatbot()
