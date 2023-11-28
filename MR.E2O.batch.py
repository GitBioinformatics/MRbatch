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
import re
import pandas as pd
from optparse import OptionParser

# BaiduSyncdisk BaiduNetdiskWorkspace
# os.chdir('E:/BaiduNetdiskWorkspace/003.MPU/004.Batch.MR')
import mine.GenerateShell as Gshell

def UsageInfo():
    ''' 
    
    帮助信息 
    '''
    usage ='''         
    Usage: xxx.py [options]
    
    Options:
      -h, --help            show this help message and exit
      -e EID, --eid=EID     exposure id
      -o OUT, --out=OUT     OpenGWAS outcome data directory
      --info=INFO           info file
      --outdir=OUTDIR       Output directory
      --bcftools=BCFTOOLS   bcftools
      --Rscript=RSCRIPT     Rscript
      --plink=PLINK         plink directory
      --python3=PYTHON3     python3 directory
      -m MINE, --mine=MINE  self-definied scripts
      --pop=POP             Super-population to use as reference panel. Default =
                            "EUR". Options are "EUR", "SAS", "EAS", "AFR", "AMR".
                            "legacy" also available - which is a previously used
                            verison of the EUR panel with a slightly different set
                            of markers.
      --batch               batch mode
      --keep-going          在某个任务失败后, 继续运行其他的独立任务
      --jobs=JOBS           批量模式运行时，最大支持并行的任务数
      
    Description:
        This is main process for MR pipeline.
        
    Example:
        xxx
        
    '''
    print(usage)
    exit(1)
    
