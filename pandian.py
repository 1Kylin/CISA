import os
import numpy as np
import pandas as pd


# 定义一个空列表，装ID列表数据
ID_list = []
# 识别指定目录下的文件夹ID生成 ID列表
ID_list = os.listdir('F:\BaiduNetdiskDownload\资产盘点\惠州分行营业部\营业部')


path = 'F:\BaiduNetdiskDownload\资产盘点\惠州分行营业部\营业部\\'


# 定义一个空列表，用于装img的数量统计列表
num_list = []

# 循环目录
for name in ID_list:
    # 进入目录
    quantity = os.listdir(path + name)
    # 将统计的ID目录下的img文件数量保存至num_list 列表内
    num_list.append(len(quantity))


# 定义一个空列表
num_ID_list = []

# 遍历出相应数量的ID列表
for i,n in zip(ID_list,num_list):
    for _ in range(n):
        num_ID_list.append(i)


# 导入需要处理的表格
df = pd.DataFrame(pd.read_excel('F:\BaiduNetdiskDownload\\2025年设备盘点登记表-XXX单位.xlsx',header=7))

df['new使用人'] = num_ID_list
print(df)