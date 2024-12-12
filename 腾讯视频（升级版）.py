import requests,re,pprint
url = 'https://vd6.l.qq.com/proxyhttp'
headers = {
    'refer':'https://v.qq.com/',
    'cookie':'qq_domain_video_guid_verify=ce4c32cf98b4611f; _qimei_uuid42=18b1e1436031001cec41c55f5d7ba7bb3a017a169c; _qimei_fingerprint=2c442ac4bbb0db2bc1d448a7d61743a5; pgv_pvid=4132009985; _qimei_h38=086db226ec41c55f5d7ba7bb02000005b18b1e; _qimei_q32=e201bfbcb1b50885f9ecee824c1e93a8; RK=8vdN0KaTHq; ptcz=b554771741d6d8235d35c1a6bbb28bab195539f37d51cd2f1c31ca0375ed5e4d; _qimei_q36=118003deac7101b87501c3b930001c318805; appuser=490354D1595DA285; lv_play_index=25; o_minduid=42uBvBvINLLtiE25V_gj-c0SbNwhJp5o; ad_session_id=ps6tkuy7noku2; ufc=r64_1_1732975987; pgv_info=ssid=s1120153887; vversion_name=8.2.95; video_omgid=ce4c32cf98b4611f; LPSJturn=83; LVINturn=902; LPHLSturn=834; LDERturn=163; LPPBturn=759; LZTturn=484; LPVLturn=564; LPLFturn=129',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
}
video_ids = ["q0043cz9x20","g0043coq0o9","j0043iim7f4","j0043trz63t","c004403vcth","d00449rnmkt","m00441gxqlm","q004481tx3m","p00444qbf0e","z0044g9u2eu","h0044an3ivq","v0044o4z52l","f0044r3j0wk","i00440o39cc","y0044c85f6k","c0044nelexp","c0044v6apa5","d0044q8qny5","x0044bz1hzv","l0044c0ijvb","d0044rz559u","v0045u848w1","p004593ixd2","e0045y5uojf","a0045clhgt1","s0045ijgu54","z004559evt1","p0045xgkh0a","w0045pj6ldc","w0045irgspv","s0045sst2xf","z0045zq3jp4","k0045fqhm4x","o0045izsb5h","g0045jxxr5l","v00452fsc7j","l0045ackra4","v0045ofdwmb","z00460kc935","a0046w7tx5n","v0046pkj3f4","s0046l2my82","l0046v689aq","o004642wru4","u004666xmlf","w0046ekr7zg","n0046xm8z39","a00467ug30i","c0046u15fgd","a0046azxa6u","v00461ufg8k","t00461sbfsc","f0046tem82w","j0046gce0dk","u00465uzz7k","h00460yq9qx","l0046l89vds","f0046wldqxo","w0046x0b61f","z004722zzg0","k0047cko40f","l0047gd6p19","g0047sfds6t","f00476ojdxh","m0047xl3iup","h004712um59","x0047gefz3r","c0047fx25re","v0047jnrzsv","c0047src7eq","b0047dnvxpw","g0047j3s2rc","h0047691aw0","q0047g0bvt5","h00479ejger","d00476lcv4u","l0047y1rnv7","d0047vhu7z5","u0047jwq84q","m004813geh9","k00483h9qw3","f0048m5ffqs","g0048avrg0w","q0048bhkehr","p0048853vo6","m0048f9wo8n","u00480s7zuv","r00485wmkxj","s0048jn22un","c004818xlkx","o00484foako","b4100elcvmu","x4100bao9vz","u4100ycjuqz","i4100z989g1","m41003o78fj","y4100a39f8d","d4100dyrfu4","r4100h4li6j","g4100onll9m","a410041u9ff","d4100rsrkxb","p4100uhl3un","i4100rzeplq","x4100gifzji","v4100c5euw3","j410053zoy4","e4100dbvz6u","t4100xcg4q2","h4100u5qsta","w4100flgtmv","o4100su0p56","h4100x0g1rs","p4100e8d632","y4100nyn3o0","m4100smgrr1","v4100tsbkcw","h410021nur4","b41005q1db5","p4100ayhmlz","k4100dso637","h4100kcuovx","h4100bcv8n7","u4100t6ql1a","d41001reb2d","i410097trtw","a4100e9rde9"]
sspAdParam = "{\"ad_scene\":1,\"pre_ad_params\":{\"ad_scene\":1,\"user_type\":2,\"video\":{\"base\":{\"vid\":\"q0043cz9x20\",\"cid\":\"mzc0020027yzd9e\"},\"is_live\":false,\"type_id\":3,\"referer\":\"https://v.qq.com/channel/cartoon\",\"url\":\"https://v.qq.com/x/cover/mzc0020027yzd9e/q0043cz9x20.html\",\"flow_id\":\"38336cbace2e1820bf4cfda1a8cc0bf3\",\"refresh_id\":\"9c974879032354bf37c0da78a3b8f76c_1733039217\",\"fmt\":\"fhd\"},\"platform\":{\"guid\":\"ce4c32cf98b4611f\",\"channel_id\":0,\"site\":\"web\",\"platform\":\"in\",\"from\":0,\"device\":\"pc\",\"play_platform\":10201,\"pv_tag\":\"|channel\",\"support_click_scan_integration\":true,\"qimei32\":\"e201bfbcb1b50885f9ecee824c1e93a8\"},\"player\":{\"version\":\"1.36.3\",\"plugin\":\"4.1.20\",\"switch\":1,\"play_type\":\"0\"},\"token\":{\"type\":1,\"vuid\":1712509234,\"vuser_session\":\"kEoE7JE7n13xP3Y5g9PzhA.M\",\"app_id\":\"101483052\",\"open_id\":\"6D4712A0534D8AB9CC546F43313D8DD6\",\"access_token\":\"A2BDDFB9B37527CDA2A7E84D12817826\"},\"req_extra_info\":{\"now_timestamp_s\":1733896103,\"ad_frequency_control_time_list\":{\"full_pause_short_vip\":{\"ad_frequency_control_time_list\":[1732975973]}}},\"extra_info\":{}}}"
vinfoparam = "charge=0&otype=ojson&defnpayver=3&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc0020027yzd9e%2Fq0043cz9x20.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc0020027yzd9e%2Fq0043cz9x20.html&sphttps=1&encryptVer=9.2&cKey=By3ve6MPx_S1MM1Orq2-LnCjnpb8Ocr0cPTenep1zEul_f4uOWcoVGJNR8Gp77I5PgBJjwwNlmrqCp7VHCeQghpmp7rG5tiHjLv_PnnatnPaZfOXktuBpd_Iyrki7YDMjF3w_IMO4pIsFjOj-NmZhE-NjjawCzIdF66cdsFdzz5jk70UOmynTHDptaxqIemxrSlkg-M_BbDaBoWwiX7uSsBkDK_qlv9BvC71CgXl1BaviS_BqOyu7myQxXaZw0af2pySApuO_cBm7THy64l64PYvrkyjWSbCwYTpt0h-SZN7K4XX143rt8mNnLeut5kJP7AFmOExsITvfbCpmYgjx7BFifu8ZqEYKbfoP7gBj8GpsUQVISZahbkTUidOkxpLSb0tc_4cPbE805dmqqxwlaO1dNCR_pe-oj7W56J11tgPi5fOMVGU1vb14Cj_huZELbu9pXacds9TRg9jpTmZy0BKpa_OswsXSoW8G9z4Z9LYWrK1wa7RHsg8WDbaDWlRBBWmbcUYyiZa_7PLazmCfs2fN4cEBAQEL7irWw&clip=4&guid=ce4c32cf98b4611f&flowid=38336cbace2e1820bf4cfda1a8cc0bf3&platform=10201&sdtfrom=v1010&appVer=1.36.3&unid=&auth_from=&auth_ext=&vid=q0043cz9x20&defn=uhd&fhdswitch=0&dtype=3&spsrt=2&tm=1733896103&lang_code=0&logintoken=%7B%22access_token%22%3A%22A2BDDFB9B37527CDA2A7E84D12817826%22%2C%22appid%22%3A%22101483052%22%2C%22vusession%22%3A%22kEoE7JE7n13xP3Y5g9PzhA.M%22%2C%22openid%22%3A%226D4712A0534D8AB9CC546F43313D8DD6%22%2C%22vuserid%22%3A%221712509234%22%2C%22video_guid%22%3A%22ce4c32cf98b4611f%22%2C%22main_login%22%3A%22qq%22%7D&spvvpay=1&spadseg=3&spvvc=3&spav1=15&hevclv=28&spsfrhdr=0&spvideo=0&spm3u8tag=67&spmasterm3u8=3&track=undefined&drm=40"
adparam = "adType=preAd&vid=q0043cz9x20&sspKey=sktv"
t = video_ids[0]
for i in range(len(video_ids)):
    sspAdParam = re.sub(t,video_ids[i],sspAdParam)
    vinfoparam = re.sub(t,video_ids[i],vinfoparam)
    adparam = re.sub(t,video_ids[i],adparam)
    t = video_ids[i]
    json = {
    "buid": "vinfoad",
    "vinfoparam": vinfoparam,
    "sspAdParam": sspAdParam,
    "adparam": adparam
}
    url_req = requests.post(url,headers=headers,json=json)
    url_req_t = url_req.text
    pprint.pprint(url_req_t)
    m3u8_url = 'https://'+re.findall(r'url\\":\\"https://(.*?)ver=4',url_req_t)[-1]+'ver=4'

    m3u8_req = requests.get(m3u8_url,headers=headers)
    ts_url = re.findall(r'^(.*?)gzc',m3u8_url)[0]
    a = m3u8_req.text
    a = a.split('\n')
    print(a)
    # with open('F:\年番\第37集.m3u8','wb') as f:
    with open(f'斗破苍穹年番\\第{i+1}集.m3u8','wb') as f:
        for j in a:
            str_j = str(j)
            if j.startswith('#') or j == '':
                continue
            else:
                ts_req = requests.get(ts_url+'/'+j,headers=headers)
                f.write(ts_req.content)