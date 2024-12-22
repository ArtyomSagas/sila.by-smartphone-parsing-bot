from sqlalchemy import Table, Column, Integer, String, Float, MetaData

metadata_obj = MetaData()

products_table = Table(
    "products",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("link", String),
    Column("cur_price", Float),
    Column("old_price", Float),
    Column("sale", Float),
    Column("cur_price_rub", Float),
    Column("old_price_rub", Float),
    Column("sale_rub", Float),
)
