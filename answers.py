from core import select_data
start_answer = 'Здравствуйте, я готов помочь вам с переводом цен на смартфоны с белорусского сайта sila.by'


async def run_answer(page_number):
    data = await select_data(page_number)
    page = ''
    for product in data:
        product_output = f'{"-" * 102}\n' \
                         f'Название: {product[1]}\n' \
                         f'Ссылка: {product[2]}\n' \
                         f'Цена в белорусских рублях: {product[3]}\n' \
                         f'Старая цена в белорусских рублях: {product[4]}\n' \
                         f'Скидка в белорусских рублях: {product[5]}\n' \
                         f'Цена в русских рублях: {product[6]}\n' \
                         f'Старая цена в русских рублях: {product[7]}\n' \
                         f'Скидка в русских рублях: {product[8]}\n' \
                         f'{"-" * 102}\n'
        page += product_output
    return f'Страница: {page_number}\n{page}'