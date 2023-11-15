# -*- coding: utf-8 -*-

"""
Created on Wed Nov 15 11:37:07 2023
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

import sys
import os
import pandas as pd
from optparse import OptionParser

if __name__ == '__main__':
    
    # ------ 收集参数 ------   
    opt = OptionParser()
    opt.add_option('--eids',                dest = 'eids',         type = str,
                   help = 'exposure id')
    opt.add_option('-o', '--out',           dest = 'out',          type = str,
                   help = 'OpenGWAS outcome data directory')
    
    
    (opts, args) = opt.parse_args()
    if sys.platform.find('win') > -1:
        opts.eids = 'E:/BaiduSyncdisk/003.MPU/004.Batch.MR/test/exposures.txt'
        opts.out = 'G:/GWAS/IEU.GWAS.200'

    eidstmp = opts.eids
    if eidstmp != None:
        if os.path.exists(eidstmp):
            eids = [item.strip() for item in list(set(pd.read_csv(eidstmp, header = None)[0])) if item.strip() != '']
        else:
            eids = [item.strip() for item in list(set(eidstmp.split(';'))) if item.strip() != '']
    else:
        eids = []

    exposurestmp = os.listdir(opts.out)
    if len(eids) == 0:
        exposures = [outcome.rstrip('.vcf.gz') for outcome in exposurestmp if outcome.endswith('.vcf.gz')]
    else:
        exposures = [outcome.rstrip('.vcf.gz') for outcome in exposurestmp if outcome.endswith('.vcf.gz') and outcome.rstrip('.vcf.gz') in eids]
    

step = 18
ebatchs = [exposures[i:i + step] for i in range(0, len(exposures), step)]

for ebid in ebatchs[0]:
    shell = f'/tools/Python-3.8.3/python /analysis/Batch.MR/MR.E2O.batch.py --out /mnt/GDRIVE/GWAS/IEU.GWAS.200 --outdir /mnt/GDRIVE/src.out/IEU.GWAS.E2O.out --info /mnt/GDRIVE/GWAS/IEU.GWAS-v2.xlsx --eid {ebid} --pval 8 --batch --keep-going --jobs 1 --batch'
    print(shell)