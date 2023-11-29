package com.ruoyi.web.controller.system;

import com.ruoyi.common.config.RuoYiConfig;
import com.ruoyi.common.core.controller.BaseController;
import com.ruoyi.common.core.page.TableDataInfo;
import com.ruoyi.system.domain.SysGwas;
import com.ruoyi.system.service.ISysGwasService;
import org.apache.shiro.authz.annotation.RequiresPermissions;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

/**
 * @Author Albert
 * @create 2023-11-29 23:53
 * @DESC GWAS Controller
 **/

@Controller
@RequestMapping("/system/gwas")
public class SysGwasController  extends BaseController {

    private String prefix = "system/gwas";

    @Autowired
    private ISysGwasService sysGwasService;

    @RequiresPermissions("system:gwas:view")
    @GetMapping()
    public String openlog() {
        return prefix + "/gwas";
    }

    /* 列表展示 */
    @RequiresPermissions("system:gwas:list")
    @PostMapping("/list")
    @ResponseBody
    public TableDataInfo list(SysGwas sysGwas) {
        startPage();
        List<SysGwas> list = sysGwasService.selectSysGwasList();
        return getDataTable(list);
    }
}
