    def __init__(self, n: int):
        self.pointer = 1
        self.stream = (n+1)*[""]
    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id] = value
//每次插入初始化都爲[],類似每次先做清理工作...
        ans = []
//如果id和指針匹配..有點類似擊中了g點..沒擊中就return []
        if self.pointer == id:
//將id選一個分身即i...
            i = id
//這個i是以擊中的id爲起點可以移動到到爲空的位置..且最多移動到n...
            while i < len(self.stream):
//如果爲空則停止...即此時i爲第一個空..
                if not self.stream[i]:
                    break
//每次嘗試一步
                i+=1 
//此時i有點類似ai排雷機器人..將位置給pointer...
            self.pointer = i
//起點到終點-1
            ans = self.stream[id:i]
        return ans

"""

1656. 设计有序流
有 n 个 (id, value) 对，其中 id 是 1 到 n 之间的一个整数，value 是一个字符串。不存在 id 相同的两个 (id, value) 对。

设计一个流，以 任意 顺序获取 n 个 (id, value) 对，并在多次调用时 按 id 递增的顺序 返回一些值。

实现 OrderedStream 类：

OrderedStream(int n) 构造一个能接收 n 个值的流，并将当前指针 ptr 设为 1 。
String[] insert(int id, String value) 向流中存储新的 (id, value) 对。存储后：
如果流存储有 id = ptr 的 (id, value) 对，则找出从 id = ptr 开始的 最长 id 连续递增序列 ，并 按顺序 返回与这些 id 关联的值的列表。然后，将 ptr 更新为最后那个  id + 1 。
否则，返回一个空列表。

 


"""
