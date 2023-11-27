# -*- coding: utf-8 -*-

"""
Created on Thu Nov 16 08:01:18 2023
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

if False:
    wkdir = 'G:/src.out/IEU.GWAS.E2M.out'
    eids = os.listdir(wkdir)
    eids = [eid for eid in eids if eid.find('-') > -1]
    DF = pd.DataFrame()
    for eid in eids:
        try:
            mids = os.listdir(f'{wkdir}/{eid}/.MR')
            for mid in mids:
                midd = mid.rstrip('.tsv')
                try:
                    DFtmp  = pd.read_csv(f'{wkdir}/{eid}/.MR/{mid}', sep = '\t')
                    DFtmp['id.exposure'] = eid
                    DFtmp['id.outcome'] = midd
                    DF = pd.concat([DF, DFtmp])
                except:
                    pass
        except:
            pass

    DF.to_excel('C:/Users/Administrator/Desktop/E2M.xlsx', index = False)


if False:
    wkdir = 'G:/src.out/IEU.GWAS.M2O.out'
    mids = os.listdir(wkdir)
    mid = [mid for mid in mids if mid.find('-') > -1]
    DF = pd.DataFrame()
    for mid in mids:
        try:
            oids = os.listdir(f'{wkdir}/{mid}/.MR')
            for oid in oids:
                oidd = oid.rstrip('.tsv')
                try:
                    DFtmp  = pd.read_csv(f'{wkdir}/{mid}/.MR/{oid}', sep = '\t')
                    DFtmp['id.exposure'] = mid
                    DFtmp['id.outcome'] = oidd
                    DF = pd.concat([DF, DFtmp])
                except:
                    pass
        except:
            pass

    DF.to_excel('C:/Users/Administrator/Desktop/M2O.xlsx', index = False)
    

if False:
    wkdir = 'G:/src.out/IEU.GWAS.E2O.out'
    mids = os.listdir(wkdir)
    mid = [mid for mid in mids if mid.find('-') > -1]
    DF = pd.DataFrame()
    for mid in mids:
        try:
            oids = os.listdir(f'{wkdir}/{mid}/.MR')
            for oid in oids:
                oidd = oid.rstrip('.tsv')
                try:
                    DFtmp  = pd.read_csv(f'{wkdir}/{mid}/.MR/{oid}', sep = '\t')
                    DFtmp['id.exposure'] = mid
                    DFtmp['id.outcome'] = oidd
                    DF = pd.concat([DF, DFtmp])
                except:
                    pass
        except:
            pass

    DF.to_excel('C:/Users/Administrator/Desktop/E2O.xlsx', index = False)
    
    
if False:
    wkdir = 'G:/src.out/IEU.GWAS.O2E.out'
    mids = os.listdir(wkdir)
    mid = [mid for mid in mids if mid.find('-') > -1]
    DF = pd.DataFrame()
    for mid in mids:
        try:
            oids = os.listdir(f'{wkdir}/{mid}/.MR')
            for oid in oids:
                oidd = oid.rstrip('.tsv')
                try:
                    DFtmp  = pd.read_csv(f'{wkdir}/{mid}/.MR/{oid}', sep = '\t')
                    DFtmp['id.exposure'] = mid
                    DFtmp['id.outcome'] = oidd
                    DF = pd.concat([DF, DFtmp])
                except:
                    pass
        except:
            pass

    DF.to_excel('C:/Users/Administrator/Desktop/O2E.xlsx', index = False)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    