import os
import re
import toml
from jinja2 import Template
from template.eneity import entity_template_str
from db.getDatabaseDesc import getAllTableName,getTableDesc
import sys

# 读取config.toml配置文件
def loadConfig():
    global config
    config = toml.load('config.toml')
    global databaseConfig
    databaseConfig = config.get("database")

# 判断要生成那些层的代码
def generateCode():
    print("开始生成代码")
    print("项目路径为：",config.get("generate").get("projectLocalPath"))
    if(config.get("generate").get("isGenerateEntity")):
        # print("开始生成entity层代码")
        generateEntityCode()
    if(config.get("generate").get("isGenerateService")):
        # print("开始生成service层代码")
        generateServiceCode()
    if(config.get("generate").get("isGenerateController")):
        # print("开始生成controller层代码")
        generateConttrollerCode()

# 生成entity层实体类代码
def generateEntityCode():
    print("开始生成entity层实体类代码")
    # 读取项目，获取项目包名
    packageName = getJavaProjectPackageName(config.get("generate").get("projectLocalPath"))
    if(packageName):
        print("获取包名为:{}".format(packageName))
    else:
        print("未获取到包名，请检查配置文件projectLocalPath项")
        sys.exit(0)


    # 从数据库获取表名与表结构
    tableList = getAllTableName(databaseConfig)
    if(len(tableList) == 0):
        print("未查询到表无法生成代码请在数据库添加表")
        sys.exit(0)
    print("查询到{}张表".format(len(tableList)))

    tableStructure = []
    for i in tableList:
        tableStructure.append(getTableDesc(databaseConfig,i))

    # 把需要的数据传输到entity代码模板里
    for list in tableStructure:
        # print(list)
        tmpl = Template(entity_template_str)
        result = tmpl.render(packageName=packageName, tableStructure=list)
        # 保存到项目entity目录
        packageName = packageName.replace(".","\\")
        saveCodeToJavaProject("entity",result,packageName,list[0].get("tableName"))



    # 读取entity代码模板
    # print(entity_template_str)


# 生成service层代码
def generateServiceCode():
    print("开始生成service层代码")

# 生成controller层代码
def generateConttrollerCode():
    print("开始生成controller层代码")

# 读取java项目获取项目包名
def getJavaProjectPackageName(rootDir):
    main_class_pattern = re.compile(r'^\s*@SpringBootApplication')
    package_pattern = re.compile(r'^\s*package\s+([a-zA-Z0-9_.]+);')

    for subdir, _, files in os.walk(rootDir):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if main_class_pattern.search(line):
                            for j in range(i - 10, i):
                                if j >= 0:
                                    package_match = package_pattern.match(lines[j])
                                    if package_match:
                                        return package_match.group(1)
    return None


# 保存生成的代码到java项目里
def saveCodeToJavaProject(dirName,code,packageName,tableName):
    # 设置文件名
    fileName = tableName + ".java"
    path = config.get("generate").get("projectLocalPath") + "\\src" + "\\main" + "\\java"
    path = path + "\\" + packageName + "\\" + dirName
    # print("路径为：",path)
    if not os.path.exists(path):  # 如果路径不存在
        os.makedirs(path)

    path = path + "\\" + fileName

    with open(path, 'wb') as f:
        code = code.encode('utf-8')
        f.write(code)
    print(fileName,"生成成功")


    return None

if __name__ == "__main__":
    loadConfig()
    generateCode()