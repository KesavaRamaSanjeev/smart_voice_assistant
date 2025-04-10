import requests

def get_weather(city="Guntur"):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "Sorry, I couldn't fetch the weather."
    except:
        return "Error getting weather information."
