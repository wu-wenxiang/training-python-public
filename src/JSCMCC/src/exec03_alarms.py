# -*- coding: UTF-8 -*- 
import pandas as pd
from exec01_count import getCityData, getProvinceData, getBsDataFromCache
from exec02_citys import getAlarmDataFromCache

def filterAlarmData(alarmData):
    alarmData = alarmData[alarmData['网管告警ID'] == '007-103-00-040012']
    alarmData = alarmData[(alarmData['工程状态'] != '退网')
                          & (alarmData['工程状态'] != '工程')]
    return alarmData

def buildAlarmCount(alarmData):
    alarmStart = pd.DataFrame({'告警时间':alarmData['告警发生时间'], '地市':alarmData['地市'], 'Delta':1})
    alarmEnd = pd.DataFrame({'告警时间':alarmData['告警恢复时间'], '地市':alarmData['地市'], 'Delta':-1})
    alarmCount = pd.concat([alarmStart, alarmEnd], axis=0)
    alarmCount.sort_values(by=['告警时间'], inplace=True)
    alarmCount['Count'] = 0
    alarmCount.reset_index(inplace=True, drop=True)
    
    zoneSet = set(alarmCount['地市'])
    zoneDict = dict(zip(zoneSet, [0]*len(zoneSet)))
    for i,delta,zone in zip(alarmCount.index, alarmCount['Delta'],
                            alarmCount['地市']):
        zoneDict[zone] += delta
        if zoneDict[zone] < 0:
            zoneDict[zone] = 0
        alarmCount.at[i,'Count'] = zoneDict[zone]
    return alarmCount

def buildAlarmStat(alarmCount, num, alarmId, alarmName):
    alarmCount['预警'] = alarmCount['Count'].apply(lambda x:x>=num)
    zoneDict = {}
    alarmStat = []
    for _i, row in alarmCount.iterrows():
        zoneDict.setdefault(row['地市'], (row['告警时间'], row['预警']))
        if row['预警'] == zoneDict[row['地市']][1]:
            continue
        if not row['预警']:
            alarmStat.append([zoneDict[row['地市']][0], row['告警时间'], row['地市']])
        zoneDict[row['地市']] = (row['告警时间'], row['预警'])
    for _zone,(_ts,status) in zoneDict.items():
        if status:
            alarmStat.append([zoneDict[row['地市']][0], None, row['地市']])
    alarmStat = pd.DataFrame(alarmStat, columns=['告警发生时间', '告警恢复时间', '告警对象ID'])
    alarmStat['网管告警ID'] = alarmId
    alarmStat['告警标题'] = alarmName
    return alarmStat
 
if __name__ == '__main__':
    provinceData = getProvinceData(r'../data/省区域.csv')
    provinceId = provinceData.loc['河南省']['区域ID']
    cityData = getCityData(r'../data/市区域.csv', provinceId)
    bsData = getBsDataFromCache(r'../tmp/_bsData.csv')
    alarmData = getAlarmDataFromCache(r'../tmp/_alarmData.csv')
    
    alarmData = filterAlarmData(alarmData)
#     alarmData[alarmData['地市']=='1005'].to_csv(r'../tmp/_alarmFilter.csv')
    alarmCount = buildAlarmCount(alarmData)
    alarmStat2 = buildAlarmStat(alarmCount, 60, '007-103-00-840002', '本地网大面积断站二级预警')
    alarmStat1 = buildAlarmStat(alarmCount, 150, '007-103-00-840001', '本地网大面积断站一级预警')
    alarmStat = pd.concat([alarmStat1, alarmStat2], axis=0)
    alarmStat['告警对象名称'] = alarmStat['告警对象ID'].apply(lambda x:cityData.loc[x]['区域名称'])
    
    columns = ['网管告警ID', '告警发生时间', '告警恢复时间', '告警对象名称', '告警标题', '告警对象ID']
    output = open(r'../tmp/alarms.csv', 'w', encoding='utf-8')
    for _i, row in alarmStat.iterrows():
        items = [row[i] for i in columns]
        line = ','.join('"%s"' % row[i] for i in columns)
        output.write('%s\n' % line)
    output.close()
    print('Run finished.')