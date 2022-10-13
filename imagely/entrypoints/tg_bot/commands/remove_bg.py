from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

from imagely.service.remove_background import remove_bg


async def removebg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id = update.message.photo[-1].file_id
    file = await context.bot.get_file(file_id)
    img = await file.download_as_bytearray()
    img = remove_bg(img)
    await context.bot.send_document(
        chat_id=update.effective_chat.id,
        document=img,
        filename="removed_file.png",
    )


remove_bg_handler = MessageHandler(filters.PHOTO, removebg)
