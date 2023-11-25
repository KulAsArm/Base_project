from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, func


class Post(Base):
    """This class for using table post in Postgres"""

    __tablename__ = "post"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, name='id')
    text = Column(String, name='text')
    topic = Column(String, name='topic')


# if __name__ == "__main__":
#  session = SessionLocal()
# post = (session.query(User.country, User.os, func.count(User.id))
#         .filter(User.exp_group == 3)
#         .group_by(User.country, User.os)
#         .having(func.count(User.id) > 100)
#         .order_by(func.count(User.id).desc())
#         .all())
# print(post)
# # list_id = [x.id for x in post]
#
# print(list_id)
#
