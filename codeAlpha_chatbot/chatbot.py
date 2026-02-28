def chatbot_response(user_input):
    # Convert input to lowercase to make it case-insensitive
    user_input = user_input.lower().strip()

    # Rule-based logic using if-elif-else
    if "hello" in user_input or "hi" in user_input:
        return "Yes! hello"
    
    elif "how are you" in user_input:
        return "I'm fine, thanks! How about you?"
    
    elif "good" in user_input:
        return "That's cool, okay how can i help you?"
    
    
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    
   
    else:
        return "I'm sorry, I don't understand that. Could you try saying 'hello'?"

def start_chat():
    print("****Simple Python Chatbot*****")
    print("Greet me or type 'bye' to exit the conversation.")

    # Loop to keep the conversation going
    while True:
        # Get input from user
        user_text = input("You: ")
        
        # Get response from the function
        response = chatbot_response(user_text)
        
        # Display the reply
        print(f"Chatbot: {response}")

        # Break the loop if the user says goodbye
        if "bye" in user_text.lower():
            break

# Run the chatbot
start_chat()