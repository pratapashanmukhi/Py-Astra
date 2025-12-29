import google.generativeai as ai 
import speech_recognition as sr
import pyttsx3
import os


# API and Model setup
API_KEY = 'Your_api_key'
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()


# Default prompt
default_prompt = (
    "You are Py Astra, a professional and friendly Python tutor. "
    "Provide concise Python programming answers. Don't use emojis. Be interactive."
)

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()


# Function to speak a response
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()


# Function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Py Astra: Listening... Speak clearly.")
        speak("Listening. Please speak clearly.")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=15, phrase_time_limit=30)
            text = recognizer.recognize_google(audio).lower()
            print(f"Py Astra: You said: {text}")
            return text
        except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
            print("Py Astra: I couldn't hear or understand you. Please try again.")
            speak("I couldn't hear or understand you. Please try again.")
            return None


# Function to inform the user that the system is processing information
def processing_info():
    print("Py Astra: Processing your request, please wait...")
    speak("Processing your request, please wait.")


# Chatbot loop
print("Py Astra Assistant. Say 'exit' to stop.")
print(
    "Py Astra: Hello! I'm Py Astra, your Python assistant. "
    "Ask Python questions or say exit anytime to stop."
)
speak(
    "Hello! I'm Py Astra, your Python assistant. "
    "Ask Python questions or say exit anytime to stop."
)


while True:
    user_input = listen()

    if user_input:
        if "exit" in user_input:
            print("Py Astra: Exiting...")
            speak("Exiting.")
            speak("Goodbye! Happy coding.")
            break

        # Check if the user wants a detailed explanation
        if "explain in detail" in user_input or "give me more details" in user_input:
            modified_prompt = "Provide a detailed explanation of Python concepts."
        else:
            modified_prompt = default_prompt

        # Inform the user that Py Astra is processing the request
        processing_info()

        # Send modified prompt + user input to API
        response = chat.send_message(f"{modified_prompt}\nUser: {user_input}")

        # Chatbot response
        bot_response = response.text
        print(f"Py Astra: {bot_response}")
        speak(bot_response)
