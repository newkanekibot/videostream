import asyncio
from pytgcalls import idle
from driver.kaneki import call_py, bot

async def mulai_bot():
    print("[KANEKI]: STARTING BOT CLIENT")
    await bot.start()
    print("[KANEKI]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    await pidle()
    print("[KANEKI]: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())
