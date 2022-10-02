from .login import user
from telethon import events
import time


@user.on(events.NewMessage(pattern=r'^re[ 0-9]*$', outgoing=True))
async def mycp(event):
    num = event.raw_text.split(' ')
    if isinstance(num, list) and len(num) == 2:
        num = int(num[-1])
    else:
        num = 1
    reply = await event.get_reply_message()
    await event.delete()
    for _ in range(0, num):
        await reply.forward_to(int(event.chat_id))


@user.on(events.NewMessage(pattern=r'^id$', outgoing=True))
async def myid(event):
    text = f'当前聊天ID:`{event.chat_id}`'
    reply = await event.get_reply_message()
    if reply:
        text += "\n\n**回复用户**\nid: `" + str(reply.sender_id) + "`"
        if reply.forward:
            if str(reply.forward.chat_id).startswith('-100'):
                text += "\n\n**转发来自频道**\nid: `" + str(reply.forward.chat_id) + "`\ntitle: `" + reply.forward.chat.title + "`"
            else:
                text += "\n\n**转发来自用户**\nid: `" + str(reply.forward.sender_id) + "`"
    await event.edit(text)


@user.on(events.NewMessage(pattern=r'^del[ 0-9]*$', outgoing=True))
async def selfprune(event):
    try:
        num = event.raw_text.split(' ')
        if isinstance(num, list) and len(num) == 2:
            count = int(num[-1])
        else:
            count = 1
        await event.delete()
        count_buffer = 0
        async for message in user.iter_messages(event.chat_id, from_user="me"):
            if count_buffer == count:
                break
            await message.delete()
            count_buffer += 1
        notification = await user.send_message(event.chat_id, f'已删除{count_buffer}/{count}')
        time.sleep(.5)
        await notification.delete()
    except Exception as e:
        await user.send_message(event.chat_id, str(e))


# @user.on(events.NewMessage(pattern=r'^spy 签到$', outgoing=True))
# async def qd(event):
#    await user.send_message(5137236682, f'/SPY 签到')
# time.sleep(3)
# await user.send_message(5137236682, f'/SPY 签到 {str((time.time()+786552)*1000)[0:13]}')
#
#
# @user.on(events.NewMessage(incoming=True))
# async def qd1(event):
#    try:
#        if event.chat_id == 5137236682:
#            res = re.search("/SPY 签到 [0-9]*", event.raw_text)
#            if res:
#                await user.send_message(5137236682, f'{res.group()}')
#    except Exception as e:
#        await user.send_message(2028602503, str(e))
