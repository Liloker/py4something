from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex  # 处理位数
from Crypto import Random


class PrpCrypt(object):
    def __init__(self, key):
        """
        初始化方法
        :param key:
        """
        self.key = key.encode('utf-8')  # 先将传进来的数据进行编码，utf-8是目前互联网中使用最为广泛的一种
        self.mode = AES.MODE_CBC  # 根据要求返回的数据，选择对应的算法，这里mode-cbc返回的是2
        self.iv = Random.new().read(AES.block_size)  # 随机生成十六进制数字 读取处理的数据

    def encrypto(self, text):
        """
        加密函数 如果text不足16位就使用空格来补足16位（16位 密钥规则）
        :return:统一加密后的字符串转换成16进制后的字符串
        """
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, self.iv)
        # 密钥长度   AES-128(16)    AES-192(24)     AES-256(32)     Bytes 长度
        length = 16
        # 用户输入的字符串长度
        count = len(text)
        if count < length:
            add = (length - count)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            text = text + ('\0' * add).encode('utf-8')

        self.ciphertext = cryptor.encrypt(text)  # 加密
        return b2a_hex(self.ciphertext)  # 返回16进制加密结果

    def dencrypto(self, text):
        """
        解密函数
        :return:
        """
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return bytes.decode(plain_text).rstrip('\0')  # rstrip去除空格,decode将二进制反编码为str

if __name__ == '__main__':  # 程序入口
    i = 1
    while i:
        judge = input('加密请输入1，解密请输入2：')
        if judge == '1':
            keys = input('请输入16位长度的加密密钥：')
            pc = PrpCrypt(keys)
            data = input('请输入你要加密的数据：')
            e = pc.encrypto(data)  # 加密
            print('加密', e)
        elif judge == '2':
            # key2 = input('请输入16位长度的解密密钥：')
            # pc = PrpCrypt(key2)
            data2 = input('请输入你需要解密的数据：')   # 解密encode编码
            d = pc.dencrypto(data2).encode()
            #d = pc.dencrypto(e).encode()
            #d = pc.dencrypto(b2a_hex(data2)).encode()   #Data must be padded to 16 byte boundary in CBC mode
            print('解密', d)