from numpy import *
import operator
def createDataset():
    group=array([1.0,2.0],[1.3,0.2])
    labels=['A','A','B','B']
    return group,labels

def KNN(input,dataset,label,k):
    datasize=dataset.shape[0]
    diff=tile(input,(datasize,1))-dataset
    sqdiff=diff**2
    squaredist =sum(sqdiff,axis=1)
    dist=squaredist**0.5
    sorteddist=argsort(dist)
    classcount={}
    for i in range(k):
        votelabel = label[sorteddist[i]]
        classcount[votelabel]=classcount.get(votelabel,0)+1
    maxcount=0
    for key,value in classcount.items():
        if value>maxcount:
            maxcount=value
            classes=key

    return classes
dataset,labels=createDataset()
input=arry([1.1,0.3])
k=3
output=KNN(input,dataset,labels,k)
print("测试数据是：",input,"分类结果是:",output)
