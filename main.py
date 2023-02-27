import base64

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from lxml import etree

response = requests.get('http://ggzy.zwfwb.tj.gov.cn/jyxxzfcg/index.jhtml')
data = etree.HTML(response.text)

parents = data.xpath("//div[@class='article-list3-t']")

for per_data in parents:
    publish_time = ''.join(per_data.xpath(".//div[@class='list-times']//text()"))
    title = ''.join(per_data.xpath(".//a//text()")).strip("\r\n").strip()
    url = ''.join(per_data.xpath("./a/@url"))
    key = 'qnbyzzwmdgghmcnm'
    hh = url
    aa = hh.split("/")
    aaa = len(aa)
    bbb = aa[aaa - 1].split('.')
    ccc = bbb[0]
    cccc = bbb[1]
    if cccc.find('jhtml') != -1:
        aes = AES.new(key.encode(), AES.MODE_ECB)
        res = aes.encrypt(pad(ccc.encode(), AES.block_size, style='pkcs7'))
        # 用base64转成字符串形式
        ddd = base64.b64encode(res).decode()
        ddd = ddd.replace("/", "^")
        ddd = ddd[0:-2]
        bbbb = ddd + '.' + bbb[1]
        aa[aaa - 1] = bbbb

        uuu = ''
        for i in aa:
            uuu += i + '/'
        uuu = uuu.strip('/')
        url = uuu
        # print(uuu)
    print(url, title, publish_time)
