import os
import shutil

def mkdir(path):#生成文件夹
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")
    else:
        print("---  There is this folder!  ---")

file1 = "A:\PythonEnvironment\Pycharm_location_projects\Myprojects\FDD_3Sites_xml\EAK065"
mkdir(file1)  # 调用函数
file2 = "A:\PythonEnvironment\Pycharm_location_projects\Myprojects\FDD_3Sites_xml\EJD690"
mkdir(file2)
file3 = "A:\PythonEnvironment\Pycharm_location_projects\Myprojects\FDD_3Sites_xml\EJD779"
mkdir(file3)


def move_file(src_path, dst_path, file):
    print ('from : ',src_path)
    print ('to : ',dst_path)
   # try:
        # cmd = 'chmod -R +x ' + src_path
        # os.popen(cmd)
    f_src = os.path.join(src_path, file)
    # if not os.path.exists(dst_path):
    #     os.mkdir(dst_path)
    f_dst = os.path.join(dst_path, file)
    shutil.move(f_src, f_dst)
    #redis.set(file, 'move_success')
    # except Exception as e:
    #     print ('move_file ERROR: ',e)
    #     traceback.print_exc()

filePath = "A:\PythonEnvironment\Pycharm_location_projects\Myprojects\FDD_3Sites_xml"
name = os.listdir(filePath) #os.listdir()用于返回指定的文件夹下包含的文件或文件夹名字的列表，这个列表按字母顺序排序
tar1 = 'EAK065'
tar2 = 'EJD690'
tar3 = 'EJD779'
tar0 = 'xml'
for i in range(36):
    #print(name[i])
    if tar0 in name[i] and tar1 in name[i]:
        move_file(filePath, file1, name[i])
    if tar0 in name[i] and tar2 in name[i]:
        move_file(filePath, file2, name[i])
    if tar0 in name[i] and tar3 in name[i]:
        move_file(filePath, file3, name[i])