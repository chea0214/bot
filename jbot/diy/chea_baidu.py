# 引入库文件，基于telethon
from telethon import events
# 从上级目录引入 jdbot,chat_id变量
from .. import jdbot, chat_id
# 格式基本固定，本例子表示从chat_id处接收到包含hello消息后，要做的事情
from requests_html import HTMLSession


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
        text = getothe("novel")
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, text)
    except Exception as e:
        await jdbot.send_message(chat_id, f'错误：{str(e)}')


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/getdianying')))
async def dianying(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的命令，请稍后')
    try:
        text = getothe("movie")
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, text)
    except Exception as e:
        await jdbot.send_message(chat_id, f'错误：{str(e)}')


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/getdianshiju')))
async def dianshiju(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的命令，请稍后')
    try:
        text = getothe("teleplay")
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, text)
    except Exception as e:
        await jdbot.send_message(chat_id, f'错误：{str(e)}')


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/getzongyi')))
async def zongyi(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的命令，请稍后')
    try:
        text = getothe("variety")
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, text)
    except Exception as e:
        await jdbot.send_message(chat_id, f'错误：{str(e)}')


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/getqiche')))
async def qiche(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的命令，请稍后')
    try:
        text = getothe("car")
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
    ii = 0
    try:
        session = HTMLSession()
        response = session.get(url, headers=headers)
        if response:
            test = response.html.xpath("//div[@class='content_1YWBm']/div[2]/text()")
            dess = [ii for ii in test if ii != ' ']
            for title in response.html.xpath("//div[@class='c-single-text-ellipsis']/text()"):
                title = title.strip()
                des = dess[i]
                i += 1
                tt += str(i) + '. ' + title + '\n' + des + '\n'
                if i > 25:
                    break
            tt = tt[:4096]
            return tt
    except Exception as e:
        return f'出错：{str(e)}'


def getothe(tabdes):
    url = f"https://top.baidu.com/board?tab={tabdes}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
    }
    tt = ''
    i = 0
    try:
        session = HTMLSession()
        response = session.get(url, headers=headers)
        if response:
            dess = response.html.xpath("//div[@class='content_1YWBm']/div[1]/text()")
            dess2 = response.html.xpath("//div[@class='content_1YWBm']/div[2]/text()")
            test = response.html.xpath("//div[@class='c-single-text-ellipsis desc_3CTjT']/text()")
            dess3 = [i for i in test if i != ' ']
            for title in response.html.xpath("//div[@class='c-single-text-ellipsis']/text()"):
                title = title.strip()
                if len(dess) != 0:
                    des = dess[i]
                    tt += str(i + 1) + '. ' + title + '\n' + des + '\n'
                if len(dess2) != 0:
                    des2 = dess2[i]
                    tt += des2 + '\n'
                if len(dess3) != 0:
                    des3 = dess3[i]
                    tt += des3 + '\n'
                i += 1
            tt = tt[:4096]
            return tt
    except Exception as e:
        return f'出错：{str(e)}'
