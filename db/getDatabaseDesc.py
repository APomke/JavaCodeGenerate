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
        if ("varchar" in row[1]):
            row[1] = "String"
        if("int" in row[1]):
            row[1] = "int"
        # 等待后续添加

        field = {"tableName":"{}".format(tableName),"attributesName":"{}".format(row[0]),"attributesType":"{}".format(row[1])}
        # is_nullable = row[2]
        # key = row[3]
        # extra = row[4]
        # table_structure.append((field_name, data_type, is_nullable, key, extra))
        table_structure.append((field))
    return table_structure