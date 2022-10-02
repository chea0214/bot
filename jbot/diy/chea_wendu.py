# 引入库文件，基于telethon
from telethon import events
# 从上级目录引入 jdbot,chat_id变量
from .. import jdbot, chat_id
# 格式基本固定，本例子表示从chat_id处接收到包含hello消息后，要做的事情
import requests


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/getwendu')))
# 定义自己的函数名称
async def wendu(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的命令，请稍后')
    try:
        text = getwendu()
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, text)
    except Exception as e:
        await jdbot.send_message(chat_id, f'错误：{str(e)}')

icomfort = {
    '9999': '',
    '4': '很热，极不适应',
    '3': '热，很不舒适',
    '2': '暖，不舒适',
    '1': '温暖，较舒适',
    '0': '舒适，最可接受',
    '-1': '凉爽，较舒适',
    '-2': '凉，不舒适',
    '-3': '冷，很不舒适',
    '-4': '很冷，极不适应'
}


def json_path_value(jsondict, path):
    try:
        num = 1
        pahts = path.split(".")
        mydict = {}
        for p in pahts:
            if num == 1:
                mydict = jsondict[p+""]
                num = num+1
            else:
                mydict = mydict[p+""]
                num = num+1
        return mydict
    except Exception as e:
        print("从路径失败中获取值，异常为 "+str(e))
        return None


def getwendu():
    txt = '周至县天气预报'
    url = 'http://www.nmc.cn/rest/weather?stationid=57032'
    try:
        html = requests.get(url)
        jsont = (html.json())
        txt += '\n        温度：' + str(json_path_value(jsont, 'data.real.weather.temperature'))
        txt += '\n        湿度：' + str(json_path_value(jsont, 'data.real.weather.humidity'))
        txt += '\n体感温度：' + str(json_path_value(jsont, 'data.real.weather.feelst'))
        txt += '\n        天气：' + str(json_path_value(jsont, 'data.real.weather.info'))
        txt += '\n空气质量：' + str(json_path_value(jsont, 'data.air.text'))
        txt += '\n    舒适度：' + icomfort[str(json_path_value(jsont, 'data.real.weather.icomfort'))]
        txt += '\n更新时间：' + str(json_path_value(jsont, 'data.real.publish_time'))
        detail = json_path_value(jsont, 'data.predict.detail')
        txt += '\n天气预报：' + str(detail[1]['date'])
        txt += '\n最高温度：' + str(json_path_value(detail[1], 'day.weather.temperature'))
        txt += '\n最低温度：' + str(json_path_value(detail[1], 'night.weather.temperature'))
        txt += '\n        天气：' + json_path_value(detail[1], 'day.weather.info') + '转' + json_path_value(detail[1], 'night.weather.info')
        txt += '\n更新时间：' + str(detail[1]['pt'])
        return txt
    except Exception as error:
        return f'出错：{str(error)}'
