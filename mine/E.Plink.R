options(stringsAsFactors = FALSE, warn = -1, scipen = 200)
suppressMessages(library(glue))
suppressMessages(library(dplyr))
suppressMessages(library(getopt))
suppressMessages(library(ieugwasr))
suppressMessages(library(gwasglue))
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
    'plinkd', 'x', 1, 'character', 'plink',
    'pval', 'v', 1, 'integer', 'pval',
    'r2', 'r', 1, 'integer', 'r2',
    'kb', 'k', 1, 'integer', 'kb',
    
    'sn', 'n', 1, 'integer', 'sample number',
    'pop', 'p', 1, 'character', 'pop type'),
    byrow = TRUE,
    ncol = 5)
  Args = getopt(command)
  
  if (!is.null(Args$help) || is.null(Args$efile) || is.null(Args$plinkd) || is.null(Args$pval) || is.null(Args$r2)  || is.null(Args$kb)  || is.null(Args$pop) || is.null(Args$sn)) {
    cat(paste(getopt(command, usage = TRUE), "\n"))
    q( status = 1)
  }
  e.file <- Args$efile
  plink.d <- Args$plinkd
  pop <- Args$pop
  pval <- 5 * 10 ^ -as.integer(Args$pval)
  N <- as.integer(Args$sn)
  r2 <- as.integer(Args$r2)
  kb <- as.integer(Args$kb)
} else {
  e.file <- 'E:/BaiduNetdiskWorkspace/003.MPU/004.Batch.MR/test/ieu-a-2.vcf.gz'
  plink.d <- 'E:/BaiduNetdiskWorkspace/005.Bioinformatics/MRanalysis/www/bin'
  pval <- 5e-8
  pop <- 'EUR'
  N <- 33226
  r2 <- 0.001
  kb <- 10000
}


TRY <- try({
  eid <- gsub(pattern = '.vcf.gz', replacement = '', x = basename(e.file), fixed = TRUE)
  eofile <- glue('{dirname(e.file)}/{eid}.xlsx')
  eofilen <- glue('{dirname(e.file)}/{eid}.txt')
  
  vcfRT = readVcf(e.file)
  e.data = gwasglue::gwasvcf_to_TwoSampleMR(vcf = vcfRT, type = 'exposure')
  e.data = subset(e.data, pval.exposure < pval)
  
  c.data <- ieugwasr::ld_clump(
    clump_kb = kb,
    clump_r2 = r2,
    clump_p = 0.99,
    pop = pop,
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
}, silent = FALSE)

if (class(TRY) == "try-error") {
  openxlsx::write.xlsx(x = '', file = eofile)
  write.table(x = 0, file = eofilen, sep = '\t', row.names = FALSE, quote = FALSE)
} else {
  openxlsx::write.xlsx(x = f.data, file = eofile)
  write.table(x = nrow(f.data), file = eofilen, sep = '\t', row.names = FALSE, quote = FALSE)
}














