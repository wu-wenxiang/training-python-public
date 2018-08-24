# -*- coding: UTF-8 -*- 
import pandas as pd
from collections import Counter
from exec01_count import getBsDataFromCache

def getAlarmData(csv, bsData):
    alarmData = pd.read_csv(csv, header=None, dtype=str)
    alarmData.columns = ['告警流水号', '网管告警ID', '告警发生时间', '告警恢复时间', '告警对象名称']
    alarmData = alarmData[[i in bsData.index for i in alarmData['告警对象名称']]]
    alarmData['告警对象ID'] = alarmData['告警对象名称'].apply(lambda x:bsData.loc[x]['基站ID'])
    alarmData['工程状态'] = alarmData['告警对象名称'].apply(lambda x:bsData.loc[x]['基站状态'])
    alarmData['省'] = alarmData['告警对象名称'].apply(lambda x:bsData.loc[x]['省区域ID'])
    alarmData['地市'] = alarmData['告警对象名称'].apply(lambda x:bsData.loc[x]['市区域ID'])
    alarmData['区县'] = alarmData['告警对象名称'].apply(lambda x:bsData.loc[x]['所属区县ID'])
    alarmData['告警发生时间'] = pd.to_datetime(alarmData['告警发生时间'], infer_datetime_format=True)
    alarmData['告警恢复时间'] = pd.to_datetime(alarmData['告警恢复时间'], infer_datetime_format=True)
    alarmData.set_index('告警流水号', inplace=True)
    alarmData = alarmData[~alarmData.index.duplicated(keep='first')]
    return alarmData

def getAlarmDataFromCache(csv):
    alarmData = pd.read_csv(csv, dtype=str)
    alarmData['告警发生时间'] = pd.to_datetime(alarmData['告警发生时间'], infer_datetime_format=True)
    alarmData['告警恢复时间'] = pd.to_datetime(alarmData['告警恢复时间'], infer_datetime_format=True)
    alarmData.set_index('告警流水号', inplace=True)
    return alarmData
 
if __name__ == '__main__':
    bsData = getBsDataFromCache(r'../tmp/_bsData.csv')
    alarmData = getAlarmData(r'../data/告警.csv', bsData)
    alarmData.to_csv(r'../tmp/_alarmData.csv')
#     alarmData = getAlarmDataFromCache(r'../tmp/_alarmData.csv')
    alarmData = alarmData[(alarmData['告警发生时间'] >= pd.datetime(2018,8,8))
                          & (alarmData['告警发生时间'] < pd.datetime(2018,8,9))]
    
    output = open(r'../tmp/citys.csv', 'w')
    aDict = Counter(alarmData['地市'])
    aList = sorted(aDict, key=lambda x:aDict[x], reverse=True)
    output.write('\n'.join(str(aDict[i]) for i in aList[:3]))
    output.close()
    print('Run finished.')