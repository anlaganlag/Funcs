
    # 初始化
    def __init__(self, input):
        # 初始化两个列表
        self.fatherList = {} # 保存元素所属集合的代表元素
        self.sizeList = {} # 保存父节点包含的元素个数
        for x in input:
            self.make_set(x)
    # MAKE-SET操作
    # 将节点的父节点设为自身，size设为1
    def make_set(self, x):
        self.fatherList[x] = x
        self.sizeList[x] = 1
    # FIND-SET操作
    # 采用递归的策略定位父节点
    # 在父节点查找过程中，将当前节点连接到父节点上，进行路径压缩
    def find_set(self, x):
        father = self.fatherList[x]
        if(x != father): # 递归定位父节点
            father = self.find_set(father)
        self.fatherList[x] = father # 路径压缩
        return father
    # UNION操作
    # 将a和b两个集合合并在一起
    def union(self, a, b):
        if a is None or b is None:
            return
        a_father = self.find_set(a) # 获取两元素所在集合的代表元素
        b_father = self.find_set(b)
        if(a_father != b_father):
            a_size = self.sizeList[a_father] # 获取两元素所在集合的大小
            b_size = self.sizeList[b_father]
            if(a_size >= b_size): # 将规模较小的集合合并到规模较大的集合下面
                self.fatherList[b_father] = a_father
                self.sizeList[a_father] = a_size + b_size
                self.sizeList[b_father] = 0
            else:
                self.fatherList[a_father] = b_father
                self.sizeList[b_father] = a_size + b_size
                self.sizeList[a_father] = 0
