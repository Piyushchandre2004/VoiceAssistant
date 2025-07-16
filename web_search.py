import webbrowser
from text_to_speech import speak

def search_wikipedia(query):
    """Searches Wikipedia and opens the page"""
    speak(f"Searching Wikipedia for {query}")
    url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
    webbrowser.open(url)

def search_youtube(query):
    """Searches YouTube for the given query"""
    speak(f"Searching YouTube for {query}")
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(url)
