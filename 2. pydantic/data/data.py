from multiprocessing.heap import Arena
from os import name
from model.model import Creature

_creatures: list[Creature] = [
    Creature(
        name="yeti",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
        aka="Abominable Snowman"
    ),
    Creature(
        name="sasquatch",
        country="US",
        area="Himalayas",
        description="Yeti's Cousin Eddie",
        aka="Bigfoot"
    )
]

def get_creatures() -> list[Creature]:
    return _creatures