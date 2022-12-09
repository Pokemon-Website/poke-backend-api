import json
import requests
from pprint import pprint
from pokemontcgsdk import Card

URL_base = 'https://api.pokemontcg.io/v2/cards'

async def get_card_by_id(id_card):

    card = Card.find(id_card)
    return card



