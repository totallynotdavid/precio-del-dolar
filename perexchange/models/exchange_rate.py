from sqlalchemy import Column, DateTime, Float, Index, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ExchangeRate(Base):
    __tablename__ = 'exchange_rates'

    id = Column(Integer, primary_key=True)
    exchange_house = Column(String, index=True)
    buy_price = Column(Float)
    sell_price = Column(Float)
    timestamp = Column(DateTime, index=True)

    __table_args__ = (Index('idx_exchange_house_timestamp', 'exchange_house', 'timestamp'),)
