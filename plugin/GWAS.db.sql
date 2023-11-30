-- ----------------------------
-- 1.GWAS DB
-- ----------------------------
DROP TABLE IF EXISTS `dm_gwasdb`;
CREATE TABLE `dm_gwasdb`  (
  `dbid`          			bigint(20)      NOT NULL 	auto_increment	comment '疾病名称表主键',
  `gwas_id` 				varchar(10) 	NOT NULL	UNIQUE			comment 'GWAS ID',
  `gwas_id_online` 			varchar(64) 	NOT NULL	UNIQUE			comment 'GWAS Online ID',
  `gwas_url` 				varchar(512) 	DEFAULT NULL				comment 'GWAS Online URL',
  `gwas_download_url` 		varchar(512) 	DEFAULT NULL				comment 'GWAS Download URL',
  `gwas_year` 				varchar(4) 		DEFAULT NULL				comment 'GWAS Year',
  `gwas_trait` 				varchar(1024) 	DEFAULT NULL				comment 'GWAS Trait',
  `gwas_consortium` 		varchar(1024) 	DEFAULT NULL				comment 'GWAS Consortium',
  `gwas_sample_size` 		varchar(10) 	DEFAULT NULL				comment 'GWAS Sample Size',
  `gwas_snp_size` 			varchar(10) 	DEFAULT NULL				comment 'GWAS SNP Size',
  `gwas_case_size` 			varchar(10) 	DEFAULT NULL				comment 'GWAS Case Size',
  `gwas_control_size` 		varchar(10) 	DEFAULT NULL				comment 'GWAS Control Size',
  `gwas_pmid` 				varchar(128) 	DEFAULT NULL				comment 'GWAS PMID',
  `gwas_category` 			varchar(10) 	DEFAULT NULL				comment 'GWAS Category',
  `gwas_subcategory` 		varchar(10) 	DEFAULT NULL				comment 'GWAS Subcategory',
  `gwas_population` 		varchar(1) 		DEFAULT NULL				comment 'GWAS Population',
  `gwas_gender` 			varchar(1) 		DEFAULT NULL				comment 'GWAS Gender',
  `gwas_author` 			varchar(128) 	DEFAULT NULL				comment 'GWAS Author',
  `gwas_build` 				varchar(1) 		DEFAULT NULL				comment 'GWAS Build',
  `data_source` 			varchar(64) 	DEFAULT NULL				comment '数据来源',
  `is_delete`           	char(1)         DEFAULT '0'                	comment '删除状态（0=未删除 1=已删除）',
  `is_update`           	char(1)     	DEFAULT '0'                	comment '更新状态（0=未更新 1=更新 2=新增）',
  `status`           		char(1)         DEFAULT '0'                	comment '审核状态（0=未审核 1=已审核）',
  `create_by`        		varchar(64)     DEFAULT ''                 	comment '创建者',
  `create_time`      		datetime                                   	comment '创建时间',
  `update_by`        		varchar(64)     DEFAULT ''                 	comment '更新者',
  `update_time`      		datetime                                   	comment '更新时间',
  `remark`           		varchar(2048)    DEFAULT NULL               comment '备注',
  PRIMARY KEY (dbid),
  UNIQUE (gwas_id, gwas_id_online)
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic comment 'GWAD db';

INSERT INTO `dm_gwasdb` VALUES (1, 'GS0000001', 'met-b-225', '', '', '2023', 'CD8mem:%"pre-Th17" (1)', 'Consortium', '10', '10', '10', '10', '', '', '', '1', '', '1', '3', '0', '0', '0', '0', 'admin', sysdate(), '', null, '');
INSERT INTO `dm_gwasdb` VALUES (2, 'GS0000002', 'met-b-226', '', '', '2018', 'CD8mem:%"pre-Th17" (2)', 'Consortium', '10', '10', '10', '10', '', '', '', '1', '', '1', '3', '3', '0', '0', '0', 'admin', sysdate(), '', null, '');




