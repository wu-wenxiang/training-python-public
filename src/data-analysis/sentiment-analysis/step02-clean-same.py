#-*- coding: utf-8 -*-
import pandas as pd

DIR = '/Users/wuwenxiang/Desktop/other/chapter15/demo'

inputfile = f'{DIR}/data/meidi_jd.txt' #评论文件
outputfile = f'{DIR}/data/meidi_jd_process_1.txt' #评论处理后保存路径
data = pd.Series([line for line in open(inputfile)])
l1 = len(data)
data = pd.DataFrame(data.unique())
l2 = len(data)
data.to_csv(outputfile, index = False, header = False, encoding = 'utf-8')
print(u'删除了%s条评论。' %(l1 - l2))