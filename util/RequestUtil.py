import requests

def getPage(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.text
    return None