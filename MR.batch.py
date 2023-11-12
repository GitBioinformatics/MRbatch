# -*- coding: utf-8 -*-

"""
Created on Fri Nov 10 22:38:14 2023
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

# os.chdir('E:/BaiduNetdiskWorkspace/003.MPU/004.Batch.MR')
import mine.GenerateShell as Gshell


def isNumber(s):
    """ 判断是否为数字 """
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

    
def creatDirs(ro, ot, it):
    '''
    
    创建样本输出路径.
    '''
    odirs = {}
    for o in ot:
        if o.endswith('.vcf.gz'):
            oid = o.split('.')[0]
            _dir = '%s/%s/%s' % (ro, it, oid)
            odirs[oid] = _dir
            # 当路径不存在时, 创建该目录 .
            if not os.path.exists(_dir):
                os.makedirs(_dir)
            
    return odirs


if __name__ == '__main__':
    
    # ------ 收集参数 ------   
    opt = OptionParser()
    opt.add_option('-i', '--input',         dest = 'input',        type = str,
                   help = 'exposure data')
    opt.add_option('-o', '--out',           dest = 'out',          type = str,             default = 'G:/GWAS/OpenGWAS.test', 
                   help = 'OpenGWAS outcome data directory')
    opt.add_option('--info',                dest = 'info',         type = str,
                   help = 'info file')
    opt.add_option('--outdir',              dest = 'outdir',       type = str,             default = 'G:/src.out/OpenGWAS.out/', 
                   help = 'Output directory')
    opt.add_option('--bcftools',            dest = 'bcftools',     type = str,             default = '/tools/bcftools-1.18/bcftools', 
                   help = 'bcftools')
    opt.add_option('--Rscript',             dest = 'Rscript',      type = str,             default = '/tools/R-4.3.2/bin/Rscript', 
                   help = 'Rscript')
    opt.add_option('--plink',               dest = 'plink',        type = str,             default = '/tools/plink-1.90', 
                   help = 'plink directory')
    opt.add_option('--python3',             dest = 'python3',      type = str,             default = '/tools/Python-3.8.3', 
                   help = 'python3 directory')
    opt.add_option('-m', '--mine',          dest = 'mine',         type = str,             default = '/analysis/Batch.MR/mine', 
                   help = 'self-definied scripts')
    opt.add_option('--batch',               dest = 'batch',        action = 'store_true',  default = False, 
                   help = 'batch mode')
    opt.add_option('--keep-going',          dest = 'keep',         action = 'store_true',  default = False, 
                   help = '在某个任务失败后, 继续运行其他的独立任务')
    opt.add_option('--jobs',                dest = 'jobs',         type = int,             default = 10, 
                   help = '批量模式运行时，最大支持并行的任务数')
    
    (opts, args) = opt.parse_args()
    outcomes = os.listdir(opts.out)
    outcomes = [outcome for outcome in outcomes if outcome.endswith('.vcf.gz')]
    if sys.platform.find('win') > -1:
        opts.info = 'G:/GWAS/OpenGWAS-Checked.xlsx'
        opts.input = 'C:/Users/Administrator/Desktop/ieu-a-2-LP.vcf.gz'

    eid = os.path.basename(opts.input).split('.')[0]
    eid = eid.rstrip('-LP')
    DF = pd.read_excel(opts.info)
    DF = DF[DF['Status'] == 'TRUE']
    infos = {}
    for index in DF.index:
        ID = DF.loc[index, 'GWAS ID']
        SN = DF.loc[index, 'Sample size']
        TRAIT = DF.loc[index, 'Trait']
        SN = int(SN) if isNumber(SN) else -1
        infos[ID] = [TRAIT, SN]
    
    odirs = creatDirs(ro = opts.outdir, ot = outcomes, it = eid)
    batchs = []
    CS = Gshell.GenerateShell(opts.Rscript, opts.bcftools, opts.plink, opts.python3, opts.mine)
    ename = infos[eid][0]
    for outcome in outcomes:
        oid = outcome.split('.')[0]
        shellFile = '%s/%s.s' % (odirs[oid], oid) 
        SH = open(shellFile, mode = 'w', encoding = 'utf-8')
        SH.write(CS.AddHead())
        SH.write(CS.AddEnvPATH(oid = oid, efile = opts.input, ename = ename, ofile = os.path.join(opts.out, outcome), oname = infos[oid][0], samplen = infos[oid][1], outdir = f'{opts.outdir}/{eid}')) 
        SH.write(CS.all())
        SH.write(CS.TwoSampleMR())
        SH.write(CS.done())
        SH.close()
        batchs.append(oid)
        
    if not os.path.exists(f'{opts.outdir}/{eid}/.MR'):
        os.mkdir(f'{opts.outdir}/{eid}/.MR')

    if not os.path.exists(f'{opts.outdir}/{eid}/.done'):
        os.mkdir(f'{opts.outdir}/{eid}/.done')

    # . 是否自动提交任务 .
    snakefile = '%s/%s/%s.s' % (opts.outdir, eid, 'batch') 
    SH = open(snakefile, mode = 'w', encoding = 'utf-8')
    SH.write(CS.batch(ids = batchs, outdir = opts.outdir, eid = eid))
    SH.close()
    if opts.batch:
        snakemake = '%s/bin/snakemake' % opts.python3
        nohup = '%s/%s/.nohup'  % (opts.outdir, eid)
        if opts.keep:
            shell = 'cd %s/%s && nohup %s --snakefile %s --jobs %s --keep-going > %s 2>&1' % (opts.outdir, eid, snakemake, snakefile, opts.jobs, nohup)
        else:
            shell = 'cd %s/%s && nohup %s --snakefile %s --jobs %s > %s 2>&1' % (opts.outdir, eid, snakemake, snakefile, opts.jobs, nohup)
        print('RUN', shell); os.system(shell)













