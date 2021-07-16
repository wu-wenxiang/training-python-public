'''
Tip_120108 IIS Log Analysis

日志文件：https://share.weiyun.com/5zY4yG9

Code:
'''

aList = [i.split() for i in open('test.txt', encoding='utf-8') if i.startswith('20')]
bList = 'date time s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) sc-status sc-substatus sc-win32-status time-taken'.split()

# print(aList[:5], end='')
# print(bList)

import pandas as pd

p = pd.DataFrame(aList, columns=bList)
p1 = p.loc[:, ['cs-uri-stem', 'cs-method', 'c-ip', 'time-taken']]
p1['datetime'] = pd.to_datetime(p['date']+' '+p['time'])
p1['time-taken'] = pd.to_numeric(p1['time-taken'])
pTime = p1.set_index('datetime')
pTimeAll = pTime.loc[:, ['time-taken']].resample(rule = '1T').count()
pTime20S = pTime[pTime['time-taken']>20000].loc[:, ['time-taken']].resample(rule = '1T').count()
pTime20SPercent = pTime20S/pTimeAll*100

pIP = p1[p1['time-taken']>20000].loc[:, ['c-ip', 'time-taken']]
pIP = pIP.groupby('c-ip').count()
print(pIP[pIP['time-taken']>10])

pURI = p1[p1['time-taken']>20000].loc[:, ['cs-uri-stem', 'time-taken']]
pURI = pURI.groupby('cs-uri-stem').count()
pURIAll = p1.loc[:, ['cs-uri-stem', 'time-taken']]
pURIAll = pURIAll.groupby('cs-uri-stem').count()
pURI = pURI/pURIAll*100
print(pURI[pURI['time-taken']>5])

import matplotlib.pyplot as plt

# plot the data
pTimeAll.plot()
pTime20S.plot()
pTime20SPercent.plot()
plt.show()
