import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    #GET request to the URL passed in on initialization. 
    # This method should return the body of the response.
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        return json.loads(self.get_response_body())
    

# get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
# get_requester.load_json()