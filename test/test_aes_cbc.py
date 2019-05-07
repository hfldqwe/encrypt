import time
from encrypt.aes_cbc import encrypt,decrypt

data = "Qp3Brxm6FxpW46akTJKDiDBcX2fkQEWtD8XXr3T8dsBtd7PBmxjeR5MJz8DYdaKw100818"
key = "PvK5RllH5DNInTCs"
# iv在以前的版本，也就是使用pycrypto模块不需要进行二进制处理，但是在pycrypto‎demo中要求更严格，所以必须使用bytes
iv = "hjD3RYMadSmCFFAt".encode()

t1 = time.time()
# 加密
en = encrypt(data, key, iv)
t2 = time.time()
print("加密时间：", t2 - t1)

t1 = time.time()
# 解密
de = decrypt(en, key, iv)
t2 = time.time()
print("解密时间：", t2 - t1)

print("加密之后的字符串：", en)
print("解密之后的字符串：", de)