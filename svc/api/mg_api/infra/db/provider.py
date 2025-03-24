from typing import AsyncIterator, Iterator

from dishka import Provider, Scope, provide
from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import Session, sessionmaker

from app.infra.db.config import DbConfig


class DbProv(Provider):
    @provide(scope=Scope.APP)
    def config(self) -> DbConfig:
        return DbConfig()

    @provide(scope=Scope.APP)
    def sync_engine(self, settings: DbConfig) -> Engine:
        return create_engine(
            settings.SYNC_URL,
            echo=settings.ECHO,
            future=True,
            pool_size=settings.POOL_SIZE,
            max_overflow=settings.MAX_OVERFLOW,
        )

    @provide(scope=Scope.APP)
    def async_engine(self, settings: DbConfig) -> AsyncEngine:
        return create_async_engine(
            settings.ASYNC_URL,
            echo=settings.ECHO,
            future=True,
            pool_size=settings.POOL_SIZE,
            max_overflow=settings.MAX_OVERFLOW,
        )

    @provide(scope=Scope.APP)
    def sync_session_factory(self, engine: Engine) -> sessionmaker[Session]:
        return sessionmaker(bind=engine)

    @provide(scope=Scope.APP)
    def async_session_factory(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=engine, class_=AsyncSession)

    @provide(scope=Scope.REQUEST)
    def session(self, sess_factory: sessionmaker[Session]) -> Iterator[Session]:
        with sess_factory() as sess:
            yield sess

    @provide(scope=Scope.REQUEST)
    async def async_session(
        self, sess_factory: async_sessionmaker[AsyncSession]
    ) -> AsyncIterator[AsyncSession]:
        async with sess_factory() as sess:
            yield sess
