import telebot
import requests
import json

# Bot token
bot = telebot.TeleBot('6770440133:AAFpaXgqPqErzqmdJXufW4bVJcBZ_o9KP0Q')

# File to store user data
USER_DB = "users.json"

# Function to load users
def load_users():
    try:
        with open(USER_DB, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save users
def save_users(users):
    with open(USER_DB, "w") as file:
        json.dump(users, file)

# Start command
@bot.message_handler(commands=['start'])
def start_msg(message):
    user_id = message.from_user.id
    usr = message.from_user.first_name

    users = load_users()
    if user_id not in users:
        users.append(user_id)  # Add new user
        save_users(users)

    bot.send_message(user_id, f'<b>👋 Hello {usr}!\n\n🤖 Send a message to ChatGPT.</b>', parse_mode="HTML")

