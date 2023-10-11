from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
    Updater,
)
import logging
from urbanagent import agentQuery
import os
from dotenv import load_dotenv

load_dotenv()


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

# Token from @BotFather on Telegram

TOKEN = os.environ.get("TELE_TOKEN")


async def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(f"Hello {user.first_name}!")


async def echo(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""
    text = update.message.text
    answer = agentQuery(text)
    await update.message.reply_text(answer)


if __name__ == "__main__":
    """Start the bot."""

    app = ApplicationBuilder().token(TOKEN).build()

    # Command Handlers
    app.add_handler(CommandHandler("start", start))

    # Message Handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()
