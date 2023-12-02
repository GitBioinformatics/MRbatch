
# -*- coding: utf-8 -*-

"""
Created on Mon Feb 22 12:40:25 2021
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
import time
date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
daty = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime()) 


def fileExist(base, file):
    ''' 
    
    判断文件是否存在 
    '''
    basefile = str(base) + '/' + str(file)
    if os.path.exists(basefile) and not os.path.isdir(basefile):
        return basefile
    elif os.path.exists(file) and not os.path.isdir(file):
        return file        
    else:
        print('Error: File [%s or %s] is not exist!' % (basefile, file))
        exit(1)
    
    
    
def dirExist(base, path):
    ''' 
    
    判断路径是否存在 
    '''
    basepath = str(base) + '/' + str(path)
    if os.path.exists(basepath) and os.path.isdir(basepath):
        return basepath
    elif os.path.exists(path) and os.path.isdir(path):
        return path        
    else:
        print('Error: Path [%s or %s] is not exist!' % (basepath, path))
        exit(1)    




class GenerateShell(object):
    
    def __init__(self, Rscript, bcftools, plink, python3, mine):
        '''
        
        初始化模块os.path.dirname(
        '''
        self.Rscript = Rscript
        self.bcftools = bcftools
        self.plink = plink
        self.python3 = python3
        self.mine = mine
        
    def AddHead(self, verbose = True):
        '''
        
        @: PGSLife
        @: PGSBGI.SE50
        @: PGSBGI.PE150
        添加头信息
        '''
        commond = '\n'
        commond += '# -*- coding: utf-8 -*-'; commond += '\n'
        if verbose:
            commond += """
'''            
Created on %s
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
'''""" % daty; commond += '\n'

        return commond
    
    
    def AddEnvPATH(self, oid, efile, ename, ofile, oname, samplen, outdir, verbose = True):
        '''
        
        @: PGSBGI.SE50
        添加环境变量, 样本信息等
        '''
        commond = '\n'
        commond += '\n'
        if verbose:
            commond += '# . 样本信息 .'; commond += '\n'
        
        commond += 'EFILE = "%s"' % efile; commond += '\n'
        commond += 'ENAME = "%s"' % ename; commond += '\n'
        commond += 'OFILE = "%s"' % ofile; commond += '\n'
        commond += 'ONAME = "%s"' % oname; commond += '\n'
        commond += 'OID = "%s"' % oid; commond += '\n'
        commond += 'SAMPLEN = "%s"' % samplen; commond += '\n'
        
        commond += '\n'
        if verbose:
            commond += '# . 数据和输出的主目录 .'; commond += '\n'
        commond += "OUTDIR = '%s'" % outdir; commond += '\n'
        
        commond += '\n'
        if verbose:
            commond += '# . 工具路径 .'; commond += '\n'
        commond += "MINE = '%s'" % self.mine; commond += '\n'
        commond += "BCFTOOLS = '%s'" % self.bcftools; commond += '\n'
        commond += "RSCRIPT = '%s'" % self.Rscript; commond += '\n'
        commond += "PLINK = '%s'" % self.plink; commond += '\n'
        
        return commond
    
    
    def AddEnvPATHO2E(self, eid, efile, ename, oid, ofile, oname, pval, r2, kb, fs, samplen, outdir, pop, verbose = True):
        '''
        
        @: PGSBGI.SE50
        添加环境变量, 样本信息等
        '''
        commond = '\n'
        commond += '\n'
        if verbose:
            commond += '# . 样本信息 .'; commond += '\n'
        
        commond += 'EFILE = "%s"' % efile; commond += '\n'
        commond += 'ENAME = "%s"' % ename; commond += '\n'
        commond += 'OFILE = "%s"' % ofile; commond += '\n'
        commond += 'ONAME = "%s"' % oname; commond += '\n'
        commond += 'EID = "%s"' % eid; commond += '\n'
        commond += 'OID = "%s"' % oid; commond += '\n'
        commond += 'PVAL = "%s"' % pval; commond += '\n'
        commond += 'R2 = "%s"' % r2; commond += '\n'
        commond += 'KB = "%s"' % kb; commond += '\n'
        commond += 'FS = "%s"' % fs; commond += '\n'
        commond += 'POP = "%s"' % pop; commond += '\n'
        commond += 'SAMPLEN = "%s"' % samplen; commond += '\n'
        
        commond += '\n'
        if verbose:
            commond += '# . 数据和输出的主目录 .'; commond += '\n'
        commond += "OUTDIR = '%s'" % outdir; commond += '\n'
        
        commond += '\n'
        if verbose:
            commond += '# . 工具路径 .'; commond += '\n'
        commond += "MINE = '%s'" % self.mine; commond += '\n'
        commond += "BCFTOOLS = '%s'" % self.bcftools; commond += '\n'
        commond += "RSCRIPT = '%s'" % self.Rscript; commond += '\n'
        commond += "PLINK = '%s'" % self.plink; commond += '\n'
        
        return commond
    
    
    def AddEnvPATHE2O(self, eid, oid, efile, ename, ofile, oname, pval, outdir, verbose = True):
        '''
        
        @: PGSBGI.SE50
        添加环境变量, 样本信息等
        '''
        commond = '\n'
        commond += '\n'
        if verbose:
            commond += '# . 样本信息 .'; commond += '\n'
        
        commond += 'EFILE = "%s"' % efile; commond += '\n'
        commond += 'ENAME = "%s"' % ename; commond += '\n'
        commond += 'OFILE = "%s"' % ofile; commond += '\n'
        commond += 'ONAME = "%s"' % oname; commond += '\n'
        commond += 'EID = "%s"' % eid; commond += '\n'
        commond += 'OID = "%s"' % oid; commond += '\n'
        commond += 'PVAL = "%s"' % pval; commond += '\n'
        
        commond += '\n'
        if verbose:
            commond += '# . 数据和输出的主目录 .'; commond += '\n'
        commond += "OUTDIR = '%s'" % outdir; commond += '\n'
        
        commond += '\n'
        if verbose:
            commond += '# . 工具路径 .'; commond += '\n'
        commond += "MINE = '%s'" % self.mine; commond += '\n'
        commond += "BCFTOOLS = '%s'" % self.bcftools; commond += '\n'
        commond += "RSCRIPT = '%s'" % self.Rscript; commond += '\n'
        
        return commond

    
    def all(self, ):
        '''
        '''
        commond = '\n'
        commond += """
