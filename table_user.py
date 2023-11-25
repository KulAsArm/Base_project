from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, func, ForeignKey, TIMESTAMP


class User(Base):
    """This class for using table user in ..."""

    __tablename__ = "user"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, name="id")
    gender = Column(Integer, name="gender")
    age = Column(Integer, name="age")
    country = Column(String, name="country")
    city = Column(String, name="city")
    exp_group = Column(Integer, name="exp_group")
    os = Column(String, name="os")
    source = Column(String, name="source")
