from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 1. تسمية الكلاس بحرف كبير احترافياً
class UserInfo(BaseModel):
    id: int
    email: str
    password: str


users_db = [
    {"name": "Muhammed"},
    {"name": "Ali"},
    {"name": "Ahmed"},
    {"name": "Sajjad"},
]


@app.get("/")
def say_hello():
    return {"id": 1, "name": "muhammed"}


@app.get("/users/{user_id}")
def get_user_id(user_id: int):
    return {"user_id": user_id}


@app.get("/user")
async def search_user(i: int = 2, search: str = ""):
    # 1. استخدام الاقتطاع [:i] يمنع حدوث خطأ الخروج عن حدود القائمة IndexError
    if search == "":
        return {"users": users_db[:i]}

    users_found = []
    for user in users_db:
        # 2. استخدام in يتيح البحث الجزئي بأسلوب أنظف
        if search.lower() in user["name"].lower():
            users_found.append(user)

    return users_found


info = {"id": 1, "email": "muhammed@gmail.com", "password": "12345"}


@app.post("/user_info")
async def check_user_info(user: UserInfo):
    print(f"id : {user.id} , email : {user.email} , password : {user.password}")
    if (
        user.id == info["id"]
        and user.email == info["email"]
        and user.password == info["password"]
    ):
        return {"message": "valid"}

    return {"message": "invalid"}