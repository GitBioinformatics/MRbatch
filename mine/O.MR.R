options(stringsAsFactors = FALSE, warn = -1, scipen = 10)
suppressMessages(library(glue))
suppressMessages(library(dplyr))
suppressMessages(library(getopt))
suppressMessages(library(ieugwasr))
suppressMessages(library(gwasglue))
suppressMessages(library(TwoSampleMR))
suppressMessages(library(VariantAnnotation))

if (Sys.info()['sysname'] == 'Linux') {
  PROD = TRUE
} else {
  PROD = FALSE
}

if (PROD) {
  command = matrix(c( 
    'help', 'h', 0, 'loical', '帮助文档',
    'efile', 'efile', 1, 'character', 'exposure file',
    'ofile', 'ofile', 1, 'character', 'outcome file',
    'ename', 'ename', 1, 'character', 'exposure name',
    'oname', 'oname', 1, 'character', 'outcome name',
    'eid', 'eid', 1, 'character', 'exposure id',
    'oid', 'oid', 1, 'character', 'outcome id',
    'plinkd', 'plinkd', 1, 'character', 'plink',
    'bcftoolsd', 'bcftoolsd', 1, 'character', 'bcftools',
    
    'pval', 'pval', 1, 'integer', 'pval',
    'r2', 'r2', 1, 'numeric', 'r2',
    'kb', 'kb', 1, 'integer', 'kb',
    'FS', 'FS', 1, 'character', 'F-statistics',
    
    'pop', 'pop', 1, 'character', 'pop type',
    'thisdir', 'thisdir', 1, 'character', 'thisdir',
    'sn', 'sn', 1, 'integer', 'sample number',
    'mrfile', 'mrfile', 1, 'character', 'mrfile'),
    byrow = TRUE,
    ncol = 5)
  Args = getopt(command)
  
  if (!is.null(Args$help) || is.null(Args$efile) || is.null(Args$ofile) || is.null(Args$ename) || is.null(Args$oname) || is.null(Args$eid) || is.null(Args$oid) || is.null(Args$plinkd) || is.null(Args$bcftoolsd) || is.null(Args$mrfile) || is.null(Args$thisdir) || is.null(Args$pop) || is.null(Args$sn) || is.null(Args$pval) || is.null(Args$r2)  || is.null(Args$kb) || is.null(Args$FS)) {
    cat(paste(getopt(command, usage = TRUE), "\n"))
    q( status = 1)
  }
  e.file <- Args$efile
  o.file <- Args$ofile
  e.name <- Args$ename
  o.name <- Args$oname
  eid <- Args$eid
  oid <- Args$oid
  plink.d <- Args$plinkd
  bcftools.d <- Args$bcftoolsd
  mrfile <- Args$mrfile
  thisdir <- Args$thisdir
  N <- as.integer(Args$sn)
  pop <- Args$pop
  olp.file <- glue('{thisdir}/{oid}-LP.vcf.gz')
  a.pval <- -as.integer(Args$pval)
  pval <- 5 * 10 ^ -as.integer(Args$pval)
  r2 <- as.numeric(Args$r2)
  kb <- as.integer(Args$kb)
  FS <- as.logical(Args$FS)
} else {
  eid <- 'ieu-b-40'
  oid <- 'ukb-b-15541'
  e.file <- '/mnt/GDRIVE/GWAS/IEU.GWAS.200/ieu-b-40.vcf.gz'
  o.file <- '/mnt/GDRIVE/GWAS/IEU.GWAS.200/ukb-b-15541.vcf.gz'
  thisdir <- '/mnt/GDRIVE/src.out/IEU.GWAS.O2E.out/ukb-b-15541/ieu-b-40'
  bcftools.d <- '/tools/bcftools-1.18/bcftools'
  plink.d <- '/tools/plink-1.90'
  a.pval <- 8
  r2 <- 0.001
  kb <- 10000
  FS <- as.logical('T')
  pop <- 'EUR'
  N <- 786578
  olp.file <- glue('{thisdir}/{oid}-LP.vcf.gz')
  e.name <- 'Body Fat Percentage'
  o.name <- 'Gastric Cancer'
  mrfile <- glue('{thisdir}/{oid}.tsv')
}

if (as.integer(a.pval) == 8) {
  b.pval = 7.30103
} else if (as.integer(a.pval) == 7) {
  b.pval = 6.30103
} else if (as.integer(a.pval) == 6) {
  b.pval = 5.30103
} else {
  b.pval = 7.30103
}

