import requests

def obtener_feriados():
    url = "https://calendarific.com/api/v2/holidays"
    params = {
        'api_key': '9Ug5z0uNhbha28lrR6fGeV1eMLJfSMzr',
        'country': 'CL',
        'year': 2024
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None