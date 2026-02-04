import os
import asyncio
import logging
import datetime
import json
import psutil
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# ==================== НАСТРОЙКИ ====================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Токен ВТОРОГО бота
TOKEN = "8569326475:AAFvb2WW41GIaKGzD415Lo8Z4jwyw5xdqi4"

# Инициализация бота
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Файл для логов
LOG_FILE = "bot_logs.json"

# ==================== ЛОГИРОВАНИЕ ====================
def init_log_file():
    """Создаём файл логов если его нет"""
    try:
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=2)
    except Exception as e:
        logger.error(f"Ошибка создания файла логов: {e}")

def save_log_entry(entry_data):
    """Сохраняем запись в лог"""
    try:
        # Читаем текущие логи
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                logs = json.load(f)
        else:
            logs = []
        
        # Добавляем новую запись
        logs.append(entry_data)
        
        # Сохраняем (максимум 1000 записей)
        if len(logs) > 1000:
            logs = logs[-1000:]
        
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)
        
        logger.info(f"📝 Записано в лог: {entry_data.get('type', 'unknown')}")
        return True
    except Exception as e:
        logger.error(f"❌ Ошибка записи в лог: {e}")
        return False

def create_log_entry(user_data, action_type, content=""):
    """Создаём запись для лога"""
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "user_id": user_data.get('id'),
        "username": user_data.get('username'),
        "first_name": user_data.get('first_name'),
        "type": action_type,
        "content": str(content)[:500],
        "bot": "bot2"
    }

# Инициализируем файл логов
init_log_file()

