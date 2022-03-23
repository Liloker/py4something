def print_menu():
    print("||---------------- 商品销售管理系统 ------------------||")
    print("||---- 1.添加用户信息               2.查询用户信息 ----||")
    print("||---- 3.删除用户信息               4.添加商品信息 ----||")
    print("||---- 5.查询商品信息               6.删除商品信息 ----||")
    print("||-----7.统计用户数量               8.统计商品销售总额 --||")
    print("||------------------ 10.退出系统  --------------------||")
    print("||---------------- 商品销售管理系统 ------------------||")


def add_user():
    user_inform = open("users.csv", "a+", encoding='UTF-8-sig')
    ID = input("请输入用户ID:>")
    name = input("请输入用户名:>")
    age = input("请输入用户年龄:>")
    usr = [ID, name, age]
    user_inform.write(",".join(usr) + "\n")
    print("添加成功！")
    user_inform.close()


def add_goods():
    goods_inform = open("goods.csv", "a+", encoding='UTF-8-sig')
    name = input("请输入添加商品名称:>")
    price = input("请输入添加商品价格:>")
    sell = input("请输入商品销量:>")
    good = [name, price, sell]
    goods_inform.write(",".join(good) + "\n")
    print("添加成功！")
    goods_inform.close()


def del_user():
    user_inform = open("users.csv", "r+", encoding='UTF-8-sig')
    i = input("请输入需要删除的用户ID:>")
    count = 0
    for j in user_inform.readlines():
        j = j.replace("\n", "")
        j = j.split(",")
        if i == j[0]:
            j[1] = ""
            user_inform.writelines(j)
            print("删除成功")
            count = count + 1
    if count == 0:
        print("没有相关用户！")
    user_inform.close()


def del_goods():
    goods_inform = open("goods.csv", "r+", encoding='UTF-8-sig')
    i = input("请输入需要删除的商品名称:>")
    count = 0
    for jj in goods_inform.readlines():
        jj = jj.replace("\n", "")
        jj = jj.split(",")
        if i == jj[0]:
            jj[1] = ""
            user_inform.writelines(j)
            print("删除成功")
            count = count + 1
    if count == 0:
        print("没有相关商品！")
    goods_inform.close()


def find_goods():
    goods_inform = open("goods.csv", "r+", encoding='UTF-8-sig')
    i = input("请输入需要查询的商品名称:>")
    count1 = 0
    for jk in goods_inform.readlines():
        jk = jk.replace("\n", "")
        jk = jk.split(",")
        if i == jk[0]:
            print(jk)
            count1 = count1 + 1
    if count1 == 0:
        print("没有相关商品！")
    goods_inform.close()


def find_user():
    user_inform = open("users.csv", "r+", encoding='UTF-8-sig')
    k = input("请输入需要查询的用户ID:>")
    count = 0
    for l in user_inform.readlines():
        l = l.replace("\n", "")
        l = l.split(",")
        if k == l[0]:
            print(l)
            count = count + 1
    if count == 0:
        print("没有相关用户！")
    user_inform.close()


def avr():
    age = 0
    for m in user_inform.readlines():
        m = m.replace("\n", "")
        m = m.split(",")
        age = age + int(m[2])
    avr = age / len(user_inform.readlines())
    print("用户平均年龄是{}岁".format(avr))
    user_inform.close()


def sum():
    sum = 0
    for o in goods_inform.readlines():
        o = o.replace("\n", "")
        o = o.split(",")
        print(o)
        sum = sum + int(o[2]) * int(o[1])
        print("销售总额是{}元".format(sum))
        goods_inform.close()


while True:
    print_menu()
    user_inform = open("users.csv", "r+", encoding='UTF-8-sig')
    goods_inform = open("goods.csv", "r+", encoding='UTF-8-sig')
    option = input("请输入您要进行的的操作：")
    if option == '1':
        add_user()
    if option == '2':
        find_user()
    if option == '3':
        del_user()
    if option == '4':
        add_goods()
    if option == '5':
        find_goods()
        user_inform.close()
        goods_inform.close()
    if option == '6':
        del_goods()
    if option == '7':
        z = len(user_inform.readlines())
        print("共有{}位用户".format(z))
    if option == '8':
        sum()
    if option == '10':
        print("正在退出")
        user_inform.close()
        goods_inform.close()
        break
