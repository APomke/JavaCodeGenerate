import os
import toml
from jinja2 import Template
from template.eneity import entity_template_str
from template.service import service_template_str
from template.serviceimpl import serviceimpl_template_str
from db.get_database_desc import get_all_table_name, get_table_desc
from utils.string_utils import word_first_letter_size
from utils.package_utils import get_java_project_package_name
import sys


config = {}
database_config = {}


# 读取config.toml配置文件
def load_config():
    
    global config
    global database_config

    config = toml.load('config.toml')
    database_config = config.get("database")


# 判断要生成那些层的代码
def generate_code():
    print("开始生成代码")
    print("项目路径为：", config.get("generate").get("projectLocalPath"))
    if config.get("generate").get("isGenerateEntity"):
        # print("开始生成entity层代码")
        generate_entity_code()
    if config.get("generate").get("isGenerateService"):
        # print("开始生成service层代码")
        generate_service_code()
    if config.get("generate").get("isGenerateController"):
        # print("开始生成controller层代码")
        generate_controller_code()


# 生成entity层实体类代码
def generate_entity_code():
    print("开始生成entity层实体类代码")
    # 读取项目，获取项目包名
    package_name = get_java_project_package_name(config.get("generate").get("projectLocalPath"))
    if package_name:
        print("获取包名为:{}".format(package_name))
    else:
        print("未获取到包名，请检查配置文件projectLocalPath项")
        sys.exit(0)
    package_name_root = package_name
    # 从数据库获取表名与表结构
    table_list = get_all_table_name(database_config)
    if len(table_list) == 0:
        print("未查询到表无法生成代码请在数据库添加表")
        sys.exit(0)
    print("查询到{}张表".format(len(table_list)))

    table_structure = []
    for i in table_list:
        table_structure.append(get_table_desc(database_config, i))

    # 判断是否自定义生成代码的路径
    if config.get("generate").get("EntityGenerateLocalPath") != "":
        print("需要保存到自定义路径：", config.get("generate").get("EntityGenerateLocalPath"))

    # 把需要的数据传输到entity代码模板里
    for list in table_structure:
        # 生成类名为首字母大写
        class_name = word_first_letter_size(list[0].get("table_name"))
        tmpl = Template(entity_template_str)
        result = tmpl.render(package_name=package_name_root, table_structure=list, class_name=class_name)

        # 保存到项目entity目录
        # 判断是否自定义生成代码的路径
        if config.get("generate").get("EntityGenerateLocalPath") != "":
            save_code_to_java_project_to_path(config.get("generate").get("EntityGenerateLocalPath"), list[0].get("table_name"), result)
        else:
            package_name = package_name.replace(".", "\\")
            save_code_to_java_project("entity", result, package_name, list[0].get("table_name"))
    print("entity层代码生成完成")


# 生成service层代码
def generate_service_code():
    print("开始生成service层代码")

    # 读取项目，获取项目包名
    package_name = get_java_project_package_name(config.get("generate").get("projectLocalPath"))
    if package_name:
        print("获取包名为:{}".format(package_name))
    else:
        print("未获取到包名，请检查配置文件projectLocalPath项")
        sys.exit(0)

    # 生成service接口

    # 读取entity层对象 获取类名
    package_name_root = package_name

    package_name = package_name.replace(".", "\\")
    path = config.get("generate").get("projectLocalPath") + "\\src" + "\\main" + "\\java" + "\\" + package_name + "\\" + "entity"
    print("查找{}路径下的实体类".format(path))
    for subdir, _, files in os.walk(path):
        if files is None:
            print("未在entity目录里找到实体类，生成结束")
            sys.exit(0)
        for file in files:
            if file.split(".")[1] == "java":
                class_name = file.split(".")[0] + "Service"
                tmpl = Template(service_template_str)
                result = tmpl.render(class_name=class_name, package_name=package_name_root,entity_name=file.split(".")[0],package_name_root=package_name_root)
                file_name = class_name
                # 保存service接口代码到java项目
                # 判断是否自定义生成代码的路径
                if config.get("generate").get("ServiceGenerateLocalPath") != "":
                    save_code_to_java_project_to_path(config.get("generate").get("ServiceGenerateLocalPath"),file_name,result)
                else:
                    save_code_to_java_project("service", result, package_name, file_name)
                print("service接口层代码生成完成")

                # 生成service实现层接口
                mapper_name = file.split(".")[0] + "Mapper"
                entity_name = file.split(".")[0]
                service_name = file.split(".")[0] + "Service"
                impl_class_name = file.split(".")[0] + "Service" + "Impl"
                service_impl_tmpl = Template(serviceimpl_template_str)
                impl_result = service_impl_tmpl.render(package_name=package_name_root, mapper_name=mapper_name, entity_name=entity_name, service_name=service_name, class_name=impl_class_name)

                # print(impl_result)
                # 保存service接口实现到Java项目
                if config.get("generate").get("ServiceGenerateLocalPath") != "":
                    diy_path = config.get("generate").get("ServiceGenerateLocalPath") + "\\impl"
                    save_code_to_java_project_to_path(diy_path,impl_class_name,impl_result)
                else:
                    save_code_to_java_project("service\\impl", impl_result, package_name,impl_class_name)






# 生成controller层代码
def generate_controller_code():
    print("开始生成controller层代码")


# 保存生成的代码到java项目里
def save_code_to_java_project(dir_name, code, package_name, file_name):
    # 设置文件名
    path = config.get("generate").get("projectLocalPath") + "\\src" + "\\main" + "\\java"
    path = path + "\\" + package_name + "\\" + dir_name
    # print("路径为：",path)
    if not os.path.exists(path):  # 如果路径不存在
        os.makedirs(path)
    # 每个单词首字母大小
    if dir_name == "entity":
        file_name = word_first_letter_size(file_name)
    file_name = file_name + ".java"
    path = path + "\\" + file_name

    # 判断要生成的文件是否在排除列表里
    if path in config.get("generate").get("ExclusionList"):
        print("{}在配置文件ExclusionList项中，代码将不会保存".format(path))
        return None
    else:
        with open(path, 'wb') as f:
            code = code.encode('utf-8')
            f.write(code)
        print(file_name, "生成成功")
        return None
    

# 保存生成的代码到自定义路径
def save_code_to_java_project_to_path(path, file_name, code):
    # 设置文件名
    # 每个单词首字母大小
    file_name = word_first_letter_size(file_name)
    file_name = file_name + ".java"
    if not os.path.exists(path):  # 如果路径不存在
        os.makedirs(path)
    path = path + "\\" + file_name
    # 判断要生成的文件是否在排除列表里
    if path in config.get("generate").get("ExclusionList"):
        print("{}在配置文件ExclusionList项中，代码将不会保存".format(path))
        return None
    else:
        with open(path, 'wb') as f:
            code = code.encode('utf-8')
            f.write(code)
        print("生成成功:{}".format(path))
        return None


if __name__ == "__main__":
    load_config()
    generate_code()
