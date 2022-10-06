from .login import user
from .. import chat_id
from telethon import events
import requests
import re


QL_URL = "http://172.17.0.5:5700"
Client_Id = "4V-ZvI8Y_NK6"
Client_Secret = "c4-KUDKG74Zq6Ux5Wm0fW1-2"
Authorization = ""

KuName = "Faker2 助力池版"
listen_CK = -1001253455116
KeyWord = "本次变动如下"

listen_CH = -1001670294604


res = requests.get(QL_URL + "/open/auth/token?client_id=" + Client_Id + "&client_secret=" + Client_Secret).json()
if res['code'] == 200:
    Authorization = res['data']['token']

headers = {
           'Authorization': f'Bearer {Authorization}',
           'Content-Type': 'application/json'
          }


@user.on(events.NewMessage(pattern=r'^拉库$', outgoing=True))
async def subupdate(event):
    text = LQCK()
    await event.edit(text)


@user.on(events.NewMessage(pattern=r'^拉库日志$', outgoing=True))
async def subupdate_log(event):
    text = "开始提取日志..."
    res = requests.get(QL_URL + "/open/subscriptions", headers=headers).json()
    if res['code'] == 200:
        for subs in res['data']:
            if subs['name'] == KuName:
                res = requests.get(QL_URL + "/open/subscriptions/" + str(subs['id']) + "/log", headers=headers).json()
                if res['code'] == 200:
                    text = res['data']
                else:
                    text = "日志提取失败"
        else:
            text = "未找到关键字仓库"
    else:
        text = "订阅获取失败"
    await event.edit(res['data'])


@user.on(events.NewMessage(incoming=True))
async def mylisten(event):
    if event.is_channel:
        if event.chat_id == listen_CK:
            res = re.search(KeyWord, event.raw_text)
            if res:
                await user.send_message(2028602503, str("更新仓库"))
                LQCK()
#       elif event.chat_id == listen_CH:
#           res = re.findall("LUCK_DRAW_URL=\"(\S*)\"", event.raw_text)
#           if res:
#               ZXRW("LUCK_DRAW_URL", res[0], "jd_luck_draw.js")


def LQCK():
    res = requests.get(QL_URL + "/open/subscriptions", headers=headers).json()
    if res['code'] == 200:
        for env in res['data']:
            if env['name'] == KuName:
                ress = requests.put(QL_URL + "/open/subscriptions/run", json=[env['id']], headers=headers).json()
                if ress['code'] == 200:
                    text = "订阅更新开始..."
                else:
                    text = "订阅更新未执行，请检查"
        else:
            text = "未找到拉库设置的名称"
    else:
        text = "青龙登录失败，请检查青龙地址、Client_Id、Client_Secret"
    return text


def ZXRW(key, vlaue, jscripts):
    url = QL_URL + "/open/envs"
    data = ([{
            "name": f"{key}",
            "value": f"{vlaue}",
            }])
    res = requests.get(url, headers=headers).json()
    if res['code'] == 200:
        for env in res['data']:
            if env['name'] == f"{key}":
                requests.delete(url, json=[env['id']], headers=headers).json()
        res = requests.post(url, json=data, headers=headers).json()
        if res['code'] == 200:
            res = requests.get(QL_URL + "/open/crons", headers=headers).json()
            if res['code'] == 200:
                for cron in res['data']:
                    if cron["command"].find(f"{jscripts}") != -1:
                        requests.put(QL_URL + "/open/crons/run", json=[cron["id"]], headers=headers).json()
