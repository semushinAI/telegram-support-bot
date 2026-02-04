import os
import sys
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties  # ← ДОБАВЬТЕ ЭТО

# ==================== НАСТРОЙКА ЛОГГИНГА ====================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ==================== ПОЛУЧЕНИЕ ТОКЕНА ====================
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    logger.error("❌ BOT_TOKEN not found!")
    logger.info("👉 Add in Render: Environment → Add Variable")
    logger.info("👉 Key: BOT_TOKEN, Value: your_token")
    sys.exit(1)

logger.info(f"✅ Token loaded (length: {len(TOKEN)})")

# ==================== ИНИЦИАЛИЗАЦИЯ БОТА (ИСПРАВЛЕНО) ====================
# НОВЫЙ СПОСОБ для aiogram 3.7+
bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # ← ТАК ТЕПЕРЬ
)
dp = Dispatcher()
logger.info("✅ Bot initialized")

# ==================== КОМАНДЫ ====================

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    await message.answer(
        "🚀 <b>Добро пожаловать!</b>\n\n"
        
        "📋 <b>Доступные команды:</b>\n"
        "/start - Главное меню\n"
        "/help - 📚 Помощь\n"
        "/order - 📝 Создать заказ\n"
        "/status - 📊 Статус\n"
        "/tariff - 💰 Тарифы\n"
        "/support - 👨‍💼 Связь с менеджером\n"
        "/balance - 💳 Баланс\n"
        "/history - 📋 История\n"
        "/promo - 🎁 Промокоды\n"
        "/rules - 📜 Правила\n"
        "/contact - 📞 Контакты\n"
        "/report - 🚨 Жалоба\n"
        "/faq - ❓ Частые вопросы\n\n"
        
        "<i>Напишите /support для поддержки</i>"
    )

@dp.message(Command("support"))
async def cmd_support(message: types.Message):
    """Обработчик команды /support"""
    await message.answer(
        "👨‍💼 <b>Поддержка</b>\n\n"
        "Опишите ваш вопрос прямо здесь.\n"
        "Оператор ответит в течение 15 минут.\n\n"
        "<i>Просто напишите сообщение ниже ⬇️</i>"
    )

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    """Обработчик команды /help"""
    await message.answer(
        "📚 <b>Помощь</b>\n\n"
        "1. /order - создать заказ\n"
        "2. /status - проверить статус\n"
        "3. /balance - пополнить баланс\n"
        "4. /support - связь с менеджером\n"
        "5. /history - история заказов\n\n"
        "<i>Для помощи: /support</i>"
    )

@dp.message()
async def handle_all_messages(message: types.Message):
    """Обработка всех сообщений"""
    if message.text and not message.text.startswith('/'):
        await message.answer(
            f"✅ <b>Сообщение получено!</b>\n\n"
            f"Оператор скоро ответит.\n\n"
            f"<i>Вы:</i> {message.text[:100]}"
        )

# ==================== ЗАПУСК БОТА ====================
async def main():
    """Основная функция запуска бота"""
    logger.info("🤖 Starting bot...")
    
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"❌ Error: {e}")
    finally:
        await bot.session.close()
        logger.info("🛑 Bot stopped")

if __name__ == "__main__":
    asyncio.run(main())