# ==================== КОМАНДЫ БОТА ====================

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Команда /start - начать"""
    response = (
        "🤖 <b>БОТ #2 АКТИВИРОВАН</b>\n\n"
        "📊 <b>Функции бота:</b>\n"
        "• Запись всех сообщений в лог\n"
        "• Мониторинг системы\n"
        "• Тестирование связи\n"
        "• Полезные команды\n\n"
        "<b>📋 Доступные команды:</b>\n"
        "/start - начать\n"
        "/help - справка\n"
        "/id - ваш Chat ID\n"
        "/test - тест связи\n"
        "/site - ссылки на сайт\n"
        "/status - статус системы\n"
        "/time - текущее время\n"
        "/logs - посмотреть логи\n\n"
        "<i>Все сообщения записываются в файл bot_logs.json</i>"
    )
    
    await message.answer(response)
    
    # Логируем команду
    save_log_entry(create_log_entry(
        {
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name
        },
        "command",
        "/start"
    ))

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    """Команда /help - справка"""
    help_text = (
        "📚 <b>СПРАВКА ПО КОМАНДАМ</b>\n\n"
        
        "<b>📋 Основные команды:</b>\n"
        "/start - информация о боте\n"
        "/help - эта справка\n\n"
        
        "<b>👤 Информационные:</b>\n"
        "/id - ваш Chat ID и информация\n"
        "/time - текущее время\n"
        "/status - статус системы\n\n"
        
        "<b>🔧 Тестовые:</b>\n"
        "/test - тест связи с ботом\n"
        "/site - полезные ссылки\n"
        "/logs - посмотреть логи (последние 5)\n\n"
        
        "<b>💾 Логирование:</b>\n"
        "• Все команды записываются\n"
        "• Все сообщения сохраняются\n"
        "• Логи хранятся в bot_logs.json\n\n"
        
        "<i>Бот работает на базе aiogram 3.x</i>"
    )
    
    await message.answer(help_text)
    
    save_log_entry(create_log_entry(
        {
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name
        },
        "command",
        "/help"
    ))

@dp.message(Command("id"))
async def cmd_id(message: types.Message):
    """Команда /id - ваш Chat ID"""
    now = datetime.datetime.now()
    
    response = (
        "🆔 <b>ВАШИ ИДЕНТИФИКАТОРЫ</b>\n\n"
        f"<b>👤 User ID:</b> <code>{message.from_user.id}</code>\n"
        f"<b>💬 Chat ID:</b> <code>{message.chat.id}</code>\n"
        f"<b>📛 Имя:</b> {message.from_user.first_name or 'Не указано'}\n"
        f"<b>📛 Фамилия:</b> {message.from_user.last_name or 'Не указана'}\n"
        f"<b>📱 Username:</b> @{message.from_user.username or 'нет'}\n"
        f"<b>🌐 Язык:</b> {message.from_user.language_code or 'Не указан'}\n"
        f"<b>⏰ Время запроса:</b> {now.strftime('%H:%M:%S')}\n"
        f"<b>📅 Дата:</b> {now.strftime('%d.%m.%Y')}\n\n"
        "<i>Сохраните эти данные для обращения в поддержку</i>"
    )
    
    await message.answer(response)
    
    save_log_entry(create_log_entry(
        {
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name
        },
        "command",
        "/id"
    ))

@dp.message(Command("test"))
async def cmd_test(message: types.Message):
    """Команда /test - тест связи"""
    start_time = datetime.datetime.now()
    msg = await message.answer("🔄 <b>Тестирование связи...</b>")
    end_time = datetime.datetime.now()
    
    response_time = (end_time - start_time).total_seconds() * 1000
    
    response = (
        "✅ <b>ТЕСТ СВЯЗИ ПРОЙДЕН</b>\n\n"
        f"<b>🏓 Результаты теста:</b>\n"
        f"• Статус: <b>УСПЕШНО</b>\n"
        f"• Время ответа: <b>{response_time:.0f} мс</b>\n"
        f"• Бот: <b>АКТИВЕН</b>\n"
        f"• Дата: {end_time.strftime('%d.%m.%Y')}\n"
        f"• Время: {end_time.strftime('%H:%M:%S')}\n\n"
        "<i>Связь с сервером установлена и работает стабильно</i>"
    )
    
    await msg.edit_text(response)
    
    save_log_entry(create_log_entry(
        {
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name
        },
        "command",
        "/test"
    ))

@dp.message(Command("site"))
async def cmd_site(message: types.Message):
    """Команда /site - ссылки на сайт"""
    sites = (
        "🌐 <b>ПОЛЕЗНЫЕ ССЫЛКИ</b>\n\n"
        
        "<b>📊 Мониторинг и логи:</b>\n"
        "• <a href='https://render.com'>Render.com</a> - хостинг бота\n"
        "• <a href='https://github.com'>GitHub.com</a> - исходный код\n"
        "• <a href='https://cloud.google.com'>Google Cloud</a> - облако\n\n"
        
        "<b>📚 Документация:</b>\n"
        "• <a href='https://docs.aiogram.dev'>Aiogram Docs</a> - документация\n"
        "• <a href='https://core.telegram.org/bots/api'>Telegram API</a> - API\n"
        "• <a href='https://python.org'>Python.org</a> - Python\n\n"
        
        "<b>🛠️ Инструменты:</b>\n"
        "• <a href='https://jsonformatter.org'>JSON Formatter</a> - форматирование\n"
        "• <a href='https://crontab.guru'>CronTab Guru</a> - планировщик\n\n"
        
        "<i>Все переходы по ссылкам логируются</i>"
    )
    
    await message.answer(sites, disable_web_page_preview=True)
    
    save_log_entry(create_log_entry(
        {
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name
        },
        "command",
        "/site"
    ))

@dp.message(Command("status"))
async def cmd_status(message: types.Message):
    """Команда /status - статус системы"""
    try:
        # Получаем информацию о системе
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.datetime.now() - boot_time
        
        # Форматируем аптайм
        days = uptime.days
        hours, remainder = divmod(uptime.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        response = (
            "📊 <b>СТАТУС СИСТЕМЫ</b>\n\n"
            
            "<b>💻 Процессор:</b>\n"
            f"• Загрузка: <b>{cpu_percent}%</b>\n"
            f"• Ядра: <b>{psutil.cpu_count()}</b>\n\n"
            
            "<b>🧠 Память:</b>\n"
            f"• Использовано: <b>{memory.percent}%</b>\n"
            f"• Всего: <b>{memory.total // (1024**3)} ГБ</b>\n"
            f"• Свободно: <b>{memory.available // (1024**3)} ГБ</b>\n\n"
            
            "<b>💾 Диск:</b>\n"
            f"• Использовано: <b>{disk.percent}%</b>\n"
            f"• Свободно: <b>{disk.free // (1024**3)} ГБ</b>\n\n"
            
            "<b>⏱️ Время работы:</b>\n"
            f"• Запущена: <b>{boot_time.strftime('%d.%m.%Y %H:%M')}</b>\n"
            f"• Работает: <b>{days}д {hours}ч {minutes}м {seconds}с</b>\n\n"
            
            "<b>🐍 Python:</b>\n"
            f"• Версия: <b>{sys.version.split()[0]}</b>\n"
            f"• Платформа: <b>{sys.platform}</b>\n\n"
            
            "<i>Система работает стабильно ✅</i>"
        )
        
        await message.answer(response)
        
    except Exception as e:
        error_response = (
            "❌ <b>ОШИБКА ПОЛУЧЕНИЯ СТАТУСА</b>\n\n"
            f"<i>Техническая информация:</i>\n"
            f"Ошибка: {str(e)[:100]}\n\n"
            "Попробуйте позже или обратитесь в поддержку"
        )
        await message.answer(error_response)
    
    save_log_entry(create_log_entry(
        {
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name
        },
        "command",
        "/status"
    ))

@dp.message(Command("time"))
async def cmd_time(message: types.Message):
    """Команда /time - текущее время"""
    now = datetime.datetime.now()
    
    # Разные форматы времени
    formats = {
        "Дата и время": now.strftime("%d.%m.%Y %H:%M:%S"),
        "Только дата": now.strftime("%d %B %Y"),
        "Только время": now.strftime("%H:%M:%S"),
        "ISO формат": now.isoformat(),
        "День недели": ["Понедельник", "Вторник", "Среда", "Четверг", 
                       "Пятница", "Суббота", "Воскресенье"][now.weekday()],
        "Неделя года": f"Неделя {now.isocalendar()[1]}",
        "Таймстамп": str(int(now.timestamp()))
    }
    
    response_lines = ["⏰ <b>ТЕКУЩЕЕ ВРЕМЯ</b>\n"]
    
    for label, value in formats.items():
        response_lines.append(f"<b>{label}:</b> {value}")
    
    response_lines.append("\n<i>Время сервера (Render.com)</i>")
    
    await message.answer("\n".join(response_lines))
    
    save_log_entry(create_log_entry(
        {
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name
        },
        "command",
        "/time"
    ))

@dp.message(Command("logs"))
async def cmd_logs(message: types.Message):
    """Команда /logs - посмотреть логи"""
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                logs = json.load(f)
            
            if logs:
                # Берем последние 5 записей
                recent_logs = logs[-5:] if len(logs) >= 5 else logs
                
                response_lines = ["📋 <b>ПОСЛЕДНИЕ 5 ЗАПИСЕЙ В ЛОГЕ:</b>\n\n"]
                
                for i, log in enumerate(recent_logs, 1):
                    time_str = datetime.datetime.fromisoformat(
                        log['timestamp']
                    ).strftime('%H:%M')
                    
                    user_info = f"{log.get('first_name', '?')}"
                    if log.get('username'):
                        user_info += f" (@{log['username']})"
                    
                    response_lines.append(
                        f"{i}. <b>{time_str}</b> | {user_info}\n"
                        f"   Тип: <i>{log.get('type', 'unknown')}</i>\n"
                        f"   Содержимое: {log.get('content', '')[:50]}...\n"
                    )
                
                response_lines.append(
                    f"\n<i>Всего записей в логе: {len(logs)}</i>"
                )
                
                await message.answer("\n".join(response_lines))
            else:
                await message.answer("📭 <b>Логи пусты</b>\n\nПока нет записей в лог-файле.")
        else:
            await message.answer("❌ <b>Файл логов не найден</b>")
    
    except Exception as e:
        await message.answer(f"❌ <b>Ошибка чтения логов:</b>\n{str(e)}")
    
    save_log_entry(create_log_entry(
        {
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name
        },
        "command",
        "/logs"
    ))

# ==================== ОБРАБОТКА ВСЕХ СООБЩЕНИЙ ====================
@dp.message()
async def handle_all_messages(message: types.Message):
    """Обработка ВСЕХ сообщений (не команд)"""
    
    # Отвечаем пользователю
    response = (
        "💬 <b>СООБЩЕНИЕ ПОЛУЧЕНО</b>\n\n"
        f"<i>Ваше сообщение сохранено в лог</i>\n\n"
        f"📝 <b>Текст:</b> {message.text[:150]}\n"
        f"👤 <b>От:</b> {message.from_user.first_name or 'Пользователь'}\n"
        f"⏰ <b>Время:</b> {message.date.strftime('%H:%M:%S')}\n\n"
        "Используйте /help для списка команд"
    )
    
    await message.answer(response)
    
    # Логируем сообщение
    save_log_entry(create_log_entry(
        {
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name
        },
        "message",
        message.text
    ))

# ==================== ЗАПУСК БОТА ====================
async def main():
    """Запуск бота"""
    logger.info("🚀 Запуск второго бота (с логированием)...")
    logger.info(f"📁 Файл логов: {LOG_FILE}")
    logger.info(f"🤖 Токен: {TOKEN[:10]}...")
    
    try:
        # Удаляем старый вебхук
        await bot.delete_webhook(drop_pending_updates=True)
        logger.info("✅ Вебхук удалён")
        
        # Запускаем поллинг
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.error(f"❌ Критическая ошибка запуска: {e}")
    
    finally:
        logger.info("🛑 Бот остановлен")
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
