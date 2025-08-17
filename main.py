
import google.generativeai as genai
import os

API_KEY = "YOUR_API_KEY_GOES_HERE" 

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    print("AI Assistant is configured and ready!")
except Exception as e:
    print(f"Error configuring the API. Please check your API key. Error: {e}")
    exit()

def get_ai_response(prompt):
    """Sends a prompt to the AI and returns the response."""
    try:
        print("\nAssistant is thinking...")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while generating the response: {e}"

def get_user_feedback(prompt, response):
    """Asks for user feedback and logs it to a file."""
    print("-" * 20) 
    feedback = input("Was this response helpful? (yes/no): ").lower()
    
    try:
        with open("feedback.log", "a") as log_file:
            log_file.write(f"--- New Feedback ---\n")
            log_file.write(f"Timestamp: {__import__('datetime').datetime.now()}\n")
            log_file.write(f"Prompt Used: {prompt}\n")
            log_file.write(f"Generated Response: {response}\n")
            log_file.write(f"User Feedback (Helpful?): {feedback}\n\n")
        
        print("Thank you for your feedback!")
    except Exception as e:
        print(f"Error saving feedback: {e}")

def handle_question_answering():
    """Handles the Question Answering feature."""
    print("\n--- Question Answering ---")
    user_question = input("What is your question? ")
    
    print("\nChoose a prompt style:")
    print("1. Simple & Direct")
    print("2. Detailed Explanation (Act as an Expert)")
    print("3. Fun Facts Format")
    style_choice = input("Select a style (1-3): ")

    if style_choice == '1':
        prompt = f"Answer the following question concisely: {user_question}"
    elif style_choice == '2':
        prompt = f"You are a subject matter expert. Provide a detailed and clear explanation for the following question: {user_question}"
    elif style_choice == '3':
        prompt = f"Tell me three interesting and little-known facts related to this topic: {user_question}. Present them as a numbered list."
    else:
        print("Invalid style choice. Using default (Simple & Direct).")
        prompt = f"Answer the following question: {user_question}"
        
    response = get_ai_response(prompt)
    print("\n--- AI Response ---")
    print(response)
    get_user_feedback(prompt, response)

def handle_summarization():
    """Handles the Text Summarization feature."""
    print("\n--- Text Summarization ---")
    user_text = input("Paste the text you want to summarize:\n")

    print("\nChoose a summary style:")
    print("1. Brief Overview (Single Paragraph)")
    print("2. Key Bullet Points")
    print("3. TL;DR (Too Long; Didn't Read - One Sentence)")
    style_choice = input("Select a style (1-3): ")

    if style_choice == '1':
        prompt = f"Provide a brief, single-paragraph overview of the following text: \n\n{user_text}"
    elif style_choice == '2':
        prompt = f"Extract the main points from this text and present them as a bulleted list: \n\n{user_text}"
    elif style_choice == '3':
        prompt = f"Summarize the following text in a single, concise 'TL;DR' sentence: \n\n{user_text}"
    else:
        print("Invalid style choice. Using default (Brief Overview).")
        prompt = f"Summarize this text: \n\n{user_text}"

    response = get_ai_response(prompt)
    print("\n--- AI Response ---")
    print(response)
    get_user_feedback(prompt, response)

def handle_creative_content():
    """Handles the Creative Content Generation feature."""
    print("\n--- Creative Content Generation ---")
    user_topic = input("What is the topic for the creative content? ")

    print("\nChoose a content type:")
    print("1. Short Poem")
    print("2. Story Idea")
    print("3. Marketing Tagline")
    style_choice = input("Select a type (1-3): ")

    if style_choice == '1':
        prompt = f"Write a creative, four-stanza poem about {user_topic}."
    elif style_choice == '2':
        prompt = f"Generate an intriguing story idea or plot hook based on the topic of '{user_topic}'. Include a main character, a setting, and a central conflict."
    elif style_choice == '3':
        prompt = f"Create three catchy and memorable marketing taglines for a product related to {user_topic}."
    else:
        print("Invalid style choice. Using default (Short Poem).")
        prompt = f"Generate some creative content about {user_topic}."

    response = get_ai_response(prompt)
    print("\n--- AI Response ---")
    print(response)
    get_user_feedback(prompt, response)

def main():
    """The main function to run the AI Assistant."""
    while True:
        print("\n" + "="*15 + " AI Assistant Menu " + "="*15)
        print("1. Answer a Question")
        print("2. Summarize Text")
        print("3. Generate Creative Content")
        print("4. Exit")
        print("="*47)

        choice = input("Select an option (1-4): ")

        if choice == '1':
            handle_question_answering() 
        elif choice == '2':
            handle_summarization()
        elif choice == '3':
            handle_creative_content()
        elif choice == '4':
            print("\nThank you for using the AI Assistant.")
            break
        else:
            print("\nInvalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()