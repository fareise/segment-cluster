#分段，返回每一区段的开始位置和终止位置
def getDis(series):
    i = 0
    start = []
    end = []
    flag = -1
    while i < series.size:
        if series[i] == 0:
            i = i + 1
        else:
            flag = flag + 1
            start.append(i)
            for m in range(i, series.size):
                if series[m] == 0:
                    end.append(m)
                    break
                else:
                    continue
            i = end[flag]
    return start, end
