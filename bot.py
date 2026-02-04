import os
import sys

# ЯВНАЯ ПРОВЕРКА ТОКЕНА
TOKEN = os.getenv("8468223830:AAG2pFIMyAd7lqW8VtNw6OMqRL9AgyLTLkY")

print("=" * 50)
print("DEBUG INFO:")
print(f"BOT_TOKEN from env: {TOKEN}")
print(f"Type: {type(TOKEN)}")
print("=" * 50)

if not TOKEN:
    print("❌ CRITICAL ERROR: BOT_TOKEN is None or empty!")
    print("👉 You MUST add BOT_TOKEN in Render Variables")
    print("👉 Steps:")
    print("   1. Go to Render Dashboard")
    print("   2. Select your project")
    print("   3. Click 'Environment'")
    print("   4. Add Variable: Key=BOT_TOKEN, Value=your_token")
    sys.exit(1)

if TOKEN == "8468223830:AAHTcQTYvnROnkO_vApWArKiKLDkfecJAVk":
    print("⚠️ WARNING: Using hardcoded token. Add to Render Variables!")
else:
    print(f"✅ Token length: {len(TOKEN)}")

# Только после проверки импортируем aiogram
try:
    from aiogram import Bot, Dispatcher, types
    from aiogram.filters import Command
    from aiogram.enums import ParseMode
    print("✅ Aiogram imported")
except ImportError:
    print("❌ Aiogram not installed. Check requirements.txt")
    sys.exit(1)

# Создаём бота
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("🚀 Бот работает! Напишите /support")

@dp.message(Command("support"))
async def support(msg: types.Message):
    await msg.answer("👨‍💼 Поддержка активна. Опишите проблему.")

async def main():
    print("🤖 Starting bot polling...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
