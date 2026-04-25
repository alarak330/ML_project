import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv("Supervised learning/House Prices - Advanced Regression Techniques/house-prices-advanced-regression-techniques/train.csv")
# missing_ratio = train.isnull().sum().sort_values(ascending=False) / len(train)
# print(missing_ratio[missing_ratio > 0]) # 看一下缺失率高的特征
# PoolQC 0.995205 MiscFeature 0.963014 Alley 0.937671 Fence 0.807534

train.drop(columns=["PoolQC","MiscFeature","Alley","Fence"], inplace=True)

