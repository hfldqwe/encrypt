# 加密的使用

## 基本描述

在文件夹`encrypt`中基本上都是基本的加密和解密

## AES-BCB-128加密

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
