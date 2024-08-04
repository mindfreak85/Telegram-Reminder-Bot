from datetime import datetime, timedelta
import time
import schedule
from threading import Thread
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher

#TOKEN = "6042107411:AAHSzve9V17mGIL7UY0gXvN733ZQleqFpG8"



# def route(update, context):
#     text = update.message.text
    
#     # Control what your chatbot replies in this block of code! 
#     time.sleep(3600)
#     update.message.reply_text(text)

# updater = Updater(TOKEN, use_context=True)
# updater.dispatcher.add_handler(MessageHandler(Filters.text, route))
# updater.start_polling()

#print("Your telegram bot is running!")

#updater.idle()

bot = Bot(token="6042107411:AAHSzve9V17mGIL7UY0gXvN733ZQleqFpG8")
dp = Dispatcher(bot)

def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)

button1 = InlineKeyboardButton(text = "1 min", callback_data= "1")
button2 = InlineKeyboardButton(text = "10 mins", callback_data= "10")
button3 = InlineKeyboardButton(text = "30 mins", callback_data= "30")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3)

message_store= ""

@dp.message_handler(commands=['start'])
async def welcome (message: types.Message):
    await message.reply("Hello! Put your reminders here and select time frame for me to send!")

@dp.message_handler()
async def send_inline_options(message: types.Message):
    global message_store 
    message_store = message.text
    await message.reply("Select reminder time", reply_markup=keyboard_inline)

#Problem lies here echo_message was never awaited
# async def echo_message(message: types.Message):
#     global message_store
#     await message.reply(message.text)
#     message_store = ""
#     return schedule.CancelJob

@dp.callback_query_handler(text = ["1", "10", "30"])
async def reminder_message(call: types.CallbackQuery):
    global message_store
    if call.data == "1":
        await call.message.answer("I'll send your reminder in 1 min!")
        time_to_send_message = datetime.now() + timedelta(minutes=1)
        time_to_send_message = time_to_send_message.strftime("%H:%M:%S")
        print(time_to_send_message)
        print(message_store)
        #time.sleep(60)
    elif call.data == "10":
        await call.message.answer("I'll send your reminder in 10 mins!")
        time_to_send_message = datetime.now() + timedelta(minutes=10)
        time_to_send_message = time_to_send_message.strftime("%H:%M:%S")
        #time.sleep(600)
    elif call.data == "30":
        await call.message.answer("I'll send your reminder in 30 mins!")
        time_to_send_message = datetime.now() + timedelta(minutes=30)
        time_to_send_message = time_to_send_message.strftime("%H:%M:%S")
        #time.sleep(1800)

    #schedule.every().day.at(time_to_send_message).do(echo_message(message_store))
    #await call.message.answer(message_store)
    print("Checkpt2")
    

print("Your telegram bot is running!")


executor.start_polling(dp)

while True:
    schedule.run_pending()
    time.sleep(1)