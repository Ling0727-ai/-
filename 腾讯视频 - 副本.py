import requests,re,pprint
m3u8_url = input()
ts_url = re.findall(r'^(.*?)gzc',m3u8_url)[0]
# ts_url = 'https://ltsxmty.gtimg.com/B_tRCdt2L6hl1ezG-aht1_p2lNJdTchBBRNPdK-x19c-D3T9ZZXyo7nZ-iY9wStnWB/BkdVCkmGzvkam5vpCZDBnu2vJ8lV70wNs9OS-SMsjgUNWHsFBg52wImdnW3Oy1jgcGAzJicF35YZsL06w4Ayb_n2YR9N0rulGxtH8ENZSu0f3cs1wPKZrTb_kRoAEa218jkWLNYkUsnJGWQzWFUhJ6P-ebTZ-rrc93OO_Y7zHYncwwzs645x3JhXXQPtRECrjgDNufXrcvgzuizUZIz84XYyGjvsGFi-0qHSFOlnhZxL9IDHKesTJg/'
url = 'https://vd6.l.qq.com/proxyhttp'
# print(ts_url)
headers = {
    'refer':'https://v.qq.com/',
    'cookie':'RK=pmdFkqaDTq; ptcz=4502498dbc1960c01c5544b0d3c05722c375c2cbcb04dc1a31294f4bfcf3c5ae; qq_domain_video_guid_verify=c687c9f46c595882; _qimei_uuid42=188060f1c3a100a0dc12311f5db8b57121faf26652; _qimei_h38=716d2633dc12311f5db8b57102000008a18806; video_platform=2; pgv_pvid=3179327564; video_guid=c687c9f46c595882; _qimei_q32=e201bfbcb1b50885f9ecee824c1e93a8; _qimei_q36=118003deac7101b87501c3b930001c318805; pac_uid=0_9QSDJt7sT4jX0; suid=user_0_9QSDJt7sT4jX0; QIMEI32=e201bfbcb1b50885f9ecee824c1e93a8; fqm_pvqid=5ba16826-2a4a-4aeb-ab1a-49caf0c01688; o_cookie=1163840260; eas_sid=v1Z7e381Z1T3w7O1X6T5r6v8j8; check_16=46fe47dd598bacf3feed81d1c6550691; _qimei_fingerprint=2c442ac4bbb0db2bc1d448a7d61743a5; pgv_info=ssid=s4188433376; vversion_name=8.2.95; video_omgid=c687c9f46c595882; _qpsvr_localtk=0.29945409556430147; role=0; p_vuserid=0; main_login=qq; vqq_access_token=1B34EFE3E0CA27DC10D2A0481873171A; vqq_appid=101483052; vqq_openid=6D4712A0534D8AB9CC546F43313D8DD6; vqq_vuserid=1712509234; vqq_vusession=hAn8ydkxR6jaHnJXuGrC8Q.M; vqq_refresh_token=F480A9391CB5646D959D688B67DB669E; login_time_init=2024-11-28 9:13:21; qq_nick=%E7%9B%B8%E5%AE%88; qq_head=https%3A%2F%2Fcommunity.image.video.qpic.cn%2F1234_08f6bf-2_997249819_1692892384876752; vqq_next_refresh_time=6596; vqq_login_time_init=1732756403; login_time_last=2024-11-28 9:13:24',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}
data = {}
m3u8_req = requests.get(m3u8_url,headers=headers)
# url_req = requests.post(url,headers=headers,data=data)
# print(url_req.text)
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
            ts_req = requests.get(ts_url+'/'+i,headers=headers)
            f.write(ts_req.content)