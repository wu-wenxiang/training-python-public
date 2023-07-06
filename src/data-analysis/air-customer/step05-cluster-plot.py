#-*- coding: utf-8 -*-
#画出特征雷达图，代码接KMeans_cluster.py

import os
import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法

DIR = r'/Users/wuwenxiang/Desktop/AirCustomer/test'
# DIR = r'C:\Users\Administrator\Desktop\AirCustomer\test'

inputfile =os.path.join(DIR, 'tmp', 'zscoreddata.csv') #待聚类的数据文件
k = 5                       #需要进行的聚类类别数


#读取数据并进行聚类分析
data = pd.read_csv(inputfile) #读取数据

#调用k-means算法，进行聚类分析
kmodel = KMeans(n_clusters = k) #n_jobs是并行数，一般等于CPU数较好
kmodel.fit(data) #训练模型

print(kmodel.cluster_centers_) #查看聚类中心
a = kmodel.labels_
print(a[a==4]) #查看各样本对应的类别

import numpy as np
import matplotlib.pyplot as plt

labels = data.columns #标签
k = 5 #数据个数
plot_data = kmodel.cluster_centers_
color = ['b', 'g', 'r', 'c', 'y'] #指定颜色

angles = np.linspace(0, 2*np.pi, k, endpoint=False)
plot_data = np.concatenate((plot_data, plot_data[:,[0]]), axis=1) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合
labels = np.concatenate((labels, [labels[0]]))

fig = plt.figure()
ax = fig.add_subplot(111, polar=True) #polar参数！！
for i in range(len(plot_data)):
  ax.plot(angles, plot_data[i], 'o-', color = color[i], label = u'Cu_'+str(i), linewidth=2)# 画线

ax.set_rgrids(np.arange(0.01, 3.5, 0.5), np.arange(-1, 2.5, 0.5), fontproperties="SimHei")
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
plt.legend(loc = 4)
plt.show()