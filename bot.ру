import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("8468223830:AAG2pFIMyAd7lqW8VtNw6OMqRL9AgyLTLkY")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🚀 **Добро пожаловать!**\n\n"
        "📋 **Доступные команды:**\n"
        "/start - Главное меню\n"
        "/help - Помощь и инструкции\n"
        "/order - 📝 Создать заказ\n"
        "/status - 📊 Статус заказа\n"
        "/tariff - 💰 Тарифы и цены\n"
        "/support - 👨‍💼 Связаться с менеджером\n"
        "/balance - 💳 Баланс и оплата\n"
        "/history - 📋 История заказов\n"
        "/promo - 🎁 Акции и промокоды\n"
        "/rules - 📜 Правила использования\n"
        "/contact - 📞 Контакты компании\n"
        "/report - 🚨 Пожаловаться на работу\n"
        "/faq - ❓ Частые вопросы\n\n"
        "Напишите /support для связи с поддержкой!"
    )

@dp.message(Command("support"))
async def cmd_support(message: types.Message):
    await message.answer(
        "👨‍💼 **Служба поддержки**\n\n"
        "Опишите ваш вопрос или проблему прямо здесь.\n"
        "Оператор ответит в течение 15 минут.\n\n"
        "⏱️ Время ответа: 9:00-21:00\n"
        "📬 Просто напишите сообщение ниже ⬇️"
    )

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "📚 **Помощь по использованию:**\n\n"
        "1. /order - создать новый заказ\n"
        "2. /status - проверить статус заказа\n"
        "3. /balance - пополнить баланс\n"
        "4. /support - связаться с менеджером\n"
        "5. /history - история заказов\n\n"
        "Техподдержка: @ваш_логин"
    )

@dp.message()
async def handle_all_messages(message: types.Message):
    if message.text and not message.text.startswith('/'):
        await message.answer(
            f"✅ Сообщение получено!\n"
            f"Оператор скоро ответит.\n\n"
            f"Вы написали: {message.text[:100]}"
        )

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
