from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8094129723:AAEwl-aELZ0Elxsn_UWNMVHlm2dfium72g4"

def main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("🎸 Табы", callback_data="tabs")],
        [InlineKeyboardButton("💎 Бесплатные табы", callback_data="free")],
        [InlineKeyboardButton("ℹ️ Обо мне", callback_data="about")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, _context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(
            "Привет! Снизу можешь выбрать интересующие тебя табы 👇",
            reply_markup=main_menu_keyboard()
        )
    elif update.message:
        await update.message.reply_text(
            "Привет! Снизу можешь выбрать интересующие тебя табы 👇",
            reply_markup=main_menu_keyboard()
        )


async def button_handler(update: Update, _context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if not query:
        return

    await query.answer()
    data = query.data

    if data == "tabs":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Дыхание - Наутилус – 300₽", callback_data="buy_tab1")],
            [InlineKeyboardButton("Повод - Моргенштерн – 150₽", callback_data="buy_tab2")],
            [InlineKeyboardButton("Кино - Macan – 200₽", callback_data="buy_tab3")],
            [InlineKeyboardButton("Бобр - Слава Скрипка – 200₽", callback_data="buy_tab4")],
            [InlineKeyboardButton("Кукла Колдуна - КиШ – 150₽", callback_data="buy_tab5")],
            [InlineKeyboardButton("Половинка - Танцы Минус – 150₽", callback_data="buy_tab6")],
            [InlineKeyboardButton("Ты меня не ищи - Вирус – 150₽", callback_data="buy_tab7")],
            [InlineKeyboardButton("Туман - Сектор Газа – 100₽", callback_data="buy_tab8")],
            [InlineKeyboardButton("Alors on dance – 150₽", callback_data="buy_tab9")],
            [InlineKeyboardButton("⬅ Назад", callback_data="back")]
        ])
        await query.edit_message_text("🎸 Категория: Табы\nВыберите табулатуру из предложенных:", reply_markup=keyboard)

    elif data == "free":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Smells Like Teen Spirit - Nirvana", callback_data="free1")],
            [InlineKeyboardButton("Батарейка - Жуки", callback_data="free2")],
            [InlineKeyboardButton("Барабулька - Вова Солодков", callback_data="free3")],
            [InlineKeyboardButton("Sigma Boy", callback_data="free4")],
            [InlineKeyboardButton("Slay! Phonk", callback_data="free5")],
            [InlineKeyboardButton("Мама - первое слово", callback_data="free6")],
            [InlineKeyboardButton("⬅ Назад", callback_data="back")]
        ])
        await query.edit_message_text("💎 Бесплатные табы:\nВыберите:", reply_markup=keyboard)

    elif data == "about":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅ Назад", callback_data="back")]
        ])
        # <-- УБРАЛ parse_mode, чтобы избежать ошибок разбора разметки.
        about_text = (
            "ℹ️ Обо мне\n\n"
            "Привет! Меня зовут Егор, я гитарист и делаю фингерстайл аранжировки известных песен.\n"
            "🎸 Играю более 3-x лет\n"
            "🔥 Делаю уникальные аранжировки на популярные песни.\n"
            "📩 Пиши по любым вопросам, стараюсь отвечать): @losos111k"
        )
        await query.edit_message_text(about_text, reply_markup=keyboard)

    elif data == "back":
        await start(update, _context)

    elif data.startswith("buy_"):
        await query.edit_message_text("🛒 Чтобы купить аранжировку — напишите админу: @losos111k \n Стараюсь отвечать как можно быстрее)")

    elif data == "free1":
        await query.edit_message_text("🎁 Бесплатные табы можешь скачать в моем ТГК:\n https://t.me/losos11k")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
