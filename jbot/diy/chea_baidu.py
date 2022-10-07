# 引入库文件，基于telethon
from telethon import events
# 从上级目录引入 jdbot,chat_id变量
from .. import jdbot, chat_id
# 格式基本固定，本例子表示从chat_id处接收到包含hello消息后，要做的事情
import requests
import json


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/getbaidu')))
async def baidu(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的命令，请稍后')
    try:
        text = getbaidu("realtime")
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, text)
    except Exception as e:
        await jdbot.send_message(chat_id, f'错误：{str(e)}')


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/getbook')))
async def book(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的命令，请稍后')
    try:
        text = getbaidu("novel")
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, text)
    except Exception as e:
        await jdbot.send_message(chat_id, f'错误：{str(e)}')


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/getdianying')))
async def dianying(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的命令，请稍后')
    try:
        text = getbaidu("movie")
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, text)
    except Exception as e:
        await jdbot.send_message(chat_id, f'错误：{str(e)}')


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/getdianshiju')))
async def dianshiju(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的命令，请稍后')
    try:
        text = getbaidu("teleplay")
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, text)
    except Exception as e:
        await jdbot.send_message(chat_id, f'错误：{str(e)}')


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/getzongyi')))
async def zongyi(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的命令，请稍后')
    try:
        text = getbaidu("variety")
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, text)
    except Exception as e:
        await jdbot.send_message(chat_id, f'错误：{str(e)}')


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/getqiche')))
async def qiche(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的命令，请稍后')
    try:
        text = getbaidu("car")
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, text)
    except Exception as e:
        await jdbot.send_message(chat_id, f'错误：{str(e)}')


def getbaidu(tabdes):
    url = f"https://top.baidu.com/board?tab={tabdes}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
    }
    tt = ''
    i = 0
    try:
        res = requests.get(url, headers=headers).text
        jsontxt = res[res.index("content\":")+9:res.index(",\"more")]
        jss = json.loads(jsontxt)
        for js in jss:
            i += 1
            desc = ""
            showtxt = ""
            title = js['word'] + "\n"
            if js['desc']:
                desc = js['desc'] + "\n"
            for show in js['show']:
                showtxt = showtxt + show + "\n"
            tt = tt + str(i) + "、" + title + showtxt + desc
        tt = tt[:4096]
        return tt
    except Exception as e:
        return f'出错：{str(e)}'
