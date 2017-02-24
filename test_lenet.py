# -*-coding:utf-8 -*-

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

caffe_root = '/media/vincent/2b883524-c33e-45ca-ab8d-a885f22e38d6/vincent/caffe/caffe/'

#把pycaffe添加到pythonpath中
sys.path.insert(0,caffe_root + 'python') 
import caffe

MODEL_FILE = '/media/vincent/2b883524-c33e-45ca-ab8d-a885f22e38d6/vincent/caffe/caffe/examples/mnist/lenet.prototxt'
PRETRAINED = '/media/vincent/2b883524-c33e-45ca-ab8d-a885f22e38d6/vincent/caffe/caffe/examples/mnist/lenet_iter_10000.caffemodel'

IMAGE_FILE = '/media/vincent/2b883524-c33e-45ca-ab8d-a885f22e38d6/vincent/caffe/caffe/examples/images/test4.bmp'

input_image = caffe.io.load_image(IMAGE_FILE, color=False)
net = caffe.Classifier(MODEL_FILE, PRETRAINED)
prediction = net.predict([input_image], oversample = False)
caffe.set_mode_cpu()
print 'predicted class:', prediction[0].argmax()


