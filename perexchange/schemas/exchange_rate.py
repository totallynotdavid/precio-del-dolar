from datetime import datetime

from pydantic import BaseModel


class ExchangeRateBase(BaseModel):
    exchange_house: str
    buy_price: float
    sell_price: float
    timestamp: datetime


class ExchangeRateCreate(ExchangeRateBase):
    pass


class ExchangeRate(ExchangeRateBase):
    id: int

    class Config:
        from_attributes = True
