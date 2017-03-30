def makeTable(files):
    skip = 0
    rollSstick = ['_ROLL_CAPT_SSTICK', '_ROLL_CAPT_SSTICK-1', '_ROLL_CAPT_SSTICK-2', '_ROLL_CAPT_SSTICK-3']
    sstick = ['_SSTICK_CAPT', '_SSTICK_CAPT-1','_SSTICK_CAPT-2','_SSTICK_CAPT-3']
    tableFactor = pd.DataFrame(columns=['FILNAME','LAST','OPERNUM','RANGENUM','VAR','GAP','NI'])
    for i, fileName in enumerate(files):
        try:
            df = pd.read_csv(wd+fileName)
            df = df.fillna(method='pad')
            df = df.loc[(df['_ALTITUDE'] < 1000) & (df['_ALTITUDE'] >100), :]
            rollSum = pd.Series(df[rollSstick].values.ravel())
            sstickSum = pd.Series(df[sstick].values.ravel())
            factors = segmentOne(rollSum, sstickSum)
            #其他参数
            height = df['_ALT_RADIO'][(factors['start']+factors['end'])/2]
            wind = df['_WIND_SPD'][factors['start']:factors['end']]
            windir = df['_WINDIR'][factors['start']:factors['end']]
            windMean = sum(wind)/(factors['end']-factors['start'])
            windirMean = sum(windir)/(factors['end']-factors['start'])
            windVar = calVar(wind)
            windirVar = calVar(windir)
            for m in range(0, len(factors["last"])):
                newFactor = pd.DataFrame({
                        "FILNAME": fileName,
                        "LAST": factors["last"][m],
                        "OPERNUM": factors["operNum"][m],
                        "RANGENUM": factors["rangeNum"][m],
                        "VAR": factors["var"][m],
                        "GAP": factors["gap"][m],
                        "NI": factors["ni"][m],
                        "HEIGHT": height,
                        "WINDMEAN": windMean,
                        "WINDVAR": windVar,
                        "WINDIRMEAN": windirMean,
                        "WINDIRVAR": windir}, index=[i])
                tableFactor = tableFactor.append(newFactor)
        except:
            skip = skip + 1
            continue
    return tableFactor, skip
