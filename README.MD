# Парсинг бот смартфонов sila.by

## О проекте:

Данный сервис скрапит данные с белорусского сайта sila.by, конвертирует цены с белорусских рублей в русские и сохраняет
их в базу данных. Обработанные данные доступны через Telegram-бота, который предоставляет интерфейс для взаимодействия
с данными.

## Функционал:

- Скрапинг информации с сайта sila.by.
- Конвертация валют.
- Сохранение данных в PostgreSQL v17.
- Взаимодействие с данными через Telegram-бота.

## Технологии:

- **BeautifulSoup**
- **SQLAlchemy**
- **PostgreSQL**
- **Aiogram**
- **Docker**
- **Docker Compose**

## Как запустить:

### 1. Клонируйте репозиторий:

```bash
git clone https://github.com/ArtyomSagas/sila.by-smartphone-parsing-bot.git
```

### 2. Создайте `.env` файл с параметрами окружения:

```env
DB_HOST=localhost
DB_USER=postgres
DB_PASS=postgres
DB_NAME=products
DB_PORT=5432
BOT_TOKEN=ваш_токен_бота
API_KEY=ваш_ключ_от https://app.exchangerate-api.com/
```

### 3. Запустите сервис:

- Запустите build.sh

## Автор

### Сафонов Артём: https://github.com/ArtyomSagas
