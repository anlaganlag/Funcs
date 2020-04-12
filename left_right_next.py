
class Solution:
    def connect(self, root: 'Node') -> 'Node':
#如果root或者left不存在的時候..
#直接返回..
        if root == None or root.left == None:
            return root
        # 将左子树的next指向右子树
        root.left.next = root.right
        # 如果当前节点存在next
        # 将它的右子树指向它的next节点的左子树
        if root.next:
            root.right.next = root.next.left
        # 递归
        self.connect(root.left)
        self.connect(root.right)
        return root


"""
116. 填充每个节点的下一个右侧节点指针
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
    Node *left;
      Node *right;
        Node *next;
        }
        填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

        初始状态下，所有 next 指针都被设置为 NULL。
"""


