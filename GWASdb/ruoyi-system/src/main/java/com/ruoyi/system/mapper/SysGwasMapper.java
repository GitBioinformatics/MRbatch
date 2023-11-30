package com.ruoyi.system.mapper;

import com.ruoyi.system.domain.SysGwas;

import java.util.List;

/**
 * @Author Albert
 * @create 2023-11-29 23:58
 * @DESC GWAS Mapper
 **/


public interface SysGwasMapper {

    /**
     * 查询 SysGwas 数据集合
     *
     * @return SysGwas 数据集合
     */
    public List<SysGwas> selectSysGwasList();

}
