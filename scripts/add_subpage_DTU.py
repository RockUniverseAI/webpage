import os

# 主网页文件路径
index_file = "index.html"

# 目标 scan 列表
scan_list = [37, 40, 55, 63, 65, 69, 83, 93, 105, 106, 110, 114, 118, 122]

# 检查主网页是否存在
if not os.path.exists(index_file):
    print(f"主网页 '{index_file}' 不存在，请检查路径。")
    exit()

# 要插入的 HTML 模板，注意转义花括号
# html_template = '''
# <a href="sub_page/DTU/model_scan{{}}.html">
#   <img src="assets/RockUniverse/DTU/scan{{}}.webp" alt="Model scan{{}}" class="thumbnail">
# </a>
# '''

html_template = '''
            <a href="sub_page/DTU/model_scan{}.html">
              <img src="assets/RockUniverse/DTU/scan{}.webp" alt="Model scan{}" class="thumbnail">
            </a>
'''


# 读取原始内容
with open(index_file, "r", encoding="utf-8") as file:
    content = file.readlines()

# 找到插入点
insert_line = None
search_string = 'href="sub_page/DTU/model_scan24.html"'  # 不要求整行完全匹配，只匹配关键部分

for i, line in enumerate(content):
    if search_string in line.strip():  # 忽略空格进行匹配
        insert_line = i + 3  # 在该行后插入
        break

if insert_line is None:
    print("未找到插入点，请检查主网页的内容格式。以下是文件内容调试信息：")
    for i, line in enumerate(content):
        print(f"第 {i + 1} 行: {line.strip()}")
    exit()

# 生成新 HTML 代码并插入
new_html_snippets = [html_template.format(scan, scan, scan) for scan in scan_list]
# print(f"new_html_snippets is {new_html_snippets}")
content[insert_line:insert_line] = new_html_snippets  # 插入生成的代码

# 写回文件
with open(index_file, "w", encoding="utf-8") as file:
    file.writelines(content)

print("子网页引用代码已成功插入到主网页中！")