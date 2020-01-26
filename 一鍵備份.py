#! /usr/bin/env python
# coding=utf-8
# author:"""HTJ"""
# time:2019/7/9
# Zen of Python:
"""
The Zen of Python, Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.

*************************************************************************************
Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.

*************************************************************************************
Now is better than never.Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
"""首先這個程序非常厲害的啦，1。source有多個來源，即source是一個列表。"""

import os,time
source = ["/home/gal/desktop/Dairy_hunger_to_succed","/home/gal/desktop/python_代碼"]#這個程序真的厲害
target_dir="/home/gal/backup"#目標目錄是一個str別弄成list啦
if not os.path.exists(target_dir):#創建文件夾：這段程序有點搞笑說的是如果沒有沒有backup這個文件夾就創建，爲什麼啊！
    os.mkdir(target_dir)

today = target_dir +os.sep + time.strftime('%Y%m%d')#os.sep 在linux裏面也就是個/罷了，當然如果在windows裏會是\\
                                                    #time.strftime("")是真的牛逼
# print("today:",today)

now = time.strftime("%H%M%S")#now爲什麼要創建她因爲要每天要一個用日期文件夾，每天的文件夾都是一個zip

# print('now:',now)

comment = input("enter comment -->")#when there is no commnet it's pure time or time plus comment
if len(comment) ==0:
    target = today + os.sep + now + '.zip'
else:
    target = today +os.sep +now +'_' +\
        comment.replace(' ',"_")+'.zip'

if not os.path.exists(today):#創建日期的文件夾
    os.mkdir(today)
    print('created dir',today)

zip_command = 'zip -r {0} {1}'.format(target," ".join(source))#zip command line  zip -r 包括子文件夾的意思
print('zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:#如果返回是0 則代表運行成功 1代表是小問題 2 代表是打問題
    print('successful backup to',target)
else:
    print("Backup failed")

