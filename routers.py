from fastapi import APIRouter
from pydantic import BaseModel
import requests

class Game(BaseModel):
    title: str
    year: int
    rating: float
    title2: str = None

router = APIRouter(prefix='/games', tags=['Games'])

@router.get('/get_game/{user}')
def get_game(user: str):
    body = requests.get(f'https://api.tesera.ru/collections/base/own/{user}?GamesType=Self&Limit=100')
    res = {}
    for obj in body.json():
        game = obj['game']
        title2 = game.get('title2', None)
        res[game['title']] = {
            'year': game['year'],
            'rating': game['ratingUser']
        }

        if title2:
            res[game['title']]['alsoknown'] = title2

    return res

@router.post("/add_game/")
def add_game(game: Game):
    return game
