import pymysql
# 获取所有表名
def getAllTableName(databaseConfig):
    # 连接数据库
    # print("数据库地址是：",databaseConfig.get("url"))
    conn = pymysql.connect(
        host=databaseConfig.get("url"),
        port=databaseConfig.get("port"),
        user=databaseConfig.get("username"),
        password=databaseConfig.get("password"),
        database=databaseConfig.get("dbname")
    )
    # 创建游标
    cursor = conn.cursor()
    # 编写sql
    sql = "show tables"
    # 运行sql
    cursor.execute(sql)
    # 获取查询结果
    table_list = [tuple[0] for tuple in cursor.fetchall()]
    # 关闭数据库连接
    conn.close()

    return table_list

# 获取表的表结构
def getTableDesc(databaseConfig,tableName):
    # 连接数据库
    # print("数据库地址是：",databaseConfig.get("url"))
    conn = pymysql.connect(
        host=databaseConfig.get("url"),
        port=databaseConfig.get("port"),
        user=databaseConfig.get("username"),
        password=databaseConfig.get("password"),
        database=databaseConfig.get("dbname")
    )
    # 创建游标
    cursor = conn.cursor()
    # 编写sql
    sql = "show columns from {}".format(tableName)
    # 运行sql
    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchall()

    # 解析结果
    table_structure = []
    for row in result:
        row = list(row)
        # 进行属性类型转换
        row[1] = convert_data_type(row[1])

        field = {"tableName":"{}".format(tableName),"attributesName":"{}".format(row[0]),"attributesType":"{}".format(row[1])}
        # is_nullable = row[2]
        # key = row[3]
        # extra = row[4]
        # table_structure.append((field_name, data_type, is_nullable, key, extra))
        table_structure.append((field))
    return table_structure

# 类型处理器 把mysql数据库类型转换为java类型
def convert_data_type(data_type):
    data_type = data_type.lower()  # 转换为小写以避免大小写问题
    if any(keyword in data_type for keyword in ["varchar", "char", "text"]):
        return "String"
    elif "int" in data_type and not any(
            keyword in data_type for keyword in ["tinyint", "smallint", "mediumint", "bigint"]):
        return "int"
    elif any(keyword in data_type for keyword in ["integrt", "id"]):
        return "Long"
    elif any(keyword in data_type for keyword in ["tinyint", "smallint", "mediumint", "boolean"]):
        return "Integer"
    elif "bit" in data_type:
        return "Boolean"
    elif "bigint" in data_type:
        return "BigInteger"
    elif "float" in data_type:
        return "Float"
    elif "double" in data_type:
        return "Double"
    elif "decimal" in data_type:
        return "BigDecimal"
    elif any(keyword in data_type for keyword in ["date", "year"]):
        return "Date"
    elif "time" in data_type:
        return "Time"
    elif any(keyword in data_type for keyword in ["datetime", "timestamp"]):
        return "Timestamp"
    elif "blob" in data_type:
        return "byte[]"
    else:
        return "Object"  # Default type if no match is found