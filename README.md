爬虫基本原理

本质：模拟用户向网页发送请求，再将请求到的数据保存下来
(建议使用python12.6以后的版本、以及pycharm)

重点：找到所需的url

>需要使用的第三方库： 
> >requests、lxml、re
---
>可利用的第三方库：
> >fake_useragent、urllib（和requests的作用类似、但功能更全面）、hashlib（数据筛选）、pandas（数据处理）

>爬虫进阶使用的第三方库：
> >scrapy
---
准备
```
pip install requests

pip install lxml

pip install fake_useragent

pip install urllib3

pip install hashlib

pip install pandas

pip install scrapy
```
---
___

>寻找url的方式： 
>1. F12 network
>2. 抓包工具如Fiddler、Winshark