TRY <- try({
  
  if (Sys.info()['sysname'] == 'Linux') {
    e.file.tmp = e.file
    e.file.filter = glue("{thisdir}/{gsub(pattern = '.vcf.gz', replacement = '-LP.vcf.gz', x = basename(e.file.tmp), fixed = TRUE)}")
    if (!file.exists(e.file.filter)) {
      system(glue("{bcftools.d} view -i 'LP>={b.pval}' {e.file.tmp} -Oz -o {e.file.filter}"), intern = FALSE)
      system(glue("{bcftools.d} index -t {e.file.filter}"), intern = FALSE)
    }
    e.file = e.file.filter
  } else {
    e.file = e.file
  }
  
  vcfRT = readVcf(e.file)
  e.data = gwasglue::gwasvcf_to_TwoSampleMR(vcf = vcfRT, type = 'exposure')
  e.data = subset(e.data, pval.exposure < 5 * 10 ^ -as.integer(a.pval))
  
  c.data <- ieugwasr::ld_clump(
    clump_kb = kb,
    clump_r2 = r2,
    clump_p = 0.99,
    pop = pop,
    dplyr::tibble(rsid = e.data$SNP, pval = e.data$pval.exposure, id = e.data$id.exposure),
    plink_bin = ifelse(test = Sys.info()['sysname'] == 'Linux', yes = glue('{plink.d}/plink'), no = glue('{plink.d}/plink.exe')),
    bfile = glue('{plink.d}/1kg.v3/{pop}')
  )
  
  e.data <- base::merge(e.data, c.data, by.x = 'SNP', by.y = 'rsid') %>% dplyr::select(-pval, -id)
  
  Ffilter <- 10
  if (FS) {
    f.data <- transform(e.data, R2 = 2*((beta.exposure)^2) * eaf.exposure*(1 - eaf.exposure))
    f.data <- transform(f.data, F = (N - 2) * R2 / (1 - R2))
    if (is.na(N) || is.null(N) || N < 0) {
      f.data
    } else {
      f.data <- f.data[f.data$F > Ffilter, ]
    }
  } else {
    f.data <- e.data
  }
  
  e.vi <- glue('{dirname(e.file)}/{eid}.txt')
  write.table(x = f.data$SNP, file = e.vi, sep = '\t', row.names = FALSE, quote = FALSE, col.names = FALSE)
  
  if (Sys.info()['sysname'] == 'Linux') {
    if (!file.exists(olp.file)) {
      system(glue("{bcftools.d} view -i 'ID=@{e.vi}' {o.file} -Oz -o {olp.file}"), intern = FALSE)
    }
    o.file = olp.file
  } else {
    o.file = o.file
  }
  
  vcfRT = readVcf(o.file)
  o.data = gwasglue::gwasvcf_to_TwoSampleMR(vcf = vcfRT, type = 'outcome')
  o.data <- merge(f.data, o.data, by.x = 'SNP', by.y = 'SNP')
  
  f.data$Phenotype <- e.name
  o.data$Phenotype <- o.name
  
  e.dat <- TwoSampleMR::format_data(
    dat = f.data,
    type = "exposure",
    snps = f.data$SNP,
    snp_col = 'SNP',
    beta_col = 'beta.exposure',
    se_col = 'se.exposure',
    effect_allele_col = 'effect_allele.exposure',
    other_allele_col = 'other_allele.exposure',
    pval_col = 'pval.exposure',
    eaf_col = 'eaf.exposure'
  )
  
  o.dat <- TwoSampleMR::format_data(
    dat = o.data,
    type = "outcome",
    snps = o.data$SNP,
    snp_col = 'SNP',
    beta_col = 'beta.outcome',
    se_col = 'se.outcome',
    effect_allele_col = 'effect_allele.outcome',
    other_allele_col = 'other_allele.outcome',
    pval_col = 'pval.outcome',
    eaf_col = 'eaf.outcome'
  )
  
  h.dat <- TwoSampleMR::harmonise_data(exposure_dat = e.dat, outcome_dat = o.dat)
  
  res.mr <- TwoSampleMR::mr(
    h.dat, 
    method_list = c('mr_wald_ratio', 'mr_egger_regression', 'mr_weighted_median', 'mr_ivw', 'mr_simple_mode', 'mr_weighted_mode', 'mr_egger_regression_bootstrap','mr_two_sample_ml')
  )
  
  mr.odds <- TwoSampleMR::generate_odds_ratios(res.mr)
}, silent = FALSE)

if (class(TRY) == "try-error") {
  write.table('', file = mrfile, sep = '\t', row.names = FALSE, quote = FALSE, col.names = FALSE)
} else {
  mr.odds$id.exposure <- eid
  mr.odds$id.outcome <- oid
  write.table(mr.odds, file = mrfile, sep = '\t', row.names = FALSE, quote = FALSE)
}














