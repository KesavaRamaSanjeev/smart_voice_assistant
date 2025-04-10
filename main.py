# main.py
import json
import os
from custom_command_handler import run_custom_command
from gemini_ai import ask_gemini
from scraper import get_latest_news  
from listener import listen, take_command
from speech_engine import speak
import pyautogui
import webbrowser
import time

def save_custom_command(trigger, action):
    file_path = "custom_commands.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data[trigger] = action

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def perform_task(command):
    # Check and run custom command if matched
    try:
        with open("custom_commands.json", "r") as f:
            custom_cmds = json.load(f)
            for trigger in custom_cmds:
                if trigger in command:
                    speak("Running your custom command.")
                    pyautogui.hotkey("win", "r")
                    time.sleep(1)
                    pyautogui.write(custom_cmds[trigger])
                    pyautogui.press("enter")
                    return
    except:
        pass

    if run_custom_command(command):
        speak("Running your custom command.")
        return

    if "add a custom command" in command:
        speak("Okay! How should I save to run this command?")
        trigger = take_command()

        speak(f"Got it! What should I do when I hear '{trigger}'?")
        action = take_command()

        save_custom_command(trigger, action)
        speak(f"Custom command saved! Next time you say '{trigger}', I will run '{action}'.")
        return

    if "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "type" in command:
        text_to_type = command.replace("type", "").strip()
        speak(f"Typing: {text_to_type}")
        pyautogui.write(text_to_type)

    elif "open notepad" in command:
        speak("Opening Notepad.")
        pyautogui.hotkey("win", "r")
        time.sleep(1)
        pyautogui.write("notepad")
        pyautogui.press("enter")

    elif "news" in command:
        speak("Fetching the latest news...")
        headlines = get_latest_news()
        if headlines:
            for i, headline in enumerate(headlines[:5], 1):
                speak(f"News {i}: {headline}")
        else:
            speak("Sorry, I couldn't fetch the news.")
    elif "weather" in command:
        from weather import get_weather
        weather = get_weather()
        speak(weather)
        # add_chat(f"Assistant: {weather}")  # Removed or commented out as it is undefined

    else:
        
        reply = ask_gemini(command)
        speak(reply)

def main():
    speak("Welcome! I'm your smart assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            if "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            perform_task(command)

if __name__ == "__main__":
    main()
