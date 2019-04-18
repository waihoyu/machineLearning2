
## 爱情片，动作片

import pandas as pd

#构建数据集合

rowdata = {'电影名称':['无问西东','后来的我们','前任3','红海行动','唐人街探案','战狼2'],
           '打斗镜头':[1,5,12,108,112,115],
           '接吻镜头':[101,89,97,5,9,8],
           '电影类型':['爱情片','爱情片','爱情片','动作片','动作片','动作片']
           }


movie_data = pd.DataFrame(rowdata)

new_data = [24,67]

dist = list((((movie_data.iloc[:6,1:3] - new_data)**2).sum(1))**0.5)

print(movie_data)

print(dist)

k = 4

dist_l = pd.DataFrame({'dist':dist,'labels':(movie_data.iloc[:6,3])})

dr = dist_l.sort_values(by = 'dist')[:k]

print(dr)

re = dr.loc[:,'labels'].value_counts()

print(re)


result1 = []

result1.append(re.index[0])

print(result1)


## 封装函数

import  pandas as pd

"""
 函数功能：KNN分类器
 参数说明：
        inX:需要预测分类的数据集
        dataSet：已知分类标签的数据集（训练集）
        k:k-近邻算法参数，选择距离最小的K个点
"""

def classify0(inX, dataSet, k):
    result = []
    dist = list((((dataSet.iloc[:6,1:3] - new_data)**2).sum(1))**0.5)
    dist_l = pd.DataFrame({'dist':dist,'labels':(dataSet.iloc[:6,3])})
    dr = dist_l.sort_values(by = 'dist')[:k]
    re = dr.loc[:,'labels'].value_counts()
    result1.append(re.index[0])
    return  result


inX = [24,67]
# dataSet = {'电影名称':['无问西东','后来的我们','前任3','红海行动','唐人街探案','战狼2'],
#            '打斗镜头':[1,5,12,108,112,115],
#            '接吻镜头':[101,89,97,5,9,8],
#            '电影类型':['爱情片','爱情片','爱情片','动作片','动作片','动作片']
#            }
dataSet = pd.DataFrame(rowdata)
k = 4
classify0(inX,dataSet,k )
