import requests

PROXY_URL = "https://proxy.jooo.tech"
KEY="blocksmc-ex" # This key may be revoked at any time

def send(json):
    json["key"] = KEY
    return requests.post(PROXY_URL, json=json)

def get(url, headers={}):
    return send({
        "url": url,
        "headers": headers
    })

if __name__ == "__main__":
    print(get("https://blocksmc.com").text)