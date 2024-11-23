from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def old_users(username: str = Path(min_length=5, max_length=20, description='Enter Username'),
                    age: int = Path(ge=18, le=80, description='Enter Age')) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    add_user = f'Имя: {username}, возраст: {age}'
    users[current_index] = add_user
    return f'User {current_index} is registered.'


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: str = Path(min_length=1, max_length=1000, description='Enter User ID'),
                   username: str = Path(min_length=5, max_length=20, description='Enter Username'),
                   age: int = Path(ge=18, le=80, description='Enter Age')) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated.'


@app.delete('/user/{user_id}')
async def delete_user(user_id: str = Path(min_length=1, max_length=1000, description='Enter User ID')) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted.'
