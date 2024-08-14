# 项目介绍
使用python编写的java SpringBoot项目代码生成器

可生成entity，service，controller层的基本代码

节省重复的代码编写

通过config.toml来配置生成

python版本:3.10

# 基本原理
从数据库读取表结构来生成实体类再通过实体类生成service层和controller层的代码

# 配置说明
```angular2html
# config.toml

[generate]
projectLocalPath = "" # java项目根目录路径

isGenerateController = true # 是否生成controller控制器层代码
isGenerateService = true # 是否生成service层代码
isGenerateEntity = true # 是否生成entity层实体类代码

# 如果需要自定义生成代码的路径可以在下面配置，不自定义忽视即可
ControllerGenerateLocalPath = "" # 存放controller控制器层代码生成的本地路径
ServiceGenerateLocalPath = "" # 存放service层代码生成的本地路径
EntityGenerateLocalPath = "" # 存放entity层实体类代码生成的本地路径


[database]
url = "" # 数据库url
port = 3306
username = "" # 数据库用户名
password = "" # 数据库密码
dbname = "" # 数据库名称
```
