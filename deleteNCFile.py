import shutil
import xlrd
import os

#共享文件夹路径
dirspath = "C:\\Users\\Admin\\Desktop\\other\\shareFolder_url.xlsx"

# filepath = '//192.168.1.116/zhanwan_11/dnc_file'

ftpDir_data = xlrd.open_workbook(dirspath)
tables = ftpDir_data.sheets()[0]
ftpdir = tables.col_values(0, start_rowx=0, end_rowx=tables.nrows)
for n in range(1,76):
    dir = ftpdir[n-1].replace("\\", "/")
    dirpath = dir + "/dnc_file"
    if os.path.isdir(dirpath):
        shutil.rmtree(dirpath)
        print("删除成功====%d",%n dirpath)
    else:
        print("该路径不存在")

