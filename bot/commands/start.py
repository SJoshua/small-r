"""command - start"""
from telegram import Update
from telegram.ext import ContextTypes

from bot.utils import logger


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """start command"""
    assert update.effective_chat
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, this is Small R.")
