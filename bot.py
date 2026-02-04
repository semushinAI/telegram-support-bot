import os
import sys
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode

# ==================== НАСТРОЙКА ЛОГГИНГА ====================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ==================== ПОЛУЧЕНИЕ ТОКЕНА ====================
# Токен должен быть в переменных окружения Render!
TOKEN = os.getenv("BOT_TOKEN")

# Проверяем наличие токена
if not TOKEN:
    logger.error("❌ BOT_TOKEN not found in environment variables!")
    logger.info("👉 How to fix:")
    logger.info("1. Go to Render Dashboard")
    logger.info("2. Select your project")
    logger.info("3. Click 'Environment' tab")
    logger.info("4. Add Variable: Key=BOT_TOKEN, Value=your_token_from_@BotFather")
    sys.exit(1)

logger.info(f"✅ Token loaded successfully (length: {len(TOKEN)})")

# ==================== ИНИЦИАЛИЗАЦИЯ БОТА ====================
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
logger.info("✅ Bot initialized")

# ==================== КОМАНДЫ ====================

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    logger.info(f"User {message.from_user.id} used /start")
    
    await message.answer(
        "🚀 <b>Добро пожаловать!</b>\n\n"
        
        "📋 <b>Доступные команды:</b>\n"
        "/start - Главное меню\n"
        "/help - 📚 Помощь и инструкции\n"
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
        
        "<i>Напишите /support для связи с поддержкой</i>"
    )

@dp.message(Command("support"))
async def cmd_support(message: types.Message):
    """Обработчик команды /support"""
    logger.info(f"User {message.from_user.id} requested support")
    
    await message.answer(
        "👨‍💼 <b>Служба поддержки</b>\n\n"
        
        "Опишите ваш вопрос или проблему прямо здесь.\n"
        "Оператор ответит в ближайшее время.\n\n"
        
        "⏱️ <b>Время ответа:</b> 15-30 минут\n"
        "🕐 <b>Рабочие часы:</b> 9:00-21:00\n\n"
        
        "<i>Просто напишите ваше сообщение ниже ⬇️</i>"
    )

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    """Обработчик команды /help"""
    await message.answer(
        "📚 <b>Помощь и инструкции</b>\n\n"
        
        "1. <b>Создать заказ:</b> /order\n"
        "2. <b>Проверить статус:</b> /status\n"
        "3. <b>Пополнить баланс:</b> /balance\n"
        "4. <b>История заказов:</b> /history\n"
        "5. <b>Связаться с менеджером:</b> /support\n"
        "6. <b>Частые вопросы:</b> /faq\n\n"
        
        "<i>Для срочной помощи пишите в поддержку: /support</i>"
    )

# Обработка текстовых сообщений (для поддержки)
@dp.message()
async def handle_text_messages(message: types.Message):
    """Обработка всех текстовых сообщений"""
    if message.text and not message.text.startswith('/'):
        logger.info(f"Message from {message.from_user.id}: {message.text[:50]}...")
        
        # Простое эхо для теста
        await message.answer(
            f"✅ <b>Сообщение получено!</b>\n\n"
            f"Оператор скоро с вами свяжется.\n\n"
            f"<i>Вы написали:</i> {message.text[:200]}"
        )

# ==================== ЗАПУСК БОТА ====================
async def main():
    """Основная функция запуска бота"""
    logger.info("🤖 Starting Telegram bot...")
    
    try:
        # Удаляем вебхук если был
        await bot.delete_webhook(drop_pending_updates=True)
        
        # Запускаем поллинг
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"❌ Bot stopped with error: {e}")
    finally:
        logger.info("🛑 Bot stopped")
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
