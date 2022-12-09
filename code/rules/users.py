from models.users import User
import persist.users

async def get_by_email(email):
    user = await persist.users.get_user_by_email(email)
    if user == None:
        return 'Not found'
    return user

async def post_new_user(user: User):
    exist = await get_by_email(user.email)
    if exist == None:
        new_user = await persist.users.new_user(user)
        return new_user