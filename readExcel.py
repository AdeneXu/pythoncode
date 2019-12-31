import xlrd
import pandas as pd
from pandas import DataFrame

filename = "F:\\TestCode\\twinkle\\testlib\\dataconfig\\case.xls"

data = xlrd.open_workbook(filename)

sheets = data.sheet_names()
for sheet_name in sheets:
    table = data.sheet_by_name(sheet_name)

# 循环遍历所有sheet
df_28 = DataFrame()
for i in range(len(sheets)):
#skiprows=2 忽略前两行
    df = pd.read_excel(filename, sheet_name=i, skiprows=2, index=False, encoding='utf8')
    df_28 = df_28.append(df)

    # 去除缺省值
    df_28 = df_28.dropna()
    df_28 = df_28.reset_index(drop=True)
    print(len(df_28))