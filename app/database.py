import os
from typing import Any

import sqlalchemy as sa
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL, encoding="utf-8", echo=True, future=True)

metadata = sa.MetaData()
# metadata.reflect(bind=engine)
# Base = declarative_base(metadata=metadata)  # type: Any
Base = declarative_base(bind=engine, metadata=metadata)  # type: Any

# user_table = Table(
#     "user_accounts",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(30)),
#     Column("fullname", String(50)),
# )

# address_table = Table(
#     "addresses",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("user_id", ForeignKey("user_account.id"), nullable=False),
#     Column("email_address", String(100), nullable=False),
# )


class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


class Description(Base):
    __tablename__ = "descriptions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_accounts.id"), nullable=False)
    description = Column(String(255), nullable=False)

    user = relationship("User", back_populates="descriptions")


# ターゲットデータベース（MariaDB の "metheus"）を参照する Engine を MetaData に送信する
# metadata.create_all(bind=engine)

# def create_some_table():
#     with engine.connect() as conn:
#         conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#         conn.execute(
#             text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#             [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
#         )
#         conn.commit()


# def show_some_table():
#     with engine.connect() as conn:
#         result = conn.execute(text("select x, y from some_table"))
#         # for row in result:
#         #     print(type(row))
#         #     print(f"x: {row.x} y: {row.y}")

#         for row_mapping in result.mappings():
#             print(type(row_mapping))
#             print(f"x: {row_mapping['x']} y: {row_mapping['y']}")
