def orderByAvail(n):
	"""在處理kkt問題,即騎士巡遊問題,選擇下一個V會極大的影響性能
	  所以用了個啓發式的技巧,創建list是按照最少步來排序的可選v的列表
	  相當於每次都優先選擇邊角位置,不斷地縮小問題的尺寸"""
    resList = []
    #初始化一個列表來用
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
         #訪問nbr列表中的每個未訪問的V,初始化c用來記錄每個nbr的合法下法
            for w in v.getConnections():
            #如果該nbr的有一個下發就+1
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
            #將每個nbr的nbr情況記錄,第一個參數是下法數,第二個是v即名字
    resList.sort(key=lambda x: x[0])
    #key = lambda x : x[0]這是一個超級簡單的技巧,sortyong key/lambda技巧
    #先按照c排序
    即按照第一個元素來排序
    return [y[1] for y in resList]
    #但是確實return時候,卻是返回對應的v
