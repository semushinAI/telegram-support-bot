# Telegram Support Bot

Бот для поддержки клиентов с полным набором команд.

## Команды бота:
- /start - Главное меню
- /support - Связь с менеджером
- /order - Создать заказ
- /status - Статус заказа
- /balance - Баланс и оплата
- /history - История заказов
- /help - Помощь и инструкции

## Развертывание

### Railway
1. Нажмите кнопку:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/telegram-bot)

2. Добавьте переменную `BOT_TOKEN` с токеном бота

### Render
1. Создайте новый Web Service
2. Подключите этот репозиторий
3. Добавьте переменные окружения

## Локальный запуск
```bash
pip install -r requirements.txt
python bot.py
