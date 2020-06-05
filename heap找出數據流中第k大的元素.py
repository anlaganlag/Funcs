class KthLargest:
    import heapq#在pyt中用最小和最大都是heapq

    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        heapq.heapify(self.pool)#獲取數據加上創建堆
        self.k = k
        while len(self.pool) > k:
            heapq.heappop(self.pool)#堆頂放如第k大的元素..

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)#不夠k則push進heap
        elif val > self.pool[0]:#比k大就重置堆
            heapq.heapreplace(self.pool, val)
        return self.pool[0]#比k大小直接返回k大

"""
703. 数据流中的第K大元素
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
"""
