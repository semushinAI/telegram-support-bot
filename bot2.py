import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# Токен ВТОРОГО бота
TOKEN = "8569326475:AAFvb2WW41GIaKGzD415Lo8Z4jwyw5xdqi4"

# Проверка токена
if not TOKEN:
    print("❌ ERROR: No token!")
    exit(1)

# Инициализация
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# ==================== КОМАНДЫ ====================

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🤖 <b>Второй бот активирован!</b>\n\n"
        "Это дополнительный бот для:\n"
        "• Автоматизации процессов\n"
        "• Уведомлений\n"
        "• Резервной поддержки\n\n"
        "Команды:\n"
        "/start - информация\n"
        "/help - помощь\n"
        "/notify - тест уведомления\n"
        "/status - статус системы"
    )

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "📚 <b>Помощь по второму боту</b>\n\n"
        "Этот бот может:\n"
        "1. Отправлять уведомления\n"
        "2. Мониторить статусы\n"
        "3. Автоматизировать задачи\n\n"
        "Для настройки функций свяжитесь с разработчиком."
    )

@dp.message(Command("notify"))
async def cmd_notify(message: types.Message):
    """Тестовая команда для уведомлений"""
    await message.answer(
        "🔔 <b>Тестовое уведомление</b>\n\n"
        "Бот работает корректно!\n"
        f"Ваш ID: <code>{message.from_user.id}</code>\n"
        f"Время: {message.date.strftime('%H:%M:%S')}"
    )

@dp.message(Command("status"))
async def cmd_status(message: types.Message):
    """Статус системы"""
    import psutil
    import datetime
    
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    
    await message.answer(
        "📊 <b>Статус системы</b>\n\n"
        f"• CPU: {cpu}%\n"
        f"• Память: {memory}%\n"
        f"• Запущено: {boot_time.strftime('%d.%m.%Y %H:%M')}\n"
        f"• Бот: Активен ✅"
    )

@dp.message(Command("echo"))
async def cmd_echo(message: types.Message):
    """Эхо-команда"""
    if len(message.text) > 6:
        text = message.text[6:]  # Убираем "/echo "
        await message.answer(f"📨 Эхо: {text}")
    else:
        await message.answer("Напишите: /echo ваш текст")

# Обработка всех сообщений
@dp.message()
async def handle_messages(message: types.Message):
    if message.text and not message.text.startswith('/'):
        await message.answer(
            f"✅ Получено: {message.text[:100]}\n\n"
            "Используйте команды:\n"
            "/start - информация\n"
            "/notify - тест уведомления"
        )

# ==================== ЗАПУСК ====================
async def main():
    logging.basicConfig(level=logging.INFO)
    print("🤖 Второй бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
