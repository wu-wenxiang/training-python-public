#-*- coding: utf-8 -*- 
#对数据进行基本的探索
#返回缺失值个数以及最大最小值

import os
import pandas as pd

DIR = r'/Users/wuwenxiang/Desktop/AirCustomer/test'
datafile = os.path.join(DIR, 'data', 'air_data.csv')
resultfile = os.path.join(DIR, 'data', 'air_data.xlsx')

data = pd.read_csv(datafile, encoding = 'utf-8') #读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）

explore = data.describe(percentiles = [], include = 'all').T #包括对数据的基本描述，percentiles参数是指定计算多少的分位数表（如1/4分位数、中位数等）；T是转置，转置后更方便查阅
explore['null'] = len(data)-explore['count'] #describe()函数自动计算非空值数，需要手动计算空值数
print(data.head())

data1 = data.loc[:, ['FFP_DATE', 'FLIGHT_COUNT', 'SUM_YR_1', 'SUM_YR_2', 'LAST_FLIGHT_DATE', 'avg_discount']]
data1['SUM_YR'] = data1['SUM_YR_1'] + data1['SUM_YR_2']
data1['FFP_DATE'] = pd.to_datetime('2014/03/31') - pd.to_datetime(data1['FFP_DATE'])
data1['FFP_DATE'] = data1['FFP_DATE'].dt.days
data1 = data1[data1['LAST_FLIGHT_DATE']!='2014/2/29  0:00:00']
data1['LAST_FLIGHT_DATE'] = pd.to_datetime('2014/03/31') - pd.to_datetime(data1['LAST_FLIGHT_DATE'])
data1['LAST_FLIGHT_DATE'] = data1['LAST_FLIGHT_DATE'].dt.days
print(data1.head())

explore = explore[['null', 'max', 'min']]
explore.columns = [u'空值数', u'最大值', u'最小值'] #表头重命名
'''这里只选取部分探索结果。
describe()函数自动计算的字段有count（非空值数）、unique（唯一值数）、top（频数最高者）、freq（最高频数）、mean（平均值）、std（方差）、min（最小值）、50%（中位数）、max（最大值）'''

explore.to_excel(resultfile) #导出结果