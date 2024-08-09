# 此脚本用于构建当前目录的图片缓存，会自动排除本身以及产出的数据文件
# 此脚本需要放在存放图片的文件夹内运行，否则将产生不恰当的结果

import hashlib,os,json
from pathlib import Path  
md5list = {}
# 获取当前文件所在的目录  
current_directory = str(Path(__file__).resolve().parent)+"\\"

for item in os.scandir(current_directory):
    if item.is_file():
        with open(item.path, 'rb') as f:
            md5 = hashlib.md5(f.read()).hexdigest()
            path = item.path.split(current_directory)
            if path[1] == "md5.json" or path[1] == "md5.py":
                continue
            md5list[md5] = path[1]
            #print("文件名",path[1],"md5",md5)


# 现在，我们将这个字典写入一个JSON文件  
with open('md5.json', 'w', encoding='utf-8') as json_file:  
    json.dump(md5list, json_file, indent=4)  # indent=4用于美化输出，使JSON文件更易读  
  
print("数据已成功写入JSON文件")