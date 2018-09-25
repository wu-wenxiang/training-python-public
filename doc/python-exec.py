# Tip_001 WinningRate-Simulation

import copy
import random
from functools import reduce

def choiceN(n, seq):
    while True:
        aList = copy.copy(seq)
        bList = []
        for _i in range(n):
            tmp = random.choice(aList)
            bList.append(tmp)
            aList.remove(tmp)
        yield bList

if __name__ == '__main__':
    SAMPLE = 1000000
    NUM_ALL = 11
    NUM_CHOICE = 8
    NUM_WIN = 5

    seq = list(range(NUM_ALL))
    gChoiceN = choiceN(NUM_CHOICE, seq)
    setWin = set(range(NUM_WIN))
        
    count = 0
    for i in range(SAMPLE):
        if setWin < set(gChoiceN.__next__()):
            count += 1

    print("Percent %.2f%%" % (100.0*count/SAMPLE))

# Tip_002 StockSpider-KLine

# -*- coding: utf-8 -*-
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts==0.5.5 --upgrade

import requests
from lxml import etree

SHANGHAI = 0
SHENZHEN = 1

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

def parseUrl(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return etree.HTML(response.content)
    return False
    
def getDate(response):
    # 得到股票代码，开始和结束的日期
    start_date = response.xpath('//input[@name="date_start_type"]/@value')[0]
    start_date = ''.join(start_date.split('-'))
    end_date = response.xpath('//input[@name="date_end_type"]/@value')[0]
    end_date = ''.join(end_date.split('-'))
    code = response.xpath('//h1[@class="name"]/span/a/text()')[0]
    return code, start_date, end_date

def _download(code, area, startDate, endDate):
    downloadUrl = ('http://quotes.money.163.com/service/chddata.html?code=%s'
                   '%s&start=%s&end=%s&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;'
                   'CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP')
    downloadUrl = downloadUrl % (area, code, startDate, endDate)
    print(downloadUrl) 
    data = requests.get(downloadUrl, headers=headers)
    f = open('%s.csv' % code, 'wb')
    for chunk in data.iter_content(chunk_size=10000):
        if chunk:
            f.write(chunk)
    print('股票---%s历史数据正在下载' % code)

def download(code, area):
    url = 'http://quotes.money.163.com/trade/lsjysj_%s.html' % code
    response = parseUrl(url)
    code, startDate, endDate = getDate(response)
    _download(code, area, startDate, endDate)

def draw(code):
    import pandas as pd
    stock  = pd.read_csv(code + '.csv',
                         usecols=[0,1,2,3,4,5,6], encoding='gbk')
    stock.head()
    
    stock_new = stock.iloc[:180,:]
    stock_new_sorted = stock_new.sort_values('日期', ascending=True)
    stock_new_sorted.head()
    
    from pyecharts import Kline
    stock_code = stock_new_sorted['股票代码'][0]
    stock_name = stock_new_sorted['名称'][0]
    index = stock_new_sorted['日期']
    v = [[o,close,lowest,highest] for o,close,lowest,highest in 
         zip(stock_new_sorted['开盘价'], stock_new_sorted['收盘价'],
             stock_new_sorted['最低价'],stock_new_sorted['最高价'])]
    kline = Kline()
    kline.add(stock_name+'('+stock_code+')'+'日K线图', index, v,
              mark_point=["max"], is_datazoom_show=True)
    kline.render()

if __name__ == '__main__':
    download('601899', SHANGHAI)
    draw('601899')