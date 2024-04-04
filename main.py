import datetime as dt
import asyncio
import aiohttp
import time

import repo
import services as srvs
import db


async def save_trading_data(session,  date) -> None:
    data = await srvs.get_response_data(session, date)
    if data:
        dct_data = srvs.get_trading_data(data, date)
        db_models = srvs.convert_dict_to_db_models(dct_data)
        await repo.add_trading_results(db_models)
    print(date)


async def main(date):
    cur = date
    today = dt.date.today()
    tasks = []
    async with aiohttp.ClientSession() as session:
        while cur <= today:
            task = asyncio.create_task(save_trading_data(session, cur))
            tasks.append(task)
            cur += dt.timedelta(days=1)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    db.create_tables()
    start = time.time()
    asyncio.run(main(dt.date(2024, 1, 1)))
    print(time.time() - start)
