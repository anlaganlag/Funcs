def knightTour(n,path,u,limit):
	"""n是當前深度,
	   path路徑
	   u處理/下個節點
	   limit
	"""
        u.setColor('gray')
        path.append(u)
       #首先是將當前階段標記成灰色,加入path
        if n < limit:
        #基線條件/base case 進入else
            nbrList = list(u.getConnections())
            i = 0
            done = False
            #獲取nbr,i用於index所有nbr,默認是done爲false
            while i < len(nbrList) and not done:
            	#當前深度下還有可探索的v i<len(..)
                if nbrList[i].getColor() == 'white':
                
                    done = knightTour(n+1, path, nbrList[i], limit)
                    #對nv遞歸的調用處理,相當與level加一,遞歸的處理
                i = i + 1
                #如果某個節點dead,會嘗試同一深度的其他的v繼續使用dfs
            if not done:  # prepare to backtrack
            #如果同一深度所有的都是kkt之後return false即爲dead_end走不同
            #則該節點的dead,需將該節點彈出,重新染色成white即未探索的狀態
                path.pop()
                u.setColor('white')
        else:
            done = True
            #達成base,即深度滿足了63
        return done
