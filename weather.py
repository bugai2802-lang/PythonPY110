import requests
from pprint import pprint
from datetime import datetime

from django.db.models.expressions import result

# Словарь перевода значений направления ветра
DIRECTION_TRANSFORM = {
    'n': 'северное',
    'nne': 'северо - северо - восточное',
    'ne': 'северо - восточное',
    'ene': 'восточно - северо - восточное',
    'e': 'восточное',
    'ese': 'восточно - юго - восточное',
    'se': 'юго - восточное',
    'sse': 'юго - юго - восточное',
    's': 'южное',
    'ssw': 'юго - юго - западное',
    'sw': 'юго - западное',
    'wsw': 'западно - юго - западное',
    'w': 'западное',
    'wnw': 'западно - северо - западное',
    'nw': 'северо - западное',
    'nnw': 'северо - северо - западное',
    'c': 'штиль',
}


def current_weather(lat, lon):
    """
    Описание функции, входных и выходных переменных
    """
    token = '379bc81dbd434dc3a5f75707260305' # Вставить ваш токен из api.weatherapi.com
    url = f"https://api.weatherapi.com/v1/current.json?key={token}&q={lat},{lon}"
    response = requests.get(url)
    data = response.json()

    # Данная реализация приведена для api.weatherapi.com
    result = {
        'city': data['location']['name'],
        'time': data['current']['last_updated'],
        'temp': 19.3,
        'feels_like_temp': 19.3,
        'pressure': 1005.0,
        'humidity': 40,
        'wind_speed': 19.4,
        'wind_gust': 22.6,
        'wind_dir': DIRECTION_TRANSFORM.get(data['current']['wind_dir'].lower()),
    }
    return result


if __name__ == "__main__":
    res=current_weather(59.93, 30.31)
    pprint(res)
