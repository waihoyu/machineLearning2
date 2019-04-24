"""
    函数功能：计算香农熵
    参数说明
    dataSet 原始数据集
    返回：
    ent:香农熵的值
"""
import numpy as np
import pandas as pd


def calEnt(dataset):
    n = dataset.shape[0]
    iSet = dataset.iloc[:, -1].value_counts()
    p = iSet / n
    ent = (-p * np.log2(p)).sum()
    return ent

# 创建数据集


'''

'''


def createDataSet():
    row_data = {'no surfacing':[1,1,1,0,0],
                'flippers':[1,1,0,1,1],
                'fish':['yes','yes','no','no','no']
                }
    dataSet = pd.DataFrame(row_data)
    return  dataSet


dataSet = createDataSet()
print(dataSet)
ent = calEnt(dataSet)
print(ent)
