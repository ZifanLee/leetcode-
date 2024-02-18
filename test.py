import re

str = "123456."
patterns = r"^(0|[1-9][0-9]*)(\.[0-9]+)?$"
tmp = str.split(",")
print(re.fullmatch(patterns, str))

dp = [[[0,0,0]]*2 for _ in range(2)]
print(dp)

import os
import glob

current_dir = os.getcwd()  # 获取当前目录

py_files = glob.glob(os.path.join(current_dir, '*.py'))  # 匹配所有以.py结尾的文件

count = len(py_files)  # 统计文件数量

print(f"当前目录下有 {count} 个.py文件")

