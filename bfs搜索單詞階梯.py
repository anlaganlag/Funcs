class Vertex:
    def __init__(self,key):
        #簡單來說初始化名字,和al
        self.id = key#用字符串string命名
        self.connectedTo = {}
        #用dict來keep track追蹤相鄰的V及其權重
    
    def addNeighbor(self,nbr,weight=0):
        #在本V上添加其他V
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        #返回所有的V的al,即返回的dict
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    #其實就是一個dict,也就是每個V和其al
    #即V和nbr的關系
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
	
    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertlist.keys()

    def __iter__(self):
        return iter(self.vertList.values())

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
def bfs(g,start):
	#所以總的是O(V+E)
    start.setDistance(0)
    start.setPred(None)
    #起始點當然是沒有predecessor
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.start() > 0):
    #處理q中的所有頂點,只要沒有處理完畢,就一直執行while循環這裏是O(V)
        currentVert = vertQueue.dequeue()
        #執行出隊
        for nbr in currentVert.getconnections():
        #依次對所有的E進行處理,主要是做4件事情這裏是O(E)
            if (nbr.getcolor() == 'white'):
                #入隊前首次發現
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                #將當前V設定predecessor,方面遍歷找到起點
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')
		#出隊必變黑
