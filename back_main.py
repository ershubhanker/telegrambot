from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

TOKEN = "6594776797:AAHfT8jKuIlZVXeNswQDPnMtiJoyI8ex39c"

# States for the conversation
MENU, MARKET, WALLET, RULES, FAQ_MENU, CHANNEL_UPDATE, OPEN_A_TICKET, CANADAPOST, DSS_VERIFICATION, POST_PREPAID, MAIL_FORWARDING, BANK_DROPS,BANK_LOGS,CVV,DOCUMENTS,EXCHANGE_CRYPTO,HACKED,PROFILES,SCAM,TEMPLATES,TUTORIALS = range(21)
POST_PREPAID_VERIFICATION = 11


def start(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["Market", "Wallet"], ["Rules", "F.A.Q"], ["Channel Update", "Open a Ticket"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Welcome to Our Service! Choose an option:', reply_markup=reply_markup)
    return MENU


def market(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["Bank Drops", "Bank Logs"], ["Canada Post Services", "CVV/Fullz"],
                                        ["Documents & IDs", "Exchange Fiat for Crypto"],
                                        ["Hacked Accounts", "Profiles"], ["Scam Pages", "Templates"],
                                        ["Tutorials", "Back"]], one_time_keyboard=True)
    update.message.reply_text('Select a category:', reply_markup=reply_markup)
    return MARKET


def wallet(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["Add Balance", "View Balance"], ["Order History", "Usage History"], ["Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return WALLET


def rules(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["Proof of Identity", "Document Identity"], ["Custom", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return RULES


def faq_menu(update: Update, context: CallbackContext) -> int:
    faq_text = """
    FAQ
    ---------------------------
    Frequently asked questions
    ⭕ How does the Passport picture system work?
    ...
    """
    update.message.reply_text(faq_text)
    return FAQ_MENU


def channel_update(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["Proof of Identity", "Document Identity"], ["Custom", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return CHANNEL_UPDATE


def open_a_ticket(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["Proof of Identity", "Document Identity"], ["Custom", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return OPEN_A_TICKET


def bank_drops(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["DSS Verification", "Canada Post Prepaid"],[ "Mail Forwarding", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return BANK_DROPS # Assuming that this option doesn't lead to further sub-menus
def bank_logs(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["DSS Verification", "Canada Post Prepaid"],[ "Mail Forwarding", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return BANK_LOGS# Assuming that this option doesn't lead to further sub-menus
def canada_post_services(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["DSS Verification", "Canada Post Prepaid"],[ "Mail Forwarding", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return CANADAPOST # Assuming that this option doesn't lead to further sub-menus
def CVV_Fullz(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["DSS Verification", "Canada Post Prepaid"],[ "Mail Forwarding", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return CVV # Assuming that this option doesn't lead to further sub-menus
def documents(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["DSS Verification", "Canada Post Prepaid"],[ "Mail Forwarding", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return DOCUMENTS# Assuming that this option doesn't lead to further sub-menus
def exchange_crypto(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["DSS Verification", "Canada Post Prepaid"],[ "Mail Forwarding", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return EXCHANGE_CRYPTO # Assuming that this option doesn't lead to further sub-menus
def hacked(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["DSS Verification", "Canada Post Prepaid"],[ "Mail Forwarding", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return HACKED # Assuming that this option doesn't lead to further sub-menus
def profiles(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["DSS Verification", "Canada Post Prepaid"],[ "Mail Forwarding", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return PROFILES # Assuming that this option doesn't lead to further sub-menus
def scam_pages(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["DSS Verification", "Canada Post Prepaid"],[ "Mail Forwarding", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return SCAM # Assuming that this option doesn't lead to further sub-menus
def templates(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["DSS Verification", "Canada Post Prepaid"],[ "Mail Forwarding", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return TEMPLATES # Assuming that this option doesn't lead to further sub-menus
def tutorails(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["DSS Verification", "Canada Post Prepaid"],[ "Mail Forwarding", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return TUTORIALS # Assuming that this option doesn't lead to further sub-menus

# Assuming CANADAPOST is defined somewhere in your code

def cvv_(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    
    return CANADAPOST

def bank_logs(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["DSS Verification", "Canada Post Prepaid"],["Mail Forwarding", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return CANADAPOST  # Assuming that this option doesn't lead to further sub-menus

def canada_post_services(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["DSS Verification", "Canada Post Prepaid", "Mail Forwarding", "Back"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Select an option:', reply_markup=reply_markup)
    return CANADAPOST
def handle_catalog_selection(update: Update, context: CallbackContext) -> int:
    selected_option = update.message.text
    
    if selected_option in {"1", "2", "3", "4", "5", "6", "7"}:
        catalog_number = int(selected_option)
        update.message.reply_text(f'You have selected the catalog for {catalog_number} which is of $20.')
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("1", callback_data="catalog_1")],
            [InlineKeyboardButton("Back", callback_data="back")]
        ])
        update.message.reply_text('Select a catalog option:', reply_markup=reply_markup)
    elif selected_option == "Back":
        update.message.reply_text('Going back to the previous menu.')
        return back_to_menu(update, context)
    else:
        update.message.reply_text('Invalid selection. Please choose a valid option.')

    return CANADAPOST

def start_dss_verification(update: Update, context: CallbackContext) -> int:
    context.user_data['verification_data'] = {'first_name': None, 'last_name': None, 'dob': None, 'address': None,
                                              'sex': None, 'dss_number': None}
    update.message.reply_text("What is your first name?")
    return DSS_VERIFICATION

def get_verification_data(update: Update, context: CallbackContext) -> int:
    verification_data = context.user_data['verification_data']
    
    if verification_data['first_name'] is None:
        verification_data['first_name'] = update.message.text
        update.message.reply_text(f"First name set to: {verification_data['first_name']}\nWhat is your last name?")
        return DSS_VERIFICATION
    elif verification_data['last_name'] is None:
        verification_data['last_name'] = update.message.text
        update.message.reply_text(f"Last name set to: {verification_data['last_name']}\nWhat is your Date of Birth (DD/MM/YYYY)?")
        return DSS_VERIFICATION
    elif verification_data['dob'] is None:
        verification_data['dob'] = update.message.text
        update.message.reply_text(f"Date of Birth set to: {verification_data['dob']}\nWhat is your Address (Street, City, Province, Postal Code)?")
        return DSS_VERIFICATION
    elif verification_data['address'] is None:
        verification_data['address'] = update.message.text
        update.message.reply_text(f"Address set to: {verification_data['address']}\nWhat is your Sex (M/F/Other)?")
        return DSS_VERIFICATION
    elif verification_data['sex'] is None:
        verification_data['sex'] = update.message.text
        update.message.reply_text(f"Sex set to: {verification_data['sex']}\nWhat is your DSS Number?")
        return DSS_VERIFICATION
    elif verification_data['dss_number'] is None:
        verification_data['dss_number'] = update.message.text
        # Print details in the terminal
        print("DSS Verification Details:")
        for key, value in verification_data.items():
            print(f"{key}: {value}")

        update.message.reply_text(f"DSS Verification completed. Returning to the main menu.")
        return start(update, context)

def cancel_dss_verification(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('DSS Verification canceled. Returning to the main menu.')
    return start(update, context)

def back_to_menu(update: Update, context: CallbackContext) -> int:
    reply_markup = ReplyKeyboardMarkup([["Market", "Wallet"], ["Rules", "F.A.Q"], ["Channel Update", "Open a Ticket"]],
                                       one_time_keyboard=True)
    update.message.reply_text('Back to main menu. Choose an option:', reply_markup=reply_markup)
    return MENU


def end(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Thank you for using our service!", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def main() -> None:
    updater = Updater(TOKEN)

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            MENU: [MessageHandler(Filters.regex('^(Market)$'), market),
                   MessageHandler(Filters.regex('^(Wallet)$'), wallet),
                   MessageHandler(Filters.regex('^(Rules)$'), rules),
                   MessageHandler(Filters.regex('^(F.A.Q)$'), faq_menu),
                   MessageHandler(Filters.regex('^(Channel Update)$'), channel_update),
                   MessageHandler(Filters.regex('^(Open a Ticket)$'), open_a_ticket)],

            MARKET: [MessageHandler(Filters.regex('^(Bank Drops)$'), bank_drops),
                     MessageHandler(Filters.regex('^(Bank Logs)$'), bank_logs),
                     MessageHandler(Filters.regex('^(Canada Post Services)$'), canada_post_services),
                     MessageHandler(Filters.regex('^(CVV/Fullz)$'), cvv_),
                     MessageHandler(Filters.regex('^(Documents & IDs)$'), documents),
                     MessageHandler(Filters.regex('^(Exchange Fiat for Crypto)$'), exchange_crypto),
                     MessageHandler(Filters.regex('^(Hacked Accounts)$'), channel_update),
                     MessageHandler(Filters.regex('^(Profiles)$'), profiles),
                     MessageHandler(Filters.regex('^(Scam Pages)$'), scam_pages),
                     MessageHandler(Filters.regex('^(Templates)$'), templates),
                     MessageHandler(Filters.regex('^(Tutorials)$'), tutorails),
                     MessageHandler(Filters.regex('^(Back)$'), back_to_menu)],
            # MARKET: [MessageHandler(Filters.regex('^(Bank Drops|Bank Logs|Canada Post Services|CVV/Fullz|Documents & IDs|Exchange Fiat for Crypto|Hacked Accounts|Profiles|Scam Pages|Templates|Tutorials|Back)$'), back_to_menu)],
            WALLET: [MessageHandler(Filters.regex('^(Add Balance|View Balance|Order History|Usage History|Back)$'),
                                    back_to_menu)],
            RULES: [MessageHandler(Filters.regex('^(Proof of Identity|Document Identity|Custom|Back)$'), back_to_menu)],
            FAQ_MENU: [MessageHandler(Filters.regex('^Back$'), back_to_menu)],
            CHANNEL_UPDATE: [
                MessageHandler(Filters.regex('^(Proof of Identity|Document Identity|Custom|Back)$'), back_to_menu)],
            OPEN_A_TICKET: [
                MessageHandler(Filters.regex('^(Proof of Identity|Document Identity|Custom|Back)$'), back_to_menu)],
            BANK_DROPS: [
                MessageHandler(Filters.regex('^(DSS Verification|Canada Post Prepaid|Mail Forwarding|Back)$'), back_to_menu)],
            BANK_LOGS: [
                MessageHandler(Filters.regex('^(DSS Verification|Canada Post Prepaid|Mail Forwarding|Back)$'), back_to_menu)],
            CANADAPOST:[MessageHandler(Filters.regex('^(DSS Verification|Canada Post Prepaid|Mail Forwarding|Back)$'),
                                         handle_catalog_selection),
                         MessageHandler(Filters.text & ~Filters.command, handle_catalog_selection)],
            DSS_VERIFICATION: [MessageHandler(Filters.text & ~Filters.command, get_verification_data)],
            CVV: [
                MessageHandler(Filters.regex('^(DSS Verification|Canada Post Prepaid|Mail Forwarding|Back)$'), back_to_menu)],
            DOCUMENTS: [
                MessageHandler(Filters.regex('^(DSS Verification|Canada Post Prepaid|Mail Forwarding|Back)$'), back_to_menu)],
            EXCHANGE_CRYPTO: [
                MessageHandler(Filters.regex('^(DSS Verification|Canada Post Prepaid|Mail Forwarding|Back)$'), back_to_menu)],
            HACKED: [
                MessageHandler(Filters.regex('^(DSS Verification|Canada Post Prepaid|Mail Forwarding|Back)$'), back_to_menu)],
            PROFILES: [
                MessageHandler(Filters.regex('^(DSS Verification|Canada Post Prepaid|Mail Forwarding|Back)$'), back_to_menu)],
            SCAM: [
                MessageHandler(Filters.regex('^(DSS Verification|Canada Post Prepaid|Mail Forwarding|Back)$'), back_to_menu)],
            TEMPLATES: [
                MessageHandler(Filters.regex('^(DSS Verification|Canada Post Prepaid|Mail Forwarding|Back)$'), back_to_menu)],
            TUTORIALS: [
                MessageHandler(Filters.regex('^(DSS Verification|Canada Post Prepaid|Mail Forwarding|Back)$'), back_to_menu)],
            ConversationHandler.END: [],  # Empty list, as END is not a state
        },
        fallbacks=[CommandHandler('end', end)],
    )

    updater.dispatcher.add_handler(conversation_handler)
    # updater.dispatcher.add_handler(canada_post_services_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()





