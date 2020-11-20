import sys
import requests as r
import json

sign=''
current='https://n.cg.163.com/api/v2/client-settings/@current'
cookie=sys.argv[1]

header={
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

def post(url,data,header):
    result=r.post(url=url,headers=header)
    return result

def getme(url,data,header):
    result=r.get(url=url,headers=header)
    print(result)
    return result

if __name__ == "__main__":
    me=getme(current,None,header)
    print(me.text)