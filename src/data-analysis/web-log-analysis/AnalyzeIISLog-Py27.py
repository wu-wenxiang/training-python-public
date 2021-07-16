DATE = '170704'
LOG_FILE = r'u_ex%s.log' % DATE
LOG_DIR = r'C:\Users\wenw\Desktop'
STAT_DIR = LOG_DIR

import os
import re
from collections import Counter

def _buildSecStat(lineList, postfix):
    aCounter = Counter(lineList)
    with open(os.path.join(STAT_DIR, r'%s-%s.csv' % (DATE, postfix)), 'w') as outputStat:
        for i in range(24):
            for j in range(60):
                for k in range(60):
                    aCounter.setdefault('%02d:%02d:%02d' % (i,j,k), 0)
        for k in sorted(aCounter):
            outputStat.write('%s, %s' % (k, aCounter[k]) + '\n')

def _buildMinStat(lineList, postfix):
    aCounter = Counter(lineList)
    outputStat = open(os.path.join(STAT_DIR, r'%s-%s.csv' % (DATE, postfix)), 'w')
    for i in range(24):
        for j in range(60):
            aCounter.setdefault('%02d:%02d' % (i,j), 0)
    for k in sorted(aCounter):
        outputStat.write('%s, %s' % (k, aCounter[k]) + '\n')

def buildSecStat(lineList, postfix='sec'):
    lineList = [line[1] for line in lineList]
    _buildSecStat(lineList, postfix)

def buildMinStat(lineList, postfix='min'):
    lineList = [line[1] for line in lineList]
    lineList = [r':'.join(line.split(r':')[:2]) for line in lineList]
    _buildMinStat(lineList, postfix)

def buildMinStat_10s(lineList):
    postfix = '10sec'
    lineList = [line[1] for line in lineList if int(line[-1]) > 10000]
    lineList = [r':'.join(line.split(r':')[:2]) for line in lineList]
    _buildMinStat(lineList, postfix)

def buildMinStat_30s(lineList):
    postfix = '30sec'
    lineList = [line[1] for line in lineList if int(line[-1]) > 30000]
    lineList = [r':'.join(line.split(r':')[:2]) for line in lineList]
    _buildMinStat(lineList, postfix)

def buildIPStat(lineList):
    aDict = {}
    for line in lineList:
        aDict.setdefault(line[8], [])
        aDict[line[8]].append(int(line[-1]))
    bDict = {}
    for k,v in aDict.items():
        reqNum = len(v)
        req30Num = len([i for i in v if i>30000])
        req30Rate = float(req30Num)/reqNum
        req10Num = len([i for i in v if i>10000])
        req10Rate = float(req10Num)/reqNum
        avg = sum(v) / len(v)
        bDict[k] = [reqNum, avg, req30Num, req30Rate, req10Num, req10Rate]
    with open(os.path.join(STAT_DIR, r'%s-IP-stat.csv' % DATE), 'w') as outputStat:
        outputStat.write('IP, Requests, Average, 30+sec, 30+Percent, 10+Sec, 10+Percent\n')
        for k in sorted(bDict): #, key=(lamba x:bDict[x][0]), reverse=True):
            v = ['%s' % i for i in bDict[k]]
            v = ', '.join(v)
            outputStat.write('%s, %s' % (k, v) + '\n')

def buildURLStat(lineList):
    aDict = {}
    for line in lineList:
        k = ' '.join(line[3:5])
        aDict.setdefault(k, [])
        aDict[k].append(int(line[-1]))
    bDict = {}
    for k,v in aDict.items():
        reqNum = len(v)
        req30Num = len([i for i in v if i>30000])
        req30Rate = float(req30Num)/reqNum
        req10Num = len([i for i in v if i>10000])
        req10Rate = float(req10Num)/reqNum
        avg = sum(v) / len(v)
        bDict[k] = [reqNum, avg, req30Num, req30Rate, req10Num, req10Rate]
    secStat = open(os.path.join(STAT_DIR, r'%s-URL-stat.csv' % DATE), 'w')
    secStat.write('URL, Requests, Average, 30+sec, 30+Percent, 10+Sec, 10+Percent\n')
    for k in sorted(bDict): #, key=(lamba x:bDict[x][0]), reverse=True):
        v = ['%s' % i for i in bDict[k]]
        v = ', '.join(v)
        secStat.write('%s, %s' % (k, v) + '\n')

if __name__ == '__main__':
    logFile = os.path.join(LOG_DIR, LOG_FILE)
    lineList = [line for line in open(logFile) if line.startswith(r'20')]
    # reCmp = re.compile(r'^\S+\s+1[2-3]:')
    # aList = [i for i in aList if reCmp.search(i)]
    lineList = [line.split() for line in lineList]

    buildSecStat(lineList)
    buildMinStat(lineList)
    buildMinStat_10s(lineList)
    buildMinStat_30s(lineList)
    buildIPStat(lineList)
    buildURLStat(lineList)
