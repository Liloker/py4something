import os, shutil
import re


def replcaeFileName(pic_path,frname,bit):  # 修改pic_path路径下的文件名
    #piclist = os.listdir(pic_path)
    #total_num = len(piclist)
    i = 1
    #for pic in piclist:
    for folder, subfolders, files in os.walk(pic_path):
        for file in files:
            hz = os.path.splitext(file)[-1]#使用os.path.splitext(file)[-1]可获得以.开头的文件后缀名。
            temp = ("%s_%"+bit+"d") %(frname,int(i))  #数字统一为3位，不够的前面补0
            if hz in image_ext:
            #if pic.endswith(".jpg"):  # 修改成你自己想要重命名的文件格式
                old_path = os.path.join(os.path.abspath(pic_path), file)
                #只有当在脚本中执行的时候，os.path.abspath(__file__)才起作用，因为该命令是获取的当前执行脚本的完整路径，如果在交互模式或者terminate 终端中运行会报没有__file__这个错误
                new_path = os.path.join(os.path.abspath(pic_path), temp + hz)  # 修改成了1000+N这种格式
                os.renames(old_path, new_path)
                print("把原图片命名格式：" + old_path + U"转换为新图片命名格式：" + new_path)
                print(i,'done')
                i = i + 1


        # if pic.endswith(".png"):  # 修改成你自己想要重命名的文件格式
        #     old_path = os.path.join(os.path.abspath(pic_path), pic)
        #     new_path = os.path.join(os.path.abspath(pic_path), temp + '.png')  # 修改成了1000+N这种格式
        #     os.renames(old_path, new_path)
        #     print("把原图片命名格式：" + old_path + U"转换为新图片命名格式：" + new_path)
        #     print(i,'done')
        #     i = i + 1


def replaceDirName(rootDir):  # 修改rootDir路径下的文件夹名
    num = 0
    dirs = os.listdir(rootDir)
    for dir in dirs:
        print('oldname is:' + dir)  # 输出老的名字

        num = num + 1
        temp = "%04d" % int(num)  # 主要目的是在数字统一为3位，不够的前面补0

        oldname = os.path.join(rootDir, dir)  # 老文件夹的名字
        newname = os.path.join(rootDir, temp)  # 新文件夹的名字

        os.rename(oldname, newname)  # 替换


if __name__ == '__main__':
    rootDir = input("请输入需要整理文件夹的路径:")
    frname = input("请输入命名前缀:")
    bit = input("百度%02d表示法，这里输入02可表示2位，不够前面补0，下面请输入命名序号的位数:")
    #rootDir = 'A:\PythonEnvironment\Pycharm_location_projects\Myprojects\pic'
    image_ext = ['.JPG', '.jpg', '.png', '.PNG', '.jpeg', '.wdp','.mp3']
    #replaceDirName(rootDir)
    replcaeFileName(rootDir,frname,bit)



