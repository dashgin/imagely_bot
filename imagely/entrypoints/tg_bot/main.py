from telegram.ext import ApplicationBuilder

from imagely.domain.config import settings
from .handlers import setup_handlers


def run_bot():
    app = ApplicationBuilder().token(settings.TG_BOT_TOKEN).build()
    setup_handlers(app)
    print("Bot is running...")
    print("Press Ctrl+C to stop.")
    app.run_polling()
