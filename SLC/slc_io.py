# 2025/3/3
# Jiang Lixiang 
# 读入并存储原始几何描述文件

import json
from typing import Union
from pathlib import Path

class RawData:
    def __init__(self, path: Union[str, Path]):
        if isinstance(path, str):
            path = Path(path)
        
        if not path.is_file():
            raise FileNotFoundError(f"The file at {path} does not exist.")

        with open(path, 'r') as file:
            self.data = json.load(file)

    def get_data(self):
        return self.data