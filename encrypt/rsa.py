# -*- coding: utf-8 -*-
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64


# rsa算法生成实例
def get_key():
    rsa = RSA.generate(1024, Random.new().read)
    # master的秘钥对的生成
    private_pem = rsa.exportKey()
    public_pem = rsa.publickey().exportKey()

    return {
        "public_key": public_pem.decode(),
        "private_key": private_pem.decode()
    }

# 生成的公钥私钥对
private_key = """-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgQC2I3U7bH2DCTl/hkopZhq0mGx0paQVU9+w+Xm5w4h8Y2MzhCSg
M47PCi9Rirho8PGmJptagfS/lsq+LHt2eDiEoDLD3ICTBVlVlmvHnwQvK5xzmRUS
qJiZuJIjM89rGLk2avdMk0U+GrGTrPI7T/6mFBnfhGC9ly9SKVAjJCzaHQIDAQAB
AoGAIObjWsZ0ntrn/Nomo/danCSLtP+mFic2WasbWtwQV/4BMdFtZ1Yg9lQd66I+
QVDDKlM/jZg7vO9RtQxmiiZZ+QaMwNViKO9voZU2JmhAnj55B0phjUFVEgmv9rt9
9eO/G9O+Z5v/JsYQsrnJ5f2bSVvf4Y27+WhQayqkj7ZzjEkCQQC731eXq/n90HRB
/93wJWJ5VO4Zk8LW/modXALI/b6PQ9jWUq8EcLpl3ucXql7ZvU16IBIWyPn+Ut6B
QP4qZBElAkEA+C/SWjSxYv3WjFolbpqAJVQxWyMas7+0zG7MmTsHN7yBsLo7UpoX
dpRC4sGoPXcDEIuXpZ6otPs73C28DQS/mQJAL/NeMOkFAmIs+hdrNvrjumIR71dG
WIdQ4DN2xoP1Gi3P70vlPbXj7VJKG0ExulNVrgD3fPdIzz+paMYE2R73PQJAd1iv
w9cQ8jR0ppt24qADPXAmJ9hSr9thOumRE6JyDxhkGTME8ezNmaUkINzVZXFElQE7
lFYedKFXoMKRaoU9CQJAIIXKHEo4exl/EGnywr2yhpBnbFe5eW8qSz783LFD24Ke
PrtKHZYrA2Anz6m2nNd/42PaMgp7BY5FlYTrrrXRQA==
-----END RSA PRIVATE KEY-----"""

public_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC2I3U7bH2DCTl/hkopZhq0mGx0
paQVU9+w+Xm5w4h8Y2MzhCSgM47PCi9Rirho8PGmJptagfS/lsq+LHt2eDiEoDLD
3ICTBVlVlmvHnwQvK5xzmRUSqJiZuJIjM89rGLk2avdMk0U+GrGTrPI7T/6mFBnf
hGC9ly9SKVAjJCzaHQIDAQAB
-----END PUBLIC KEY-----
"""

# 公钥加密
def encrypt(message, public_key):
    rsakey = RSA.importKey(public_key)  # 导入读取到的公钥
    cipher = PKCS1_v1_5.new(rsakey)  # 生成对象
    # 通过生成的对象加密message明文，注意，在python3中加密的数据必须是bytes类型的数据，不能是str类型的数据
    cipher_text = base64.b64encode(
        cipher.encrypt(message.encode(encoding="utf-8")))
    # 公钥每次加密的结果不一样跟对数据的padding（填充）有关
    return cipher_text.decode()


# 公钥解密
def decrypt(cipher_text, private_key):
    rsakey = RSA.importKey(private_key)  # 导入读取到的私钥
    cipher = PKCS1_v1_5.new(rsakey)  # 生成对象
    # 将密文解密成明文，返回的是一个bytes类型数据，需要自己转换成str
    text = cipher.decrypt(base64.b64decode(cipher_text), "ERROR")
    return text.decode()


if __name__ == '__main__':
    message = "hello world!"
    cipher = encrypt(message, public_key)
    print("加密字符串：",cipher)
    print("长度：", len(cipher))

    msg = decrypt(cipher, private_key)
    print("解密后字符串：",msg)
