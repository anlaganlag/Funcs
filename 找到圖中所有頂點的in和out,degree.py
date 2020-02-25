
def findInOutDegree(adjList,n):
    #adjList相當於列表中的列表
    #用adjList可以表示一個G
    #初始化_in 和 out 表
    _in = [0] *  n
    out = [0] *  n

    #遍歷所有v
    for i in range(0,len(adjList)):
    #取出對應v的adj表
        lst = adjList[i]
        out[i] = len(lst)
        for j in range(len(lst)):
            _in[lst[j]]  += 1
    print("Vertex\tIn\tOut")
    for k in range(n):
        print(str(k) + "\t" + str(_in[k]) + "\t" + str(out[k]))  

if __name__ == "__main__":  
    adjList = []  
#各個V的的adjList情況
    adjList.append([1, 2])     #V0

    adjList.append([3])        #V1

    adjList.append([0, 5, 6])  #V2

    adjList.append([1, 4])     #V3

    adjList.append([2, 3])     #V4

    adjList.append([4, 6])     #V5

    adjList.append([5])        #V6

    n = len(adjList)  
    findInOutDegree(adjList, n)  

"""
python -i 找到圖中所 有頂點的in和out,degree.py 
Vertex	In	Out
0	1	2
1	2	1
2	2	3
3	2	2
4	2	2
5	2	2
6	2	1
>>> 
"""


