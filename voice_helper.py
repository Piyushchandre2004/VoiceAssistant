import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:  # Using index 2 for Boult Audio Airbass
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, could not understand audio."
        except sr.RequestError:
            return "Error connecting to Google API."
        except Exception as e:
            return f"Error: {e}"
