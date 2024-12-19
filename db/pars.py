import requests
from bs4 import BeautifulSoup
from key import key

# URL
base_url = 'https://m.sila.by/catalog/mobilnye_telefony/page/{}'

# Exchange API
ex_api = f'https://v6.exchangerate-api.com/v6/{key}/latest/BYN'

# Find course
# response = requests.get(ex_api)
# exchange_rates_for_BYN = response.json()['conversion_rates']
# BYN_to_RUB = exchange_rates_for_BYN['RUB']

BYN_to_RUB = 31


def pars_cite(page):
    url = base_url.format(page)

    response = requests.get(url)
    response.encoding = 'windows-1251'
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    product_blocks = soup.find_all('div', class_='tov_prew')

    products = []
    for block in product_blocks:
        # Link
        link_tag = block.find('a', href=True)
        link = link_tag['href'] if link_tag else None

        # Name
        product_name_tag = block.find('a')
        name = product_name_tag.text.strip() if product_name_tag else None

        # Price box
        price_container = block.find('div', class_='price')
        if price_container:
            prices = list(price_container.stripped_strings)

            # cur
            current_price = int(prices[0].replace('.', '', -1))

            if len(prices) == 8:

                # old
                old_price = int(prices[4].replace('.', '', -1))

                # sale
                sale = abs(current_price - old_price)

            else:
                old_price = 0
                sale = 0
        current_price_rub = current_price * BYN_to_RUB
        old_price_rub = old_price * BYN_to_RUB
        sale_rub = sale * BYN_to_RUB
        product = dict()
        product.update({'name': name,
                        'link': link,
                        'cur_price': current_price,
                        'old_price': old_price,
                        'sale': sale,
                        'cur_price_rub': current_price_rub,
                        'old_price_rub': old_price_rub,
                        'sale_rub': sale_rub
                        })
        products.append(product)
    return products
