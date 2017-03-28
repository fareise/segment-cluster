#计算持续时间
def getLast(series):
    series = np.array(series)
    for i in range(0, series.size-1):
        start = 0
        end = 0
        if series[i] != 0:
            start = i
            break
    for j in range(0, series.size):
        if(series[series.size-j-1] != 0):
            end = series.size-j
            break
        else:
            end = series.size
    return end - start

#计算操纵次数
def getOperNum(series):
    operNum = 0;
    series = np.array(series)
    diffSeries = np.diff(series)
    for i in range(0, diffSeries.size):
        if(diffSeries[i] != 0):
            operNum = operNum + 1
    return operNum

#计算平均操纵幅度
def getRange(series):
    series = np.array(series)
    rangeAll = abs(np.diff(series)).sum()
    rangeSin = rangeAll / getOperNum(series)
    return rangeSin

#计算方差
def getVar(series):
    series = np.array(series)
    sum1 = series.sum()
    narray2=series*series
    sum2=narray2.sum()
    mean=sum1/series.size
    var=sum2/series.size-mean**2
    return var

#计算极差
def getGap(series):
    series = np.array(series)
    gap = max(series) - min(series)
    return gap

#计算逆转率（旧）
def getNi(series):
    series = np.array(series)
    ni = 0;
    for i in range(0, series.size-1):
        if(series[i]*series[i+1] < -1):
            ni = ni + 1
    nirate = ni / getOperNum(series)
    return nirate
