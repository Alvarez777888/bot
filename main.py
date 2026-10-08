import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)


BOT_TOKEN = "8870486445:AAEcfROO1xxNTFaAomTd3kLIfqeeuzmhu84"   
VPN_REF_LINK = "https://t.me/KrevetkaVpn666bot?start=71TDXL7V"


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔐 Получить ускоритель интернета", url=VPN_REF_LINK)],
        [InlineKeyboardButton(text="✅ Я запустил ускоритель интернета", callback_data="done")],
    ])


@dp.message(CommandStart())
async def start(message: Message):
    name = message.from_user.first_name or "друг"
    await message.answer(
        f"👋 Привет, {name}!\n\n"
        "🚀 Нажми кнопку ниже, чтобы получить доступ к ускорителю 👇\n\n"
        "❗️ Важно: после перехода обязательно нажми <b>«Запустить»</b> в VPN-боте, "
        "иначе доступ не активируется.",
        reply_markup=kb(),
        parse_mode="HTML",
    )


@dp.callback_query(F.data == "done")
async def done(cb: CallbackQuery):
    await cb.answer("Отлично! 🎉 VPN-бот должен был открыться", show_alert=True)
    await cb.message.answer(
        "Если VPN-бот не открылся — нажми кнопку ещё раз 👇",
        reply_markup=kb(),
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
