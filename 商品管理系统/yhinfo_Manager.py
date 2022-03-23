from yhinfo import yh_info


class yhinfo_Manager(object):  # 将对于用户信息操作的函数放到yhinfo_Manager类当中，功能包括管理员以及普通用户的，在登录后进行分流选择

    def __init__(self, path):  # path:表示读取文件的路径 yhdic：表示存放内存的容器
        self.path = path
        self.yhdic = self.readFileToDic()

    def readFileToDic(self):  # 读取文件，写入到字典中
        fy = open(self.path, 'r', encoding='utf-8', errors='ignore')
        ylist = fy.readlines()
        fy.close()
        index = 0
        yhdic = {}
        while index < len(ylist):  # 将每一行的字符串进行分割，存放到新的列表中
            ylist = ylist[index].replace('\n', "").split("|")  # 将每行的内容存放到一个对象中
            yhinfo = yh_info(ylist[0], ylist[1], int(ylist[2]), int(ylist[3]))  # 将对向存放到集合中
            yhdic[yh_info.id] = yhinfo
            index = index + 1
        return yhdic

    def writeContentFile(self):  # 将内存当中的信息写入到文件当中
        str1 = ''
        for key in self.yhdic.keys():
            yh_info = self.yhdic[key]
            ele = yh_info.id + "|" + yh_info.name + "|" + str(yh_info.phone) + "|" + str(yh_info.age) + "\n"
            str1 = str1 + ele
            f = open(self.path, 'w', encoding='utf-8', errors='ignore')
            f.write(str1)
            f.close()

    def addGoods(self):  # 添加商品的方法
        id = input("请输入添加商品编号:>")
        if self.yhdic.get(id):
            print("商品编号已存在，请重新选择！")
            #return
        else:
            name = input("请输入添加商品名称:>")
            price = int(input("请输入添加商品价格:>"))
            good = Goods(id, name, price)
            self.yhdic[id] = good
            print("添加成功！")

    def deleteGoods(self):  # 删除商品的方法
        id = input("请输入删除商品编号:>")
        if self.yhdic.get(id):
            del self.yhdic[id]
            print("删除成功！")
        else:
            print("商品编号不存在！")

    def showGoods(self):  # 展示所有商品信息
        # print("=" * 40)
        for key in self.yhdic.keys():
            good = self.yhdic[key]
            print(good)
            print("=" * 40)

    def adminWork(self):
        info = """
        ==========欢迎进入好海哦购物商场==========
        输入功能编号，您可以选择以下功能：
        输入“1”：显示商品的信息
        输入“2”：添加商品的信息
        输入“3”：删除商品的信息
        输入“4”：退出系统功能
        ==========================================
        """
        print(info)
        while True:
            code = input("请输入功能编号:>")
            if code == "1":
                self.showGoods()
            elif code == "2":
                self.addGoods()
            elif code == "3":
                self.deleteGoods()
            elif code == "4":
                print("感谢您的使用，正在退出系统！！")
                self.writeContentFile()
                break
            else:
                print("输入编号有误，请重新输入！！")

    def userWork(self):
        print(" ==============欢迎进入好海哦购物商场==============")
        print("您可输入编号和购买数量选购商品，输入编号为n则结账")
        self.showGoods()
        total = 0
        while True:
            id = input("请输入购买商品编号:>")
            if id == "n":
                print("本次购买商品共消费%d元，感谢您的光临！" % (total))
                break
            if self.yhdic.get(id):
                good = self.yhdic[id]
                num = int(input("请输入购买数量:>"))
                total = total + good.price * num
            else:
                print("输入商品编号有误，请核对后重新输入！")

    def login(self):  # 登录功能
        print("==========欢迎登录好海哦购物商场==========")
        uname = input("请输入用户名:>")
        password = input("请输入密码:>")
        if uname == "admin":
            if password == "123456":
                print("欢迎您，admin管理员")
                self.adminWork()
            else:
                print("管理员密码错误，登录失败！")
        else:
            print("欢迎你，%s用户" % (uname))
            # 执行用户的购买功能
            self.userWork()

