import os
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME", "userdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    username = Column(String(50))
    created = Column(String(50))
    modified = Column(String(50))
    email = Column(String(50))
    phone_number = Column(String(50))

    def __repr__(self):
        return f"<User(name='{self.name}', username='{self.username}', email='{self.email}')>"

    @staticmethod
    def create_table():
        Base.metadata.create_all(engine)


class UserDB:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def add_user(self, name: str, username: str, email: str, phone_number: str) -> User:
        user = User(
            name=name,
            username=username,
            email=email,
            phone_number=phone_number,
            created=str(datetime.now().timestamp()),
            modified=str(datetime.now().timestamp())
        )
        try:
            self.session.add(user)
            self.session.commit()
            return user
        except ValueError:
            self.session.rollback()
            raise ValueError("Data couldn't save")

    def get_user(self, **kwargs):
        if kwargs:
            return self.session.query(User).filter_by(**kwargs).all()
        return self.session.query(User).all()