from datetime import datetime
from typing import List

import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..core.config import settings
from ..models.exchange_rate import ExchangeRate
from ..schemas.exchange_rate import ExchangeRateCreate


async def get_exchange_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(settings.API_URL)
        return response.json()['pageProps']['onlineExchangeHouses']


async def get_exchange_houses() -> List[ExchangeRateCreate]:
    data = await get_exchange_data()
    return [
        ExchangeRateCreate(
            exchange_house=house['title'],
            buy_price=float(house['rates']['buy']['cost']),
            sell_price=float(house['rates']['sale']['cost']),
            timestamp=datetime.utcnow(),
        )
        for house in data
    ]


async def save_exchange_rates(db: AsyncSession, exchange_houses: List[ExchangeRateCreate]):
    db_objects = [ExchangeRate(**house.dict()) for house in exchange_houses]
    db.add_all(db_objects)
    await db.commit()


async def get_best_price(db: AsyncSession, operation: str = 'buy'):
    stmt = (
        select(ExchangeRate)
        .order_by(ExchangeRate.buy_price.desc() if operation == 'buy' else ExchangeRate.sell_price)
        .limit(1)
    )
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_top_exchanges(db: AsyncSession, n: int = 3, operation: str = 'buy'):
    stmt = (
        select(ExchangeRate)
        .order_by(ExchangeRate.buy_price.desc() if operation == 'buy' else ExchangeRate.sell_price)
        .limit(n)
    )
    result = await db.execute(stmt)
    return result.scalars().all()
