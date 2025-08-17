
from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai

API_KEY = "YOUR_API_KEY_GOES_HERE"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    print("AI Model is configured.")
except Exception as e:
    print(f"Error configuring the API: {e}")

app = Flask(__name__)

def log_feedback(prompt, response, feedback):
    """Logs the prompt, response, and user feedback to a file."""
    try:
        with open("feedback.log", "a") as log_file:
            log_file.write(f"--- New Feedback ---\n")
            log_file.write(f"Timestamp: {__import__('datetime').datetime.now()}\n")
            log_file.write(f"Prompt Used: {prompt}\n")
            log_file.write(f"Generated Response: {response}\n")
            log_file.write(f"User Feedback (Helpful?): {feedback}\n\n")
        print("Feedback logged successfully.")
    except Exception as e:
        print(f"Error saving feedback: {e}")

def get_ai_response(prompt):
    """Sends a prompt to the AI and returns the response."""
    try:
        print(f"Sending prompt: {prompt[:100]}...") # Log first 100 chars
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    ai_response = None
    user_query = ""
    prompt = "" 

    if request.method == 'POST':
        user_query = request.form['query']
        function_choice = request.form['function']
        style_choice = "1" 

        if function_choice == 'qa':
            style_choice = request.form.get('qa_style')
        elif function_choice == 'summarize':
            style_choice = request.form.get('summarize_style')
        elif function_choice == 'creative':
            style_choice = request.form.get('creative_style')
    
        if function_choice == 'qa':
            if style_choice == '1':
                prompt = f"Answer the following question concisely: {user_query}"
            elif style_choice == '2':
                prompt = f"You are a subject matter expert. Provide a detailed and clear explanation for the question: {user_query}"
            elif style_choice == '3':
                prompt = f"Tell me three interesting and little-known facts related to this topic: {user_query}. Present as a numbered list."
        
        elif function_choice == 'summarize':
            if style_choice == '1':
                prompt = f"Provide a brief, single-paragraph overview of the following text:\n\n{user_query}"
            elif style_choice == '2':
                prompt = f"Extract the main points from this text and present them as a bulleted list:\n\n{user_query}"
            elif style_choice == '3':
                prompt = f"Summarize the following text in a single, concise 'TL;DR' sentence:\n\n{user_query}"
        
        elif function_choice == 'creative':
            if style_choice == '1':
                prompt = f"Write a creative, four-stanza poem about {user_query}."
            elif style_choice == '2':
                prompt = f"Generate an intriguing story idea for a topic: '{user_query}'. Include a character, setting, and conflict."
            elif style_choice == '3':
                prompt = f"Create three catchy marketing taglines for a product related to {user_query}."
        
        if prompt:
            ai_response = get_ai_response(prompt)
    
    return render_template('index.html', response=ai_response, query=user_query, prompt=prompt)

@app.route('/feedback', methods=['POST'])
def feedback():
    prompt = request.form['prompt']
    response = request.form['response']
    feedback_value = request.form['feedback']

    log_feedback(prompt, response, feedback_value)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)