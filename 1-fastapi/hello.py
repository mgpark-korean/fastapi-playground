from fastapi import Body, FastAPI, Header, Response

app = FastAPI()

# FastAPI Get method
@app.get("/hello")
def greetGet():
    return "Hello, FastAPI"

# FastAPI Get Path Valriable
@app.get("/hello/{who}")
def greetPathValriable(who):
    return f"Hello {who}?"

### FastAPI Query Paramter
@app.get("/hello-query")
def greetQueryParameter(who):
    return f"Hello {who}"

### FastAPI Body
@app.post("/hello")
def greetPost(who: str = Body(embed=True)):
    return f"Hello {who}"

### FastAPI Header
@app.get("/hello-header")
def greetHeader(who: str = Header()):
    return f"hello, {who}"

### FastAPI 200 response
@app.get("/happy")
def happy(status_code=200):
    return ":)"

### FastAPI Http Response header
@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return f"header set name={name} :: value={value}"
    
### 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)