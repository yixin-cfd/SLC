# 2025/3/3
# Jiang Lixiang 
# 读入并存储原始几何描述文件

import json
from typing import Union
from pathlib import Path
from slc_io import RawData

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

class Geometry:
    def __init__(self, path: Union[str, Path]):
        data = RawData(path).data
        self.J = data['M']  # 流线数量
        self.I = data['N']
    def build_flow_path(self, data):
        # 构建流道
        pass
    def build_stations(self, data):
        # 构建计算站
        pass
    def build_geometry(self, date):
        # 构建计算网格
        pass


if __name__ == '__main__':
    # Example usage (provide a valid path to your JSON file)
    try:
        raw_data = RawData("TP1493.json")
        data = raw_data.data
        print(data)  # or use the data for further processing
        Geometry("TP1493.json")
    except Exception as e:
        print(f"Error: {e}")