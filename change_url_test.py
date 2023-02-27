# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: change_url_test.py
# @Author: Yunchang,Wang
# @E-mail: 360812146@qq.com
# @Site: 
# @Time: 2月 28, 2023
# ---
import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# result = 'http://ggzy.zwfwb.tj.gov.cn:80/jyxxcgjg/X^taCNA1q62qn1w3MI5ILA.jhtml'
# 网页源代码链接
url = 'http://ggzy.zwfwb.tj.gov.cn:80/jyxxcgjg/1005397.jhtml'
# 密钥 s
key = 'qnbyzzwmdgghmcnm'
# 网页源代码的链接分解赋值
hh = url
aa = hh.split("/")
aaa = len(aa)
bbb = aa[aaa - 1].split('.')
ccc = bbb[0]
cccc = bbb[1]
# 使用CryptoJS进行AES加密
if cccc.find('jhtml') != -1:
    # 初始化加密器，本例采用ECB加密模式
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
    print(url)
