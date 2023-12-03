# Dependencies

```R
install.packages('glue')
install.packages('usethis') # libgit2-dev
install.packages('ragg') # libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev
install.packages('pkgdown') # libxml2-dev
install.packages('profvis')
install.packages('devtools') # libharfbuzz-dev libfribidi-dev
install.packages('gmp') # libgmp-dev
install.packages('arrangements')
install.packages('remotes')

install.packages('BiocManager')
BiocManager::install('VariantAnnotation') # libbz2-dev
BiocManager::install('MendelianRandomization')
devtools::install_github('mrcieu/gwasglue')
remotes::install_github('MRCIEU/TwoSampleMR')

install.packages('getopt')
install.packages('readr')
install.packages('openxlsx')
```

```shell
apt-get install -y libgit2-dev libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev libxml2-dev libharfbuzz-dev libfribidi-dev libgmp-dev libbz2-dev
```

# MR.batch (Exposure to Outcome)

```shell
nohup /tools/Python-3.8.3/python /analysis/Batch.MR/MRbatch.py \
--out /mnt/GDRIVE/GWAS/OpenGWAS.200 \
--outdir /mnt/GDRIVE/src.out/OpenGWAS.out \
--info /mnt/GDRIVE/GWAS/OpenGWAS-Checked.xlsx \
--input /home/hello/ieu-a-2-LP.vcf.gz \
--batch --keep-going --jobs 24 &
```

```shell
/tools/R-4.3.2/bin/Rscript /analysis/004.Batch.MR/mine/TwoSampleMR.R \
--efile /home/hello/ieu-a-2-LP.vcf.gz \
--ofile /mnt/GDRIVE/OpenGWAS.test/bbj-a-5.vcf.gz \
--ename 'Body fat percentage' \
--oname 'Gastric Cancer' \
--oid bbj-a-5 \
--plinkd /tools/plink-1.90 \
--bcftoolsd /tools/bcftools-1.18/bcftools \
--outdir /mnt/GDRIVE/src.out/OpenGWAS.out/ieu-a-2/.done \
--thisdir /mnt/GDRIVE/src.out/OpenGWAS.out/ieu-a-2/bbj-a-5 \
--sn 338903
```

# MR.E2O.batch (Exposure to Outcome)

```shell
# Test
/tools/Python-3.8.3/python \
/analysis/Batch.MR/MR.E2O.batch.py \
--out /mnt/GDRIVE/GWAS/OpenGWAS.test \
--outdir /mnt/GDRIVE/src.out/OpenGWAS.E2O.out \
--info /mnt/GDRIVE/GWAS/OpenGWAS-Checked.xlsx \
--eid ieu-b-40 \
--pval 8 \
--batch \
--keep-going \
--jobs 10 \
--batch
```

```shell
# 2023-11-27
/tools/Python-3.8.3/python \
/analysis/Batch.MR/MR.E2O.batch.py \
--out /mnt/GDRIVE/GWAS/IEU.GWAS.200 \
--outdir /mnt/GDRIVE/src.out/IEU.GWAS.E2O.out \
--info /mnt/GDRIVE/GWAS/IEU.GWAS-v2b.xlsx \
--eid ebi-a-GCST003156 \
--pval 8 \
--keep-going \
--jobs 18 \
--batch
```

```shell
# 2023-11-30
/tools/Python-3.8.3/python \
/analysis/Batch.MR/MR.E2O.batch.py \
--out /mnt/GDRIVE/GWAS/IEU.GWAS.200 \
--outdir /mnt/GDRIVE/src.out/IEU.GWAS.E2O.out \
--info /mnt/GDRIVE/GWAS/IEU.GWAS-v2b.xlsx \
--eid ebi-a-GCST003156 \
--oids /mnt/GDRIVE/src.out/id.outcomes.txt \
--pval 8 \
--keep-going \
--jobs 24 \
--r2 0.01 \
--kb 500 \
--fs F \
--batch
```

```shell
# 2023-11-30
/tools/Python-3.8.3/python \
/analysis/Batch.MR/MR.E2O.batch.py \
--out /mnt/GDRIVE/GWAS/IEU.GWAS.200 \
--outdir /mnt/GDRIVE/src.out/IEU.GWAS.E2O.out \
--info /mnt/GDRIVE/GWAS/IEU.GWAS-v2b.xlsx \
--eid ukb-b-8961 \
--pval 8 \
--keep-going \
--jobs 24 \
--batch
```

