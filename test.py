s = "hello_world"
# 以_分隔
name = ""
for i in s.split("_"):
    name += "".join(i.title())
print(name)
