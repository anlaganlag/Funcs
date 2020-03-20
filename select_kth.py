
#找到最k最小的元素用的是,類似快排的方法!!

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]: 
        n = len(arr) 
        def kthSmallest(arr, l, r, k):
            if (k > 0 and k <= r - l + 1):      
                pos = partition(arr, l, r)    
                if (pos - l+1 == k ): 
                    return arr[:pos+1]
                if (pos - l +1> k ):                                
                    return kthSmallest(arr, l, pos - 1, k) 
                return kthSmallest(arr, pos + 1, r, 
                                    k - pos + l - 1)
            return []
        def partition(arr, l, r):   
            x = arr[r] 
            i = l 
            for j in range(l, r): 
                if (arr[j] <= x): 
                    arr[i], arr[j] = arr[j], arr[i] 
                    i += 1
            arr[i], arr[r] = arr[r], arr[i] 
            return i 
        return kthSmallest(arr,0,n-1,k) 
