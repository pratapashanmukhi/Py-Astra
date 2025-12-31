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

## 📦 **Required Python Libraries**

Install these using `pip`:

- `google-generativeai`
- `SpeechRecognition`
- `pyttsx3`
- `pyaudio`

## ⚙️ Installation & Setup
### ✅ Prerequisites
Make sure you have the following installed:

Python 3.8 or higher

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Py-Astra.git
cd Py-Astra
 ```
### 2. Create Virtual Environment
```bash
python -m venv venv
  ```

### 3. Activate the Virtual Environment

Activate the virtual environment using the command below.
Windows
```bash
venv\Scripts\activate
 ```
Mac / Linux
```bash
source venv/bin/activate
 ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
 ```
If requirements.txt is not available:
```bash
pip install google-generativeai speechrecognition pyttsx3 pyaudio
 ```
* with your Google Generative AI API Key.

### 5. How to Run the Project
```bash
python main.py
 ```

### 6. API Configuration
* For API Key: Visit Google AI Studio to get your API key.
Open main.py and replace:
```bash
API_KEY = 'Your_api_key'
 ```
* For Model: If you want to use a different model than the default (gemini-pro), you can:
 ```bash
model = ai.GenerativeModel("your-model-name")  # Replace the model name you have copied
  ```    
    
* Visit the Google AI Studio to browse and select the model that best suits your needs.

### ⚠️ Note:

* Google provides a free tier for Generative AI with limited monthly usage.
  
* If you exceed the free quota or use premium models, charges may apply.
  
* Use Responsibly, stay within free limits and avoid unexpected charges.

---

## 🧑‍💻 **How Py Astra Works**

- Listens to the user’s voice input using the SpeechRecognition library.
- Converts the spoken input into text.
- Sends the user’s query along with a predefined prompt to Google Gemini AI.
- Processes the response received from the AI model.
- Converts the AI-generated text response into speech using pyttsx3.
- Speaks the response back to the user in real time.
- Continuously runs in a loop until the user says "exit".

---
### 🚀 Usage
* Run the script:
 ```bash
   python Py Astra.py
 ```

* Speak your Python-related question when prompted.

* Py Astra will respond with a spoken answer.

* Say "explain in detail" or "give me more details" if you want a longer explanation.

* Say "exit" anytime to stop the program.

---

### 🧠 Code Structure

   *  `pytutor.py` : Main script containing:
   *  API configuration `google-generativeai`
   *  Voice input using `speech_recognition`
   *  Voice output using `pyttsx3`
   *  Gemini model prompt construction and interaction
   *  Voice-based command loop

---

## 🤝 Contributing

Contributions are welcome! If you'd like to suggest improvements, report bugs, or add new features, please open an issue or submit a pull request.

---

## 📬Contact
* For queries or suggestions, please contact:  
   [Pratapa Shanmukhi](mailto:pratapashanumukhi@gmail.com)
  
- 🔗 **LinkedIn:**  [Pratapa Shanmukhi](https://www.linkedin.com/in/shanmukhi-pratapa-6a4484336)

---
## 🚀 **Future Enhancements**

- Add GUI interface
- Support multiple programming languages
- Improve response accuracy with context memory
  
---

⚠️ **Disclaimer**

This project uses Google Generative AI. Make sure to follow their  
[terms of services](https://policies.google.com/terms) when using the API.

---
