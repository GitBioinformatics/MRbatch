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

oid = 'P0DJD7'
oid = 'ukb-b-18336'
eid = 'ukb-a-114'
eid = 'ebi-a-GCST90038607'

if sys.platform.find('win') > -1:
    wkdir = f'G:/src.out/IEU.GWAS.O2E.out/{oid}/.MR'
    wkdir = f'G:/src.out/IEU.GWAS.E2O.out/{oid}/.MR'
    wkdir = 'C:/Users/Administrator/Desktop/.MR'
else:
    wkdir = f'/results/test/IEU.GWAS.E2O.out/{eid}/.MR'


mrs = os.listdir(wkdir)
DF = pd.DataFrame()

Es = []
pval = 0.05

if True:
    
    for index in range(len(mrs)):
        mr = mrs[index]
        oid = mr.split('.')[0]
        mrf = os.path.join(wkdir, mr)
        if os.stat(mrf).st_size > 10:
            DFtmp = pd.read_csv(mrf, sep = '\t')
            DFtmp['id.exposure'] = eid
            DFtmp['id.outcome'] = oid
            try:
                if list(DFtmp[DFtmp['method'] == 'Inverse variance weighted']['pval'])[0] < pval:
                    if len(DFtmp[DFtmp['pval'] < pval]) == 1:
                        DFtmp['Group'] = 1
                    elif len(DFtmp[DFtmp['pval'] < pval]) == 2:
                        DFtmp['Group'] = 2
                    elif len(DFtmp[DFtmp['pval'] < pval]) == 3:
                        DFtmp['Group'] = 3
                    elif len(DFtmp[DFtmp['pval'] < pval]) == 4:
                        DFtmp['Group'] = 4
                    elif len(DFtmp[DFtmp['pval'] < pval]) == 5:
                        DFtmp['Group'] = 5
                    elif len(DFtmp[DFtmp['pval'] < pval]) == 6:
                        DFtmp['Group'] = 6
                    elif len(DFtmp[DFtmp['pval'] < pval]) == 7:
                        DFtmp['Group'] = 7
                    print(mrf)
                    DF = pd.concat([DF, DFtmp])
                    Es.append(list(DFtmp['outcome'])[0])
            except:
                pass
        else:
            pass
    
        if index % 1000 == 0:
            print(index)
        
    DF = DF.loc[:, ['id.exposure', 'exposure', 'id.outcome', 'outcome', 'method', 'nsnp', 'b', 'se', 'pval', 'lo_ci', 'up_ci', 'or', 'or_lci95', 'or_uci95', 'Group']]
    

print()
print('\n'.join(Es))
if sys.platform.find('win') > -1:
    DF.to_excel(f'C:/Users/Administrator/Desktop/MR-{oid}.xlsx', index = False)
else:
    DF.to_excel(f'/home/hello/MR-{oid}.xlsx', index = False)
