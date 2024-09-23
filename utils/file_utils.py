import re
from utils import string_utils

# 获取实体类里的属性名和类型
def get_entity_field_and_type(entity_path):
    # 用来存放获取到的属性
    entity_list = []
    # print(entity_path)
    # 使用正则匹配private后面的内容
    private_pattern = re.compile(r'^\s*private\s+([a-zA-Z0-9_. ]+);')
    with  open(entity_path, "r", encoding='utf-8') as entity_file:
        # 循环读取该文件的每一行
        for line in entity_file:
            if private_pattern.search(line):
                # 消除前面的private和后面的;
                line = line.replace("private","")
                line = line.replace(";","")
                # 消除前面的空格
                line = line.strip()
                # 以空格标志切割出属性类型和属性名
                line = line.split(" ")
                entity_dict = {"type": line[0], "name": line[1], "name_first": string_utils.word_first_letter_size(line[1])}
                entity_list.append(entity_dict)
    # print(entity_list)
    return entity_list

if __name__ == "__main__":
    get_entity_field_and_type("C:\\Users\\admin\\Desktop\\实战\\JavaCodeGenerate\\SpingBootSimpleTemplate\\src\\main\\java\\com\\lidong\\spingbootsimpletemplate\\entity\\HelloWorld.java")