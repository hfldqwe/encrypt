# coding=utf-8
# AES AES/CBC/PKCS5|Zero

import base64
from Crypto.Cipher import AES
import time


def ByteToHex(bins):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """
    return ''.join(["%02X" % x for x in bins]).strip()


'''
采用AES对称加密算法
'''
# str不是16的倍数那就补足为16的倍数. ZeroPadding

'''
    在PKCS5Padding中，明确定义Block的大小是8位
    而在PKCS7Padding定义中，对于块的大小是不确定的，可以在1-255之间
    PKCS #7 填充字符串由一个字节序列组成，每个字节填充该字节序列的长度。
    假定块长度为 8，数据长度为 9，
    数据： FF FF FF FF FF FF FF FF FF
    PKCS7 填充： FF FF FF FF FF FF FF FF FF 01 01 01 01 01 01 01   ?应该是填充01

    python3:填充bytes(这个说法不对,AES的参数是字符串,不是byte)
    length = 16 - (len(data) % 16)
    data += bytes([length])*length

    python2:填充字符串
    length = 16 - (len(data) % 16)
    data += chr(length)*length

    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    unpad = lambda s : s[0:-ord(s[-1])]
'''


def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


def ZeroPadding(value, bs):
    while len(value) % bs != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes

def PKCS7Padding(value, bs):
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)  # PKS7
    return str.encode(pad(value))  # 返回bytes


def PKCS7UnPadding(value):
    # value = value[:-value[-1]]
    unpad = lambda s: s[0:-ord(s[-1])]  # 获得数据的长度,截取
    return unpad(value)

# 加密方法
def encrypt_oracle(data,key,iv):
    '''
    使用AES-BCB进行加密
    :param data: 待加密的数据
    :param key:秘钥
    :param iv:偏移量
    :return:加密文本
    '''
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_CBC, iv)
    bs = AES.block_size

    # 先进行aes加密
    # Zeropadding
    # encrypt_aes = aes.encrypt(add_to_16(text))
    # Pkcs7 padding 加密之后转化成了二进制格式
    encrypt_aes = aes.encrypt(PKCS7Padding(data,bs))

    # 转为hex格式字符串
    #print(ByteToHex(encrypt_aes))

    # 转为base64格式字符串
    encrypted_b64 = str(base64.b64encode(encrypt_aes), encoding='utf-8')

    return encrypted_b64


# 解密方法
def decrypt_oralce(encrypted_data,key,iv):
    '''
    使用AES-BCB进行解密
    :param encrypted_data: 待解密的数据
    :param key:秘钥
    :param iv:偏移量
    :return:解密数据
    '''
    aes = AES.new(add_to_16(key), AES.MODE_CBC, iv)
    # 将base64解码
    base64_decrypted = base64.b64decode(encrypted_data.encode("utf-8"))
    # 解密
    decrypt_data = str(aes.decrypt(base64_decrypted), encoding='utf-8')  # 执行解密密并转码返回str

    # 去掉填充字符串
    # PADDING = '\0'
    # print decrypted_text.rstrip(PADDING)  #zeropadding只见诶去掉结尾\0
    return PKCS7UnPadding(decrypt_data)

if __name__ == '__main__':
    data = "Qp3Brxm6FxpW46akTJKDiDBcX2fkQEWtD8XXr3T8dsBtd7PBmxjeR5MJz8DYdaKw100818"
    key = "PvK5RllH5DNInTCs"
    iv = "hjD3RYMadSmCFFAt"

    t1 = time.time()
    en = encrypt_oracle(data,key,iv)
    t2 = time.time()
    print("加密时间：",t2-t1)

    t1 = time.time()
    de = decrypt_oralce(en,key,iv)
    t2 = time.time()
    print("解密时间：",t2-t1)

    print("加密之后的字符串：",en)
    print("解密之后的字符串：",de)
