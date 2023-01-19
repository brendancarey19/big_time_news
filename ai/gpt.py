import requests
import json

class AIBot:

    def __init__(self, article, token, url):
        self.token = token
        self.url = url
        self.article = article
        self.prompt = self.article + "\n tl;dr:"
        self.data = {
            "model": "text-curie-001",
            "max_tokens": 140,
            "prompt": self.prompt,
            "temperature": 0.7
        }
        self.header = {'Authorization': 'Bearer ' + self.token}
        response = requests.post(self.url, json=self.data, headers = self.header)
        print(response)
        print(response.json())
        self.response = response.json()
        with open('data.json', 'a') as f:
            json.dump(response.json(), f)
            f.write('\n\n')
