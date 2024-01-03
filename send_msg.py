import asyncio
from telegram import Bot
def get_msg():
    return "ok"

def sendTgMessage(msg):
        async def send_message():
            # 创建 Bot 实例
            bot_token = '1582443382:AAGZHjDtgK5R1hNdcWXviBjQ1ihXaoIW4FE'
            group_id = '-911547716'
            bot = Bot(token=bot_token)

            # 发送消息到群组
            await bot.send_message(chat_id=group_id, text=msg)
        # 创建事件循环并运行异步函数
        loop = asyncio.get_event_loop()
        loop.run_until_complete(send_message())
        loop.close()
msg = get_msg()
sendTgMessage(msg)
