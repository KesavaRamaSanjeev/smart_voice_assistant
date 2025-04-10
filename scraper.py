import requests
from bs4 import BeautifulSoup

def get_latest_news():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []

    for item in soup.select(".gs-c-promo-heading__title"):
        if item.text.strip():
            headlines.append(item.text.strip())
        if len(headlines) >= 5:
            break

    return headlines

def get_weather_data():
    try:
        url = "https://wttr.in/?format=3"
        response = requests.get(url)
        return response.text
    except Exception as e:
        return "Sorry, I couldn't fetch the weather right now."
