# 2025/3/3
# Jiang Lixiang 
# 读入并存储原始几何描述文件

import numpy as np
from scipy.interpolate import PchipInterpolator

class Pchip:
    def __init__(self, x, y):
        assert len(x) != 0 and len(x) == len(y), "bad data in pchip"
        if not isinstance(x, np.ndarray):
            x = np.array(x)
        if not isinstance(y, np.ndarray):
            y = np.array(y)
        

        self.min = np.min(x)
        self.max = np.max(x)
        self.interpolator = PchipInterpolator(x, y)

    def interp(self, x):
        return self.interpolator(x)
 
