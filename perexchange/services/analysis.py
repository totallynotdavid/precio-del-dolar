from datetime import datetime, timedelta

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from perexchange.models.exchange_rate import ExchangeRate


async def get_average_rates(db: AsyncSession, days: int = 30):
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)

    stmt = (
        select(
            ExchangeRate.exchange_house,
            func.avg(ExchangeRate.buy_price).label('avg_buy'),
            func.avg(ExchangeRate.sell_price).label('avg_sell'),
        )
        .filter(ExchangeRate.timestamp.between(start_date, end_date))
        .group_by(ExchangeRate.exchange_house)
    )

    result = await db.execute(stmt)
    return result.all()
