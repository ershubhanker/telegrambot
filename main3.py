from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters, ConversationHandler

TOKEN = "6594776797:AAHfT8jKuIlZVXeNswQDPnMtiJoyI8ex39c"
# PHONE_NUMBER = range(1)

# States for the conversation
MENU, FULLZ_AUTOSHOP, BALANCE, DIGITAL_DOCS, FAQ = range(5)

def start(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["Fullz Autoshop", "Balance"], ["Digital Docs & Ids", "F.A.Q"]], one_time_keyboard=True)
    update.message.reply_text('Welcome to Our Service! Choose an option:', reply_markup=reply_markup)
    return MENU

def fullz_autoshop_menu(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["Scene Point", "Search Bin"], ["Sorting Tools", "F.A.Qs"], ["Fullz", "Nodob"],
                                        ["Atm+mmm", "Noaddy"], ["PreOrder"], ["Back"]], one_time_keyboard=True)
    update.message.reply_text('Select a category:', reply_markup=reply_markup)
    return FULLZ_AUTOSHOP

def balance_menu(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["Add Balance", "View Balance"], ["Order History", "Usage History"], ["Back"]], one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return BALANCE

def digital_docs_menu(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["Proof of Identity", "Document Identity"], ["Custom", "Back"]], one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return DIGITAL_DOCS

def faq_menu(update: Update, context: CallbackContext) -> int:
    faq_text = """
        FAQ
    ---------------------------
    Frequently asked questions
    ⭕️ How does the Passport picture system work?
    ✅ To choose a passport picture for your ID you can Refer to our sheet
    M1 to M35 (M for MALE)
    F1 to F35 (F for FEMALE) and you input your choice in the bot (MAJ IMPORTANT) or if you have your Private code you can use it on the page

    ⭕️ Can I add my own passport picture on the bot?
    ✅ You can add custom pictures by Contacting the support at @xxxxx you will receive a private code that you can use on the bot at the Picture selection step if you don't share your private code nobody will be able to use your picture, we are asking a one time fee of XXX to add picture because we have to adjust them on every project

    ⭕️ I made an error on my order is there a way to get a replacement?
    ✅ Our team understands that it can be frustrating to make error, You can contact the support with your Order Number, if there a problem with your order and someone will assist you ASAP

    ⭕️ How long will it take to receive my order?
    ✅ Once the payment reaches 1 confirmations on the Bitcoin network, it will usually take less than 10 minutes to receive your order, if it take more then 30 minute please contact us with your order number

    ⭕️ Do I have to wait bitcoin confirmation every time?
    ✅ You can contact the support to buy some Prepaid coupon code (5-10-20-50) so you won't have to wait Bitcoin confirmation between each Purchase

    ⭕️ What if I want a card with more specific information on it?
    ✅ We understand that some project are not 100% Editable, because it would bring more error for our customer, so many number are Randomised, if you need something custom please contact the support

    ⭕️ Can I choose a custom signature?
    ✅ At the moment it harder for us to support Custom Signature because or our system who use a Police fonts to make them, but you can ask assistance to support and we will see what we can do for you

    ⭕️Does every ID are scannable?
    ✅ Barcode are 100% scannable and match the information on the front of your ID

    ⭕️How can I avoid error on my order?
    ✅ You can refer to our tutorial video on our channel, and you should always take your time to read what the bot are asking
    Example (DOB CAN BE 95/01/01 1995/01/01 1995-01-01)

    ⭕️Will my order always be the same?
    ✅ We offer different background for each project and we will work hard to add some every week, so if your doing the same thing over and over with them people won't notice it the same picture with different information

    ⭕️I sent bitcoin but my order did not go through
    ✅ If you have a problem with your Payment please contact support with your ORDER NUMBER

    ⭕️Can your team does a custom project on the bot for me?
    ✅ If you have a custom request, we might be open to make it you can contact us and we will discuss about it

    ⭕️Do you plan to add the missing provinces?
    ✅ We added Most popular project at the moment you can DM us at anytime if you have some advice for the bot


    ⭕️How do I download my order?
    ✅ When the payment is done and your order processed, you will receive a download link on ufile.io (Usually 2 link for the FRONT and the BACK) you will click on ''Free download'' and then ''Slow speed''

    ⭕️My file has been archived by ufile.io can I get it back?
    ✅ We don't keep any file from our side so it's your responsibility to keep them in security after your purchase

    ⭕️How do I pay with coupon code?
    ✅ To redeem a coupon code, it will be the last option after you have confirmed your input onto the bot, if you don't have any you just click on ''Pay without coupon''

    ⭕️I didn't send enough bitcoin to the payment address provided to complete my order what is my option?
    ✅ The bot will only process your order if the exact amount asked are receive so please verify the amount you are sending before, Or else you can contact the support and we will try to solve the issue ASAP
    """
    update.message.reply_text(faq_text)
    return FAQ

def back_to_menu(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["Fullz Autoshop", "Balance"], ["Digital Docs & Ids", "F.A.Q"]], one_time_keyboard=True)
    update.message.reply_text('Back to main menu. Choose an option:', reply_markup=reply_markup)
    return MENU

def end(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Thank you for using our service!")
    return ConversationHandler.END

def main() -> None:
    updater = Updater(TOKEN, use_context=True)

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            MENU: [MessageHandler(Filters.regex('^(Fullz Autoshop)$'), fullz_autoshop_menu),
                   MessageHandler(Filters.regex('^(Balance)$'), balance_menu),
                   MessageHandler(Filters.regex('^(Digital Docs & Ids)$'), digital_docs_menu),
                   MessageHandler(Filters.regex('^(F.A.Q)$'), faq_menu)],
            FULLZ_AUTOSHOP: [MessageHandler(Filters.regex('^(Scene Point|Search Bin|Sorting Tools|F.A.Qs|Fullz|Nodob|Atm\+mmm|Noaddy|PreOrder|Back)$'), back_to_menu)],
            BALANCE: [MessageHandler(Filters.regex('^(Add Balance|View Balance|Order History|Usage History|Back)$'), back_to_menu)],
            DIGITAL_DOCS: [MessageHandler(Filters.regex('^(Proof of Identity|Document Identity|Custom|Back)$'), back_to_menu)],
            FAQ: [MessageHandler(Filters.regex('^Back$'), back_to_menu)]
        },
        fallbacks=[CommandHandler('end', end)]
    )

    updater.dispatcher.add_handler(conversation_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()