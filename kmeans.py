from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
#进行聚类
def kmeans(table, num):
    loan = np.array(table)
    clf=KMeans(n_clusters=num)
    clf=clf.fit(loan)
    table['label']=clf.labels_
    return table
    
#计算分类数
def calNum(table, maxNum):
    clfNum = []
    loan = np.array(table)
    for i in range(1, maxNum+1):
        clf=KMeans(n_clusters=i)
        clf=clf.fit(loan)
        clfNum.append(clf.inertia_)
    return clfNum
