from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def sayHello():
    return {"id":1,"name":"muhammed"}


@app.get("/users/{user_id}")
def get_user_id(user_id:int):
    return {"user_id":user_id}

info={"id":1,"email":"muhammed@gmail.com","password":"12345"}

@app.post("/user_info/{user_id,email,password}")
async def git_user_info(user_id:int,email:str,password:str):
   
    print(f"id : {user_id} , email : {email} , password : {password}")
    if user_id==info["id"] and email ==info["email"] and password==info["password"]:
        return {"massage":"valid"}
    else:
        return {"massage":"invalid"}
    
   