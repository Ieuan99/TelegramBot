# importing the os to read the env
import os
import dotenv
import telebot
import json

dotenv.load_dotenv()

# getting the bot token from the env
BOT_TOKEN = os.getenv("BOT_TOKEN")


# setting up a new bot instance using the bot token
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", 'hello'])
def start(message):
    bot.reply_to(message, "Hello, " + message.from_user.first_name + "! type '/help' for a list of commands")


@bot.message_handler(commands=["help"])
def help(message):
    help_message = "Here are the available commands:\n" \
                   "/start - Start the bot\n" \
                   "/help - Show available commands\n" \
                   "/add <task> - Add a task to the list\n" \
                   "/list - Show the current task list\n" \
                   "/done <task #> - Mark a task as done\n" \
                   "/clear - Clear completed tasks\n" \
                   "/weather <city> - Get the current weather\n" \
                   "/fact - Get a random fact\n" \
                   "/joke - Get a dad joke\n" \
                   "/quote - Get an inspirational quote"
    bot.reply_to(message, help_message)

task_to_add = None

@bot.message_handler(commands=["add"])
def add_task(message):
    global task_to_add
    task_to_add = message.chat.id
    bot.reply_to(message, "Please enter the task you want to add:")

@bot.message_handler(content_types=['text'])
def get_task(message):
    global task_to_add
    if task_to_add is not None and message.chat.id == task_to_add:
        task = message.text.strip()
        if task:
            from datetime import datetime
            filename = f"tasks_{datetime.now().strftime('%Y-%m-%d')}.json"

            # Checking if the file exists
            if not os.path.exists(filename):
                # If not, creating a new file with an empty list
                with open(filename, 'w') as file:
                    json.dump([], file)

            # If the file exists, reading the existing tasks and appending the new one
            with open(filename, 'r') as file:
                tasks = json.load(file)
                tasks.append(task)
            with open(filename, 'w') as file:
                json.dump(tasks, file)
                bot.reply_to(message, f"Task '{task}' added to your list.")
        else:
            bot.reply_to(message, "Please enter a task.")
        task_to_add = None
    elif message.text.startswith('/list'):
        list_tasks(message)
    elif message.text.startswith('/'):
        pass
    else:
        bot.reply_to(message, "Invalid command. Please use /add, /list or other available commands.")

def list_tasks(message):
    bot.reply_to(message, "Here are your tasks:")
    from datetime import datetime
    filename = f"tasks_{datetime.now().strftime('%Y-%m-%d')}.json"

    # Checking if the file exists
    if not os.path.exists(filename):
        # If not, creating a new file with an empty list
        with open(filename, 'w') as file:
            json.dump([], file)
        bot.reply_to(message, "No tasks found.")
    else:
        # If the file exists, reading the existing tasks
        with open(filename, 'r') as file:
            tasks = json.load(file)
            if tasks:
                task_list = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
                bot.reply_to(message, task_list)
            else:
                bot.reply_to(message, "No tasks found.")

@bot.message_handler(commands=["list"])
def list_tasks(message):
    bot.reply_to(message, "Here are your tasks:")
    from datetime import datetime
    filename = f"tasks_{datetime.now().strftime('%Y-%m-%d')}.json"

    # Checking if the file exists
    if not os.path.exists(filename):
        # If not, creating a new file with an empty list
        with open(filename, 'w') as file:
            json.dump([], file)
        bot.reply_to(message, "No tasks found.")
    else:
        # If the file exists, reading the existing tasks
        with open(filename, 'r') as file:
            tasks = json.load(file)
            if tasks:
                task_list = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
                bot.reply_to(message, task_list)
            else:
                bot.reply_to(message, "No tasks found.")

@bot.message_handler(commands=["done"])
def mark_done(message):
    bot.reply_to(message, "Please enter the number of the task you want to mark as done:")

@bot.message_handler(commands=["clear"])
def clear_completed(message):
    bot.reply_to(message, "All completed tasks have been cleared.")

@bot.message_handler(commands=["weather"])
def get_weather(message):
    bot.reply_to(message, "Please enter the name of the city you want to get the weather for:")

@bot.message_handler(commands=["fact"])
def get_fact(message):
    bot.reply_to(message, "Here's a random fact:")

@bot.message_handler(commands=["joke"])
def get_joke(message):
    bot.reply_to(message, "Here's a dad joke:")

@bot.message_handler(commands=["quote"])
def get_quote(message):
    bot.reply_to(message, "Here's an inspirational quote:")

# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, "You said: " + message.text)

bot.infinity_polling()