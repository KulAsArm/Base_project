from fastapi import Depends, FastAPI, HTTPException
from typing import List

from database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from table_post import Post
from table_user import User
from table_feed import Feed

from schema import UserGet, PostGet, FeedGet

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


@app.get("/user/{id}", response_model=UserGet)
def get_user_id(id: int, db: Session = Depends(get_db)):
    results = db.query(User).filter(User.id == id).one_or_none()
    if results is None:
        raise HTTPException(404, f"{id} not find")
    else:
        return results


@app.get("/post/{id}", response_model=PostGet)
def get_post_id(id: int, db: Session = Depends(get_db)):
    results = db.query(Post).filter(Post.id == id).one_or_none()
    if results is None:
        raise HTTPException(404, f"{id} not find")
    else:
        return results


@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_user_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    result = db.query(Feed).filter(Feed.user_id == id).order_by(Feed.time.desc()).limit(limit).all()
    # action_list = [x.action for x in result]
    if result is None:
        raise HTTPException(200, f"{id} not find")
    else:
        return result


@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_post_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    result = db.query(Feed).filter(Feed.post_id == id).order_by(Feed.time.desc()).limit(limit).all()

    return result


@app.get("/post/recommendations/", response_model=List[PostGet])
def get_post_rec(id: int, limit: int = 10, db: Session = Depends(get_db)):
    result = (db.query(Post)
              .select_from(Feed)
              .filter(Feed.action == "like")
              .join(Post)
              .group_by(Post.id)
              .order_by(desc(func.count(Post.id)))
              .limit(limit)
              .all())
    return result


