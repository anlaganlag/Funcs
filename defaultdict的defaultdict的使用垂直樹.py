
"""

此处撰写解题思路
987. 二叉树的垂序遍历
给定二叉树，按垂序遍历返回其结点值。

对位于 (X, Y) 的每个结点而言，其左右子结点分别位于 (X-1, Y-1) 和 (X+1, Y-1)。

把一条垂线从 X = -infinity 移动到 X = +infinity ，每当该垂线与结点接触时，我们按从上到下的顺序报告结点的值（ Y 坐标递减）。

如果两个结点位置相同，则首先报告的结点值较小。

按 X 坐标顺序返回非空报告的列表。每个报告都有一个结点值列表。

 

示例 1：



输入：[3,9,20,null,null,15,7]
输出：[[9],[3,15],[20],[7]]


"""


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict as d
        m = d(lambda: d(list))
        #設定value是defaultdict默認值爲list
        #即要區兩次才能取到該list..有點類似二位列表的字典中的應用..
        def h(n, x=0, y=0):
            if not n:
                return
            m[x][y].append(n)
            #位置相同的則添加到list中..
            #用的是深度有限..
            h(n.left, x-1, y+1)
            #下一行左邊
            h(n.right, x+1, y+1)
            #下一行右邊
            #用的坐標系類似左上角..
        h(root)
        ans = []
        for x in sorted(m):
        #先按照x排序取出..
        #每個x對應一哥tmp又來收集該col列的數據..
            col = []
            for y in sorted(m[x]):
                tmp.extend(sorted(n.val for n in m[x][y]))
            ans.append(col)

        return ans

```
