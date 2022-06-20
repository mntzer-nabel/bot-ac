from pyrogram import Client, filters
import time
import asyncio
import async_timeout

api_id = "ваш_api_id с сайта - my.telegram.org"
api_hash = "ваш_api_hash с сайта - my.telegram.org"

app = Client("account", api_id, api_hash)



@app.on_message(filters.regex("сердечки"))
async def heart(client, message):
    await message.edit_text("❤️")
    await asyncio.sleep(0.1)
    await message.edit_text("❤️🧡")
    await asyncio.sleep(0.1)
    await message.edit_text("❤️🧡💛")
    await asyncio.sleep(0.1)
    await message.edit_text("❤️🧡💛💙")
    await asyncio.sleep(0.1)
    await message.edit_text("💙")
    await asyncio.sleep(0.1)
    await message.edit_text("💙💙")
    await asyncio.sleep(0.1)
    await message.edit_text("💙💙💙")
    await asyncio.sleep(0.1)
    await message.edit_text("💙💙💙💙")
    await asyncio.sleep(0.1)
    await message.edit_text("💙💙💙💙\n💙💙💙💙")
    await asyncio.sleep(0.1)
    await message.edit_text("💙💙💙💙\n💛💛💛💛")
    await asyncio.sleep(0.1)
    await message.edit_text("💙💙💙💙\n💛💛💛")
    await asyncio.sleep(0.1)
    await message.edit_text("💙💙💙💙\n💛💛")
    await asyncio.sleep(0.1)
    await message.edit_text("💙💙💙💙\n💛")
    await asyncio.sleep(0.1)
    await message.edit_text("💙💙💙💙")
    await asyncio.sleep(0.1)
    await message.edit_text("💙💙💙")
    await asyncio.sleep(0.1)
    await message.edit_text("💙💙")
    await asyncio.sleep(0.1)
    await message.edit_text("💙")
    await asyncio.sleep(0.1)
    await message.edit_text("❤️")
    await asyncio.sleep(0.1)
    await message.edit_text("❤️❤️\n💛")
    await asyncio.sleep(0.03)
    await message.edit_text("❤️❤️❤️\n💛💛")
    await asyncio.sleep(0.02)
    await message.edit_text("❤️❤️❤️❤️\n💛💛💛")
    await asyncio.sleep(0.03)
    await message.edit_text("❤️❤️❤️❤️❤️\n💛💛💛💛")
    await asyncio.sleep(0.04)
    await message.edit_text("❤️❤️❤️❤️❤️❤️❤️\n💛💛💛💛💛")
    await asyncio.sleep(0.02)
    await message.edit_text("❤️❤️❤️❤️❤️❤️\n💛💛💛💛💛💛")
    await asyncio.sleep(0.01)
    await message.edit_text("❤️❤️❤️❤️❤️\n💛💛💛💛💛💛💛\n💚")
    await asyncio.sleep(0.2)
    await message.edit_text("❤️❤️❤️❤️\n💛💛💛💛💛💛💛\n💚💚")
    await asyncio.sleep(0.3)
    await message.edit_text("❤️❤️❤️\n💛💛💛💛💛💛💛\n💚💚💚")
    await asyncio.sleep(0.01)
    await message.edit_text("❤️❤️\n💛💛💛💛💛💛💛\n💚💚💚💚")
    await asyncio.sleep(0.01)
    await message.edit_text("❤️\n💛💛💛💛💛💛💛\n💚💚💚💚💚")
    await asyncio.sleep(0.03)
    await message.edit_text("❤️💙💛💚\n💛💛💛💛💛💛💛\n💚💚💚💚💚💚")
    await asyncio.sleep(0.04)
    await message.edit_text("💚❤️💛❤️❤️💚❤️\n💛💛💛💛💛💛💛\n💚💚💚💚💚💚💚")








app.run()