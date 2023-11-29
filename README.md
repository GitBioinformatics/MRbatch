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
BiocManager::install('VariantAnnotation')
BiocManager::install('MendelianRandomization')
devtools::install_github('mrcieu/gwasglue')
remotes::install_github('MRCIEU/TwoSampleMR')

install.packages('getopt')
install.packages('readr')
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
--jobs 24 \
--batch &
```

# MR.O2E.batch (Outcome to Exposure)

```shell
# Test
/tools/Python-3.8.3/python \
/analysis/Batch.MR/MR.O2E.batch.py \
--input /mnt/GDRIVE/GWAS/OpenGWAS.test \
--outdir /mnt/GDRIVE/src.out/OpenGWAS.O2E.out \
--info /mnt/GDRIVE/GWAS/OpenGWAS-Checked.xlsx \
--oid ieu-b-40 \
--pval 8 \
--batch \
--keep-going \
--jobs 2 \
--batch
```

