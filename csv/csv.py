# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        csv
# Purpose:     read and write csv files
# Author:      tsui
# Created:     9 Apr, 2013
# Copyright:   ©tsui 2013
# Licence:     GPL v2
#-------------------------------------------------------------------------------

#!/usr/bin/python


# -*- coding: utf-8 -*-
# Filename:file_cut.py
path = raw_input('please enter the file path：')
savepath = raw_input('please enter the save path:(not include the last \'\\\')')
newname = raw_input('please enter the new name:')
fr = file(path,'r')
flag = True
i = 0 #记录数
c = 1 #分割文件
while flag:
    line = fr.readline()
    i+=1
    if i < 2000:         #分割200000行
        print i
        save =savepath +'\\'+ newname + str(c) + ".csv"
        file(save,'a').write(line)
    else:
        i = 0    #记录数清零
        c+=1      #文件名+1
        continue   #继续循环
    if len(line) == 0:
        flag = False
#    if c == 5:
#        flag = False
fr.close()
