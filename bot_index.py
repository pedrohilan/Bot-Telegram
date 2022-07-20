from os import getenv
from dotenv import load_dotenv, find_dotenv
from uvloop import install
from tkinter.tix import Tree
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

load_dotenv(find_dotenv('ambiente.env'))
install()

app = Client(
    'pedrohilan_bot',
    api_id=getenv("TELEGRAM_API_ID"),
    api_hash=getenv("TELEGRAM_API_HASH"),
    bot_token=getenv("TELEGRAM_BOT_TOKEN")
)
@app.on_message(filters.command('teclado'))
async def keyboard(client, message):
    teclado=ReplyKeyboardMarkup(
        [
            ['/ajuda', '/iniciar', '/foto'],
            ['/parar', '/comandoa', 'comandob']
        ], 
        resize_keyboard=True)
    await message.reply('Escolha uma opção', reply_markup=teclado)

@app.on_message(filters.command('foto'))
async def photo(client, message):
    await app.send_photo(message.chat.id, 'https://lh3.googleusercontent.com/CVlqAu59CbaLlmGB5zaBg0lwUUC22tUAZbAdH9uBhg_VIB8c5ORQnD5RzpiOBCbyECeM_L0ZhqVNUKG1hs3oqMdiPyg=w640-h400-e365-rj-sc0x00ffffff')

@app.on_message(filters.sticker)
async def sticker(client, message):
    await app.send_sticker(
        message.chat.id,
        message.sticker.file_id
    )

@app.on_message(filters.photo)
async def photo2(client, message):
    await app.send_photo(
        message.chat.id,
        message.photo.file_id
    )

@app.on_message(filters.voice | filters.audio)
async def photo(client, message):
    await message.reply('Meu fone tá quebrado :/')

@app.on_message(filters.command('ajuda'))
async def help(client, message):
    await message.reply('Este é o comando de ajuda')

@app.on_message()
async def messages(client, message):
    print(message.chat.username, message.text)
    await message.reply(message.text + '???')

app.run()