import shutil
import xlrd
import os

# filepath = '//192.168.1.116/zhanwan_11'

dirspath = "C:\\Users\\Admin\\Desktop\\FreeNC-tool\\FreeNC_Folder_url.xlsx"

src = 'C:\\Users\\Admin\\Desktop\\FreeNC-tool\\folder\\folder'

ftpDir_data = xlrd.open_workbook(dirspath)
tables = ftpDir_data.sheets()[0]
ftpdir = tables.col_values(0, start_rowx=0, end_rowx=tables.nrows)

for n in range(1,76):

    dir = ftpdir[n-1].replace("\\", "/")
    dst_path = dir + "/dnc_file/folder" + str(n)

    src_path = src + str(n)
    if not os.path.isdir(dst_path):
        shutil.copytree(src_path,dst_path)
        print("复制成功，复制路径 -----------", dst_path)
    else:
        print("已有该路径")