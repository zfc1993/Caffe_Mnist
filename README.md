# Caffe_Mnist
mnist caffe linux

# Part 1
# Linux下安装配置caffe
一、安装依赖项
1.打开命令行控制台（哪个目录下也可以），输入以下命令，安装基本依赖（General dependencies）。

sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler  
sudo apt-get install --no-install-recommends libboost-all-dev  

注意：由于网络情况的不同，一次安装可能不能全部安装成功，重复输入上述命令，再次安装（本人用了三次），这里建议大家一次安装一个软件包，便于弄清是那个未安装成功，以节省时间。

2.安装ATLAS，输入下述命令：

sudo apt-get install libatlas-base-dev  

3.安装剩余依赖：

sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev  

之后编译时可能会要求安装numpy 即：sudo apt-get install python-numpy

二、PYTHON需要2.7版本（ubuntu系统内置）,这是操作系统本身已经安装好的. 输入python2.7 --version 会显示具体的版本号说明安装了.
但是还需要sudo apt-get install python-dev

三、安装git clone github上的caffe至本地


四、修改配置文件
到CAFFE文件夹, 使用模板写个Makefile.config. 具体就是先复制一下模板, 再改一些内容(我喜欢用EMACS).
cp Makefile.config.example Makefile.config
-因为CPU MODE, 所以在CPU_ONLY := 1前面的#要去掉.
-两个路径要改成这样:(添加后面的两个hdf5的路径, 否则编译时报hdf5错误)
# Whatever else you find you need goes here.
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial
LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu/hdf5/serial
 
五、执行编译
make pycaffe 需要进入caffe目录下？？？
make all
make test
make runtest
--结果显示ALL TESTS PASSED就安装好了, 只需要再加上一个PYTHONPATH  怎么加？？在哪儿加？？
命令行进入 python import os import sys sys.path.insert(0,'CAFFE_ROOT' + ‘python’);
每次python调用caffe都得加一次么？好像是的！！！如果是的话 能不能一下加好？？？

references:
http://blog.csdn.net/oyjxer/article/details/51824254
http://www.linuxidc.com/Linux/2016-09/135034.htm

# Part 2
# Linux 下使用caffe+mnist数据集训练lenet
1、定义网络protobuf file（里面包含了训练集数据层和测试集数据层） and solver protobuf file（用于模型调优）

2、调用脚本文件train_lenet.sh 进行模型训练（或者进入caffe可执行文件所在的目录位置 linux下为 ./build/tools/ 直接命令行 caffe train --solver examples/mnist/lenet_solver.prototxt ）

3、最终的模型被存储为binary protobuf file at lenet_iter_10000(训练执行10000次时的参数), which you can deploy as a trained model in your application, if you are training on a real-world application dataset.

4、最后的到的这个model使用三种方法：命令行、python接口、matlab接口 详见caffe-tutorials-interfaces

5、使用最后训练得到的参数及原网络模型进行测试（测试集也在该网络模型中定义了层）

# python接口调用caffe
确保已经编译过pycaffe (make pycaffe) 

测试单张图片 确保图片格式被转化为caffe接受的格式 

import caffe (每次都需要先把pycaffe添加到 PYTHONPATH中 )
import sys sys.path.insert(0,'caffe_root + 'python'')

#指定网络结构 与 lenet_train_test.prototxt不同 

#网络结构
MODEL_FILE = '你的caffe路径/examples/mnist/lenet.prototxt' 

#训练好参数的模型
PRETRAINED = '你的caffe路径/examples/mnist/lenet_iter_10000.caffemodel'
