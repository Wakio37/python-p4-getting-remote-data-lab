import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        return json.loads(self.get_response_body())
        


if __name__ == "__main__":
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    requester = GetRequester(url)
    print(requester.get_response_body())