rule all:
	input:
		r'{OUTDIR}/.MR/{OID}.tsv'.format(**locals()),
		r'{OUTDIR}/.done/{OID}.done'.format(**locals())
        """
        
        return commond
    
    
    def allO2E(self, ):
        '''
        '''
        commond = '\n'
        commond += """
rule all:
	input:
		r'{OUTDIR}/.MR/{EID}.tsv'.format(**locals()),
		r'{OUTDIR}/.done/{EID}.done'.format(**locals())
        """
        
        return commond
    
    
    def TwoSampleMR(self, ):
        ''' 
        
        TwoSampleMR
        '''
        commond = '\n'
        commond += """
rule TwoSampleMR:
	input:
		ofile = r'{OFILE}'.format(**locals())
	output:
		mrfile = r'{OUTDIR}/.MR/{OID}.tsv'.format(**locals())
	shell:
		r'''
		{RSCRIPT} {MINE}/TwoSampleMR.R --efile "{EFILE}" --ofile "{input.ofile}" --ename "{ENAME}" --oname "{ONAME}" --oid {OID} --plinkd {PLINK} --bcftoolsd {BCFTOOLS} --thisdir {OUTDIR}/{OID} --sn {SAMPLEN} --mrfile {output.mrfile}
		'''
        """
        
        return commond
    
    def EMR(self, ):
        ''' 
        
        TwoSampleMR
        '''
        commond = '\n'
        commond += """
rule EMR:
	input:
		ofile = r'{OFILE}'.format(**locals())
	output:
		mrfile = r'{OUTDIR}/.MR/{OID}.tsv'.format(**locals())
	shell:
		r'''
		{RSCRIPT} {MINE}/E.MR.R --efile "{EFILE}" --ofile "{input.ofile}" --ename "{ENAME}" --oname "{ONAME}" --eid {EID} --oid {OID} --bcftoolsd {BCFTOOLS} --thisdir {OUTDIR}/{OID} --mrfile {output.mrfile} --pval {PVAL}
		'''
        """
        
        return commond
    
    def OMR(self, ):
        ''' 
        
        TwoSampleMR
        '''
        commond = '\n'
        commond += """
rule OMR:
	input:
		ifile = r'{EFILE}'.format(**locals())
	output:
		mrfile = r'{OUTDIR}/.MR/{EID}.tsv'.format(**locals())
	shell:
		r'''
		{RSCRIPT} {MINE}/O.MR.R --efile "{input.Ifile}" --ofile "{OFILE}" --ename "{ENAME}" --oname "{ONAME}" --eid {EID} --oid {OID} --plinkd {PLINK} --bcftoolsd {BCFTOOLS} --pval {PVAL} --r2 {R2} --kb {KB} --FS "{FS}" --pop {POP} --thisdir {OUTDIR}/{EID} --sn {SAMPLEN} --mrfile {output.mrfile}
		'''
        """
        
        return commond
    
    def done(self, ):
        ''' 
        '''
        commond = '\n'
        commond += r"""
rule done:
	input:
		itsv = r'{OUTDIR}/.MR/{OID}.tsv'.format(**locals())
	output:
		odone = r'{OUTDIR}/.done/{OID}.done'.format(**locals())
	shell:
		r'''
		touch {output.odone}
		'''
        """
            
        return commond
    
    def doneO2E(self, ):
        ''' 
        '''
        commond = '\n'
        commond += r"""
rule done:
	input:
		itsv = r'{OUTDIR}/.MR/{EID}.tsv'.format(**locals())
	output:
		odone = r'{OUTDIR}/.done/{EID}.done'.format(**locals())
	shell:
		r'''
		touch {output.odone}
		'''
        """
            
        return commond
    
    
    def batch(self, ids, outdir, eid):
        ''' 
        '''
        python3 = self.python3
        commond = '\n'
        commond += r"""
IDS = '%s'.split()
OUTDIR = '%s'
EID = '%s'

rule all:
    input:
        expand('{outdir}/{eid}/.done/{ID}.done', outdir = OUTDIR, eid = EID, ID = IDS)
        
rule single:
    input:
        isnake = '{outdir}/{eid}/{ID}/{ID}.s'
    output:
        '{outdir}/{eid}/.done/{ID}.done'
    threads: 1
    shell:
        '''
        cd $(dirname {input.isnake})
        %s/bin/snakemake --snakefile {input.isnake} --jobs 1
        '''
        """ % (' '.join(ids), outdir, eid, python3)

        return commond
    
    
    
    
    
    
    
    