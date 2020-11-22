import sys
import requests as r
import json
import telepot

tele_enable=False
sign='https://n.cg.163.com/api/v2/sign-today'
current='https://n.cg.163.com/api/v2/client-settings/@current'
cookie=''
try:
    with open('cookie.txt','r') as f:
        cookie=f.read()
        f.close
except FileNotFoundError as e:
    print('[网易云游戏自动签到]无法读取Cookie，请检查是否正确设置Cookie！错误回显为：\n{}'.format(e))
    sys.exit()
except Exception as e:
    print('[网易云游戏自动签到]无法读取Cookie，回显为\n{}'.format(e))
    sys.exit()

try:
    with open('teleid.txt','r') as f:
        teleid=f.read()
        f.close()

    with open('teletoken.txt','r') as f:
        teletoken=f.read()
        f.close
    tele_enable=True
except:
    tele_enable=False

if tele_enable:
    bot=telepot.Bot(teletoken)


getheader={
    'Host': 'n.cg.163.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Platform': '0',
    'Authorization': cookie,
    'Origin': 'https://cg.163.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://cg.163.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5'  
}

signheader={
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5',
    'Authorization': cookie,
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Host': 'n.cg.163.com',
    'Origin': 'https://cg.163.com',
    'Referer': 'https://cg.163.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Platform': '0'
}

def signin(url,header):
    result=r.post(url=url,headers=header)
    return result

def getme(url,header):
    result=r.get(url=url,headers=header)
    print(result)
    return result

def send(id,message):
    if tele_enable:
        bot.sendMessage(id, message, parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)

if __name__ == "__main__":
    if cookie=='':
        print('[网易云游戏自动签到]未设置Cookie！正在退出……')
        sys.exit()
    me=getme(current,getheader)
    if(me.status_code!=200):
        message='[网易云游戏自动签到]签到失败！请检查Cookie是否过期！或者附上报错信息到 https://github.com/GamerNoTitle/wyycg-autosignin/issues 发起issue'
        send(teleid,message)
        print(message)
        sys.exit()
    sign=signin(sign,signheader)
    if(sign.status_code==200):
        message='[网易云游戏自动签到]签到成功！'
        send(teleid,message)
        print(message)
    else:
        message='[网易云游戏自动签到]签到失败，回显状态码为{}\n具体错误信息如下：\n{}'.format(sign.status_code,sign.text)
