class yh_info(object):  # 首先创建表达商品对象的yh_info类
    def __init__(self, id, name, phone, age):
        self.id = id
        self.name = name
        self.phone = phone
        self.age = age

    def __str__(self):
        info = "用户ID:%s\t姓名:%s\t电话:%d\t年龄:%d" % (self.id, self.name, self.phone, self.age)
        return info

