import re

def find_functions(file_path, search_str):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    functions = []
    func_pattern = re.compile(r'(bool|void|int|fixed|string) lib[\dA-F]+_gf_(.*?)\s')
    search_pattern = re.compile(r'\b' + re.escape(search_str) + r'\b')
    func_body = ""
    func_name = ""
    brace_count = 0

    for line in content:
        if brace_count == 0:
            match = func_pattern.search(line)
            if match:
                func_name = match.group(2)
                brace_count += line.count("{")
                func_body += line
        else:
            brace_count += line.count("{")
            brace_count -= line.count("}")
            func_body += line
            if brace_count == 0:
                if search_pattern.search(func_body):
                    functions.append(func_name)
                func_body = ""
                func_name = ""

    return functions

# 查找包含 "123" 的函数
functions = find_functions('C:/Users/hnldl/Desktop/MapScript.galaxy', '4520200')
for func in functions:
    print(func)