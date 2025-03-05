@bot.message_handler(commands=['broadcast'])
def broadcast_msg(message):
    if message.from_user.id != 6667876837:  # Replace with your Telegram ID
        bot.reply_to(message, "❌ You are not authorized to use this command!")
        return

    text = message.text.replace('/broadcast ', '')  # Remove command part
    users = load_users()

    sent, failed = 0, 0
    for user_id in users:
        try:
            bot.send_message(user_id, text)
            sent += 1
        except Exception:
            failed += 1

    bot.reply_to(message, f"✅ Message sent to {sent} users.\n⚠️ Failed: {failed}")

