import requests

SERVER_IP = '192.168.30.17'


def test_cuisine_1():
    cuisine_type = 'American'
    result = requests.get(f'http://192.168.30.17:5000/filter/cuisine?type={cuisine_type}')
    assert result.json()[0]['name'] == 'The Walnut Room'

def test_cuisine_2():
    cuisine_type = 'Deep Dish Pizza'
    result = requests.get(f'http://192.168.30.17:5000/filter/cuisine?type={cuisine_type}')
    assert len(result.json()) == 3

def test_neighborhood_1():
    neighborhood = 'River North'
    result = requests.get(f'http://192.168.30.17:5000/filter/neighborhood?neighborhood={neighborhood}')
    assert result.json()[2]['name'] == 'Billy Goat Tavern'

def test_neighborhood_2():
    neighborhood = 'Andersonville'
    result = requests.get(f'http://192.168.30.17:5000/filter/neighborhood?neighborhood={neighborhood}')
    assert len(result.json()) == 2

def test_score():
    score = 4.7
    result = requests.get(f'http://192.168.30.17:5000/filter/score?score={score}')
    assert len(result.json()) == 38
