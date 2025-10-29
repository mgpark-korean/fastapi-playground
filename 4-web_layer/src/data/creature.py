import sqlite3
from model.creature import Creature


DB_NAME = 'cryptid.db'
conn = sqlite3.connect(DB_NAME)
curs = conn.cursor()

curs.execute("""create table if not exists 
""")

def init():
    curs.execute("create table creature(name, description, country, area, aka)")

def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(
        name=name,
        description=description,
        country=country,
        area=area,
        aka=aka
    )

def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()

def get_one(name: str) -> Creature :
    qry = "select * from creature whrere name=:name"
    params = {'name': name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)

def get_all(name: str) -> list[Creature]:
    qry = "select * from creature whrere name=:name"
    params = {'name': name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)

def create(creature: Creature) -> None:
    qry = """insert into creature values
            (:name, :description, :country, :area, :aka)"""
    params = model_to_dict(creature)
    curs.execute(qry, params)

def modify(creature: Creature) -> None:
    return creature

def replace(creature: Creature) -> None:
    return creature

def delete(creature: Creature) -> None:
    qry = "delete from creature where name = :name"
    params = {'name': creature.name}
    curs.execute(qry, params)