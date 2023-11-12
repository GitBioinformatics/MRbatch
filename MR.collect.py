# -*- coding: utf-8 -*-

"""
Created on Sat Nov 11 21:52:40 2023
This scripts writen by Albert丶XN
@author: Albert丶XN

   ┏┓　　┏┓
  ┏┛┻━━━━┛┻┓
  ┃　　　　  ┃
  ┃　━　　━　 ┃
  ┃　┳┛　┗┳　 ┃
  ┃　　　　　 ┃
  ┃　　　┻　　┃
  ┃　　　　　 ┃
  ┗━━┓　　　┏━┛
  　　┃　　 ┃ 神兽保佑
  　　┃　　 ┃ 代码无BUG！！！
  　　┃　　 ┗━━━━━┓
  　　┃　　　　　　  ┣┓
 　　┃　　　　　　  ┏┛┃
 　　┗┓┓┏━━━━━┳┓┏━━┛
  　　┃┫┫　   ┃┫┫
  　　┗┻┛　   ┗┻┛

"""


import os
import pandas as pd

wkdir = 'G:/src.out/OpenGWAS.out/ieu-a-2/.MR'

mrs = os.listdir(wkdir)

DF = pd.DataFrame()

for mr in mrs:
    mrf = os.path.join(wkdir, mr)
    if os.stat(mrf).st_size > 10:
        DFtmp = pd.read_csv(mrf, sep = '\t')
        if len(DFtmp[DFtmp['pval'] < 0.05]) > 5:
            DF = pd.concat([DF, DFtmp])
    else:
        print(mrf)

DF.to_excel('C:/Users/Administrator/Desktop/Obesity.xlsx', index = False)

