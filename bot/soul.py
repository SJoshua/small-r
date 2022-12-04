"""soul of the bot"""
from telegram.ext import ApplicationBuilder, CommandHandler
from bot.utils import logger
from bot.commands import command_handlers


def run(config):
    """run the bot"""
    logger.info("starting bot...")

    application = ApplicationBuilder().token(config["token"]).build()

    for command, handler in command_handlers.items():
        application.add_handler(CommandHandler(command, handler))

    application.run_polling()
