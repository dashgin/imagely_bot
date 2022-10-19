import io

from imagely.service.extract_text import extract_text
from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters


async def extract(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = update.message.photo[-1].file_id
    file = await context.bot.get_file(file_id)
    out = io.BytesIO()
    img = await file.download(out=out)
    text = extract_text(img)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )


extract_text_handler = MessageHandler(filters.PHOTO, extract)
