import requests


#uso de api externa (calendarific) para obtener feriados de chile
# en ingles :(

def obtener_feriados():
    url = "https://calendarific.com/api/v2/holidays"
    params = {
        'api_key': '9Ug5z0uNhbha28lrR6fGeV1eMLJfSMzr',
        'country': 'CL',
        'year': 2024
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data=response.json()
        events = []
        for event in data['response']['holidays']:
            events.append({
                'title': event['name'],
                'start': event['date']['iso'],
                'end': event['date']['iso']
            })
        return events
    
    return None