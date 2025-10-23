from model.explorer import Explorer

_explorers = [
    Explorer(
        name="Clause Hande",
        country="FR",
        description="보름달이 뜨면 만나기 힘듦"),
    Explorer(
        name="Noah Weiser",
        country="DE",
        description="눈이 나쁘고 벌목도를 가지고 다님")
]

def get_all() -> list[Explorer]:
    """탐험가 목록을 반환한다."""
    return _explorers

def get_one(name: str) -> Explorer | None:
    """검색한 탐험가를 반환한다."""
    print(name)
    for _explorer in _explorers:
        if(_explorer.name == name):
            return _explorer
    return None


# DB 적용 전 mock 함수
def create(explorer: Explorer) -> Explorer:
    """탐험가를 추가한다."""
    return explorer

def modify(name: str, explorer: Explorer) -> Explorer:
    """탐험가를 정보를 일부 수정한다."""
    return explorer

def replace(name: str, explorer: Explorer) -> Explorer:
    """탐험가를 완전히 교체한다."""
    return explorer

def delete(name: str) -> bool:
    """탐험가를 삭제한다. 만약 대상이 없다면 False를 반환한다."""
    for _explorer in _explorers:
        if _explorer.name == name:
            return True
    return False