# listener.py
import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Adjust for ambient noise
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        # Set energy threshold to a lower value for better sensitivity
        recognizer.energy_threshold = 300  # Default is 300, lowering it makes it more sensitive
        recognizer.dynamic_energy_threshold = True
        
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Processing audio...")
            
            try:
                command = recognizer.recognize_google(audio)
                print("You said:", command)
                return command.lower()
            except sr.UnknownValueError:
                print("Sorry, I didn't understand. Please speak clearly.")
                return ""
            except sr.RequestError:
                print("Could not request results from Google.")
                return ""
        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")
            return ""

def take_command():
    return listen()