"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"


async_engine = create_async_engine(
    url=PG_CONN_URI,
    echo=True,
)


Session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    posts = relationship(
        "Post",
        back_populates="users",
    )


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey("postgres_users.id", name="fk_user_id"),
        unique=True,
        nullable=False,
    )
    title = Column(String, unique=True, nullable=False)
    body = Column(Text, nullable=False)

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )
