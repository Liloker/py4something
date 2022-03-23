data = {'陕西': {'西安':
                         {'户县': ['户太八号', '草堂烟雾'],'蓝田县': ['温泉溶洞', '暖玉核桃']},
                 '铜川':
                         {'宜君县': ['穷乡僻壤', '鸟不拉屎'],'耀县': ['物晋天华', '人杰地灵']}
                },
        '广东': {'广州':
                         {'珠海': ['物华天宝', '路不拾遗'],'白云': ['善恶难辨', '真假难分']},
                 '深圳':
                         {'龙华': ['风高放火', '月黑杀人'],'龙岗': ['钱过北斗', '米烂成仓']}
                }
        }
exit_flag = False
while not exit_flag:
    for i in data:
        print(i)
    choice = input('选择进入>>1: ')
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print('\t', i2)
            choice2 = input('选择进入>>2: ')
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print('\t', i3)
                    choice3 = input('选择进入>>3: ')
                    if choice3 in data[choice][choice2]:
                        while not exit_flag:
                            for i4 in data[choice][choice2][choice3]:
                                print('\t\t', i4)
                            choice4 = input('最后一层,按b返回: ')
                            if choice4 == 'b':
                                break
                            elif choice4 == 'q':
                                exit_flag = True
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = True