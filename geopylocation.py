
def welke_stad():
    import urllib.request
    import json
    with urllib.request.urlopen("http://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
        stad= data['city']
        postcode = data['postal']
    return (stad,postcode)
stad = welke_stad()

print('stad', stad)