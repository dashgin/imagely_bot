from imagely.domain.config import settings
from imagely.service.remove_background import remove_bg
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = " ".join(context.args).upper()
    print(context.args)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text
    )


async def remove_bg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # get image from last message
    image = update.message.photo[-1].get_file().download_as_bytearray()
    # remove background
    print("Removing background...")
    image = remove_bg(image)
    # send image
    print("Sending image...")
    update.message.reply_photo(image)
    print("Done!")


def run_bot():

    app = ApplicationBuilder().token(settings.TG_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    app.add_handler(CommandHandler("caps", caps))

    app.add_handler(CommandHandler("remove", remove_bg))

    app.run_polling()
