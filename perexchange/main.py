import asyncio

from perexchange.core.config import logger
from perexchange.db.session import AsyncSessionLocal, engine
from perexchange.models.exchange_rate import Base
from perexchange.services.analysis import get_average_rates
from perexchange.services.exchange import (
    get_best_price,
    get_exchange_houses,
    get_top_exchanges,
    save_exchange_rates,
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database initialized successfully.")


async def async_main():
    await init_db()

    async with AsyncSessionLocal() as db:
        # Fetch and save exchange rates
        houses = await get_exchange_houses()
        await save_exchange_rates(db, houses)
        logger.info("Exchange rates saved successfully.")

        # Get best price for buying
        best_buy = await get_best_price(db, 'buy')
        if best_buy:
            logger.info(
                f"Best place to buy: {best_buy.exchange_house} at {
                    best_buy.buy_price}"
            )
        else:
            logger.warning("No buy prices available.")

        # Get top 3 exchanges for selling
        top_sell = await get_top_exchanges(db, 3, 'sell')
        if top_sell:
            logger.info("Top 3 places to sell:")
            for house in top_sell:
                logger.info(f"{house.exchange_house} at {house.sell_price}")
        else:
            logger.warning("No sell prices available.")

        # Get average rates for the last 30 days
        avg_rates = await get_average_rates(db)
        if avg_rates:
            logger.info("Average rates for the last 30 days:")
            for rate in avg_rates:
                logger.info(
                    f"{rate.exchange_house}: Buy {
                        rate.avg_buy:.4f}, Sell {rate.avg_sell:.4f}"
                )
        else:
            logger.warning("No average rates available.")


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
