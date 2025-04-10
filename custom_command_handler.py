import json
import os

def load_custom_commands():
    file_path = "custom_commands.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return {}

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

def run_custom_command(command):
    commands = load_custom_commands()
    if command in commands:
        import pyautogui
        import time
        pyautogui.hotkey("win", "r")
        time.sleep(1)
        pyautogui.write(commands[command])
        pyautogui.press("enter")
        return True
    return False
