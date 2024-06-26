options(stringsAsFactors = FALSE, warn = -1, scipen = 200)
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
    'efile', 'e', 1, 'character', 'exposure file',
    'ofile', 'o', 1, 'character', 'outcome file',
    'ename', 'f', 1, 'character', 'exposure name',
    'oname', 'p', 1, 'character', 'outcome name',
    'oid', 'q', 1, 'character', 'outcome id',
    'plinkd', 'x', 1, 'character', 'plink',
    'bcftoolsd', 'y', 1, 'character', 'bcftools',
    
    'thisdir', 'v', 1, 'character', 'thisdir',
    'sn', 'n', 1, 'integer', 'sample number',
    'mrfile', 'u', 1, 'character', 'mrfile'),
    byrow = TRUE,
    ncol = 5)
  Args = getopt(command)
  
  if (!is.null(Args$help) || is.null(Args$efile) || is.null(Args$ofile) || is.null(Args$ename) || is.null(Args$oname) || is.null(Args$oid) || is.null(Args$plinkd) || is.null(Args$bcftoolsd) || is.null(Args$mrfile) || is.null(Args$thisdir) || is.null(Args$sn)) {
    cat(paste(getopt(command, usage = TRUE), "\n"))
    q( status = 1)
  }
  e.file <- Args$efile
  o.file <- Args$ofile
  e.name <- Args$ename
  o.name <- Args$oname
  oid <- Args$oid
  plink.d <- Args$plinkd
  bcftools.d <- Args$bcftoolsd
  mrfile <- Args$mrfile
  thisdir <- Args$thisdir
  N <- as.integer(Args$sn)
  olp.file <- glue('{thisdir}/{oid}-LP.vcf.gz')
} else {
  e.file <- 'E:/BaiduNetdiskWorkspace/003.MPU/004.Batch.MR/test/ieu-a-2.vcf.gz'
  o.file <- 'E:/BaiduNetdiskWorkspace/003.MPU/004.Batch.MR/test/ieu-a-7.vcf.gz'
  e.name <- 'Body Fat Percentage'
  o.name <- 'Gastric Cancer'
  oid <- 'ieu-a-7'
  plink.d <- 'E:/BaiduNetdiskWorkspace/005.Bioinformatics/MRanalysis/www/bin'
  bcftools.d <- '/tools/bcftools-1.18/bcftools'
  mrfile <- glue('E:/BaiduNetdiskWorkspace/003.MPU/004.Batch.MR/test/MR.out/{oid}.tsv')
  N <- 338903
}


TRY <- try({
  vcfRT = readVcf(e.file)
  e.data = gwasglue::gwasvcf_to_TwoSampleMR(vcf = vcfRT, type = 'exposure')
  e.data = subset(e.data, pval.exposure < 5e-8)
  
  c.data <- ieugwasr::ld_clump(
    clump_kb = 10000,
    clump_r2 = 0.001,
    clump_p = 0.99,
    pop = 'EUR',
    dplyr::tibble(rsid = e.data$SNP, pval = e.data$pval.exposure, id = e.data$id.exposure),
    plink_bin = ifelse(test = Sys.info()['sysname'] == 'Linux', yes = glue('{plink.d}/plink'), no = glue('{plink.d}/plink.exe')),
    bfile = glue('{plink.d}/1kg.v3/EUR')
  )
  
  e.data <- base::merge(e.data, c.data, by.x = 'SNP', by.y = 'rsid') %>% dplyr::select(-pval, -id)
  
  Ffilter <- 10
  f.data <- transform(e.data, R2 = 2*((beta.exposure)^2) * eaf.exposure*(1 - eaf.exposure))
  f.data <- transform(f.data, F = (N - 2) * R2 / (1 - R2))
  if (is.na(N) || is.null(N) || N < 0) {
    f.data
  } else {
    f.data <- f.data[f.data$F > Ffilter, ]
  }
  
  if (Sys.info()['sysname'] == 'Linux') {
    system(glue('{bcftools.d} index -t {o.file}'), intern = FALSE)
    system(glue('{bcftools.d} isec -n =2 -w 1 {o.file} {e.file} -Oz -o {olp.file}'), intern = FALSE)
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
  write.table(mr.odds, file = mrfile, sep = '\t', row.names = FALSE, quote = FALSE)
}














