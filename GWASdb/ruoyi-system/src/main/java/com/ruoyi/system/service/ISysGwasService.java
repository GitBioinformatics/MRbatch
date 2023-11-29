package com.ruoyi.system.service;

import com.ruoyi.system.domain.SysGwas;

import java.util.List;

/**
 * @Author Albert
 * @create 2023-11-29 23:59
 * @DESC GWAS Service
 **/

public interface ISysGwasService {

    /**
     * 查询 SysGwas 数据集合
     *
     * @return SysGwas 数据集合
     */
    public List<SysGwas> selectSysGwasList();
}
