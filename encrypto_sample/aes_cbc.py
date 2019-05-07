from encrypt import aes_cbc
import random
import time

string = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'
def random_string(iterable,length):
    '''
    从一个指定可迭代对象中取可重复的随机长度的字符串
    :param iterable:
    :param length:
    :return:
    '''
    sequence = [random.choice(iterable) for i in range(length)]
    return "".join(sequence)

def encrypt_aes(data,key):
    '''
    爬虫过程中遇到的一个实际加密的逻辑
    :param data: 数据
    :param key: 密钥
    :return: 加密字符串
    '''
    data = random_string(string, 64)+str(data)
    key = key
    iv = random_string(string, 16).encode()

    return aes_cbc.encrypt(data, key, iv)

if __name__ == '__main__':
    pwd = 146542
    key = "PvK5RllH5DNInTCs"

    print(encrypt_aes(pwd,key))