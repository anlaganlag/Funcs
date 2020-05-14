import re,random

def displaymatch(match):
   """"戰士re匹配結果的函數"""
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())



text = "Professor Abdolmalek, please report your absences promptly."
def r(m):
   """體驗下用用sub改變函數"""
    i=list(m.group(2))
    #將匹配的第二部分取出list,並打亂
    random.shuffle(i)
    return m.group(1) + ''.join(i)+m.group(3)
   #將第一第二部分(打亂)和第三那部分連接
re.sub(r'(\w)(\w+)(\w)',r,text)
          #pattern#要替換的函數或者文本#原來的文本

