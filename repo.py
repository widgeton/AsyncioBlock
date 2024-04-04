import models
import db


async def add_trading_results(results: list[models.TradingResults]) -> None:
    async with db.AsyncSession() as session:
        session.add_all(results)
        await session.commit()
