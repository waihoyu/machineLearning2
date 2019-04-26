from numpy import  *
import matplotlib
import matplotlib.pyplot as plt

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    #zeros 生成零矩阵
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in  arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        print(listFromLine[0:3])
        returnMat[index,:] = listFromLine[0:3]
        if listFromLine[-1] == "largeDoses":
           temp = 3
           # break
        elif (listFromLine[-1] == "smallDoses"):
            temp = 2
            # break
        elif (listFromLine[-1] == "didntLike"):
            temp = 1
            # break
        else:
            temp = listFromLine[-1]
        classLabelVector.append(int(temp))
        index += 1
    return returnMat,classLabelVector

datingDataMat,datingLabels = file2matrix('datingTestSet.txt')

fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()
