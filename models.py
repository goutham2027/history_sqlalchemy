import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy_continuum import make_versioned
from sqlalchemy_continuum.plugins import TransactionMetaPlugin


Base = declarative_base(metadata=MetaData(schema='history_sqlalchemy'))

make_versioned(user_cls=None, plugins=[TransactionMetaPlugin()])


class Animal(Base):
    __versioned__ = {}
    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    uuids = Column(String(50))

sa.orm.configure_mappers()
