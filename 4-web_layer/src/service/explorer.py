from model.explorer import Explorer
import fake.explorer as data

def get_all() -> list[Explorer]:
    return data.get_all()

def get_one(name: str) -> Explorer | None:
    return data.get_one(name)

def create(Explorer: Explorer) -> Explorer:
    return data.create(Explorer)

def replace(name: str, Explorer: Explorer) -> Explorer:
    return data.replace(name, Explorer)

def modify(name: str, Explorer: Explorer) -> Explorer:
    return data.modify(name, Explorer)

def delete(name: str) -> bool:
    return data.delete(name)