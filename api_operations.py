import requests

def load_moon_phases(params):
    query_params = "&".join(f"{key}={requests.utils.quote(str(value))}" for key, value in params.items())
    url = f"https://www.icalendar37.net/lunar/api/?{query_params}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return data