def BREAK(n):
    ''' 

    '''
    INFO = f'一共有 {n} 个工具变量，数量过少（≤10） '
    print(INFO)
    if sys.platform.find('win') == -1:
        exit(1)


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
    opt.add_option('-e', '--eid',           dest = 'eid',          type = str,
                   help = 'exposure id')
    opt.add_option('-o', '--out',           dest = 'out',          type = str,
                   help = 'OpenGWAS outcome data directory')
    opt.add_option('--info',                dest = 'info',         type = str,
                   help = 'info file')
    opt.add_option('--outdir',              dest = 'outdir',       type = str,
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
    opt.add_option('--pop',                 dest = 'pop',          type = str,
                   help = 'Super-population to use as reference panel. Default = "EUR". Options are "EUR", "SAS", "EAS", "AFR", "AMR". "legacy" also available - which is a previously used verison of the EUR panel with a slightly different set of markers.')
    opt.add_option('--pval',                dest = 'pval',         type = int,             default = 8, 
                   help = 'pval, [8, 7, 6]')
    opt.add_option('--niv',                 dest = 'niv',          type = int,             default = 5, 
                   help = 'Minimum value of instrumental variables.')
    opt.add_option('--oids',                dest = 'oids',         type = str,
                   help = 'outcome ids')
    opt.add_option('--exclude',             dest = 'exclude',      type = str,
                   help = 'exclude ids')
    opt.add_option('--batch',               dest = 'batch',        action = 'store_true',  default = False, 
                   help = 'batch mode')
    opt.add_option('--keep-going',          dest = 'keep',         action = 'store_true',  default = False, 
                   help = '在某个任务失败后, 继续运行其他的独立任务')
    opt.add_option('--jobs',                dest = 'jobs',         type = int,             default = 10, 
                   help = '批量模式运行时，最大支持并行的任务数')
    
    (opts, args) = opt.parse_args()
    if sys.platform.find('win') > -1:
        opts.info = 'G:/GWAS/IEU.GWAS-v2b.xlsx'
        opts.eid = 'ebi-a-GCST003156'
        opts.out = 'G:/GWAS/IEU.GWAS.test'
        opts.out = 'G:/GWAS/IEU.GWAS.200'
        opts.outdir = 'G:/src.out/IEU.GWAS.E2O.out2'
        opts.exclude = 'G:/src.out/IEU.GWAS.E2O.out/ebi-a-GCST003156/.MR'
        # opts.oids = 'E:/BaiduSyncdisk/003.MPU/004.Batch.MR/test/outcomes.txt'
        
    if not (opts.info and opts.eid and opts.out and opts.outdir):
        UsageInfo()
        
    if int(opts.pval) == 8:
        pvlog = 7.30103
        pvint = 8
    if int(opts.pval) == 7:
        pvlog = 6.30103
        pvint = 7
    if int(opts.pval) == 6:
        pvlog = 5.30103
        pvint = 6
    else:
        pvlog = 7.30103
        pvint = 8
        
    eid = opts.eid
    efile = f'{opts.out}/{eid}.vcf.gz'
    elpfile = f'{opts.outdir}/{eid}/{eid}-LP.vcf.gz'
    erds = f'{opts.outdir}/{eid}/{eid}-LP.rds'
    etxt = f'{opts.outdir}/{eid}/{eid}-LP.txt'
    DF = pd.read_excel(opts.info)
    infos = {}
    for index in DF.index:
        ID = DF.loc[index, 'GWAS ID']
        gz = f'{opts.out}/{ID}.vcf.gz'
        if os.path.exists(gz):
            SN = DF.loc[index, 'Sample size']
            TRAIT = str(DF.loc[index, 'Trait'])
            TRAIT = re.sub('"', "'", TRAIT) if TRAIT.find('"') > -1 else TRAIT
            Population = DF.loc[index, 'Population']
            SN = int(SN) if isNumber(SN) else -1
            infos[ID] = [TRAIT, SN, Population]
       
    if opts.pop == None:
        race = infos[eid][2]
        if race in ['East Asian']:
            opts.pop = 'EAS'
        elif race in ['European']:
            opts.pop = 'EUR'
        else:
            opts.pop = 'EUR'

    infos = {key: value for key, value in infos.items() if value[2] == race}
        
    oidstmp = opts.oids
    if oidstmp != None:
        if os.path.exists(oidstmp):
            oids = [item.strip() for item in list(set(pd.read_csv(oidstmp, header = None)[0])) if item.strip() != '']
        else:
            oids = [item.strip() for item in list(set(oidstmp.split(';'))) if item.strip() != '']
    else:
        oids = list(infos.keys())
    
    exids = []
    if opts.exclude != None:
        if os.path.exists(opts.exclude):
            exids = [item.split('.')[0] for item in os.listdir(opts.exclude) if item.find('-') > -1 and item.endswith('.tsv')]
            
    outcomestmp = os.listdir(opts.out)
    if len(oids) == 0:
        outcomes = [outcome for outcome in outcomestmp if outcome.endswith('.vcf.gz') and not outcome.rstrip('.vcf.gz') in [opts.eid] and not outcome.rstrip('.vcf.gz') in exids]
    else:
        outcomes = [outcome for outcome in outcomestmp if outcome.endswith('.vcf.gz') and outcome.rstrip('.vcf.gz') in oids and not outcome.rstrip('.vcf.gz') in [opts.eid] and not outcome.rstrip('.vcf.gz') in exids]
            
    if not os.path.exists(f'{opts.outdir}/{eid}'):
        os.makedirs(f'{opts.outdir}/{eid}')
    
    if not os.path.exists(elpfile) or not os.path.exists(etxt):
        shell = f"{opts.bcftools} view -i 'LP>={pvlog}' {efile} -Oz -o {elpfile}"
        if opts.batch and sys.platform.find('win') == -1:
            print(shell); os.system(shell)
        shell = f"{opts.bcftools} index -t {elpfile}"
        if opts.batch and sys.platform.find('win') == -1:
            print(shell); os.system(shell)
            
        shell = f"{opts.Rscript} {opts.mine}/E.Plink.R --efile {elpfile} --plinkd {opts.plink} --sn {infos[eid][1]} --pop {opts.pop} --pval {pvint}"
        if opts.batch and sys.platform.find('win') == -1:
            print(shell); os.system(shell)
    
        if opts.batch and sys.platform.find('win') == -1:
            EF = pd.read_csv(etxt); n = EF.loc[0, 'x']
            if n < opts.niv:
                BREAK(n)
            else:
                print(f'一共有 {n} 个工具变量')
        
    odirs = creatDirs(ro = opts.outdir, ot = outcomes, it = eid)
    batchs = []
    CS = Gshell.GenerateShell(opts.Rscript, opts.bcftools, opts.plink, opts.python3, opts.mine)
    ename = infos[eid][0]
    for outcome in outcomes:
        oid = outcome.split('.')[0]
        shellFile = '%s/%s.s' % (odirs[oid], oid) 
        SH = open(shellFile, mode = 'w', encoding = 'utf-8')
        SH.write(CS.AddHead())
        SH.write(CS.AddEnvPATHE2O(oid = oid, efile = erds, ename = ename, ofile = os.path.join(opts.out, outcome), oname = infos[oid][0], pval = pvint, outdir = f'{opts.outdir}/{eid}')) 
        SH.write(CS.all())
        SH.write(CS.EMR())
        SH.write(CS.done())
        SH.close()
        batchs.append(oid)
        
    if not os.path.exists(f'{opts.outdir}/{eid}/.MR'):
        os.mkdir(f'{opts.outdir}/{eid}/.MR')

    if not os.path.exists(f'{opts.outdir}/{eid}/.done'):
        os.mkdir(f'{opts.outdir}/{eid}/.done')

    snakefile = '%s/%s/%s.s' % (opts.outdir, eid, 'batch') 
    SH = open(snakefile, mode = 'w', encoding = 'utf-8')
    SH.write(CS.batch(ids = batchs, outdir = opts.outdir, eid = eid))
    SH.close()
    if opts.batch and sys.platform.find('win') == -1:
        snakemake = '%s/bin/snakemake' % opts.python3
        nohup = '%s/%s/.nohup'  % (opts.outdir, eid)
        if opts.keep:
            shell = 'cd %s/%s && nohup %s --snakefile %s --jobs %s --keep-going > %s 2>&1' % (opts.outdir, eid, snakemake, snakefile, opts.jobs, nohup)
        else:
            shell = 'cd %s/%s && nohup %s --snakefile %s --jobs %s > %s 2>&1' % (opts.outdir, eid, snakemake, snakefile, opts.jobs, nohup)
        print('RUN', shell); os.system(shell)













