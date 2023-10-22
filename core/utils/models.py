from datetime import datetime
import sqlalchemy as db
from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey

from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

engine = db.create_engine("sqlite:///bot_db.sqlite3")

session = scoped_session(sessionmaker(bind=engine))


Base = declarative_base()
Base.query = session.query_property()


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, )
    user_name = Column(String(50), nullable=False)
    telegram_id = Column(String(70), unique=True, nullable=True)
    admin = Column(Boolean, default=False)
    blocked_user = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())


class Categorys(Base):
    __tablename__ = 'categorys'

    category_id = Column(Integer, primary_key=True, )
    category_name = Column(String(30), unique=True, nullable=False)


class Links(Base):
    __tablename__ = 'links'
    link_id = Column(Integer, primary_key=True, )
    link_name = Column(String(50), nullable=False)
    link = Column(String(250), nullable=False)
    category = Column(Integer, ForeignKey('categorys.category_id'))
    user = Column(Integer, ForeignKey('users.user_id'))

    class Meta:
        database = db
        db_table = 'links'


Base.metadata.create_all(engine)
