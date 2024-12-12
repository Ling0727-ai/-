import requests,re,pprint
m3u8_url = input()
ts_url = re.findall(r'^(.*?)gzc',m3u8_url)[0]
#有时得着手寻找ts_url

headers = {
    'refer':'https://v.qq.com/',
    'cookie':'',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}

m3u8_req = requests.get(m3u8_url,headers=headers)

#存储m3u8_req的信息
a = m3u8_req.text
a = a.split('\n')
print(a)
s = input('请输入集数')
# with open('F:\年番\第37集.m3u8','wb') as f:
with open(f'F:\\斗破苍穹年番\\第{s}集.m3u8','wb') as f:
    for i in a:
        str_i = str(i)
        if i.startswith('#') or i == '':
            continue
        else:
            ts_req = requests.get(tsda_url+'/'+i,headers=headers)
            f.write(ts_req.content)

#这种方法可以使用，但是容易被识别出来，过一段时间可能刷新cookie值，需要重新寻找cookie值
