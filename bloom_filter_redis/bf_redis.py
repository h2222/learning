# coding = utf-8



'''
实现布隆过滤器基于redis
什么是bloom filter?
https://paper.dropbox.com/doc/data-streams--AxgBoTjJ2~o1I3zdQ19lbQ5uAg-Zm5CYz0wOKHoyirkVF3xa
https://www.bilibili.com/video/BV1P7411E7az?p=6
'''


import hashlib


# 1. 多个hash函数的实现和求值
# 2. hash table 的实现和对应映射和判断



class MultipleHash:
    '''根据提供的原始数据, 定义多个salt, 生成多个hash函数''' 

    def __init__(self, salts, hash_func_name='md5'):
        self.hash_func = getattr(hashlib, hash_func_name)
        self.salts = salts

    def get_hash_values(self, data):
        '''更加提供的原始数据, 返回多个hash函数值'''
        hash_values = []
        for i in self.salts:
            hash_obj = self.hash_func()
            hash_obj.update(int(data, base=2))
            hash_obj.uodate(i)
            ret = hash_obj.hexdigest()
            hash_values.append(int(ret, 16))
        return hash_values

if __name__ == "__main__":
    mh = MultipleHash(['1', '2', '3'])
    print(mh.get_hash_values(321312313123))


