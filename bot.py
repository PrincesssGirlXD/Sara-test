from pyrogram import Client, filters

bot = Client(
  "uhdhdhhd",
  api_id=18770647,
  api_hash="ed11b8af8b51418dbac60b456d1429a7",
  bot_token="6281251739:AAFGDxuibD-teVFF_wzOTc41dgJtE6kJje4"
)
@bot.on_message(filters.command("start"))
def starts(client , msg):
  message.reply_text("Alpha Server Working Fine")

bot.run()
  
