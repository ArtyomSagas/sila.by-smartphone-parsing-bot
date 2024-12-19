from core import create_tables, insert_data
from pars import pars_cite
# import subprocess
create_tables()
for page in range(1, 32):
    data = pars_cite(page)
    for product in data:
        insert_data(product['name'],
                    product['link'],
                    product['cur_price'],
                    product['old_price'],
                    product['sale'],
                    product['cur_price_rub'],
                    product['old_price_rub'],
                    product['sale_rub']
                    )
# try:
#     subprocess.run([r'F:\SUSU\Parser\venv\Scripts\python.exe', r'F:\SUSU\Parser\bot.py'])
# except KeyboardInterrupt:
#     print('Exit subprocess')