```shell
# 2023-11-30
/tools/Python-3.8.3/python \
/analysis/Batch.MR/MR.E2O.batch.py \
--out /mnt/GDRIVE/GWAS/IEU.GWAS.200 \
--outdir /mnt/GDRIVE/src.out/IEU.GWAS.E2O.out \
--info /mnt/GDRIVE/GWAS/IEU.GWAS-v2b.xlsx \
--eid ukb-b-8961 \
--pval 5 \
--keep-going \
--jobs 24 \
--r2 0.001 \
--kb 10000 \
--fs T \
--batch
```

# MR.E2O.batch.iv (Exposure to Outcome)

```shell
# Test
/tools/Python-3.8.3/python \
/analysis/Batch.MR/MR.E2O.batch.iv.py \
--out /mnt/GDRIVE/GWAS/IEU.GWAS.test \
--outdir /mnt/GDRIVE/src.out/IEU.GWAS.E2O.out2 \
--info /mnt/GDRIVE/GWAS/IEU.GWAS-v2b.xlsx \
--eid P0DJD7 \
--eif /mnt/GDRIVE/src.out/P0DJD7.xlsx \
--pval 8 \
--niv 2 \
--keep-going \
--jobs 2
```

```shell
# 2023-11-28
nohup /tools/Python-3.8.3/python \
/analysis/Batch.MR/MR.E2O.batch.iv.py \
--out /mnt/GDRIVE/GWAS/IEU.GWAS.200 \
--outdir /mnt/GDRIVE/src.out/IEU.GWAS.E2O.out \
--info /mnt/GDRIVE/GWAS/IEU.GWAS-v2b.xlsx \
--eid P0DJD7 \
--eif /mnt/GDRIVE/src.out/P0DJD7.xlsx \
--pval 8 \
--niv 2 \
--keep-going \
--jobs 20 \
--exclude /mnt/GDRIVE/src.out/IEU.GWAS.E2O.out/P0DJD7/.MR \
--batch
```

```shell
# 2023-11-30
nohup /tools/Python-3.8.3/python \
/analysis/Batch.MR/MR.E2O.batch.iv.py \
--out /mnt/GDRIVE/GWAS/IEU.GWAS.200 \
--outdir /mnt/GDRIVE/src.out/IEU.GWAS.E2O.out \
--info /mnt/GDRIVE/GWAS/IEU.GWAS-v2b.xlsx \
--eid ebi-a-GCST90038694 \
--eif /mnt/GDRIVE/src.out/ebi-a-GCST90038694.xlsx \
--pval 8 \
--niv 5 \
--keep-going \
--jobs 24 \
--exclude /mnt/GDRIVE/src.out/IEU.GWAS.E2O.out/ebi-a-GCST90038694/.MR \
--batch &
```

```shell
# 2023-12-01
nohup /tools/Python-3.8.3/python \
/analysis/Batch.MR/MR.E2O.batch.iv.py \
--out /mnt/GDRIVE/GWAS/IEU.GWAS.200 \
--outdir /mnt/GDRIVE/src.out/IEU.GWAS.E2O.out \
--info /mnt/GDRIVE/GWAS/IEU.GWAS-v2b.xlsx \
--eid ukb-b-8961 \
--eif /mnt/GDRIVE/src.out/ukb-b-8961.xlsx \
--pval 5 \
--niv 5 \
--keep-going \
--jobs 24 \
--exclude /mnt/GDRIVE/src.out/IEU.GWAS.E2O.out/ukb-b-8961/.MR \
--batch &
```

# MR.O2E.batch (Outcome to Exposure)

```shell
# Test

```

```shell
# 2023-12-02
/tools/Python-3.8.3/python \
/analysis/Batch.MR/MR.O2E.batch.py \
--input /mnt/GDRIVE/GWAS/IEU.GWAS.200 \
--outdir /mnt/GDRIVE/src.out/IEU.GWAS.O2E.out \
--info /mnt/GDRIVE/GWAS/IEU.GWAS-v2b.xlsx \
--eids /mnt/GDRIVE/src.out/ids.txt \
--oid GCST90038650 \
--pval 8 \
--r2 0.001 \
--kb 10000 \
--fs F \
--pop EUR \
--keep-going \
--jobs 24 \
--batch
```

```shell
# 2023-12-03
/tools/Python-3.8.3/python \
/analysis/Batch.MR/MR.O2E.batch.py \
--input /mnt/GDRIVE/GWAS/IEU.GWAS.200 \
--outdir /mnt/GDRIVE/src.out/IEU.GWAS.O2E.out \
--info /mnt/GDRIVE/GWAS/IEU.GWAS-v2b.xlsx \
--eids /mnt/GDRIVE/src.out/ids.txt \
--oid GCST90038650 \
--pval 6 \
--r2 0.001 \
--kb 10000 \
--fs F \
--pop EUR \
--keep-going \
--jobs 24 \
--batch
```

