# -*- coding: utf-8 -*-

"""
Created on Sat Dec 23 13:03:24 2023
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


if __name__ == '__main__':
    
    wkdir = 'G:/src.out/O2E'
    eids = os.listdir(wkdir)
    
    DF = pd.DataFrame()
    for eid in eids:
        thisdir = f'{wkdir}/{eid}'
        oids = os.listdir(thisdir)
        for oid in oids:
            indir = f'{thisdir}/{oid}'
            if os.path.isdir(indir):
                mrfile = f'{indir}/{oid}.txt'
                if os.path.exists(mrfile):
                    sub = pd.read_csv(mrfile, sep = '\t')
                    DF = pd.concat([DF, sub])
    
    DF.to_excel('C:/Users/Administrator/Desktop/MR-tmp.xlsx', index = False)

