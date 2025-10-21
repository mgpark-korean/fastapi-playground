import datetime
import logging
from fastapi import FastAPI
from model.tag import Tag, TagIn, TagOut
import service.tag as service

# uvicorm web.tag:app

logger = logging.getLogger(__name__)
app = FastAPI()

@app.post('/', response_model=Tag)
def create(tag_in: TagIn) -> Tag:
    tag: Tag = Tag(tag=tag_in.tag, created=datetime.datetime.now(datetime.UTC), secret="shhhh")
    service.create(tag)
    logger.debug(tag)
    return tag

@app.get('/{tag_str}', response_model=TagOut)
def get_one(tag_str: str) -> TagOut:
    tag: Tag = service.get(tag_str)
    return tag