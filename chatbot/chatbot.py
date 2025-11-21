# Simple Chatbot in Python
# This chatbot responds to greetings, time questions, and basic FAQs using rule-based responses.
# It runs in the terminal and keeps chatting until the user says "bye".

import datetime  # For handling time questions

def get_response(user_input):
    # Convert input to lowercase for easier matching
    user_input = user_input.lower()
    
    # Rule-based responses
    if any(word in user_input for word in ["hello", "hi", "hey", "greetings"]):
        return "Hello! How can I help you today?"
    
    elif "time" in user_input:
        # Get current time
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."
    
    elif "name" in user_input:
        return "I'm a simple chatbot created in Python. What's your name?"
    
    elif any(word in user_input for word in ["how are you", "how's it going"]):
        return "I'm doing well, thank you! How about you?"
    
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    
    else:
        return "I'm sorry, I don't understand that. Can you ask something else?"

# Main loop to run the chatbot
def main():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        
        # Exit if user says bye
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

if __name__ == "__main__":
    main()