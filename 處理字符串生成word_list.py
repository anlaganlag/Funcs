


def hand_2_wordlist(text):
	"""寫了個傻逼的處理字符串 wordlist的函數
可以把字符串按照空格分割,篩選出大於3位置,首位不包括數字及括號,再首字母小寫
再將字符的前後有數字各種標點的去掉,中間的標點去掉加上換行符
用文件.write方式寫入"""
    h1=text.split()
    h2=set([i.lower() for i in h1 if len(i)>=3 and i[0] not in "1 2 3 4 5 6 7 8 9 0 ( )".split()])
    h3=sorted([i.strip(",:.()0123456789?").replace("(","").replace("'","")+"\n" for i in h2])
    name=input("輸入想保存的文件名: ")
    with open(name,"w") as f:
        for i in h3:
            f.write(i)
    return "done"
    
