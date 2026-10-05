import requests
def deliver(url, payload, secret):
    resp = requests.post(url, json=payload, timeout=5)
    resp.raise_for_status()
    return resp.status_code
