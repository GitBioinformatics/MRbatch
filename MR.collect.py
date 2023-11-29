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
import sys
import pandas as pd

eid = 'ebi-a-GCST003156'
eid = 'P0DJD7'

if sys.platform.find('win') > -1:
    wkdir = f'G:/src.out/IEU.GWAS.E2O.out/{eid}/.MR'
else:
    wkdir = f'/mnt/GDRIVE/src.out/IEU.GWAS.E2O.out/{eid}/.MR'

mrs = os.listdir(wkdir)

eid = os.path.basename(os.path.dirname(wkdir))
DF = pd.DataFrame()

if False:
    
    
    for index in range(len(mrs)):
        mr = mrs[index]
        oid = mr.split('.')[0]
        mrf = os.path.join(wkdir, mr)
        if os.stat(mrf).st_size > 10:
            DFtmp = pd.read_csv(mrf, sep = '\t')
            DFtmp['id.exposure'] = eid
            DFtmp['id.outcome'] = oid
            try:
                if list(DFtmp[DFtmp['method'] == 'Inverse variance weighted']['pval'])[0] < 0.05:
                    if len(DFtmp[DFtmp['pval'] < 0.05]) == 1:
                        DFtmp['Group'] = 1
                    elif len(DFtmp[DFtmp['pval'] < 0.05]) == 2:
                        DFtmp['Group'] = 2
                    elif len(DFtmp[DFtmp['pval'] < 0.05]) == 3:
                        DFtmp['Group'] = 3
                    elif len(DFtmp[DFtmp['pval'] < 0.05]) == 4:
                        DFtmp['Group'] = 4
                    elif len(DFtmp[DFtmp['pval'] < 0.05]) == 5:
                        DFtmp['Group'] = 5
                    elif len(DFtmp[DFtmp['pval'] < 0.05]) == 6:
                        DFtmp['Group'] = 6
                    elif len(DFtmp[DFtmp['pval'] < 0.05]) == 7:
                        DFtmp['Group'] = 7
                    DF = pd.concat([DF, DFtmp])
            except:
                pass
        else:
            print(mrf)
    
        if index % 1000 == 0:
            print(index)
        
    DF = DF.loc[:, ['id.exposure', 'exposure', 'id.outcome', 'outcome', 'method', 'nsnp', 'b', 'se', 'pval', 'lo_ci', 'up_ci', 'or', 'or_lci95', 'or_uci95', 'Group']]
    
if True:
    
    for index in range(len(mrs)):
        mr = mrs[index]
        oid = mr.split('.')[0]
        mrf = os.path.join(wkdir, mr)
        if os.stat(mrf).st_size > 10:
            DFtmp = pd.read_csv(mrf, sep = '\t')
            DFtmp['id.exposure'] = eid
            DFtmp['id.outcome'] = oid
            if len(DFtmp[DFtmp['pval'] < 0.05]) > 0:
                DF = pd.concat([DF, DFtmp])
        else:
            print(mrf)
        
        if index % 1000 == 0:
            print(index)
            
    DF = DF.loc[:, ['id.exposure', 'exposure', 'id.outcome', 'outcome', 'method', 'nsnp', 'b', 'se', 'pval', 'lo_ci', 'up_ci', 'or', 'or_lci95', 'or_uci95']]
    

if sys.platform.find('win') > -1:
    DF.to_excel(f'C:/Users/Administrator/Desktop/MR-{eid}.xlsx', index = False)
else:
    DF.to_excel(f'/mnt/GDRIVE/src.out/MR-{eid}.xlsx', index = False)
