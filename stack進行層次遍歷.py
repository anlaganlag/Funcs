from collections import deque
def level(root):
	if not root:
		return
	q = deque()
	ans =[]
	q.append(root)
	while q:
		p = q.popleft()
		ans.append(p.val)
		if p.left:
			q.append(p.left)
		if p.right:
			q.append(p.right)
	return ans

