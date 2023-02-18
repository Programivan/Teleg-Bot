from Secret import TOKEB
from aiogram import  Bot,Dispatcher,executor,types
import subprocess

tele = Bot(token = TOKEB)
disp = Dispatcher(tele)

@disp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Hello")


@disp.message_handler(commands=['help'])
async def show(message: types.Message):
    await tele.send_message(message.from_user.id, "\n/help - bot helping you\n/full_name\n/code - my own code")

@disp.message_handler(commands=['full_name'])
async def name(message: types.Message):
    User_name = message.from_user.full_name
    print(User_name)
    await tele.send_message(message.from_user.id,f"Your full_name: {User_name}")

@disp.message_handler(commands=['code'])
async def code(message: types.Message):
    codeURL = "https://github.com/Programivan/Teleg-Bot/"
    codeZip = "https://raw.githubusercontent.com/Programivan/Teleg-Bot/main/Bot.zip"
    await message.reply(f"Code: URL {codeURL} or ZIP {codeZip} ")

#@disp.message_handler(commands=)


if __name__ == '__main__':
    executor.start_polling(disp ,skip_updates= True)
