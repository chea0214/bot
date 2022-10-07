# 引入库文件，基于telethon
from telethon import events
# 从上级目录引入 jdbot,chat_id变量
from .. import jdbot, chat_id
# 格式基本固定，本例子表示从chat_id处接收到包含hello消息后，要做的事情
from requests_html import HTMLSession


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/getweibo$')))
async def wendu(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的命令，请稍后')
    try:
        text = getweibo(True)
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, text)
    except Exception as e:
        await jdbot.send_message(chat_id, f'错误：{str(e)}')


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/getweibo1$')))
async def wendu1(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的命令，请稍后')
    try:
        text = getweibo(False)
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, text)
    except Exception as e:
        await jdbot.send_message(chat_id, f'错误：{str(e)}')


def getweibo(xq):
    url = "https://weibo.com/a/hot/realtime"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
        # "Accept:": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Cookie": "UOR=www.51testing.com,widget.weibo.com,www.baidu.com; SINAGLOBAL=5598083413392.782.1618740936707; ULV=1620394889833:6:2:2:8343914145429.253.1620394889820:1620062517984; SUB=_2AkMXyctyf8NxqwJRmf0Ry2LrboR-zwjEieKhlTqpJRMxHRl-yj92qkwZtRB6PEnlnaoG_6gBtc_5OHhKPBowG1ldUbXF; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhjMP0yYi9qTFH0EWvI2GKj; login_sid_t=5e6bf8dc4eae3667ab0a23df70be4cea; wb_view_log=1440*9001; _s_tentry=-; Apache=8343914145429.253.1620394889820; httpsupgrade_ab=SSL; WBStorage=8daec78e6a891122|undefined"
    }
    tt = ''
    i = 0
    des = ""
    try:
        session = HTMLSession()
        response = session.get(url, headers=headers)
        if response:
            # print(response.html.text)
            for a in response.html.xpath("//h3[@class='list_title_b']/a[@class='S_txt1']"):
                i += 1
                link = f'https://weibo.com/a/hot/{a.attrs["href"]}'
                r = session.get(link, headers=headers)
                title = r.html.xpath('//h2[@class="list_title"]/text()', first=True).strip()
                title = title.strip('\n')
                title = title.replace('#', '')
                if xq:
                    des = r.html.xpath('//div[@class="list_des"]/text()', first=True).strip()
                    des = des.replace('\n', '')
                    tt += str(i) + '. ' + title + '\n' + des + '\n'
                else:
                    tt += str(i) + '. ' + title + '\n'
                if len(tt) > 3900:
                    break
            return tt
    except Exception as e:
        return f'出错：{str(e)}'
