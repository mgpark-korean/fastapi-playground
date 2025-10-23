from fastapi import FastAPI
from .web import explorer, creature

# 실행시 python main.py &
#  - & : background 실행
app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)

@app.get("/")
def top():
    return "top here"

@app.get("/echo/{thing}")
def echo(thing: str):
    return f"echoing {thing}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True) 