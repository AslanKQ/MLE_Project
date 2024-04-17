import scipy.io
import numpy as np
import matplotlib.pyplot as plt
# 重新加载MAT文件
data = scipy.io.loadmat('mill.mat')

# 再次检查数据键（变量名）
data.keys()

# 检查'mill'结构体内的数据
mill_data = data['mill']

# 尝试访问并理解其结构
# 因为MATLAB结构在Python中以numpy结构数组形式存在，我们先检查其形状和字段名称
mill_data_shape = mill_data.shape
mill_data_fields = mill_data.dtype.fields.keys()

mill_data_shape, mill_data_fields
# 提取'smcAC'列和'time'列的第一行数据
smcAC_first_row_data = mill_data['smcAC'][0, 18].flatten()
time_first_row_data = mill_data['time'][0, 18]-mill_data['time'][0,17].flatten()

# 检查提取的数据的形状以确认是否正确
smcAC_first_row_shape = smcAC_first_row_data.shape
time_first_row_shape = time_first_row_data.shape

smcAC_first_row_shape, time_first_row_shape, smcAC_first_row_data[:5], time_first_row_data[0]
# 将time值分成9000份，创建x坐标轴
x_axis_real_data = np.linspace(0, time_first_row_data[0], smcAC_first_row_data.shape[0])

# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(x_axis_real_data, smcAC_first_row_data)
plt.title('smcDC Data over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('smcDC Value')
plt.grid(True)
plt.show()
