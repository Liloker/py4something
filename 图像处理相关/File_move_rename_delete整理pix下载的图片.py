#该程序可用来移动图片，其他格式的文档也是可以的
import os, shutil
import datetime

#将文件夹里的图片全部移动到新文件夹中，如果目标文件夹有相同文件名，利用系统时间来重命名
def renameFile(dstpath):
    fdirname,fbasename=os.path.split(dstpath)#将目标文件路径切片为目录名和文件名
    #文件名相同但大小不同
    fname,fext=os.path.splitext(fbasename)#将文件名切片成文件名和文件后缀名
    nowtime=datetime.datetime.now()
    strtime=str(nowtime.year)+str(nowtime.month)+str(nowtime.day)+str(nowtime.hour)+str(nowtime.minute)
    newfbasename=fname+'-'+strtime+fext
    dstpath=os.path.join(fdirname,newfbasename)#粘合文件目录名和新的文件名
    return dstpath

def moveFile(oldpath,newpath):
    if os.path.exists(newpath):#如果移动目标文件夹有相同名字的文件，则改名
        newpath=renameFile(newpath)
    try:
        shutil.move(oldpath,newpath)#使用shutil来实现移动
        print(oldpath+' is moved')
    except:
        print(oldpath+' is skipped')


def replcaeFileName(pic_path):  # 修改pic_path路径下的文件名
    #piclist = os.listdir(pic_path)
    #total_num = len(piclist)
    i = 1
    #for pic in piclist:
    for folder, subfolders, files in os.walk(pic_path):
        for file in files:
            hz = os.path.splitext(file)[-1]#使用os.path.splitext(file)[-1]可获得以.开头的文件后缀名。
            temp = "%03d" % int(i)  # 主要目的是在数字统一为3位，不够的前面补0
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


# def replaceDirName(rootDir):  # 修改rootDir路径下的文件夹名
#     num = 0
#     dirs = os.listdir(rootDir)
#     for dir in dirs:
#         print('oldname is:' + dir)  # 输出老的名字
#
#         num = num + 1
#         temp = "%03d" % int(num)  # 主要目的是在数字统一为3位，不够的前面补0
#
#         oldname = os.path.join(rootDir, dir)  # 老文件夹的名字
#         newname = os.path.join(rootDir, temp)  # 新文件夹的名字
#
#         os.rename(oldname, newname)  # 替换


if __name__ == '__main__':#整个程序有待进一步精简优化，功能主要是将母文件夹中的子文件夹內的文件指定移动到另外的一个文件夹中并对其数字序号重命名
#################################################################################################################
#准备工作将路径设置好，这里也可以做成交互式的路径读取
    inpath = input("你想整理哪个路径下的文件？（粘贴路径）")
    outpath = input("整理完，你想放在哪里？")
    #inpath = r'A:\PythonEnvironment\Pycharm_location_projects\Myprojects\Pic - 副本'
    #outpath = r'A:\PythonEnvironment\Pycharm_location_projects\Myprojects\Pic - 副本'
    image_ext = ['.JPG', '.jpg', '.png', '.PNG', '.jpeg', '.wdp']  # 常见的图像格式，作为列表
    # image_outpath=os.path.join(outpath,'image')#在目标文件夹中创建新目录
    # doc_ext=['.doc','.docx'] #用于对其他格式的文件进行操作
    # doc_outpath=os.path.join(outpath,'doc')
    # emf_ext=['.emf']
    # emf_outpath=os.path.join(image_outpath,'emf')
    # wmf_ext=['.wmf']
    # wmf_outpath=os.path.join(image_outpath,'wmf')
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    # if not os.path.exists(image_outpath):
    #     os.makedirs(image_outpath)
    # if not os.path.exists(doc_outpath):
    #     os.makedirs(doc_outpath)
    # if not os.path.exists(emf_outpath):
    #     os.makedirs(emf_outpath)
    # if not os.path.exists(wmf_outpath):
    #     os.makedirs(wmf_outpath)

#####################################################################################################
#将零碎的文件夹中的文件集中到一个地方
    for folder, subfolders, files in os.walk(inpath):#os.walk在给定的目录里面游走
        for file in files:
            oldpath = os.path.join(folder, file)
            if os.path.splitext(file)[-1] in image_ext:
                #用法： os.path.splitext(“文件路径”)    分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作
                newpath = os.path.join(outpath, file)
            #   newpath = os.path.join(image_outpath, file)
                moveFile(oldpath, newpath)#这里并没有用绝对路径
            #其他类型的文件类似下面的操作即可
            # elif os.path.splitext(file)[-1] in doc_ext:
            #     newpath = os.path.join(doc_outpath, file)
            #     moveFile(oldpath, newpath)
            # elif os.path.splitext(file)[-1] in emf_ext:
            #     newpath = os.path.join(emf_outpath, file)
            #     moveFile(oldpath, newpath)
            # elif os.path.splitext(file)[-1] in wmf_ext:
            #     newpath = os.path.join(wmf_outpath, file)
            #     moveFile(oldpath, newpath)
            else:
                continue
    print('done')
##################################################################################################
    #然后再删除零碎的空文件夹
    #import os, shutil
    # 将文件夹里的空文件夹删除
    #inpath = r'A:\PythonEnvironment\Pycharm_location_projects\Myprojects\Pic - 副本'

    for folder, subfolders, files in os.walk(inpath):
        if not os.listdir(folder):
            shutil.rmtree(folder)
            # print(folder+' is empyt')
            print(folder + ' is deleted')
##################################################################################################
    #重命名文件名
    # rootDir = input("请输入需要整理文件夹的路径:")
    #rootDir = 'A:\PythonEnvironment\Pycharm_location_projects\Myprojects\pic - 副本'
    # image_ext = ['.JPG', '.jpg', '.png', '.PNG', '.jpeg', '.wdp']
    # replaceDirName(rootDir)
    replcaeFileName(outpath)
