# 引入库文件，基于telethon
from telethon import events
# 从上级目录引入 jdbot,chat_id变量
from .. import jdbot, chat_id, CONFIG_DIR
# 格式基本固定，本例子表示从chat_id处接收到包含hello消息后，要做的事情


@jdbot.on(events.NewMessage(chats=chat_id, pattern=('^/cookie')))
# 定义自己的函数名称
async def hi(event):
    msg = await jdbot.send_message(chat_id, '正在查询您的常用命令，请稍后')
    ENV_SH_FILE = f'{CONFIG_DIR}/env.sh'
    cookies = '找到Cookie如下：\n'
    with open(ENV_SH_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    try:
        for line in lines:
            if line.find('JD_COOKIE') != -1:
                cookies += line
        await jdbot.delete_messages(chat_id, msg)
        await jdbot.send_message(chat_id, cookies)
    except Exception as e:
        await jdbot.send_message(chat_id, f'完成{str(e)}')
