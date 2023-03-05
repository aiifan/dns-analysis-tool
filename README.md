# dns-analysis-tool
使用Pyside6和dnspython编写的批量DNS解析器


# 介绍

使用Pyside6和dnspython编写的批量DNS解析器
刚学习，写的不太好，大家一起学习

多个DNS服务器，多个域名，批量解析


# 使用方法

多个dns服务器和多个域名以英文逗号(,)分割

导入域名文件为txt文本，一行一个域名。
如

    ```
    qq.com
    baidu.com
    360.com
    ```

# 编译

qt支持所有系统，可以使用打包工具自行打包

资源有限，仅提供一份windows的exe文件，使用pyinstaller打包的。为了win7下运行，使用Python3.8.5版本