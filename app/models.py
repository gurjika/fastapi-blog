from db import Base
from sqlalchemy import Boolean, Column, Integer, String, Text

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    published = Column(Boolean, nullable=True, default=True)
    # timestamp = Column(Time)

