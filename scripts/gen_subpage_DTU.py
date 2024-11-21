import os
import shutil

# 当前路径下的子文件夹和源文件
sub_page_folder = "sub_page/DTU"
source_file = os.path.join(sub_page_folder, "model_scan24.html")

# 目标 scan 列表
scan_list = [37, 40, 55, 63, 65, 69, 83, 93, 105, 106, 110, 114, 118, 122]

# 检查子文件夹是否存在
if not os.path.exists(sub_page_folder):
    print(f"子文件夹 '{sub_page_folder}' 不存在，请检查路径。")
    exit()

# 检查源文件是否存在
if not os.path.exists(source_file):
    print(f"源文件 '{source_file}' 不存在，请检查路径。")
    exit()

# 遍历 scan 列表，复制并替换内容
for scan in scan_list:
    # 目标文件名
    target_file = os.path.join(sub_page_folder, f"model_scan{scan}.html")
    
    # 复制文件
    shutil.copy(source_file, target_file)
    
    # 替换内容
    with open(target_file, "r") as file:
        content = file.read()
    
    # 替换 `24` 为目标 scan
    # new_content = content.replace("scan24", f"scan{scan}").replace("scan24.glb", f"scan{scan}.glb").replace("scan24.webp", f"scan{scan}.webp")
    # new_content = content.replace("scan24", f"scan{scan}").replace("scan24.glb", f"scan{scan}.glb").replace("scan24.webp", f"scan{scan}.webp")

    new_content = content

    new_content = new_content.replace('<h1 class="title is-1 publication-title">Scan24</h1>', f'<h1 class="title is-1 publication-title">Scan{scan}</h1>')
    new_content = new_content.replace('<model-viewer alt="scan24" src="assets/RockUniverse/DTU/scan24.glb" poster="assets/RockUniverse/DTU/scan24.webp"', 
    f'<model-viewer alt="scan{scan}" src="assets/RockUniverse/DTU/scan{scan}.glb" poster="assets/RockUniverse/DTU/scan{scan}.webp"')
    
    # 写回文件
    with open(target_file, "w") as file:
        file.write(new_content)
    
    print(f"生成文件: {target_file}")

print("任务完成！")