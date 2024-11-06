import requests
import json
import time

LIKESLIMIT = 1000

headers = {
    'Referer': 'https://www.bilibili.com/video/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.199.400 QQBrowser/11.8.5300.400'
}
cookies = {
    'SESSDATA': ''
}

oid = 974017259

res = requests.get(url = f'https://api.bilibili.com/x/v2/reply/count?type=1&oid={oid}', headers = headers, cookies = cookies)
count = json.loads(res.text)['data']['count']
r = 0
pn = 0

while r < count and pn < 251:
    pn = pn + 1
    r = r + 20
    res = requests.get(url = f'https://api.bilibili.com/x/v2/reply?type=1&oid={oid}&sort=1&pn={pn}&nohot=1', headers = headers, cookies = cookies)
    # print(res.text)
    data = json.loads(res.text)['data']
    replies = data['replies']
    for reply in replies:
        like = reply['like']
        stime = reply['ctime']
        message = reply['content']['message']
        uname = reply['member']['uname']
        if like > LIKESLIMIT:
            print("%s：%s\nat %s likes %d\n" % (uname, message, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stime)), like))
    time.sleep(0.1)