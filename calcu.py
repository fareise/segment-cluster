def calcu(tableNew):
    names = np.unique(tableNew['names'])
    labels = np.unique(tableNew['label'])
    tableCal = pd.DataFrame(columns=['NAMES', 'LABELS', 'NUM'])
    for name in names:
        for label in labels:
            temp = tableNew[(tableNew.names==name)&(tableNew.label==label)]
            size = len(temp['names'])
            cal = pd.DataFrame({
                    "NAMES": name,
                    "LABELS": label,
                    "NUM": size
                }, index=[0])
            tableCal = tableCal.append(cal)
    return tableCal
