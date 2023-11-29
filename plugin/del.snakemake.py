# -*- coding: utf-8 -*-

"""
Created on Tue Nov 28 16:37:40 2023
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
import shutil

wkdir = 'G:/src.out/IEU.GWAS.E2O.out/P0DJD7'

oids = [item for item in os.listdir(wkdir) if item.find('-') > -1]

if False:
    for oid in oids:
        thisdir = f'{wkdir}/{oid}'
        snakedir = f'{thisdir}/.snakemake'
        gz = f'{thisdir}/{oid}-LP.vcf.gz'
        if not os.path.exists(gz):
            if os.path.exists(snakedir):
                shutil.rmtree(snakedir)
                print(oid)
                
if True:
    for oid in oids:
        thisdir = f'{wkdir}/{oid}'
        gz = f'{thisdir}/{oid}-LP.vcf.gz'
        if not os.path.exists(gz):
            print(oid)
                