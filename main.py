import requests
from fastapi import FastAPI
from pyrogram import Client , filters

app = FastAPI()

bot = Client(
  "uhdhdhhd",
  api_id=18770647,
  api_hash="ed11b8af8b51418dbac60b456d1429a7",
  bot_token="6281251739:AAFGDxuibD-teVFF_wzOTc41dgJtE6kJje4"
)

requests.get("https://api.telegram.org/bot6281251739:AAFGDxuibD-teVFF_wzOTc41dgJtE6kJje4/sendMessage?chat_id=-1001544918166&text=Alpha+Server+Started")

@bot.on_message(filters.command("start"))
async def starts(client , msg):
  await message.reply_text("Alpha Server Working Fine")
  
@app.get("/")
async def heol():
  return "Hello World!"
