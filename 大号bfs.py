class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def _bfs(start, blocked: set, walked_steps: int, end: list):
            movies = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            walked = set()
            walked.add((start[0], start[1]))  # 把出发点加入walked
            q = [start]  # list的pop() O(1),当作queue用. 
            while q:
                if walked_steps > (len(blocked)*(len(blocked)-1))//2:  # 步数超过最大封锁坐标数.
                    return True
                x, y = q.pop()
                for m in movies:
                    new_x = x + m[0]
                    new_y = y + m[1]
                    if [new_x, new_y] == end:  # 如果已经走到目标点,就返回True
                            return True
                    if 0 <= new_x < 1000000 and 0 <= new_y < 1000000 and (new_x, new_y) not in blocked and (new_x, new_y) not in walked: 
                                walked_steps += 1  # 步数加1
                                q.append([new_x, new_y])  # 加到q里, 下一次开始走的坐标.
                                walked.add((new_x, new_y))  # 加到走过的坐标集合walked里.
            return False  # 能走的都走过了,步数没有超过最大封锁数,或者没有走到end(即target)
        if not blocked:  
            return True
        blocked = set([(x, y) for x, y in blocked])
        walked_steps = 1  # 开始步数,出发点也占据 1个坐标方块
        source_to_target = _bfs(source, blocked, walked_steps, target)  # 把初始点和目标点传给BFS.
        target_to_source = _bfs(target, blocked, walked_steps, source)  # 和上面一样,对调.
        return source_to_target and target_to_source
        

        
