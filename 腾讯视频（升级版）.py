import requests,re,pprint
url = 'https://vd6.l.qq.com/proxyhttp'
headers = {
    'refer':'https://v.qq.com/',
    'cookie':'',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
}
json = {
    "buid": "vinfoad",
    "vinfoparam": "charge=0&otype=ojson&defnpayver=3&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc0020027yzd9e%2Fb0047dnvxpw.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc0020027yzd9e%2Fb0047dnvxpw.html&sphttps=1&encryptVer=9.2&cKey=ceswRdXJGNq1MM1Orq2-LnCjnpb8Ocr0cPTenqaxzEul_f4uOWcoVGJNR8G677I5OgddwAxP0WrqCp7VHCeQghpmp7rG5tiHjLv_PnnatnPaZfOXktuBpd_Iyrki7YDMjF3j_IMO5pU4FjOj-NmZhE-NjjawCzIdF66cdsFdzz5jk70UOmynTHDptaxqIemxrSlkg-M_BbDaBoWwiX7uSsBkDK_qlv9BvC71CgXl1BaviS_BqOyu7myQxXaZw0af2pySApuO_cBm7THy64l64PYvrkyjWSbCwYTpt0h-SZN7K4XX143rt8mNnLeut5kJP7AFmOExsITvfbCpmYgjx7BFifu8ZqEYKbfoP7gBj8GpsUQVISZahbkTUidOkxpLSb0tc_4cPbE805dmqqxwlaO1dNCR_pe-oj7W56J3j4RSi5nPN1CRg6H04in-huZELbu9pXacds9TRg9jpTmZy0BKpa_OswsXSoW8G9z4Z9LYWrK1wa7RHsg8WDbaDWlRBBWmbXcZPvKKT-3rLhdlpteEDawEBAQEF0CNzg&clip=4&guid=ce4c32cf98b4611f&flowid=5b4da05c29a4748f10408f10bdfc41af&platform=10201&sdtfrom=v1010&appVer=1.36.3&unid=&auth_from=&auth_ext=&vid=b0047dnvxpw&defn=uhd&fhdswitch=0&dtype=3&spsrt=2&tm=1733978979&lang_code=0&logintoken=%7B%22access_token%22%3A%22A2BDDFB9B37527CDA2A7E84D12817826%22%2C%22appid%22%3A%22101483052%22%2C%22vusession%22%3A%22F4hIDnSgmfWUIQSppn7_1Q.M%22%2C%22openid%22%3A%226D4712A0534D8AB9CC546F43313D8DD6%22%2C%22vuserid%22%3A%221712509234%22%2C%22video_guid%22%3A%22ce4c32cf98b4611f%22%2C%22main_login%22%3A%22qq%22%7D&spvvpay=1&spadseg=3&spvvc=3&spav1=15&hevclv=28&spsfrhdr=0&spvideo=0&spm3u8tag=67&spmasterm3u8=3&track=undefined&drm=40",
    "sspAdParam": "{\"ad_scene\":1,\"pre_ad_params\":{\"ad_scene\":1,\"user_type\":2,\"video\":{\"base\":{\"vid\":\"b0047dnvxpw\",\"cid\":\"mzc0020027yzd9e\"},\"is_live\":false,\"type_id\":3,\"referer\":\"https://v.qq.com/channel/cartoon\",\"url\":\"https://v.qq.com/x/cover/mzc0020027yzd9e/v0046pkj3f4.html\",\"flow_id\":\"5b4da05c29a4748f10408f10bdfc41af\",\"refresh_id\":\"9c974879032354bf37c0da78a3b8f76c_1733039217\",\"fmt\":\"fhd\"},\"platform\":{\"guid\":\"ce4c32cf98b4611f\",\"channel_id\":0,\"site\":\"web\",\"platform\":\"in\",\"from\":0,\"device\":\"pc\",\"play_platform\":10201,\"pv_tag\":\"|x\",\"support_click_scan_integration\":true,\"qimei32\":\"e201bfbcb1b50885f9ecee824c1e93a8\"},\"player\":{\"version\":\"1.36.3\",\"plugin\":\"4.1.20\",\"switch\":1,\"play_type\":\"1\",\"img_type\":\"webp\"},\"token\":{\"type\":1,\"vuid\":1712509234,\"vuser_session\":\"F4hIDnSgmfWUIQSppn7_1Q.M\",\"app_id\":\"101483052\",\"open_id\":\"6D4712A0534D8AB9CC546F43313D8DD6\",\"access_token\":\"A2BDDFB9B37527CDA2A7E84D12817826\"},\"req_extra_info\":{\"now_timestamp_s\":1733978979,\"ad_frequency_control_time_list\":{\"full_pause_short_vip\":{\"ad_frequency_control_time_list\":[1732975973]}}},\"extra_info\":{}}}",
    "adparam": "adType=preAd&vid=b0047dnvxpw&sspKey=kpxb"
}
url_req = requests.post(url,headers=headers,json=json)
url_req_t = url_req.text
pprint.pprint(url_req_t)
m3u8_url = 'https://'+re.findall(r'url\\":\\"https://(.*?)ver=4',url_req_t)[-1]+'ver=4'
ts_url = re.findall(r'^(.*?)gzc',m3u8_url)[0]
m3u8_req = requests.get(m3u8_url,headers=headers)
print(url_req.text)
# #存储m3u8_req的信息
a = m3u8_req.text
a = a.split('\n')
print(a)

s = input('请输入集数')
with open(f'F:\\斗破苍穹年番\\第{s}集.m3u8','wb') as f:
    for i in a:
        str_i = str(i)
        if i.startswith('#') or i == '':
            continue
        else:
            ts_req = requests.get(ts_url+'/'+i,headers=headers)
            f.write(ts_req.content)
