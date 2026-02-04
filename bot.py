import os
import sys
import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ==================== НАСТРОЙКИ ====================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Токен из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    logger.error("❌ BOT_TOKEN not found!")
    logger.info("👉 Render → Environment → Add Variable: BOT_TOKEN=your_token")
    sys.exit(1)

# Ваш ID для получения сообщений (узнать в @userinfobot)
ADMIN_ID = "ВАШ_ID_ТЕЛЕГРАМ"  # ⚠️ ЗАМЕНИТЕ НА СВОЙ!

# ==================== ИНИЦИАЛИЗАЦИЯ ====================
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# ==================== КЛАВИАТУРЫ ====================
def get_main_keyboard():
    """Клавиатура с основными командами"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📝 Создать заказ", callback_data="order")],
        [InlineKeyboardButton(text="📊 Статус заказа", callback_data="status")],
        [InlineKeyboardButton(text="💰 Тарифы", callback_data="tariff")],
        [InlineKeyboardButton(text="💳 Баланс", callback_data="balance")],
        [InlineKeyboardButton(text="👨‍💼 Поддержка", callback_data="support")],
        [InlineKeyboardButton(text="❓ FAQ", callback_data="faq")]
    ])

def get_support_keyboard():
    """Клавиатура для поддержки"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📞 Связаться с менеджером", callback_data="contact_manager")],
        [InlineKeyboardButton(text="🛠️ Техподдержка", callback_data="tech_support")],
        [InlineKeyboardButton(text="💰 Финансы", callback_data="finance")],
        [InlineKeyboardButton(text="🚨 Жалоба", callback_data="complaint")]
    ])

