# -*- coding: UTF-8 -*- 
import pandas as pd
import time
import collections
from exec01_count import getCityData, getProvinceData, getBsDataFromCache
from exec02_citys import getAlarmDataFromCache
from exec03_alarms import filterAlarmData, buildAlarmCount

def getCityTimeAlarm(alarmData, tsStart, tsEnd):
    alarmData['告警发生时间'] = alarmData['告警发生时间'].apply(lambda x:max([x, tsStart]))
    alarmData['告警恢复时间'] = alarmData['告警恢复时间'].apply(lambda x:min([x, tsEnd]))
    alarmData['中断秒数'] = (alarmData['告警恢复时间'] - alarmData['告警发生时间'])
    alarmData['中断秒数'] = alarmData['中断秒数'].apply(lambda x:x.total_seconds())
    cityTimeAlarm = alarmData.groupby(['地市'])['中断秒数'].sum()
    return pd.DataFrame(cityTimeAlarm).to_dict('index')

def getCityTime(bsData, tsStart, tsEnd):
    secDelta = (tsEnd-tsStart).total_seconds()
    cityTime = collections.Counter(bsData['市区域ID'])
    cityTime = {k:v*secDelta for k,v in cityTime.items()}
    return cityTime

def getCityPercent(alarmData, bsData, tsStart, tsEnd):    
    cityTime = getCityTime(bsData, tsStart, tsEnd)
    cityTimeAlarm = getCityTimeAlarm(alarmData, tsStart, tsEnd)
    cityTimeAlarm = {k:v['中断秒数'] for k,v in cityTimeAlarm.items()}
    cityTimeWork = {i:cityTime[i]-cityTimeAlarm.get(i,0) for i in cityTime}
    cityPercent = {i:cityTimeWork[i]/cityTime[i] for i in cityTime}
    return cityPercent

if __name__ == '__main__':
    startTime = time.time()
    provinceData = getProvinceData(r'../data/省区域.csv')
    provinceId = provinceData.loc['河南省']['区域ID']
    cityData = getCityData(r'../data/市区域.csv', provinceId)
    bsData = getBsDataFromCache(r'../tmp/_bsData.csv')
    alarmData = getAlarmDataFromCache(r'../tmp/_alarmData.csv')
    tsStart, tsEnd = pd.datetime(2018,8,8), pd.datetime(2018,8,9)
    alarmData = filterAlarmData(alarmData, tsStart, tsEnd)
    
    cityPercent = getCityPercent(alarmData, bsData, tsStart, tsEnd)
    worst = sorted(cityPercent, key=lambda x:cityPercent[x])[0]
    
    output = open(r'../tmp/cityname.csv', 'w', encoding='utf-8')
    output.write('"%s", "%.2f%%"\n' % (cityData.loc[worst]['区域名称'], cityPercent[worst]*100))
    output.close()
    print('Run finished, cost: %.2f sec' % (time.time()-startTime))