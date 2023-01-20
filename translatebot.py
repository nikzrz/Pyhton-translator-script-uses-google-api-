import requests
import json

def translate_text(text, target_language):
    api_key = "YOUR_API_KEY"
    url = "https://translation.googleapis.com/language/translate/v2"
    payload = {
        "q": text,
        "target": target_language,
        "format": "text",
        "key": api_key
    }
    response = requests.post(url, json=payload)
    json_data = json.loads(response.text)
    return json_data["data"]["translations"][0]["translatedText"]

text = "Hello, how are you?"
target_language = "fr"
translated_text = translate_text(text, target_language)
print(translated_text)
