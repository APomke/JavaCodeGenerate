import os
import re

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