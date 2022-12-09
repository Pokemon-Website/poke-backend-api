from fastapi import FastAPI
from persist.users import User
from rules.users import post_new_user, get_by_email
app = FastAPI()

@app.get('/')
async def hello():
    return {'hello':'world!'}

# @app.get('/{id_card}/')
# async def start(id_card: str):
#     pokemon_card = await get_card_by_id(id_card)
#     return pokemon_card

@app.get('/{email}')
async def get_user(email):
    user = await get_by_email(email)
    return user


@app.post('/')
async def post_user(user: User):
    new_user = await post_new_user(user)
    return new_user
