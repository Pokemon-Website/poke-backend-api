from settings import USERS_COLLECTION
from database import get_collection
from models.users import User

collection = get_collection(USERS_COLLECTION)


async def new_user(user: User):
    insertion = await collection.insert_one(user.dict())
    if insertion.acknowledged:
        user = await get_user_by_email(user.email)
        return user


async def get_user_by_email(email):

    filter = {
        'email': email
    }
    user = await collection.find_one(filter)
    return user