# ==================== КОМАНДЫ ====================

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Главное меню"""
    await message.answer(
        "🚀 <b>Добро пожаловать!</b>\n\n"
        "Я ваш помощник. Выберите нужный вариант:",
        reply_markup=get_main_keyboard()
    )

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    """Помощь"""
    await message.answer(
        "📚 <b>Помощь и инструкции</b>\n\n"
        
        "<b>Основные команды:</b>\n"
        "/start - Главное меню\n"
        "/help - Эта справка\n"
        "/order - Создать заказ\n"
        "/status - Статус заказа\n"
        "/tariff - Тарифы и цены\n"
        "/support - Связь с менеджером\n"
        "/balance - Баланс и оплата\n"
        "/history - История заказов\n"
        "/promo - Акции и промокоды\n"
        "/rules - Правила использования\n"
        "/contact - Контакты компании\n"
        "/report - Пожаловаться\n"
        "/faq - Частые вопросы\n\n"
        
        "<b>Для быстрой помощи:</b> /support"
    )

@dp.message(Command("support"))
async def cmd_support(message: types.Message):
    """Поддержка"""
    await message.answer(
        "👨‍💼 <b>Служба поддержки</b>\n\n"
        "Выберите тип обращения:",
        reply_markup=get_support_keyboard()
    )

@dp.message(Command("order"))
async def cmd_order(message: types.Message):
    """Создание заказа"""
    await message.answer(
        "📝 <b>Создание заказа</b>\n\n"
        "Для создания заказа:\n"
        "1. Опишите что вам нужно\n"
        "2. Укажите сроки\n"
        "3. Напишите ваш бюджет\n\n"
        "Просто отправьте сообщение с деталями заказа."
    )

@dp.message(Command("status"))
async def cmd_status(message: types.Message):
    """Статус заказа"""
    await message.answer(
        "📊 <b>Проверка статуса</b>\n\n"
        "Для проверки статуса заказа напишите:\n"
        "• Номер заказа\n"
        "• Или ваше имя/контакт\n\n"
        "Отправьте номер заказа или контактные данные."
    )

@dp.message(Command("tariff"))
async def cmd_tariff(message: types.Message):
    """Тарифы"""
    await message.answer(
        "💰 <b>Тарифы и цены</b>\n\n"
        "<b>Базовый:</b> 1000 руб. - базовая настройка\n"
        "<b>Стандарт:</b> 2500 руб. - полная настройка\n"
        "<b>Профи:</b> 5000 руб. - настройка + обучение\n\n"
        "Подробнее: /support"
    )

@dp.message(Command("balance"))
async def cmd_balance(message: types.Message):
    """Баланс"""
    await message.answer(
        "💳 <b>Баланс и оплата</b>\n\n"
        "Текущий баланс: <b>0 руб.</b>\n\n"
        "Для пополнения баланса:\n"
        "1. Напишите сумму пополнения\n"
        "2. Получите реквизиты для оплаты\n"
        "3. После оплаты баланс обновится\n\n"
        "Напишите сумму для пополнения."
    )

@dp.message(Command("history"))
async def cmd_history(message: types.Message):
    """История заказов"""
    await message.answer(
        "📋 <b>История заказов</b>\n\n"
        "Список ваших заказов:\n"
        "1. #001 - Настройка бота (статус: завершено)\n"
        "2. #002 - Консультация (статус: в работе)\n\n"
        "Для деталей по заказу напишите его номер."
    )

@dp.message(Command("promo"))
async def cmd_promo(message: types.Message):
    """Промокоды"""
    await message.answer(
        "🎁 <b>Акции и промокоды</b>\n\n"
        "Действующие промокоды:\n"
        "• WELCOME10 - 10% скидка на первый заказ\n"
        "• SUPPORT20 - 20% скидка на поддержку\n"
        "• BOT25 - 25% скидка на создание бота\n\n"
        "Скидка применяется автоматически."
    )

@dp.message(Command("rules"))
async def cmd_rules(message: types.Message):
    """Правила"""
    await message.answer(
        "📜 <b>Правила использования</b>\n\n"
        "1. Уважительное общение\n"
        "2. Оплата в течение 24 часов\n"
        "3. Возврат - в течение 3 дней\n"
        "4. Конфиденциальность данных\n\n"
        "Полные правила: example.com/rules"
    )

@dp.message(Command("contact"))
async def cmd_contact(message: types.Message):
    """Контакты"""
    await message.answer(
        "📞 <b>Контакты компании</b>\n\n"
        "<b>Телефон:</b> +7 (XXX) XXX-XX-XX\n"
        "<b>Email:</b> support@example.com\n"
        "<b>Сайт:</b> example.com\n"
        "<b>График:</b> Пн-Пт, 9:00-21:00\n\n"
        "Быстрая связь: /support"
    )

@dp.message(Command("report"))
async def cmd_report(message: types.Message):
    """Жалоба"""
    await message.answer(
        "🚨 <b>Пожаловаться на работу</b>\n\n"
        "Опишите проблему подробно:\n"
        "1. Что произошло?\n"
        "2. Когда случилось?\n"
        "3. Кто был задействован?\n"
        "4. Чего ожидали?\n\n"
        "Жалобы рассматриваются в течение 24 часов."
    )

@dp.message(Command("faq"))
async def cmd_faq(message: types.Message):
    """FAQ"""
    await message.answer(
        "❓ <b>Частые вопросы</b>\n\n"
        "<b>Q:</b> Сколько времени занимает настройка?\n"
        "<b>A:</b> От 1 до 3 дней\n\n"
        "<b>Q:</b> Есть ли гарантия?\n"
        "<b>A:</b> 30 дней гарантии\n\n"
        "<b>Q:</b> Как оплатить?\n"
        "<b>A:</b> Картой, переводом, криптой\n\n"
        "Больше вопросов: /support"
    )

# ==================== ОБРАБОТКА КНОПОК ====================

@dp.callback_query(F.data.in_(["order", "status", "tariff", "balance", "support", "faq"]))
async def handle_main_buttons(callback: types.CallbackQuery):
    """Обработка главных кнопок"""
    handlers = {
        "order": cmd_order,
        "status": cmd_status,
        "tariff": cmd_tariff,
        "balance": cmd_balance,
        "support": cmd_support,
        "faq": cmd_faq
    }
    
    if callback.data in handlers:
        await handlers[callback.data](callback.message)
    await callback.answer()

@dp.callback_query(F.data.in_(["contact_manager", "tech_support", "finance", "complaint"]))
async def handle_support_buttons(callback: types.CallbackQuery):
    """Обработка кнопок поддержки"""
    await callback.message.answer(
        "✍️ <b>Опишите ваш вопрос подробно</b>\n\n"
        "Сообщение будет передано соответствующему отделу.\n"
        "Просто напишите ниже ⬇️"
    )
    await callback.answer()

# ==================== ОБРАБОТКА СООБЩЕНИЙ ====================

@dp.message()
async def handle_all_messages(message: types.Message):
    """Обработка всех текстовых сообщений"""
    if message.text and not message.text.startswith('/'):
        
        # Ответ пользователю
        await message.answer(
            "✅ <b>Сообщение получено!</b>\n\n"
            "Оператор ответит в течение 15 минут.\n"
            "Можете добавить дополнительные детали."
        )
        
        # Пересылка администратору (если указан ADMIN_ID)
        if ADMIN_ID and ADMIN_ID != "ВАШ_ID_ТЕЛЕГРАМ":
            try:
                await bot.send_message(
                    ADMIN_ID,
                    f"📨 <b>Новое сообщение</b>\n\n"
                    f"👤 От: @{message.from_user.username or 'нет'}\n"
                    f"📛 Имя: {message.from_user.first_name}\n"
                    f"🆔 ID: {message.from_user.id}\n"
                    f"💬 Текст: {message.text}\n\n"
                    f"<i>Ответьте прямо на это сообщение</i>"
                )
            except Exception as e:
                logger.error(f"Failed to forward message: {e}")

# ==================== ЗАПУСК БОТА ====================
async def main():
    """Запуск бота"""
    logger.info("🤖 Бот запускается...")
    
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"❌ Ошибка: {e}")
    finally:
        logger.info("🛑 Бот остановлен")
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
