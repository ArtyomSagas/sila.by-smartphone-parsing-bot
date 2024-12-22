from core import create_tables, insert_data
from pars import pars_site
import subprocess
import asyncio


async def main():
    await create_tables()

    for page in range(1, 32):
        data = pars_site(page)
        for product in data:
            await insert_data(product['name'],
                              product['link'],
                              product['cur_price'],
                              product['old_price'],
                              product['sale'],
                              product['cur_price_rub'],
                              product['old_price_rub'],
                              product['sale_rub']
                              )

    try:
        process = await asyncio.create_subprocess_exec(
            'python', 'bot.py',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if process.returncode == 0:
            print(f"Bot output:\n{stdout.decode()}")
        else:
            print(f"Bot error:\n{stderr.decode()}")

    except KeyboardInterrupt:
        print("Exit subprocess")

if __name__ == "__main__":
    asyncio.run(main())
