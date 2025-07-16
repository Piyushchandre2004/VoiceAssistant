import os
import webbrowser
from text_to_speech import speak

def open_application(command):
    """Opens system applications based on voice commands"""
    if "chrome" in command:
        speak("Opening Google Chrome")
        os.system("start chrome")
    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("calc")
    else:
        speak("Application not found")

def search_google(query):
    """Searches Google for the given query"""
    speak(f"Searching Google for {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

