from skimage import data_dir,io,transform,color#导入包，如果没有，请安装：  pip install skimage 
import numpy as np


def convert_gray(f):
     rgb=io.imread(f)    #依次读取rgb图片
     gray=color.rgb2gray(rgb)   #将rgb图片转换成灰度图
     dst=transform.resize(gray,(768,1024))  #将灰度图片大小转换为256*256,这里是说是裁剪，但实际上是拉伸
     return dst


#str='d:/train'+'/*.jpg'  #我的图片存放在目录'd:/train'中
str='A:\PythonEnvironment\Pycharm_location_projects2\Calibration_ZhangZhengyou_Method\pic\my_RGB_calib_img'+'/*.jpg'
#str = input("需要处理的图片文件夹路径:")
#outfile = input("彩色转灰度图之后存放路径:")
coll = io.ImageCollection(str,load_func=convert_gray)
for i in range(len(coll)):
    io.imsave(r'A:\PythonEnvironment\Pycharm_location_projects2\Calibration_ZhangZhengyou_Method\pic\my_IR_calib_img\0'+np.str(i)+'.jpg', coll[i])  # 循环保存图片,存放在提前建立的空文件夹'd:/train1/'
    #io.imsave('d:/train1'+np.str(i)+'.jpg',coll[i])#循环保存图片,存放在提前建立的空文件夹'd:/train1/'