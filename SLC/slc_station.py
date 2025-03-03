# 2025/3/3 
# Jiang Lixiang
# 描述计算站的结构，应该指明当前计算站是有叶区还是无叶区，
# 如果是有叶区，有额外的数据结构指明前缘L还是尾缘R指明是叶片的前缘还是尾缘， 有叶区还得保留对应的前缘索引


from enum import Enum, auto
from slc_numeric import Pchip
import numpy as np

# 定义计算站类型的枚举
class StationType(Enum):
    IGV = auto()    # 进口导叶
    ROTOR = auto()  # 转子
    STATOR = auto() # 静子
    UNBLADE = auto() # 无叶区


class Station:
    def __init__(self, station_type, ZR: np.ndarray,edge_type=None):

        self.station_type = station_type
        # 如果是有叶区，检查 edge_type 是否提供
        if self.station_type != StationType.UNBLADE:
            if edge_type is None:
                raise ValueError("有叶区必须指明前缘（L）或尾缘（R）")
            self.edge_type = edge_type
        else:
            self.edge_type = None  # 无叶区不需要 edge_type
        self.r2z = Pchip(ZR[:1], ZR[:, 0])

    def set_blade_idx(self, idx):
        self.blade_idx = idx
    
    def set_idx(self, idx):
        self.idx = idx


    def is_leadding(self):
        pass

    def is_trailing(self):
        pass