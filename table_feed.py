from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, func, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from table_user import User
from table_post import Post


class Feed(Base):
    """This class for using table feed_action"""

    __tablename__ = "feed_action"
    __table_args__ = {"schema": "public"}

    user = relationship("User")
    post = relationship("Post")

    user_id = Column(Integer, ForeignKey(User.id), primary_key=True, name="user_id")
    post_id = Column(Integer, ForeignKey(Post.id), name="post_id")
    action = Column(String, name="action")
    time = Column(TIMESTAMP, name="time")