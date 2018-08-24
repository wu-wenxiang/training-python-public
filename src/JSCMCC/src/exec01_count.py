# -*- coding: UTF-8 -*- 
import pandas as pd

def getProvinceData(csv):
    provinceData = pd.read_csv(csv, header=None, dtype=str)
    provinceData.columns = ['区域ID', '区域名称', '上级区域ID']
    provinceData = provinceData[provinceData['区域名称'] == '河南省']
    provinceData.set_index('区域名称', inplace=True)
    provinceData = provinceData[~provinceData.index.duplicated(keep='first')]
    return provinceData

def getCityData(csv, provinceId):
    cityData = pd.read_csv(csv, header=None, dtype=str)
    cityData.columns = ['区域ID', '区域名称', '上级区域ID']
    cityData = cityData[cityData['上级区域ID'] == provinceId] 
    cityData.set_index('区域ID', inplace=True)
    cityData = cityData[~cityData.index.duplicated(keep='first')]
    return cityData

def getTownData(csv, cityData):
    townData = pd.read_csv(csv, header=None, dtype=str)
    townData.columns = ['区域ID', '区域名称', '市区域ID']
    townData = townData[[i in cityData.index for i in townData['市区域ID']]]
    townData['省区域ID'] = townData['市区域ID'].apply(lambda x:cityData.loc[x]['上级区域ID'])
    # 务必先加column后索引，否则要重新索引
    townData.set_index('区域ID', inplace=True)
    townData = townData[~townData.index.duplicated(keep='first')]
    return townData

def getBsData(csv, townData):
    bsData = pd.read_csv(csv, header=None, dtype=str)
    bsData.columns = ['基站ID', '基站名称', '基站类型', '所属区县ID', '基站状态']
    bsData = bsData[[i in townData.index for i in bsData['所属区县ID']]]
    bsData['市区域ID'] = bsData['所属区县ID'].apply(lambda x:townData.loc[x]['市区域ID'])
    # 这里可以用Series，但尽量不要用，会有诡异的bug
    # bsData['省区域ID'] = Series(townData.loc[i]['省区域ID'] for i in bsData['所属区县ID'])
    bsData['省区域ID'] = bsData['所属区县ID'].apply(lambda x:townData.loc[x]['省区域ID'])
    bsData.set_index('基站名称', inplace=True)
    bsData = bsData[~bsData.index.duplicated(keep='first')]
    return bsData

def getBsDataFromCache(csv):
    bsData = pd.read_csv(csv, dtype=str)
    bsData.set_index('基站名称', inplace=True)
    return bsData

if __name__ == '__main__':
    provinceData = getProvinceData(r'../data/省区域.csv')
    provinceId = provinceData.loc['河南省']['区域ID']
    cityData = getCityData(r'../data/市区域.csv', provinceId)
    townData = getTownData(r'../data/县区区域.csv', cityData)
    bsData = getBsData(r'../data/基站.csv', townData)
    bsData.to_csv(r'../tmp/_bsData.csv')
#     bsData = getBsDataFromCache(r'../tmp/_bsData.csv')

    output = open(r'../tmp/count.csv', 'w')
    outputList = [len(cityData), len(townData),
                  len(bsData[(bsData['基站状态'] != '工程') & (bsData['基站状态'] != '退网')]),
                  len(bsData)]
    output.write('\n'.join(map(str, outputList))) 
    output.close()
    print('Run finished.')