import requests
import json

url = requests.get("https://opentdb.com/api.php?amount=20&category=15&difficulty=medium&type=boolean")
text = url.text

quiz_api_data = json.loads(text)

question_data = quiz_api_data["results"]
