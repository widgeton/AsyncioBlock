from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from typing import Annotated
from datetime import datetime

import config

sync_engine = create_engine(url=config.DB_URL)
async_session = create_async_engine(url=config.DB_URL)
AsyncSession = async_sessionmaker(bind=async_session, autoflush=False)

pk = Annotated[int, mapped_column(primary_key=True, nullable=False, unique=True, autoincrement=True)]

crated_dt = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_dt = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                               onupdate=text("TIMEZONE('utc', now())"))]


class Base(DeclarativeBase):
    pass


def create_tables():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
