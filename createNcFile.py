import os
import random
import time

# path = "G:\\NC程序\\NC_Perf\\NC_Perf"
path= "G:\\NC程序\\NC_Perf\\NC100M"
suffix = ['src','pgf','mod','txt','dat','nc']


#创建多个文件
def createFile():
    i=1
    for k in range(321,325):
        filename = os.path.join(path, "NCFile" + str(k) + "." + random.choice(suffix))
        with open('G:\\NC程序\\NC_all\\x180kvb_04.dat', 'r') as f1:
            with open(filename, 'w', encoding="utf-8") as f2:
                f2.write(f1.read())
                print("生成文件个数 %s,文件名称：%s" % (str(i), filename))
            i = i + 1

#每个文件夹创建多个文件
def createFileInFolder():
    for j in range(1,2):
        dir_name = path + str(j)
        os.mkdir(dir_name)
        for k in range(1,1001):
            filename = os.path.join(dir_name, "NCFile" + str(k) + "." + random.choice(suffix))
            with open('G:\\NC程序\\NC_all\\gai_500kv_6.src', 'r') as f1:
                with open(filename, 'w', encoding="utf-8") as f2:
                    f2.write(f1.read())



#创建一个5M的文件
def createFile_5M():
    filename = os.path.join(path,"NCFile_max"+"."+random.choice(suffix))
    with open('G:\\NC程序\\NC_all\\NCFile1.mod','r') as f1:
        with open(filename,'w',encoding="utf-8") as f2:
            f2.seek(1024*1024*2)
            f2.write(f1.read())
        print("文件名称：%s" %filename)

#创建多级文件夹，每级都创建文件
def createFolder():
    dir = path + '\\NCDir'
    for i in range(2, 10):
        new_dir = dir + str(i)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        print("第%s个文件夹名称 %s" % (str(i), new_dir))
        for j in range(1, 201):
            filename = os.path.join(new_dir, "NCFile" + str(j) + "." + random.choice(suffix))
            with open('G:\\NC程序\\NC_all\\gai_500kv_6.src', 'r') as f1:
                with open(filename, 'w', encoding="utf-8") as f2:
                    f2.write(f1.read())
                print("生成文件个数 %s,文件名称：%s" % (str(j), filename))
        dir = new_dir + "\\NCDir"

if __name__ == '__main__':
# 	s = input("please input file num:")
    createFile()