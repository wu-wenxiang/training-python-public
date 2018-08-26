# -*- coding: UTF-8 -*- 
import pandas as pd
import time
import math
from exec01_count import getCityData, getProvinceData, getBsDataFromCache
from exec02_citys import getAlarmDataFromCache
from exec03_alarms import filterAlarmData, buildAlarmCount

def _buildFaultCount(alarmDataCity, tsStart, tsEnd):
    minDelta = int((tsEnd-tsStart).total_seconds()//60)
    faultList = [[tsStart+pd.Timedelta(minutes=i), 0] for i in range(minDelta)]
#     print('Step 2===>, cost: %.2f sec' % (time.time()-startTime))
    alarmDict = alarmDataCity.to_dict('records')
    M1 = pd.Timedelta(minutes=1)
    for row in alarmDict:
        faultList = [[i,j] if (row['告警发生时间']>=(i+M1) or row['告警恢复时间']<i) 
                     else [i,j+math.ceil((i+M1-row['告警发生时间']).total_seconds()//60)] 
                     for (i,j) in faultList]
    return faultList

def _buildFaultStat(alarmData, city, num, tsStart, tsEnd):
    alarmDataCity = alarmData[alarmData['地市'] == city]
    faultList = _buildFaultCount(alarmDataCity, tsStart, tsEnd)
#     print('Step 2==>, cost: %.2f sec' % (time.time()-startTime))
    faultList = [[i,j,j>=num] for (i,j) in faultList]
    cityCache = [faultList[0][0], False]
    faultStat = []
    for ts,_count,faultFlag in faultList:
        if cityCache[1] == faultFlag:
            continue
        if not faultFlag:
            faultStat.append([cityCache[0], ts])
        cityCache = [ts, faultFlag]
    if faultList[-1][2]:
        faultStat.append([cityCache[0], None])
    return [i+[city] for i in faultStat]

def buildFaultStat(alarmData, num, alarmId, alarmName, tsStart, tsEnd):
    faultStat = []
    alarmData = alarmData[['地市', '告警发生时间', '告警恢复时间']]
    for i in set(cityData.index):
        faultStat.extend(_buildFaultStat(alarmData, i, num*60, tsStart, tsEnd))
#         print('Step 2=>%s, cost: %.2f sec' % (i, time.time()-startTime))
    faultStat = pd.DataFrame(faultStat, columns=['告警发生时间', '告警恢复时间', '告警对象ID'])
    faultStat['网管告警ID'] = alarmId
    faultStat['告警标题'] = alarmName
    return faultStat

if __name__ == '__main__':
    startTime = time.time()
    provinceData = getProvinceData(r'../data/省区域.csv')
    provinceId = provinceData.loc['河南省']['区域ID']
    cityData = getCityData(r'../data/市区域.csv', provinceId)
    bsData = getBsDataFromCache(r'../tmp/_bsData.csv')
    alarmData = getAlarmDataFromCache(r'../tmp/_alarmData.csv')
    tsStart, tsEnd = pd.datetime(2018,8,8), pd.datetime(2018,8,9)
    alarmData = filterAlarmData(alarmData, tsStart, tsEnd)
#     print('Step 1, cost: %.2f sec' % (time.time()-startTime))
    faultStat2 = buildFaultStat(alarmData, 120, '007-103-00-940002',
                                '本地网大面积基站中断二级严重告警', tsStart, tsEnd)
    faultStat1 = buildFaultStat(alarmData, 240, '007-103-00-940001',
                                '本地网大面积基站中断一级严重告警', tsStart, tsEnd)
    faultStat = pd.concat([faultStat1, faultStat2], axis=0)
    faultStat['告警对象名称'] = faultStat['告警对象ID'].apply(lambda x:cityData.loc[x]['区域名称'])
     
    columns = ['网管告警ID', '告警发生时间', '告警恢复时间', '告警对象名称', '告警标题', '告警对象ID']
    output = open(r'../tmp/faults.csv', 'w', encoding='utf-8')
    for _i, row in faultStat.iterrows():
        items = [row[i] for i in columns]
        line = ','.join('"%s"' % row[i] for i in columns)
        output.write('%s\n' % line)
    output.close()
    print('Run finished, cost: %.2f sec' % (time.time()-startTime))