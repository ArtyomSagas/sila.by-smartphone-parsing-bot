# from sqlalchemy import insert, select
# from database import sync_engine
# from models import metadata_obj, products_table

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert
from database import async_session_factory, async_engine
from models import metadata_obj, products_table


# def create_tables():
#     metadata_obj.drop_all(sync_engine)
#     metadata_obj.create_all(sync_engine)
#
#
# def insert_data(name, link, cur_price, old_price, sale, cur_price_rub, old_price_rub, sale_rub):
#     with sync_engine.connect() as conn:
#         stmt = insert(products_table).values(
#             [
#                 {
#                     "name": name,
#                     "link": link,
#                     "cur_price": cur_price,
#                     "old_price": old_price,
#                     "sale": sale,
#                     "cur_price_rub": cur_price_rub,
#                     "old_price_rub": old_price_rub,
#                     "sale_rub": sale_rub,
#                 }
#             ]
#         )
#         conn.execute(stmt)
#         conn.commit()
#
#
# def select_data(page):
#     row_per_page = 3
#     offset = (page - 1) * row_per_page
#     with sync_engine.connect() as conn:
#         query = select(products_table).limit(row_per_page).offset(offset)
#         result = conn.execute(query)
#         products = result.all()
#         return products

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(metadata_obj.drop_all)
        await conn.run_sync(metadata_obj.create_all)


async def insert_data(name, link, cur_price, old_price, sale, cur_price_rub, old_price_rub, sale_rub):
    async with async_session_factory() as session:
        stmt = insert(products_table).values(
            name=name,
            link=link,
            cur_price=cur_price,
            old_price=old_price,
            sale=sale,
            cur_price_rub=cur_price_rub,
            old_price_rub=old_price_rub,
            sale_rub=sale_rub,
        )
        await session.execute(stmt)
        await session.commit()


async def select_data(page):
    row_per_page = 3
    offset = (page - 1) * row_per_page
    async with async_session_factory() as session:
        query = select(products_table).limit(row_per_page).offset(offset)
        result = await session.execute(query)
        products = result.fetchall()
        return products
