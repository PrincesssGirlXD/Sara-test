import requests
from fastapi import FastAPI

app = FastAPI()



requests.get("https://api.telegram.org/bot6281251739:AAFGDxuibD-teVFF_wzOTc41dgJtE6kJje4/sendMessage?chat_id=-1001544918166&text=Alpha+Server+Started")


@app.get("/")
async def heol():
  return "Hello World!"

