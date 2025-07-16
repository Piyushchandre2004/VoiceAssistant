import os
from text_to_speech import speak

def shutdown():
    """Shuts down the system"""
    speak("Shutting down the system")
    os.system("shutdown /s /t 5")

def restart():
    """Restarts the system"""
    speak("Restarting the system")
    os.system("shutdown /r /t 5")
