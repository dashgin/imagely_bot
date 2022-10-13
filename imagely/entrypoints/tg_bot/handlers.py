from telegram.ext import Application

from .commands.remove_bg import remove_bg_handler


def setup_handlers(app: Application):
    app.add_handler(remove_bg_handler)
