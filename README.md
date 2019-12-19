# 加密的使用

## 基本描述

在文件夹`encrypt`中基本上都是基本的加密和解密

## AES BCB 128加密

**信息门户加密方式**

```python
from encrypt.aes_cbc import encrypt,decrypt

# 加密
en = encrypt(data, key, iv)

# 解密
de = decrypt(en, key, iv)
```
**参数：**

data：str，待加密数据

key：str，密钥

iv：bytes，偏移量


## RSA 非对称加密 1024

**易班登录采用的加密方式**

加密之后长度为：172（有可能经过url编码之后长度有所改变）

```python
from encrypt.rsa import encrypt,decrypt

# 加密
cipher = encrypt(message, public_key)

# 解密
decrypt(cipher, private_key)
```

**参数：**

message：str，待加密数据

public_key：str，公钥

private_key：str，秘钥