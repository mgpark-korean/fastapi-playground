
from fastapi import Depends, FastAPI, Query


app = FastAPI()

def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {"name": name, "valid": True}

@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user