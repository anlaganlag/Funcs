
"""
1028. 从先序遍历还原二叉树
我们从二叉树的根节点 root 开始进行深度优先搜索。

在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。

如果节点只有一个子节点，那么保证该子节点为左子节点。

给出遍历输出 S，还原树并返回其根节点 root。


示例 1：

输入："1-2--3--4-5--6--7"
输出：[1,2,5,3,4,6,7]
"""

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        ans = {-1: TreeNode(0)}     #字典初始化,即設點root節點的之上的節點..即哨兵-1層的root of p,root是第0層
        def addTree(d,v):          #構建樹树的函数
            ans[d] = TreeNode(int(v))#首先根據傳入的層數比如0,1..和值創建好節點之後..
            if ans[d - 1].left==None: #左子树不存在就加在左边
                ans[d- 1].left = ans[d]
            else:                   #反之加在右边
                ans[d - 1].right = ans[d]
        dep,val =  0,""            #值和对应深度初始化
        for c in S:
            if c != '-':#是數字
                val += c            #累加字符来获得数字
            elif val:               #如果是‘-’且存在val
                addTree(dep,val)   #就把累加好的数字和对应深度添加进树
                dep,val= 1,""    #值和对应深度重新初始化
            else:
                dep += 1            #连续的‘-’只加深度不加值
        addTree(dep,val)           #末尾剩余的数字也要加进树
        return ans[0]


