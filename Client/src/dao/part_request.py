import requests


def create_part(part, url):

    serialized = part.to_dict()

    data = {"part": serialized}

    response = requests.post(url, json=data)

    body = response.json()
    print(body["message"])
    

def get_part(part_id, url):

    params = {"part_id": part_id}

    response = requests.get(url, params=params)

    body = response.json()

    return body

def list_parts(url):


    response = requests.get(url)

    body = response.json()

    return body["parts"]
