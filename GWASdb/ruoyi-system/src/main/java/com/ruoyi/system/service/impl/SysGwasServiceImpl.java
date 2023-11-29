package com.ruoyi.system.service.impl;

import com.ruoyi.system.domain.SysGwas;
import com.ruoyi.system.mapper.SysGwasMapper;
import com.ruoyi.system.service.ISysGwasService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @Author Albert
 * @create 2023-11-30 0:00
 * @DESC GWAS Service Impl
 **/

@Service
public class SysGwasServiceImpl implements ISysGwasService {

    @Autowired
    private SysGwasMapper sysGwasMapper;

    /**
     * 查询 SuggestDisease 数据集合
     *
     * @return SuggestDisease 数据集合
     */
    @Override
    public List<SysGwas> selectSysGwasList() {
        return sysGwasMapper.selectSysGwasList();
    }
}

