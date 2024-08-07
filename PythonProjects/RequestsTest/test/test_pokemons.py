import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2702d1e06d118a703a19d33fb8b1f03c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 5612

def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', headers=HEADER, params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200 

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/pokemons', headers=HEADER, params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Мариозавр'

@pytest.mark.parametrize('key, value', [('name', 'Мариозавр'), ('trainer_id', TRAINER_ID), ('pokemon_id', '23456')])
def test_parametrize(key,value):
     response_get = requests.get(url=f'{URL}/pokemons', headers=HEADER, params={'trainer_id': TRAINER_ID})
     assert response_parametrize.json()["data"][0]["key"] == 'value' 
