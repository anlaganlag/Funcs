class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:    
        r = {}
	#主要是用字典来存储数据就是 深度:节点.val
        stack = [(root,0)]
        while stack:
	#while stack + pop +stack.append是经典的数据结构模式
            n,d = stack.pop()            
            if n :
	#核心代码就是这3句子,首次d会设定
                r.setdefault(d,n.val)
                stack.append((n.left,d+1))
                stack.append((n.right,d+1))

        return [r[i] for i in r]
