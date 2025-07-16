from voice_helper import listen
from text_to_speech import speak
from commands import open_application, search_google
from web_search import search_wikipedia, search_youtube
from system_control import shutdown, restart

def run_assistant():
    speak("Hello Piyush! How can I assist you?")
    while True:
        command = listen().lower()  
        
        if "open" in command:
            open_application(command)
        elif "search google for" in command:
            query = command.replace("search google for", "").strip()
            search_google(query)
        elif "search wikipedia for" in command:
            query = command.replace("search wikipedia for", "").strip()
            search_wikipedia(query)
        elif "search youtube for" in command:
            query = command.replace("search youtube for", "").strip()
            search_youtube(query)
        elif "shutdown" in command:
            shutdown()
            break
        elif "restart" in command:
            restart()
            break
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I don't recognize that command.")

if __name__ == "__main__":
    run_assistant()
