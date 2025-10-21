from ssl import DER_cert_to_PEM_cert
from fastapi import FastAPI
from model.model import Creature

app = FastAPI()

@app.get("/creature")
def get_all() -> list[Creature]:
    from data.data import get_creatures
    return get_creatures()