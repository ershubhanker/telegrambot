from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters, ConversationHandler

TOKEN = "6594776797:AAHfT8jKuIlZVXeNswQDPnMtiJoyI8ex39c"
PHONE_NUMBER = range(1)
def start(update: Update, context: CallbackContext) -> None:
    # Request the user's phone number or location immediately using a custom keyboard
    contact_keyboard = KeyboardButton(text="Send Contact", request_contact=True)
    custom_keyboard = [[contact_keyboard]]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
    update.message.reply_text("Please choose an option:", reply_markup=reply_markup)
    keyboard = [
        [InlineKeyboardButton("Buy", callback_data='buy')],
        [InlineKeyboardButton("Order Status", callback_data='order_status')],
        [InlineKeyboardButton("Cancel Order", callback_data='cancel_order')],
        [InlineKeyboardButton("Support", callback_data='support')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to Our Service! Choose an option:', reply_markup=reply_markup)

def help(update: Update,context: CallbackContext):
    update.message.reply_text(
        """
        /start -> Welcome to the channel
        /help -> This is the Particular Changes
        /buy -> To see the options to buy
        /order_status -> To see the status of the order you have purchased
        /cancel-status -> To see the status of the order and cancell the order
        /support -> To help and solve your queries
        """
    )
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'buy':
        keyboard = [
            [InlineKeyboardButton("Documents", callback_data='documents')],
            [InlineKeyboardButton("Physical_ID", callback_data='physical_id')],
            [InlineKeyboardButton("Profiles", callback_data='profiles')],
            [InlineKeyboardButton("Services", callback_data='services')],
            [InlineKeyboardButton("Back", callback_data='start')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Select a category:", reply_markup=reply_markup)

    elif query.data == 'services':
        keyboard = [
            [InlineKeyboardButton("Photoshop Services", url='https://www.youtube.com/')],
            [InlineKeyboardButton("Food Services", url='https://www.youtube.com/')],
            [InlineKeyboardButton("Hotel Services", url='https://www.youtube.com/')],
            [InlineKeyboardButton("Back", callback_data='buy')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Select a service:", reply_markup=reply_markup)

    elif query.data == 'documents':
        keyboard = [
            [InlineKeyboardButton("PAN Document", url='https://incometaxindia.gov.in/Documents/documents-required-for-pan.pdf')],
            [InlineKeyboardButton("Aadhaar Document", url='https://uidai.gov.in/images/commdoc/valid_documents_list.pdf')],
            [InlineKeyboardButton("NCERT Books", url='https://ncert.nic.in/textbook.php?jesc1=5-16')],
            [InlineKeyboardButton("Back", callback_data='buy')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Available Documents:", reply_markup=reply_markup)

    elif query.data == 'physical_id':
        keyboard = [
            [InlineKeyboardButton("ID: l8x4y06ilaqr", callback_data='noop')],
            [InlineKeyboardButton("ID: j7ugh3xzc7bx", callback_data='noop')],
            [InlineKeyboardButton("ID: z6dabvf58osq", callback_data='noop')],
            [InlineKeyboardButton("Back", callback_data='buy')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Physical IDs:", reply_markup=reply_markup)

    elif query.data == 'profiles':
        keyboard = [
            [InlineKeyboardButton("William Gates", url='https://www.linkedin.com/in/williamhgates')],
            [InlineKeyboardButton("Mark Ramsey", url='https://www.linkedin.com/in/mark-ramsey-7b745747/')],
            [InlineKeyboardButton("Imran Shaikh", url='https://www.linkedin.com/in/imran--shaikh/')],
            [InlineKeyboardButton("Back", callback_data='buy')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Professional Profiles:", reply_markup=reply_markup)

def get_phone_number(update: Update, context: CallbackContext) -> int:
    user_phone = update.message.contact.phone_number
    print(f"User's phone number: {user_phone}")
    update.message.reply_text(f"Thanks for sharing your phone number: {user_phone}")
    return ConversationHandler.END


def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    phone_number_handler = ConversationHandler(
        entry_points=[CommandHandler('getphonenumber', start)],
        states={PHONE_NUMBER: [MessageHandler(Filters.contact, get_phone_number)]},
        fallbacks=[]
    )
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(phone_number_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()



# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton, ReplyKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters, ConversationHandler

# TOKEN = "6594776797:AAHfT8jKuIlZVXeNswQDPnMtiJoyI8ex39c"

# PHONE_NUMBER = range(1)

# def start(update: Update, context: CallbackContext) -> None:
#     # Request the user's phone number or location immediately using a custom keyboard
#     contact_keyboard = KeyboardButton(text="Send Contact", request_contact=True)
#     custom_keyboard = [[contact_keyboard]]
#     reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
#     update.message.reply_text("Please choose an option:", reply_markup=reply_markup)
# def help(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(
#         """
#         /start -> Welcome to the channel
#         /help -> This is the Particular Changes
#         /buy -> To see the options to buy
#         /order_status -> To see the status of the order you have purchased
#         /cancel-status -> To see the status of the order and cancell the order
#         /support -> To help and solve your queries
#         /getphonenumber -> Request user's phone number
#         """
#     )

# def get_phone_number(update: Update, context: CallbackContext) -> int:
#     user_phone = update.message.contact.phone_number
#     print(f"User's phone number: {user_phone}")
#     update.message.reply_text(f"Thanks for sharing your phone number: {user_phone}")
#     return ConversationHandler.END

# def main() -> None:
#     updater = Updater(TOKEN, use_context=True)

#     # Create a conversation handler for getting phone number
#     phone_number_handler = ConversationHandler(
#         entry_points=[CommandHandler('getphonenumber', start)],
#         states={PHONE_NUMBER: [MessageHandler(Filters.contact, get_phone_number)]},
#         fallbacks=[]
#     )

#     updater.dispatcher.add_handler(CommandHandler('start', start))
#     updater.dispatcher.add_handler(CommandHandler('help', help))
#     updater.dispatcher.add_handler(phone_number_handler)  # Add the conversation handler

#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()