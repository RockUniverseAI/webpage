import os

# 定义根文件夹
root_dir = './sub_page/'

# 目标字符串
old_return = '<a href="../index.html">Return</a>'
new_return = '<a href="https://rockuniverseai.github.io/webpage/">Return</a>'

# 遍历所有子文件夹及文件
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):  # 只处理 .html 文件
            file_path = os.path.join(subdir, file)
            
            # 打开文件并读取内容
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            
            # 替换所有的 return
            updated_content = file_content.replace(old_return, new_return)
            
            # 如果有更改，保存文件
            if updated_content != file_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Updated: {file_path}")