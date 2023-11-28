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
    'pval', 'a', 1, 'integer', 'pval',
    
    'thisdir', 'v', 1, 'character', 'thisdir',
    'sn', 'n', 1, 'integer', 'sample number',
    'mrfile', 'u', 1, 'character', 'mrfile'),
    byrow = TRUE,
    ncol = 5)
  Args = getopt(command)
  
  if (!is.null(Args$help) || is.null(Args$efile) || is.null(Args$ofile) || is.null(Args$pval) || is.null(Args$ename) || is.null(Args$oname) || is.null(Args$oid) || is.null(Args$bcftoolsd) || is.null(Args$mrfile) || is.null(Args$thisdir)) {
    cat(paste(getopt(command, usage = TRUE), "\n"))
    q( status = 1)
  }
  e.file <- Args$efile
  o.file <- Args$ofile
  e.name <- Args$ename
  o.name <- Args$oname
  oid <- Args$oid
  bcftools.d <- Args$bcftoolsd
  mrfile <- Args$mrfile
  thisdir <- Args$thisdir
  pval <- 5 * 10 ^ -as.integer(Args$pval)
  olp.file <- glue('{thisdir}/{oid}-LP.vcf.gz')
} else {
  e.file <- 'G:/src.out/P0DJD7.xlsx'
  o.file <- 'E:/BaiduNetdiskWorkspace/003.MPU/004.Batch.MR/test/ieu-a-7.vcf.gz'
  e.name <- 'Body Fat Percentage'
  o.name <- 'Gastric Cancer'
  oid <- 'bbj-a-7'
  bcftools.d <- '/tools/bcftools-1.18/bcftools'
  pval <- 5e-8
  mrfile <- glue('E:/BaiduNetdiskWorkspace/003.MPU/004.Batch.MR/test/MR.out/{oid}.tsv')
}


TRY <- try({
  f.data <- openxlsx::read.xlsx(e.file)
  e.vcf.gz <- glue("{dirname(e.file)}/{gsub(pattern = '.xlsx', replacement = '.vcf.gz', x = basename(e.file), fixed = TRUE)}")
  
  if (Sys.info()['sysname'] == 'Linux') {
    system(glue('{bcftools.d} index -t {o.file}'), intern = FALSE)
    system(glue('{bcftools.d} isec -n =2 -w 1 {o.file} {e.vcf.gz} -Oz -o {olp.file}'), intern = FALSE)
    o.file = olp.file
  } else {
    o.file = o.file
  }
  
  vcfRT = readVcf(o.file)
  o.data = gwasglue::gwasvcf_to_TwoSampleMR(vcf = vcfRT, type = 'outcome')
  o.data <- merge(f.data, o.data, by.x = 'SNP', by.y = 'SNP')
  o.data <- o.data %>% dplyr::filter(pval.outcome > pval)
  
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










