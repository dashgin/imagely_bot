from telegram.ext import Application

from .commands.extract_text import extract_text_handler
# from .commands.remove_bg import remove_bg_handler


def setup_handlers(app: Application):
    app.add_handler(extract_text_handler)
