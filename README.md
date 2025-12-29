# 🐍 Py Astra – Interactive Python Voice Assistant

Py Astra is an interactive **voice-based Python tutoring assistant** built using Python and Google Generative AI (Gemini Pro).  
It listens to user queries through speech, understands them using AI, and responds with clear Python explanations using text-to-speech.

---

## 📌 Project Description

Py Astra acts like a personal Python tutor.  
Users can ask Python-related questions using their voice, and Py Astra responds intelligently with spoken answers.  
It supports both **short answers** and **detailed explanations** based on user commands.

---

## ✨ Features

- 🎙️ Voice input using Speech Recognition  
- 🔊 Voice output using Text-to-Speech  
- 🤖 Powered by Google Gemini Pro (Generative AI)  
- 🧠 Smart prompt handling (normal & detailed explanation)  
- 🛑 Exit anytime by saying **“exit”**  
- 🐍 Python-focused learning assistant  

---

## 🛠️ Technologies Used

- Python 3  
- Google Generative AI (Gemini Pro)  
- SpeechRecognition  
- pyttsx3  
- PyAudio
---
## ⚙️ Installation & Setup
### ✅ Prerequisites
Make sure you have the following installed:

Python 3.8 or higher

### 🌇Clone the Repository

```bash
git clone https://github.com/your-username/Py-Astra.git
cd Py-Astra
 ```
### ✅ Create Virtual Environment
```bash
python -m venv venv
  ```

### ✅ Activate the Virtual Environment

Activate the virtual environment using the command below.
Windows
```bash
venv\Scripts\activate
 ```
Mac / Linux
```bash
source venv/bin/activate
 ```

### ✅ Install Dependencies
```bash
pip install -r requirements.txt
 ```
If requirements.txt is not available:
```bash
pip install google-generativeai speechrecognition pyttsx3 pyaudio
 ```
with your Google Generative AI API Key.

### ▶️ How to Run the Project
```bash
python main.py
 ```

### 4️⃣ API Configuration
For API Key: Visit Google AI Studio to get your API key.
Open main.py and replace:
```bash
API_KEY = 'Your_api_key'
 ```
For Model: If you want to use a different model than the default (gemini-pro), you can:
Visit the Google AI Studio to browse and select the model that best suits your needs.

### ⚠️ Note:

Google provides a free tier for Generative AI with limited monthly usage.
If you exceed the free quota or use premium models, charges may apply.
Use Responsibly, stay within free limits and avoid unexpected charges.

---

### 🧑‍💻 How Py Astra Works

1.Listens to the user’s voice input

2.Converts speech to text

3.Sends query to Gemini AI

4.Receives Python-based response

5.Converts text to speech and speaks back

---

### 🚀 Usage
1. Run the script:
 ```bash
   python Py Astra.py
 ```

2.Speak your Python-related question when prompted.

3.Py Astra will respond with a spoken answer.

4.Say "explain in detail" or "give me more details" if you want a longer explanation.

5.Say "exit" anytime to stop the program.

---

### 🧠 Code Structure
---
Py Astra.py: Main script containing:

 API configuration google-generativeai

 Voice input using speech_recognition

 Voice output using pyttsx3

 Gemini model prompt construction and interaction
 
 Voice-based command loop
 
---

## 🤝 Contributing

Contributions are welcome! If you'd like to suggest improvements, report bugs, or add new features, please open an issue or submit a pull request.

---

## 📬Contact
For queries or suggestions, please contact:  
[pratapashanumukhi@gmail.com](mailto:pratapashanumukhi@gmail.com)

---
