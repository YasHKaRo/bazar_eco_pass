from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    "sqlite+aiosqlite:///passw.db"
)
new_session = async_sessionmaker(engine, expire_on_commit=False)

def get_db():
    db = new_session()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass


class TaskOrm(Base):
    __tablename__ = "pass_history"
    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[str]
    password: Mapped[str]
    user: Mapped[Optional[str]]
    date: Mapped[str]

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)