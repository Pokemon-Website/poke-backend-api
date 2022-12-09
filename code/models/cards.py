from pydantic import BaseModel

class Card(BaseModel):
    id: str
    name: str
    supertype: str
    subtypes: list(str)
    level: str
    hp: str
    types: list(str)
    evolvesFrom: str
    evolvesTo: list(str)
    rules: list(str)
    ancientTrait: dict
    abilities: list(dict)
    attacks: list(dict)
    weaknesses: list(dict)
    resistances: list(dict)
    retreatCost: list(str)
    convertedRetreatCost: int
    set: dict
    number: str
    artist: str
    rarity: str
    flavorText: str
    nationalPokedexNumbers: list(int)
    legalities: dict
    regulationMark: str
    images: dict
    tcgplayer: dict
    cardmarket: dict



