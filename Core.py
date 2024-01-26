import asyncio
import jdatetime
from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

DaysOfWeek = {
    "Saturday":"شنبه","Sunday":"یکشنبه","Monday":"دوشنبه","Tuesday":"سه‌شنبه","Wednesday":"چهارشنبه","Thursday":"پنجشبه","Friday":"جمعه"
}
Months = {
    "1":"فروردین","2":"اردیبهشت","3":"خرداد","4":"تیر","5":"مرداد","6":"شهریور","7":"مهر","8":"آبان","9":"آذر","10":"دی","11":"بهمن","12":"اسفند"
}

print("Started")
async def update_profile():
    while True:
        now = jdatetime.datetime.now()
        day = DaysOfWeek.get(now.strftime("%A")) 
        time = now.strftime("%H:%M")  
        Month = Months.get(now.strftime("%m"))
        DayOfMonth = now.strftime("%d") 
        async with TelegramClient("session.session", apiId, ApiHash) as client:
                await client(UpdateProfileRequest(first_name=f"{time} {day} {DayOfMonth} {Month}"))
	await asyncio.sleep(60)


asyncio.run(update_profile())