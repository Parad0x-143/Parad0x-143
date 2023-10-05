import telegram
from telegram.ext import Updater, MessageHandler

# Replace 'YOUR_API_TOKEN' with the token you received from BotFather
API_TOKEN = '6108248549:AAEe9VC1Tt_-O_AZYg9W28UdnyEQfAvSBU0'

# Create an updater and pass in your API token
updater = Updater(token=API_TOKEN, use_context=True)

# Define a function to handle incoming text messages
def reply(update, context):
    # Get the user's message
    user_message = Hi

    # Your auto-reply message
    auto_reply = "Thank you for your message. I am a simple bot."

    # Send the auto-reply
    update.message.reply_text(auto_reply)

# Create a message handler and pass it your reply function
message_handler = MessageHandler(Filters.text & ~Filters.command, reply)

# Add the message handler to your updater
updater.dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
updater.idle()
