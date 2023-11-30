package com.ruoyi.system.domain;

import com.ruoyi.common.annotation.Excel;
import com.ruoyi.common.core.domain.BaseEntity;
import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;

/**
 * @Author Albert
 * @create 2023-11-29 23:34
 * @DESC GWAS db
 **/

public class SysGwas extends BaseEntity {

    private static final long serialVersionUID = 1L;

    /** dbid */
    private Long dbid;

    /** GWAS ID */
    @Excel(name = "ID")
    private String gwasId;

    /** GWAS Online ID */
    @Excel(name = "OID")
    private String gwasIdOnline;

    /** GWAS Online URL */
    @Excel(name = "OURL")
    private String gwasUrl;

    /** GWAS Download URL */
    @Excel(name = "DURL")
    private String gwasDownloadUrl;

    /** GWAS Year */
    @Excel(name = "Year")
    private String gwasYear;

    /** GWAS Trait */
    @Excel(name = "Trait")
    private String gwasTrait;

    /** GWAS Consortium */
    @Excel(name = "Consortium")
    private String gwasConsortium;

    /** GWAS Sample Size */
    @Excel(name = "Sample Size")
    private String gwasSampleSize;

    /** GWAS SNP Size */
    @Excel(name = "SNP Size")
    private String gwasSnpSize;

    /** GWAS Case Size */
    @Excel(name = "Case Size")
    private String gwasCaseSize;

    /** GWAS Control Size */
    @Excel(name = "Control Size")
    private String gwasControlSize;

    /** GWAS PMID */
    @Excel(name = "PMID")
    private String gwasPmid;

    /** GWAS Category */
    @Excel(name = "GWAS Category")
    private String gwasCategory;

    /** GWAS Subcategory */
    @Excel(name = "GWAS Subcategory")
    private String gwasSubcategory;

    /** GWAS Population */
    @Excel(name = "Population")
    private String gwasPopulation;

    /** GWAS Gender */
    @Excel(name = "Gender")
    private String gwasGender;

    /** GWAS Author */
    @Excel(name = "Author")
    private String gwasAuthor;

    /** GWAS Build */
    @Excel(name = "GWAS Build")
    private String gwasBuild;

    /** 数据来源 **/
    private String dataSource;

    /** IsUpdate（0未更新 1更新 2新增） */
    private String isUpdate;

    /** 状态（0未审核 1已审核） */
    @Excel(name = "状态", readConverterExp = "0=未审核,1=已审核")
    private String status;

    public Long getDbid() {
        return dbid;
    }

    public String getGwasId() {
        return gwasId;
    }

    public String getGwasIdOnline() {
        return gwasIdOnline;
    }

    public String getGwasUrl() {
        return gwasUrl;
    }

    public String getGwasDownloadUrl() {
        return gwasDownloadUrl;
    }

    public String getGwasYear() {
        return gwasYear;
    }

    public String getGwasTrait() {
        return gwasTrait;
    }

    public String getGwasConsortium() {
        return gwasConsortium;
    }

    public String getGwasSampleSize() {
        return gwasSampleSize;
    }

    public String getGwasSnpSize() {
        return gwasSnpSize;
    }

    public String getGwasCaseSize() {
        return gwasCaseSize;
    }

    public String getGwasControlSize() {
        return gwasControlSize;
    }

    public String getGwasPmid() {
        return gwasPmid;
    }

    public String getGwasCategory() {
        return gwasCategory;
    }

    public String getGwasSubcategory() {
        return gwasSubcategory;
    }

    public String getGwasPopulation() {
        return gwasPopulation;
    }

    public String getGwasGender() {
        return gwasGender;
    }

    public String getGwasAuthor() {
        return gwasAuthor;
    }

    public String getGwasBuild() {
        return gwasBuild;
    }

    public String getDataSource() {
        return dataSource;
    }

    public String getIsUpdate() {
        return isUpdate;
    }

    public String getStatus() {
        return status;
    }

    public void setDbid(Long dbid) {
        this.dbid = dbid;
    }

    public void setGwasId(String gwasId) {
        this.gwasId = gwasId;
    }

    public void setGwasIdOnline(String gwasIdOnline) {
        this.gwasIdOnline = gwasIdOnline;
    }

    public void setGwasUrl(String gwasUrl) {
        this.gwasUrl = gwasUrl;
    }

    public void setGwasDownloadUrl(String gwasDownloadUrl) {
        this.gwasDownloadUrl = gwasDownloadUrl;
    }

    public void setGwasYear(String gwasYear) {
        this.gwasYear = gwasYear;
    }

    public void setGwasTrait(String gwasTrait) {
        this.gwasTrait = gwasTrait;
    }

    public void setGwasConsortium(String gwasConsortium) {
        this.gwasConsortium = gwasConsortium;
    }

    public void setGwasSampleSize(String gwasSampleSize) {
        this.gwasSampleSize = gwasSampleSize;
    }

    public void setGwasSnpSize(String gwasSnpSize) {
        this.gwasSnpSize = gwasSnpSize;
    }

    public void setGwasCaseSize(String gwasCaseSize) {
        this.gwasCaseSize = gwasCaseSize;
    }

    public void setGwasControlSize(String gwasControlSize) {
        this.gwasControlSize = gwasControlSize;
    }

    public void setGwasPmid(String gwasPmid) {
        this.gwasPmid = gwasPmid;
    }

    public void setGwasCategory(String gwasCategory) {
        this.gwasCategory = gwasCategory;
    }

    public void setGwasSubcategory(String gwasSubcategory) {
        this.gwasSubcategory = gwasSubcategory;
    }

    public void setGwasPopulation(String gwasPopulation) {
        this.gwasPopulation = gwasPopulation;
    }

    public void setGwasGender(String gwasGender) {
        this.gwasGender = gwasGender;
    }

    public void setGwasAuthor(String gwasAuthor) {
        this.gwasAuthor = gwasAuthor;
    }

    public void setGwasBuild(String gwasBuild) {
        this.gwasBuild = gwasBuild;
    }

    public void setDataSource(String dataSource) {
        this.dataSource = dataSource;
    }

    public void setIsUpdate(String isUpdate) {
        this.isUpdate = isUpdate;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this, ToStringStyle.MULTI_LINE_STYLE)
                .append("dbid", getDbid())
                .append("gwasId", getGwasId())
                .append("gwasIdOnline", getGwasIdOnline())
                .append("gwasUrl", getGwasUrl())
                .append("gwasDownloadUrl", getGwasDownloadUrl())
                .append("gwasYear", getGwasYear())
                .append("gwasTrait", getGwasTrait())
                .append("gwasConsortium", getGwasConsortium())
                .append("gwasSampleSize", getGwasSampleSize())
                .append("gwasSnpSize", getGwasSnpSize())
                .append("gwasCaseSize", getGwasCaseSize())
                .append("gwasControlSize", getGwasControlSize())
                .append("gwasPmid", getGwasPmid())
                .append("gwasCategory", getGwasCategory())
                .append("gwasSubcategory", getGwasSubcategory())
                .append("gwasPopulation", getGwasPopulation())
                .append("gwasGender", getGwasGender())
                .append("gwasAuthor", getGwasAuthor())
                .append("gwasBuild", getGwasBuild())
                .append("dataSource", getDataSource())
                .append("isUpdate", getIsUpdate())
                .append("status", getStatus())
                .append("createBy", getCreateBy())
                .append("createTime", getCreateTime())
                .append("updateBy", getUpdateBy())
                .append("updateTime", getUpdateTime())
                .append("remark", getRemark())
                .toString();
    }
}
