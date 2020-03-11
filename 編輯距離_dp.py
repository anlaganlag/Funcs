def editdistance(str1,str2):
    if str1 == '':
        return len(str2)
    if str2 == '':
        return len(str1)
    if str1[0] == str2[0]:
        return editdistance(str1[1:],str2[1:])
    d = editdistance(str1[1:],str2)
    u = editdistance(str1[1:],str2[1:])
    i = editdistance(str1,str2[1:])
    return min(d,u,i) +1
print(editdistance('sport','sort'))
print(editdistance('commuter','computer'))
print(editdistance('sunday','saturday'))
