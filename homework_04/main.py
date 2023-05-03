"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from .models import Base, User, Post, async_engine, Session
from .jsonplaceholder_requests import fetch_posts_data, fetch_users_data


session = Session()


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def create_users(user_list):
    users = [User(name=item["name"], username=item["username"], email=item["email"]) for item in user_list]
    await session.add_all(users)
    await session.commit()


async def create_posts(post_list):
    posts = [Post(user_id=item["user_id"], title=item["title"], body=item["body"]) for item in post_list]
    await session.add_all(posts)
    await session.commit()


async def async_main():
    await create_tables()
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    await asyncio.gather(
        create_users(users_data),
        create_posts(posts_data),
    )
    await async_engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
