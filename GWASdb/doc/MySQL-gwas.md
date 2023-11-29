# MySQL 安装部署 Linux

## 官网下载最新版 MySQL

[MySQL 官网](https://dev.mysql.com/downloads/mysql/5.7.html#downloads)

选择相应版本，这里选择：`mysql-5.7.25-linux-glibc2.12-x86_64.tar.gz`。

## 上传或 wget 下载 MySQL

```
wget ftp://nasdb.cn/Ydata/mysql-5.7.25-linux-glibc2.12-x86_64.tar.gz
```

## 解压 MySQL 安装包

```
tar -zxvf mysql-5.7.25-linux-glibc2.12-x86_64.tar.gz
mv mysql-5.7.25-linux-glibc2.12-x86_64 mysql-5.7.25
cd mysql-5.7.25/
MySQL Home: /tools/mysql-5.7.25
MySQL user: gwas
```

## 新建 my.cnf 文件

可以先通过`netstat -atunlp | grep 30306`命令提前确定 port 是否已经被占用了。然后在 MySQL 的 HOME 目录下新建一个 my.cnf 文件，添加以下内容，注意需要修改路径和端口号 (port) 。

```
[client]
port=30306
socket=/tools/mysql-5.7.25/mysql.sock

[mysqld]
port=30306
basedir=/tools/mysql-5.7.25
datadir=/tools/mysql-5.7.25/data
pid-file=/tools/mysql-5.7.25/mysql.pid
socket=/tools/mysql-5.7.25/mysql.sock
log_error=/tools/mysql-5.7.25/error.log

innodb_file_per_table=1
innodb_file_format=Barracuda
innodb_file_format_check=ON
innodb_log_file_size=512M
innodb_strict_mode=0
[mysqld_safe]
err-log=/tools/mysql-5.7.25/error.log
pid-file=/tools/mysql-5.7.25/mysql.pid
```

## 开始安装

进入 MySQL 目录，开始安装 MySQL

```
# 注意设置对应的用户.
/tools/mysql-5.7.25/bin/mysqld --defaults-file=/tools/mysql-5.7.25/my.cnf --initialize --user=gwas --basedir=/tools/mysql-5.7.25 --datadir=/tools/mysql-5.7.25/data
```

## 启动

```
# 注意设置对应的用户.
/tools/mysql-5.7.25/bin/mysqld_safe --defaults-file=/tools/mysql-5.7.25/my.cnf --user=gwas &
```

## 在 error.log 文件中获取 root 用户密码

```
cat /tools/mysql-5.7.25/error.log | grep root@localhost
```

## 使用 root 用户登陆 MySQL

```
/tools/mysql-5.7.25/bin/mysql -u root -p -S /tools/mysql-5.7.25/mysql.sock
```

## 修改 root 密码

```
# 初次登陆需要修改密码.
set password for root@localhost = password('gwasmpu@root');
```

## 新增一个子用户

```
CREATE USER 'gwas'@'localhost' IDENTIFIED BY 'gwasxing@mpugwas';
```

## 允许用户远程访问 MySQL 数据库

```
GRANT ALL PRIVILEGES ON *.* TO 'gwas'@'%' IDENTIFIED BY 'gwasxing@mpugwas' WITH GRANT OPTION;
```

# SSH

```shell
url: jdbc:mysql://42.194.182.237:30306/GWAS?useUnicode=true&characterEncoding=utf8&zeroDateTimeBehavior=convertToNull&useSSL=true&serverTimezone=GMT%2B8
username: gwas
password: gwasxing@mpugwas
```



 
